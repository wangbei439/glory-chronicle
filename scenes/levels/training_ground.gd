## 训练场 - Alpha v0.3
## 透明背景像素精灵图 + AnimatedSprite2D 动画系统
extends Node2D

# === 战士状态 ===
var player_pos: Vector2 = Vector2(125, 309)
var player_vel: Vector2 = Vector2.ZERO
var player_facing: float = 1.0
var is_attacking: bool = false
var attack_frame: int = 0
var attack_duration: int = 20
var attack_name: String = ""
var is_guarding: bool = false
var guard_flash: float = 0.0
var is_perfect_parry_window: bool = false
var parry_window_timer: float = 0.0

# === 连招系统 ===
var combo_sequence: Array = []
var combo_count: int = 0
var combo_timer: float = 0.0
var combo_tree: Dictionary = {}

# === 怒气 ===
var rage: float = 0.0
var max_rage: float = 100.0

# === 视觉节点 ===
var player_sprite: AnimatedSprite2D
var parry_indicator: ColorRect

# 木桩
var dummies: Array = []

# HUD
var hp_fill: ColorRect
var rage_fill: ColorRect
var combo_label: Label
var perfect_label: Label
var skill_label_1: Label
var skill_label_2: Label
var hit_effects: Array = []

var frame_count: int = 0
var current_anim: String = "idle"

func _ready() -> void:
	_build_combo_tree()
	_build_scene()

func _build_combo_tree() -> void:
	combo_tree["L"] = {"name": "横斩", "mult": 1.0, "rage": 5, "dur": 20}
	combo_tree["L,L"] = {"name": "逆斩", "mult": 1.2, "rage": 5, "dur": 20}
	combo_tree["L,L,L"] = {"name": "回旋斩", "mult": 1.8, "rage": 10, "dur": 25}
	combo_tree["L,L,H"] = {"name": "上挑", "mult": 1.5, "rage": 8, "dur": 25}
	combo_tree["L,L,DH"] = {"name": "下砸", "mult": 2.0, "rage": 10, "dur": 30}
	combo_tree["L,H"] = {"name": "冲刺斩", "mult": 1.3, "rage": 7, "dur": 18}
	combo_tree["H"] = {"name": "重击", "mult": 2.5, "rage": 8, "dur": 28}
	combo_tree["H,L"] = {"name": "追击斩", "mult": 1.5, "rage": 6, "dur": 15}

func _build_scene() -> void:
	# 背景 - 地下矿井
	var bg_tex = load("res://assets/sprites/background/dungeon_mine_720p.png")
	if bg_tex:
		var bg = TextureRect.new()
		bg.texture = bg_tex
		bg.size = Vector2(640, 360)
		bg.stretch_mode = TextureRect.STRETCH_SCALE
		add_child(bg)
	else:
		var bg2 = ColorRect.new()
		bg2.size = Vector2(640, 360)
		bg2.color = Color(0.06, 0.06, 0.14, 1.0)
		add_child(bg2)
	
	# 地面线
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
	
	# 平台
	var p1 = ColorRect.new()
	p1.position = Vector2(135, 255)
	p1.size = Vector2(80, 6)
	p1.color = Color(0.25, 0.27, 0.3, 0.8)
	add_child(p1)
	
	var p2 = ColorRect.new()
	p2.position = Vector2(400, 230)
	p2.size = Vector2(100, 6)
	p2.color = Color(0.25, 0.27, 0.3, 0.8)
	add_child(p2)
	
	# === 玩家 - 使用 AnimatedSprite2D ===
	player_sprite = AnimatedSprite2D.new()
	_build_player_animations()
	player_sprite.play("idle")
	add_child(player_sprite)
	
	# 格挡指示器
	parry_indicator = ColorRect.new()
	parry_indicator.size = Vector2(20, 20)
	parry_indicator.color = Color(0.5, 0.8, 1.0, 0.4)
	parry_indicator.visible = false
	add_child(parry_indicator)
	
	# === 训练木桩 ===
	_create_dummy(Vector2(275, 306))
	_create_dummy(Vector2(350, 306))
	_create_dummy(Vector2(175, 231))
	
	# === HUD ===
	_build_hud()

