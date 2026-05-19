## 幽影矿井关卡 - Alpha v0.8
## 多区域关卡：入口→矿道→Boss门前
## 小怪：矿工亡魂 ×3 + 洞穴蝙蝠 ×2 + 平台 + 落石陷阱
## v0.8新增：掉落/拾取系统、洞穴蝙蝠、技能树(Tab键)、技能效果实际生效
extends Node2D

const GROUND_Y: float = 309.0

# === 自动演示模式 ===
@export var auto_demo: bool = false
@export var auto_quit_frame: int = 0

# 子系统
var warrior: Node2D
var effects: Node2D
var hud: Node2D
var camera: Node2D
var audio: Node2D
var drop_system: Node2D
var skill_tree: Node2D

# 小怪（矿工亡魂）
var enemies: Array = []
var enemy_sprites: Array = []

# 蝙蝠
var bats: Array = []
var bat_sprites: Array = []

# 视觉
var player_sprite: AnimatedSprite2D
var parry_indicator: ColorRect
var camera_offset: Vector2 = Vector2.ZERO

# 状态
var frame_count: int = 0
var player_hit_by_enemy: Dictionary = {}
var player_hit_by_bat: Dictionary = {}

# 陷阱（落石）
var rock_traps: Array = []
var trap_triggered: Dictionary = {}

# 传送门
var portal: ColorRect
var portal_label: Label
var portal_pos: Vector2 = Vector2(610, GROUND_Y)

# 跳跃音效
var was_on_ground: bool = true

# HUD矿石计数
var ore_display: Label

func _ready() -> void:
	_build_scene()

func _build_scene() -> void:
	# === 背景 ===
	var bg_tex = load("res://assets/sprites/background/dungeon_mine_640x360.png")
	if bg_tex:
		var bg = TextureRect.new()
		bg.texture = bg_tex
		bg.size = Vector2(640, 360)
		bg.stretch_mode = TextureRect.STRETCH_SCALE
		add_child(bg)
	else:
		var bg2 = ColorRect.new()
		bg2.size = Vector2(640, 360)
		bg2.color = Color(0.05, 0.05, 0.12, 1.0)
		add_child(bg2)

	# === 地面 ===
	_build_ground()

	# === 平台 ===
	_build_platforms()

	# === 落石陷阱区域标记 ===
	_build_trap_markers()

	# === 传送门 ===
	_build_portal()

	# === 摄像机控制器 ===
	var camera_script = load("res://scripts/core/camera_controller.gd")
	camera = Node2D.new()
	camera.set_script(camera_script)
	add_child(camera)
	camera.setup(Vector2(640, 360), Vector2.ZERO, Vector2(640, 360))
	camera.set_position_immediate(Vector2(320, 180))
	camera.activate()

	# === 音效系统 ===
	var audio_script = load("res://scripts/audio/audio_manager.gd")
	audio = Node2D.new()
	audio.set_script(audio_script)
	add_child(audio)

	# === 打击感特效 ===
	var effects_script = load("res://scripts/core/combat_effects.gd")
	effects = Node2D.new()
	effects.set_script(effects_script)
	add_child(effects)

	# === 掉落系统 ===
	var drop_script = load("res://scripts/core/drop_system.gd")
	drop_system = Node2D.new()
	drop_system.set_script(drop_script)
	add_child(drop_system)

	# === 技能树 ===
	var skill_script = load("res://scripts/ui/skill_tree.gd")
	skill_tree = Node2D.new()
	skill_tree.set_script(skill_script)
	add_child(skill_tree)
	skill_tree.build()
	skill_tree.set_drop_system(drop_system)
	# 从全局状态恢复技能等级
	skill_tree.load_skill_data(GameState.skill_levels)
	drop_system.ore_fragments = GameState.ore_fragments

	# === 战士 ===
	var warrior_script = load("res://scripts/player/warrior.gd")
	warrior = Node2D.new()
	warrior.set_script(warrior_script)
	add_child(warrior)

	player_sprite = AnimatedSprite2D.new()
	add_child(player_sprite)
	warrior.setup_sprite(player_sprite)
	warrior.pos = Vector2(60, GROUND_Y)

	# 从全局状态恢复
	var state = GameState.get_player_state()
	warrior.hp = state["hp"]
	warrior.rage = state["rage"]
	warrior.hit_count = state["hit_count"]

	parry_indicator = ColorRect.new()
	parry_indicator.size = Vector2(20, 20)
	parry_indicator.color = Color(0.5, 0.8, 1.0, 0.4)
	parry_indicator.visible = false
	add_child(parry_indicator)
	warrior.parry_indicator = parry_indicator

	# 设置掉落系统的玩家引用
	drop_system.set_player(warrior)
	drop_system.set_hud(null)  # 稍后设置
	drop_system.set_audio(audio)

	# === 小怪（矿工亡魂）===
	_spawn_enemy(Vector2(220, GROUND_Y), 200)
	_spawn_enemy(Vector2(380, GROUND_Y), 180)
	_spawn_enemy(Vector2(520, GROUND_Y), 160)

	# === 蝙蝠 ===
	_spawn_bat(Vector2(160, 200), 180)
	_spawn_bat(Vector2(450, 180), 160)

	# === HUD ===
	var hud_script = load("res://scripts/ui/hud.gd")
	hud = Node2D.new()
	hud.set_script(hud_script)
	add_child(hud)
	hud.build()
	hud.update_player_hp(warrior.hp, warrior.max_hp)
	hud.update_rage(warrior.rage, warrior.max_rage)

	# 设置掉落系统的HUD引用
	drop_system.set_hud(hud)

	# === HUD矿石计数 ===
	ore_display = Label.new()
	ore_display.text = "ORE: " + str(drop_system.ore_fragments)
	ore_display.position = Vector2(560, 5)
	ore_display.add_theme_font_size_override("font_size", 8)
	ore_display.add_theme_color_override("font_color", Color(0.7, 0.6, 0.9, 0.9))
	add_child(ore_display)

	# === 关卡标题 ===
	var title = Label.new()
	title.text = "幽影矿井 - 入口"
	title.position = Vector2(240, 5)
	title.add_theme_font_size_override("font_size", 10)
	title.add_theme_color_override("font_color", Color(0.7, 0.65, 0.55, 0.9))
	add_child(title)

	# === 版本/操作提示 ===
	var ver = Label.new()
	ver.text = "v0.8"
	ver.position = Vector2(600, 350)
	ver.add_theme_font_size_override("font_size", 7)
	ver.add_theme_color_override("font_color", Color(0.5, 0.5, 0.5, 0.6))
	add_child(ver)

	var hint = Label.new()
	hint.text = "A/D:移动 W/Space:跳跃 J:轻攻 K:重攻 L:格挡 U:战吼 I:裂地斩 Tab:技能树 Esc:主菜单"
	hint.position = Vector2(60, 350)
	hint.add_theme_font_size_override("font_size", 7)
	hint.add_theme_color_override("font_color", Color(0.55, 0.55, 0.55, 0.7))
	add_child(hint)

func _build_ground() -> void:
	var ground_top = ColorRect.new()
	ground_top.position = Vector2(0, 329)
	ground_top.size = Vector2(640, 2)
	ground_top.color = Color(0.35, 0.4, 0.45, 0.8)
	add_child(ground_top)

	var ground = ColorRect.new()
	ground.position = Vector2(0, 330)
	ground.size = Vector2(640, 30)
	ground.color = Color(0.15, 0.17, 0.2, 0.6)
	add_child(ground)

	for x in [80, 200, 350, 500]:
		var crack = ColorRect.new()
		crack.position = Vector2(x, 329)
		crack.size = Vector2(randf_range(8, 20), 2)
		crack.color = Color(0.1, 0.12, 0.15, 0.5)
		add_child(crack)