func _build_player_animations() -> void:
	# 加载各动画精灵图表并创建 SpriteFrames
	var sprite_frames = SpriteFrames.new()
	
	# idle: 4帧 256x64 -> hframes=4
	var idle_tex = load("res://assets/sprites/player/warrior_idle_sheet.png")
	if idle_tex:
		sprite_frames.add_animation("idle")
		sprite_frames.set_animation_speed("idle", 8.0)
		sprite_frames.set_animation_loop("idle", true)
		for i in range(4):
			var frame_tex = _extract_frame(idle_tex, 256, 64, 4, i)
			sprite_frames.add_frame("idle", frame_tex)
	
	# run: 4帧
	var run_tex = load("res://assets/sprites/player/warrior_run_sheet.png")
	if run_tex:
		sprite_frames.add_animation("run")
		sprite_frames.set_animation_speed("run", 10.0)
		sprite_frames.set_animation_loop("run", true)
		for i in range(4):
			var frame_tex = _extract_frame(run_tex, 256, 64, 4, i)
			sprite_frames.add_frame("run", frame_tex)
	
	# attack: 4帧
	var attack_tex = load("res://assets/sprites/player/warrior_attack_sheet.png")
	if attack_tex:
		sprite_frames.add_animation("attack")
		sprite_frames.set_animation_speed("attack", 10.0)
		sprite_frames.set_animation_loop("attack", false)
		for i in range(4):
			var frame_tex = _extract_frame(attack_tex, 256, 64, 4, i)
			sprite_frames.add_frame("attack", frame_tex)
	
	# guard: 2帧
	var guard_tex = load("res://assets/sprites/player/warrior_guard_sheet.png")
	if guard_tex:
		sprite_frames.add_animation("guard")
		sprite_frames.set_animation_speed("guard", 6.0)
		sprite_frames.set_animation_loop("guard", true)
		for i in range(2):
			var frame_tex = _extract_frame(guard_tex, 128, 64, 2, i)
			sprite_frames.add_frame("guard", frame_tex)
	
	# jump: 2帧
	var jump_tex = load("res://assets/sprites/player/warrior_jump_sheet.png")
	if jump_tex:
		sprite_frames.add_animation("jump")
		sprite_frames.set_animation_speed("jump", 4.0)
		sprite_frames.set_animation_loop("jump", false)
		for i in range(2):
			var frame_tex = _extract_frame(jump_tex, 128, 64, 2, i)
			sprite_frames.add_frame("jump", frame_tex)
	
	# hurt: 2帧
	var hurt_tex = load("res://assets/sprites/player/warrior_hurt_sheet.png")
	if hurt_tex:
		sprite_frames.add_animation("hurt")
		sprite_frames.set_animation_speed("hurt", 8.0)
		sprite_frames.set_animation_loop("hurt", false)
		for i in range(2):
			var frame_tex = _extract_frame(hurt_tex, 128, 64, 2, i)
			sprite_frames.add_frame("hurt", frame_tex)
	
	# war_cry: 2帧
	var war_cry_tex = load("res://assets/sprites/player/warrior_war_cry_sheet.png")
	if war_cry_tex:
		sprite_frames.add_animation("war_cry")
		sprite_frames.set_animation_speed("war_cry", 6.0)
		sprite_frames.set_animation_loop("war_cry", false)
		for i in range(2):
			var frame_tex = _extract_frame(war_cry_tex, 128, 64, 2, i)
			sprite_frames.add_frame("war_cry", frame_tex)
	
	# earth_shatter: 2帧
	var es_tex = load("res://assets/sprites/player/warrior_earth_shatter_sheet.png")
	if es_tex:
		sprite_frames.add_animation("earth_shatter")
		sprite_frames.set_animation_speed("earth_shatter", 6.0)
		sprite_frames.set_animation_loop("earth_shatter", false)
		for i in range(2):
			var frame_tex = _extract_frame(es_tex, 128, 64, 2, i)
			sprite_frames.add_frame("earth_shatter", frame_tex)
	
	# 回退：使用单帧idle
	if not idle_tex:
		sprite_frames.add_animation("idle")
		var fallback = load("res://assets/sprites/player/warrior_idle_64.png")
		if fallback:
			sprite_frames.add_frame("idle", fallback)
	
	player_sprite.sprite_frames = sprite_frames

func _extract_frame(tex: Texture2D, sheet_w: int, sheet_h: int, hframes: int, frame_idx: int) -> AtlasTexture:
	"""从精灵图表中提取单帧作为 AtlasTexture"""
	var atlas = AtlasTexture.new()
	atlas.atlas = tex
	var frame_w: float = sheet_w / hframes
	atlas.region = Rect2(frame_idx * frame_w, 0, frame_w, sheet_h)
	atlas.filter_clip = true
	return atlas

func _play_anim(anim_name: String) -> void:
	if current_anim == anim_name:
		return
	current_anim = anim_name
	if player_sprite and player_sprite.sprite_frames and player_sprite.sprite_frames.has_animation(anim_name):
		player_sprite.play(anim_name)