func _build_platforms() -> void:
	var platforms = [
		{"pos": Vector2(130, 260), "size": Vector2(80, 6)},
		{"pos": Vector2(300, 240), "size": Vector2(100, 6)},
		{"pos": Vector2(480, 260), "size": Vector2(80, 6)},
	]
	for p in platforms:
		var plat = ColorRect.new()
		plat.position = p["pos"]
		plat.size = p["size"]
		plat.color = Color(0.25, 0.27, 0.3, 0.8)
		add_child(plat)
		var support = ColorRect.new()
		support.position = p["pos"] + Vector2(2, 6)
		support.size = Vector2(2, GROUND_Y - p["pos"].y - 6)
		support.color = Color(0.2, 0.22, 0.25, 0.4)
		add_child(support)
		var support2 = ColorRect.new()
		support2.position = p["pos"] + Vector2(p["size"].x - 4, 6)
		support2.size = Vector2(2, GROUND_Y - p["pos"].y - 6)
		support2.color = Color(0.2, 0.22, 0.25, 0.4)
		add_child(support2)

func _build_trap_markers() -> void:
	var trap_positions = [280, 450]
	for i in range(trap_positions.size()):
		var x = trap_positions[i]
		var marker = ColorRect.new()
		marker.position = Vector2(x - 15, 327)
		marker.size = Vector2(30, 2)
		marker.color = Color(0.6, 0.5, 0.2, 0.3)
		add_child(marker)

		rock_traps.append({"x": x, "active": false, "rocks": []})
		trap_triggered[i] = false

func _build_portal() -> void:
	portal = ColorRect.new()
	portal.size = Vector2(12, 50)
	portal.position = portal_pos + Vector2(0, -50)
	portal.color = Color(0.3, 0.6, 1.0, 0.5)
	add_child(portal)

	var portal_border = ColorRect.new()
	portal_border.size = Vector2(14, 52)
	portal_border.position = portal_pos + Vector2(-1, -51)
	portal_border.color = Color(0.5, 0.8, 1.0, 0.3)
	add_child(portal_border)

	portal_label = Label.new()
	portal_label.text = "→Boss"
	portal_label.position = portal_pos + Vector2(-25, -60)
	portal_label.add_theme_font_size_override("font_size", 7)
	portal_label.add_theme_color_override("font_color", Color(0.5, 0.8, 1.0, 0.7))
	add_child(portal_label)

func _spawn_enemy(pos: Vector2, detect: float) -> void:
	var enemy_script = load("res://scripts/enemy/mine_wraith.gd")
	var enemy = Node2D.new()
	enemy.set_script(enemy_script)
	enemy.pos = pos
	enemy.patrol_center = pos.x
	enemy.detect_range = detect
	add_child(enemy)

	var enemy_sprite = AnimatedSprite2D.new()
	add_child(enemy_sprite)
	enemy.setup(enemy_sprite)

	enemies.append(enemy)
	enemy_sprites.append(enemy_sprite)
	player_hit_by_enemy[enemies.size() - 1] = false

	enemy.enemy_hit_player.connect(_on_enemy_hit_player)
	enemy.enemy_died.connect(_on_enemy_died)

func _spawn_bat(pos: Vector2, detect: float) -> void:
	var bat_script = load("res://scripts/enemy/cave_bat.gd")
	var bat = Node2D.new()
	bat.set_script(bat_script)
	bat.pos = pos
	bat.hover_center = pos
	bat.detect_range = detect
	add_child(bat)

	var bat_sprite = AnimatedSprite2D.new()
	add_child(bat_sprite)
	bat.setup(bat_sprite)

	bats.append(bat)
	bat_sprites.append(bat_sprite)
	player_hit_by_bat[bats.size() - 1] = false

	bat.enemy_hit_player.connect(_on_bat_hit_player)
	bat.enemy_died.connect(_on_bat_died)

func _physics_process(delta: float) -> void:
	frame_count += 1

	# 技能树打开时暂停游戏
	if skill_tree.is_open:
		skill_tree.process_input()
		return

	# Tab键打开技能树
	if Input.is_key_pressed(KEY_TAB):
		skill_tree.toggle()
		return

	# Esc返回主菜单
	if Input.is_key_pressed(KEY_ESCAPE):
		_save_state()
		GameState.go_to_title()
		return

	# Hitstop
	if effects.hitstop_active:
		effects.process(delta)
		camera.apply_shake(effects.get_shake_offset())
		return

	# 使用combat_effects的震屏
	camera_offset = effects.get_shake_offset()
	camera.apply_shake(camera_offset)

	# 战吼buff
	if warrior.war_cry_buff:
		warrior.war_cry_timer -= delta
		if warrior.war_cry_timer <= 0:
			warrior.war_cry_buff = false

	# 处理战士
	warrior.process(delta, GROUND_Y)

	# 跳跃/落地音效
	var on_ground: bool = warrior.pos.y >= GROUND_Y - 3
	if not was_on_ground and on_ground:
		audio.play("land")
	was_on_ground = on_ground

	# 处理小怪
	for i in range(enemies.size()):
		var enemy: Node2D = enemies[i]
		if enemy.hp > 0:
			enemy.process(delta, warrior.pos, GROUND_Y)

	# 处理蝙蝠
	for i in range(bats.size()):
		var bat: Node2D = bats[i]
		if bat.hp > 0:
			bat.process(delta, warrior.pos, GROUND_Y)

	# 战士攻击小怪
	_check_player_vs_enemies()

	# 战士攻击蝙蝠
	_check_player_vs_bats()

	# 小怪攻击战士
	_check_enemies_vs_player()

	# 蝙蝠攻击战士
	_check_bats_vs_player()

	# 落石陷阱
	_process_traps()

	# 掉落物
	drop_system.process(delta)

	# 传送门检测
	_check_portal()

	# 更新视觉
	_update_visuals()

	# 更新摄像机
	camera.follow(warrior.pos, warrior.facing, delta)

	# 更新HUD
	hud.update_player_hp(warrior.hp, warrior.max_hp)
	hud.update_rage(warrior.rage, warrior.max_rage)
	hud.update_hit_count(warrior.hit_count)
	hud.show_war_cry_buff(warrior.war_cry_buff, warrior.war_cry_timer)

	# 修复：使用hud.process_effects处理伤害数字动画
	hud.process_effects(delta)

	# 处理特效系统
	effects.process(delta)

	# 矿石计数更新
	ore_display.text = "ORE: " + str(drop_system.ore_fragments)

	# 连招超时
	if warrior.combo_timer <= 0 and not warrior.is_attacking:
		hud.clear_combo()

	if warrior.is_attacking and warrior.attack_name != "":
		hud.show_combo(warrior.attack_name, warrior.war_cry_buff)

	# 死亡
	if warrior.hp <= 0 and warrior.invincible_timer <= 0:
		if Input.is_key_pressed(KEY_R):
			warrior.hp = warrior.max_hp
			warrior.rage = 0
			warrior.pos = Vector2(60, GROUND_Y)
			warrior.vel = Vector2.ZERO
			warrior.is_hurt = false
			warrior.invincible_timer = 2.0
			warrior.hit_count = 0
			audio.play("level_up", 0.5)

	# 自动截图（服务器验证用）
	if frame_count == 120:
		_take_screenshot("legend_mine_level.png")

	# 自动演示/退出
	if auto_demo:
		_run_demo()
	if auto_quit_frame > 0 and frame_count >= auto_quit_frame:
		_take_screenshot("legend_mine_level_auto.png")
		get_tree().quit()

	# 清理死亡敌人
	_cleanup_dead_enemies()
	_cleanup_dead_bats()

	# 保存全局状态
	_save_state()

	# 传送门闪烁
	if portal:
		portal.color = Color(0.3, 0.6, 1.0, 0.3 + 0.3 * sin(frame_count * 0.08))

func _save_state() -> void:
	GameState.save_player_state(warrior.hp, warrior.rage, warrior.hit_count)
	GameState.save_resources(drop_system.ore_fragments, skill_tree.get_skill_data())