func _create_dummy(pos: Vector2) -> void:
	var sprite = Sprite2D.new()
	var dummy_tex = load("res://assets/sprites/enemy/training_dummy_64.png")
	if dummy_tex:
		sprite.texture = dummy_tex
		sprite.scale = Vector2(0.8, 0.8)
	sprite.position = pos
	add_child(sprite)
	
	dummies.append({
		"sprite": sprite, "pos": pos, "flash": 0.0,
		"shake": Vector2.ZERO, "hp": 999.0
	})

func _build_hud() -> void:
	# HP背景
	var hp_bg = ColorRect.new()
	hp_bg.size = Vector2(125, 8)
	hp_bg.position = Vector2(10, 10)
	hp_bg.color = Color(0.2, 0.15, 0.15, 0.85)
	add_child(hp_bg)
	
	hp_fill = ColorRect.new()
	hp_fill.size = Vector2(124, 7)
	hp_fill.position = Vector2(10, 10)
	hp_fill.color = Color(0.85, 0.15, 0.1, 1.0)
	add_child(hp_fill)
	
	# 怒气背景
	var rage_bg = ColorRect.new()
	rage_bg.size = Vector2(125, 8)
	rage_bg.position = Vector2(10, 21)
	rage_bg.color = Color(0.15, 0.15, 0.2, 0.85)
	add_child(rage_bg)
	
	rage_fill = ColorRect.new()
	rage_fill.size = Vector2(0, 7)
	rage_fill.position = Vector2(10, 21)
	rage_fill.color = Color(0.9, 0.6, 0.1, 1.0)
	add_child(rage_fill)
	
	# 怒气50标记
	var mark50 = ColorRect.new()
	mark50.size = Vector2(1, 7)
	mark50.position = Vector2(72, 21)
	mark50.color = Color(1, 1, 1, 0.3)
	add_child(mark50)
	
	# 技能
	skill_label_1 = Label.new()
	skill_label_1.text = "[U]战吼 50怒气"
	skill_label_1.position = Vector2(10, 32)
	skill_label_1.add_theme_font_size_override("font_size", 7)
	skill_label_1.add_theme_color_override("font_color", Color(0.5, 0.5, 0.5, 0.7))
	add_child(skill_label_1)
	
	skill_label_2 = Label.new()
	skill_label_2.text = "[I]裂地斩 100怒气"
	skill_label_2.position = Vector2(10, 40)
	skill_label_2.add_theme_font_size_override("font_size", 7)
	skill_label_2.add_theme_color_override("font_color", Color(0.5, 0.5, 0.5, 0.7))
	add_child(skill_label_2)
	
	# 连招
	combo_label = Label.new()
	combo_label.position = Vector2(280, 270)
	combo_label.add_theme_font_size_override("font_size", 16)
	combo_label.add_theme_color_override("font_color", Color(1, 1, 1, 1))
	add_child(combo_label)
	
	# 完美判定
	perfect_label = Label.new()
	perfect_label.position = Vector2(250, 140)
	perfect_label.add_theme_font_size_override("font_size", 20)
	perfect_label.add_theme_color_override("font_color", Color(1, 0.9, 0.2, 1))
	perfect_label.visible = false
	add_child(perfect_label)
	
	# 标题
	var title = Label.new()
	title.text = "代号：传说"
	title.position = Vector2(230, 5)
	title.add_theme_font_size_override("font_size", 12)
	title.add_theme_color_override("font_color", Color(0.85, 0.8, 0.65, 0.9))
	add_child(title)
	
	# 版本号
	var ver = Label.new()
	ver.text = "v0.3"
	ver.position = Vector2(590, 5)
	ver.add_theme_font_size_override("font_size", 7)
	ver.add_theme_color_override("font_color", Color(0.5, 0.5, 0.5, 0.6))
	add_child(ver)
	
	# 操作提示
	var hint = Label.new()
	hint.text = "A/D:移动 W/Space:跳跃 J:轻攻 K:重攻 L:格挡 U:战吼 I:终极"
	hint.position = Vector2(100, 350)
	hint.add_theme_font_size_override("font_size", 7)
	hint.add_theme_color_override("font_color", Color(0.55, 0.55, 0.55, 0.7))
	add_child(hint)

func _physics_process(delta: float) -> void:
	frame_count += 1
	_process_player(delta)
	_update_visuals(delta)
	_update_dummies(delta)
	_process_hit_effects(delta)
	_run_demo()
	
	# 自动截图
	if frame_count == 120:
		_take_screenshot("legend_alpha_screenshot.png")
	if frame_count > 400:
		_take_screenshot("legend_alpha_combat.png")
		get_tree().quit()