# === 获取技能加成后的攻击伤害 ===
func _get_skill_boosted_damage(base_dmg: float) -> float:
	"""应用攻击强化技能加成"""
	var atk_mult: float = skill_tree.get_attack_bonus()
	return base_dmg * atk_mult

# === 获取技能减伤后的伤害 ===
func _get_skill_reduced_damage(base_dmg: float) -> float:
	"""应用防御强化技能减伤"""
	var def_reduction: float = skill_tree.get_defense_bonus()
	return base_dmg * (1.0 - def_reduction)

# === 获取技能加成后的怒气获取 ===
func _get_skill_boosted_rage(base_rage: float) -> float:
	"""应用怒气精通技能加成"""
	var rage_mult: float = skill_tree.get_rage_bonus()
	return base_rage * rage_mult

func _check_portal() -> void:
	var dist_to_portal = abs(warrior.pos.x - portal_pos.x)
	if dist_to_portal < 25:
		audio.play("portal")
		GameState.mark_level_cleared("mine")
		GameState.go_to_level("boss")

func _check_player_vs_enemies() -> void:
	if not warrior.is_in_active_frames():
		return

	for i in range(enemies.size()):
		var enemy: Node2D = enemies[i]
		if enemy.hp <= 0:
			continue

		var dist = abs(warrior.pos.x - enemy.pos.x)
		if dist < 65:
			var base_dmg: float = warrior.get_attack_damage()
			var dmg: float = _get_skill_boosted_damage(base_dmg)
			enemy.take_damage(dmg)
			warrior.mark_hit_dealt()

			var hit_pos: Vector2 = (warrior.pos + enemy.pos) / 2 + Vector2(0, -20)
			effects.spawn_hit_spark(hit_pos, Color(1, 0.9, 0.5))

			if dmg >= 20:
				effects.start_hitstop(0.08)
				effects.start_shake(3.0, 8.0)
				audio.play("hit_heavy")
			else:
				effects.start_hitstop(0.04)
				effects.start_shake(1.0, 6.0)
				audio.play("hit_light")

			hud.spawn_damage_number(enemy.pos + Vector2(0, -40), dmg, dmg >= 20)

			# 怒气（含技能加成）
			var rage_gain: float = _get_skill_boosted_rage(5.0)
			warrior.rage = min(warrior.max_rage, warrior.rage + rage_gain)

			break

func _check_player_vs_bats() -> void:
	if not warrior.is_in_active_frames():
		return

	for i in range(bats.size()):
		var bat: Node2D = bats[i]
		if bat.hp <= 0:
			continue

		var dist_x = abs(warrior.pos.x - bat.pos.x)
		var dist_y = abs(warrior.pos.y - bat.pos.y)
		if dist_x < 65 and dist_y < 50:
			var base_dmg: float = warrior.get_attack_damage()
			var dmg: float = _get_skill_boosted_damage(base_dmg)
			bat.take_damage(dmg)
			warrior.mark_hit_dealt()

			var hit_pos: Vector2 = (warrior.pos + bat.pos) / 2
			effects.spawn_hit_spark(hit_pos, Color(1, 0.6, 0.8))

			effects.start_hitstop(0.04)
			effects.start_shake(1.5, 7.0)
			audio.play("hit_light")

			hud.spawn_damage_number(bat.pos + Vector2(0, -40), dmg, dmg >= 20)

			# 怒气
			var rage_gain: float = _get_skill_boosted_rage(5.0)
			warrior.rage = min(warrior.max_rage, warrior.rage + rage_gain)

			break

func _check_enemies_vs_player() -> void:
	for i in range(enemies.size()):
		var enemy: Node2D = enemies[i]
		if enemy.hp <= 0:
			continue

		var dist = abs(warrior.pos.x - enemy.pos.x)
		if enemy.is_in_attack_active() and not player_hit_by_enemy.get(i, false):
			if dist < 60:
				var base_dmg: float = enemy.get_attack_damage()
				var dmg: float = _get_skill_reduced_damage(base_dmg)
				var kb: Vector2 = Vector2(4 * enemy.facing, -2)
				warrior.take_damage(dmg, kb)

				hud.spawn_damage_number(warrior.pos + Vector2(0, -40), dmg, false)
				effects.start_hitstop(0.04)
				effects.start_shake(2.0, 7.0)
				audio.play("hurt")

				player_hit_by_enemy[i] = true

		if not enemy.is_in_attack_active():
			player_hit_by_enemy[i] = false

func _check_bats_vs_player() -> void:
	for i in range(bats.size()):
		var bat: Node2D = bats[i]
		if bat.hp <= 0:
			continue

		if bat.is_in_attack_active() and not player_hit_by_bat.get(i, false):
			var dist_x = abs(warrior.pos.x - bat.pos.x)
			var dist_y = abs(warrior.pos.y - bat.pos.y)
			if dist_x < 45 and dist_y < 40:
				var base_dmg: float = bat.get_attack_damage()
				var dmg: float = _get_skill_reduced_damage(base_dmg)
				var kb: Vector2 = Vector2(3 * bat.facing, -3)
				warrior.take_damage(dmg, kb)

				hud.spawn_damage_number(warrior.pos + Vector2(0, -40), dmg, false)
				effects.start_hitstop(0.04)
				effects.start_shake(1.5, 7.0)
				audio.play("hurt")

				player_hit_by_bat[i] = true

		if not bat.is_in_attack_active():
			player_hit_by_bat[i] = false

func _process_traps() -> void:
	for i in range(rock_traps.size()):
		var trap: Dictionary = rock_traps[i]
		if trap["active"]:
			continue

		var dist = abs(warrior.pos.x - trap["x"])
		if dist < 25 and not trap_triggered.get(i, false):
			trap_triggered[i] = true
			trap["active"] = true
			for j in range(3):
				var rock = ColorRect.new()
				rock.size = Vector2(randf_range(4, 8), randf_range(4, 8))
				rock.position = Vector2(trap["x"] + randf_range(-15, 15), -20 - j * 20)
				rock.color = Color(0.5, 0.45, 0.4, 1)
				add_child(rock)
				trap["rocks"].append({
					"node": rock, "vel": Vector2(randf_range(-10, 10), randf_range(100, 200)),
					"ground_y": GROUND_Y - 4
				})

			hud.show_perfect("DANGER!", Color(1, 0.5, 0.1))
			effects.start_shake(1.5, 6.0)
			audio.play("rock_fall")

	# 更新落石位置
	for trap in rock_traps:
		for rock_data in trap["rocks"]:
			var node = rock_data["node"]
			if node and is_instance_valid(node):
				rock_data["vel"].y += 500 * (1.0/60.0)
				node.position += rock_data["vel"] * (1.0/60.0)

				var rock_dist = abs(warrior.pos.x - node.position.x)
				if rock_dist < 20 and abs(warrior.pos.y - 30 - node.position.y) < 30:
					var base_dmg: float = 8.0
					var dmg: float = _get_skill_reduced_damage(base_dmg)
					warrior.take_damage(dmg, Vector2(randf_range(-3, 3), -3))
					hud.spawn_damage_number(warrior.pos + Vector2(0, -40), dmg, false)
					audio.play("hurt", 0.5)
					node.queue_free()
					rock_data["node"] = null

				if node.position.y >= rock_data["ground_y"]:
					effects.start_shake(1.0, 6.0)
					audio.play("rock_fall", 0.3)
					node.queue_free()
					rock_data["node"] = null

func _on_enemy_hit_player(damage: float, knockback: Vector2) -> void:
	pass

func _on_enemy_died(pos: Vector2) -> void:
	effects.spawn_hit_spark(pos, Color(0.7, 0.8, 1.0))
	var rage_gain: float = _get_skill_boosted_rage(15.0)
	warrior.rage = min(warrior.max_rage, warrior.rage + rage_gain)
	hud.show_perfect("+15 RAGE", Color(0.5, 0.8, 1.0))
	audio.play("enemy_die")
	GameState.total_kills += 1

	# 掉落物品
	drop_system.spawn_drop(pos, "wraith", GROUND_Y)