func _process_player(delta: float) -> void:
	var speed = 280.0
	var gravity = 980.0
	
	# 连招超时
	if combo_timer > 0:
		combo_timer -= delta
		if combo_timer <= 0:
			combo_sequence.clear()
			combo_count = 0
	
	# 格挡窗口
	if is_perfect_parry_window:
		parry_window_timer -= delta
		if parry_window_timer <= 0:
			is_perfect_parry_window = false
			if parry_indicator:
				parry_indicator.visible = false
	
	# 攻击中
	if is_attacking:
		attack_frame += 1
		player_vel.x = lerp(player_vel.x, 0.0, 0.12)
		if attack_frame >= attack_duration:
			is_attacking = false
			attack_frame = 0
			attack_name = ""
			_play_anim("idle")
	
	# 格挡
	if is_guarding:
		player_vel.x = 0
		_play_anim("guard")
		return
	
	# 移动
	var is_moving = false
	if Input.is_action_pressed("move_right"):
		player_vel.x = speed
		player_facing = 1.0
		is_moving = true
	elif Input.is_action_pressed("move_left"):
		player_vel.x = -speed
		player_facing = -1.0
		is_moving = true
	else:
		player_vel.x = lerp(player_vel.x, 0.0, 0.2)
	
	# 动画状态切换
	if not is_attacking:
		if player_pos.y < 309:
			_play_anim("jump")
		elif is_moving:
			_play_anim("run")
		else:
			_play_anim("idle")
	
	# 跳跃
	if Input.is_action_just_pressed("jump") and player_pos.y >= 306:
		player_vel.y = -450.0
	
	# 攻击
	if Input.is_action_just_pressed("attack"):
		_do_attack("L")
	elif Input.is_action_just_pressed("heavy_attack"):
		_do_attack("H")
	
	# 格挡
	if Input.is_action_just_pressed("guard"):
		is_guarding = true
		is_perfect_parry_window = true
		parry_window_timer = 0.1
		parry_indicator.visible = true
		parry_indicator.color = Color(0.5, 0.8, 1.0, 0.5)
	
	if Input.is_action_just_released("guard"):
		is_guarding = false
		is_perfect_parry_window = false
		parry_indicator.visible = false
	
	# 战吼
	if Input.is_action_just_pressed("skill_1") and rage >= 50:
		rage -= 50
		_play_anim("war_cry")
		_show_perfect("WAR CRY!", Color(0.9, 0.7, 0.2))
	
	# 终极技
	if Input.is_action_just_pressed("ultimate") and rage >= 100:
		rage = 0
		_play_anim("earth_shatter")
		_show_perfect("EARTH SHATTER!", Color(1, 0.3, 0.1))
		for d in dummies:
			_hit_dummy(d, 50)
	
	# 重力
	if player_pos.y < 309:
		player_vel.y += gravity * delta
	
	player_pos += player_vel * delta
	
	# 地面
	if player_pos.y > 309:
		player_pos.y = 309
		player_vel.y = 0

func _do_attack(input_key: String) -> void:
	combo_sequence.append(input_key)
	combo_timer = 1.0
	
	var key = ",".join(combo_sequence)
	
	var combo_data = null
	if combo_tree.has(key):
		combo_data = combo_tree[key]
	else:
		combo_sequence = [input_key]
		key = input_key
		if combo_tree.has(key):
			combo_data = combo_tree[key]
	
	if combo_data == null:
		combo_sequence.clear()
		return
	
	attack_name = combo_data["name"]
	attack_duration = combo_data["dur"]
	is_attacking = true
	attack_frame = 0
	combo_count += 1
	_play_anim("attack")
	
	# 完美判定
	var is_perfect = false
	if is_perfect_parry_window or randf() < 0.2:
		is_perfect = true
	
	# 怒气
	var rage_gain: float = combo_data["rage"]
	if is_perfect:
		rage_gain *= 1.5
	rage = min(max_rage, rage + rage_gain)
	
	# 显示连招名
	combo_label.text = attack_name
	if is_perfect:
		combo_label.add_theme_color_override("font_color", Color(1, 0.9, 0.2, 1))
		_show_perfect("PERFECT!", Color(1, 0.95, 0.5))
	else:
		combo_label.add_theme_color_override("font_color", Color(1, 1, 1, 1))
	
	# 打击木桩
	for d in dummies:
		var dist = abs(d["pos"].x - player_pos.x)
		if dist < 60:
			var dmg: float = 10.0 * combo_data["mult"]
			if is_perfect:
				dmg *= 1.3
			_hit_dummy(d, dmg)

func _hit_dummy(d: Dictionary, damage: float) -> void:
	d["flash"] = 0.3
	d["shake"] = Vector2(randf_range(-3, 3), randf_range(-2, 2))
	d["hp"] -= damage
	
	var dmg_label = Label.new()
	dmg_label.text = str(int(damage))
	dmg_label.position = d["pos"] + Vector2(randf_range(-10, 10), -20)
	dmg_label.add_theme_font_size_override("font_size", 10 if damage < 20 else 14)
	dmg_label.add_theme_color_override("font_color", Color(1, 0.3, 0.1) if damage >= 20 else Color(1, 1, 1))
	add_child(dmg_label)
	hit_effects.append({"node": dmg_label, "life": 0.8, "vel": Vector2(randf_range(-15, 15), -40)})

func _show_perfect(text: String, color: Color) -> void:
	perfect_label.text = text
	perfect_label.visible = true
	perfect_label.add_theme_color_override("font_color", color)
	var tween = create_tween()
	tween.tween_property(perfect_label, "modulate:a", 0, 0.8)
	tween.tween_callback(func(): perfect_label.visible = false; perfect_label.modulate.a = 1)

func _update_visuals(delta: float) -> void:
	var f = player_facing
	
	# 角色位置（64x64精灵中心偏移）
	player_sprite.position = player_pos + Vector2(0, -32)
	player_sprite.flip_h = (f < 0)
	
	# 格挡指示器
	if is_guarding and is_perfect_parry_window:
		parry_indicator.visible = true
		parry_indicator.position = player_pos + Vector2(-10 * f, -42)
		parry_indicator.color = Color(0.5, 0.8, 1.0, 0.3 + 0.3 * sin(frame_count * 0.5))
	else:
		parry_indicator.visible = false
	
	# 怒气条
	rage_fill.size.x = 124 * (rage / max_rage)
	if rage >= 100:
		rage_fill.color = Color(1, 0.85, 0.2, 1) if int(frame_count / 6) % 2 == 0 else Color(0.9, 0.5, 0.1, 1)
	elif rage >= 50:
		rage_fill.color = Color(0.95, 0.65, 0.1, 1)
	else:
		rage_fill.color = Color(0.9, 0.6, 0.1, 1)
	
	# 技能可用状态
	skill_label_1.add_theme_color_override("font_color",
		Color(0.3, 1, 0.3, 1) if rage >= 50 else Color(0.5, 0.5, 0.5, 0.5))
	skill_label_2.add_theme_color_override("font_color",
		Color(1, 0.3, 0.2, 1) if rage >= 100 else Color(0.5, 0.5, 0.5, 0.5))
	
	# 连招超时清除
	if combo_timer <= 0 and not is_attacking:
		combo_label.text = ""

func _update_dummies(delta: float) -> void:
	for d in dummies:
		d["shake"] = d["shake"].lerp(Vector2.ZERO, 0.15)
		var offset = d["shake"]
		if d.has("sprite"):
			d["sprite"].position = d["pos"] + offset
			if d["flash"] > 0:
				d["flash"] -= delta
				d["sprite"].modulate = Color(2, 1.5, 1) if int(d["flash"] * 20) % 2 == 0 else Color(1, 1, 1)
			else:
				d["sprite"].modulate = Color(1, 1, 1)

func _process_hit_effects(delta: float) -> void:
	var to_remove = []
	for i in range(hit_effects.size()):
		var e = hit_effects[i]
		e["life"] -= delta
		e["node"].position += e["vel"] * delta
		e["vel"].y += 80 * delta
		var mod = e["node"].modulate
		mod.a = max(0, e["life"] / 0.8)
		e["node"].modulate = mod
		if e["life"] <= 0:
			e["node"].queue_free()
			to_remove.append(i)
	for i in to_remove:
		hit_effects.remove_at(i)

func _take_screenshot(filename: String) -> void:
	var img = get_viewport().get_texture().get_image()
	if img:
		img.save_png("/home/z/my-project/download/" + filename)
		print("Screenshot saved: " + filename)

# === 自动演示 ===
func _run_demo() -> void:
	match frame_count:
		60:
			player_vel.x = 220
			player_facing = 1.0
		100:
			_do_attack("L")
		130:
			_do_attack("L")
		160:
			_do_attack("L")
		190:
			player_vel.x = 150
		210:
			_do_attack("L")
		230:
			_do_attack("H")
		260:
			player_vel.x = 0
		280:
			_do_attack("H")
		310:
			rage = 100
			_show_perfect("RAGE FULL!", Color(1, 0.7, 0.1))
		340:
			_do_attack("L")
		355:
			_do_attack("L")
		370:
			_do_attack("H")