func _on_bat_hit_player(damage: float, knockback: Vector2) -> void:
	pass

func _on_bat_died(pos: Vector2) -> void:
	effects.spawn_hit_spark(pos, Color(0.8, 0.5, 0.9))
	var rage_gain: float = _get_skill_boosted_rage(10.0)
	warrior.rage = min(warrior.max_rage, warrior.rage + rage_gain)
	hud.show_perfect("+10 RAGE", Color(0.8, 0.5, 0.9))
	audio.play("enemy_die")
	GameState.total_kills += 1

	# 掉落物品
	drop_system.spawn_drop(pos, "bat", GROUND_Y)

func _cleanup_dead_enemies() -> void:
	for i in range(enemies.size() - 1, -1, -1):
		var enemy: Node2D = enemies[i]
		if enemy.hp <= 0 and enemy.current_state == 4:  # State.DYING = 4
			if not enemy.sprite or not enemy.sprite.is_playing():
				if enemy.sprite and is_instance_valid(enemy.sprite):
					enemy.sprite.queue_free()
				enemy.queue_free()
				enemies.remove_at(i)
				enemy_sprites.remove_at(i)

func _cleanup_dead_bats() -> void:
	for i in range(bats.size() - 1, -1, -1):
		var bat: Node2D = bats[i]
		if bat.hp <= 0 and bat.current_state == 5:  # State.DYING = 5
			if not bat.sprite or not bat.sprite.is_playing():
				if bat.sprite and is_instance_valid(bat.sprite):
					bat.sprite.queue_free()
				bat.queue_free()
				bats.remove_at(i)
				bat_sprites.remove_at(i)

func _update_visuals() -> void:
	var shake = camera_offset

	player_sprite.position = warrior.pos + Vector2(0, -32) + shake
	player_sprite.flip_h = (warrior.facing < 0)

	if warrior.invincible_timer > 0:
		player_sprite.visible = int(frame_count / 3) % 2 == 0
	else:
		player_sprite.visible = true

	if warrior.war_cry_buff:
		if int(frame_count / 4) % 3 == 0:
			player_sprite.modulate = Color(1.2, 1.0, 0.7)
		else:
			player_sprite.modulate = Color(1, 1, 1)

	if warrior.is_guarding and warrior.is_perfect_parry_window:
		parry_indicator.visible = true
		parry_indicator.position = warrior.pos + Vector2(-10 * warrior.facing, -42) + shake
	else:
		parry_indicator.visible = false

	# 小怪视觉
	for i in range(enemies.size()):
		if i < enemy_sprites.size() and is_instance_valid(enemy_sprites[i]):
			var esprite: AnimatedSprite2D = enemy_sprites[i]
			var enemy: Node2D = enemies[i]
			esprite.position = enemy.pos + Vector2(0, -32) + shake
			esprite.flip_h = (enemy.facing < 0)

	# 蝙蝠视觉
	for i in range(bats.size()):
		if i < bat_sprites.size() and is_instance_valid(bat_sprites[i]):
			var bsprite: AnimatedSprite2D = bat_sprites[i]
			var bat: Node2D = bats[i]
			bsprite.position = bat.pos + Vector2(0, -32) + shake
			bsprite.flip_h = (bat.facing < 0)

func _take_screenshot(filename: String) -> void:
	var img = get_viewport().get_texture().get_image()
	if img:
		img.save_png("/home/z/my-project/download/" + filename)
		print("Screenshot saved: " + filename)

func _run_demo() -> void:
	match frame_count:
		60:
			warrior.vel.x = 200
			warrior.facing = 1.0
		100:
			warrior.do_attack("L")
			audio.play("swing")
		140:
			warrior.do_attack("L")
			audio.play("swing")
		180:
			warrior.vel.x = 0
