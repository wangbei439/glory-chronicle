## 装备打造系统 - Beta v0.12
## 设计文档§3.2：基底+附材=玩家定向合成，材料来源绑定特定Boss
## 打造更强装备需要击败特定Boss获取稀有材料
extends Node2D

# === 打造材料类型 ===
enum MaterialType {
	BEETLE_SHELL,     # 甲虫壳碎片 - 矿脉甲虫Boss掉落
	LAVA_CORE,        # 熔岩核心 - 远古熔岩龟Boss掉落
	SHADOW_ESSENCE,   # 暗影精华 - 矿井小怪稀有掉落
	VEIN_CRYSTAL,     # 地脉结晶 - 地脉小怪稀有掉落
}

# === 材料信息 ===
const MATERIAL_INFO: Dictionary = {
	MaterialType.BEETLE_SHELL: {
		"name": "甲虫壳碎片",
		"color": Color(0.3, 0.5, 0.8),
		"desc": "矿脉甲虫的坚硬外壳碎片",
	},
	MaterialType.LAVA_CORE: {
		"name": "熔岩核心",
		"color": Color(1.0, 0.4, 0.1),
		"desc": "熔岩龟体内灼热的核心",
	},
	MaterialType.SHADOW_ESSENCE: {
		"name": "暗影精华",
		"color": Color(0.6, 0.4, 0.8),
		"desc": "矿井亡魂残留的暗影力量",
	},
	MaterialType.VEIN_CRYSTAL: {
		"name": "地脉结晶",
		"color": Color(0.9, 0.6, 0.2),
		"desc": "地脉中凝结的元素结晶",
	},
}

# === 打造配方 ===
# 每个配方：{name, desc, type(weapon/armor), stats, materials:{type:count}, ore_cost, color}
const RECIPES: Array = [
	{
		"id": "lava_greatsword",
		"name": "熔岩巨剑",
		"desc": "注入熔岩之力的毁灭巨剑",
		"type": "weapon",
		"stats": {
			"attack_mult": 1.8,
			"defense_mult": 0.9,
			"rage_bonus": 0.1,
			"max_hp_bonus": 0.0,
		},
		"materials": {
			MaterialType.LAVA_CORE: 2,
			MaterialType.BEETLE_SHELL: 1,
		},
		"ore_cost": 8,
		"color": Color(1.0, 0.4, 0.15),
	},
	{
		"id": "beetle_bulwark",
		"name": "甲虫壁垒",
		"desc": "以甲虫壳锻造的坚不可摧之盾",
		"type": "armor",
		"stats": {
			"defense_mult": 0.6,
			"max_hp_bonus": 30.0,
			"rage_bonus": 0.0,
		},
		"materials": {
			MaterialType.BEETLE_SHELL: 2,
			MaterialType.LAVA_CORE: 1,
		},
		"ore_cost": 8,
		"color": Color(0.3, 0.55, 0.9),
	},
	{
		"id": "shadow_twin_blades",
		"name": "暗影双刃",
		"desc": "蕴含暗影之力的双刀，怒气激增",
		"type": "weapon",
		"stats": {
			"attack_mult": 1.5,
			"defense_mult": 1.0,
			"rage_bonus": 0.3,
			"max_hp_bonus": 0.0,
		},
		"materials": {
			MaterialType.SHADOW_ESSENCE: 3,
		},
		"ore_cost": 6,
		"color": Color(0.5, 0.3, 0.8),
	},
	{
		"id": "vein_holy_garb",
		"name": "地脉圣衣",
		"desc": "元素结晶编织的攻守兼备战袍",
		"type": "armor",
		"stats": {
			"defense_mult": 0.65,
			"max_hp_bonus": 15.0,
			"rage_bonus": 0.2,
		},
		"materials": {
			MaterialType.VEIN_CRYSTAL: 2,
			MaterialType.SHADOW_ESSENCE: 1,
		},
		"ore_cost": 7,
		"color": Color(0.95, 0.7, 0.25),
	},
]

# === 材料掉落配置 ===
# boss_type: {material_type: probability, count}
const BOSS_DROPS: Dictionary = {
	"beetle": {
		MaterialType.BEETLE_SHELL: {"prob": 1.0, "count": 2},  # 必掉2个
	},
	"lava_turtle": {
		MaterialType.LAVA_CORE: {"prob": 1.0, "count": 2},  # 必掉2个
	},
}

# 小怪稀有掉落
const ENEMY_DROPS: Dictionary = {
	"wraith": {
		MaterialType.SHADOW_ESSENCE: {"prob": 0.12, "count": 1},  # 12%概率
	},
	"bat_mine": {
		MaterialType.SHADOW_ESSENCE: {"prob": 0.08, "count": 1},  # 8%
	},
	"bat_lava": {
		MaterialType.VEIN_CRYSTAL: {"prob": 0.10, "count": 1},  # 10%
	},
	"wraith_lava": {
		MaterialType.VEIN_CRYSTAL: {"prob": 0.12, "count": 1},  # 12%
	},
}

# === 材料库存 ===
var materials: Dictionary = {
	MaterialType.BEETLE_SHELL: 0,
	MaterialType.LAVA_CORE: 0,
	MaterialType.SHADOW_ESSENCE: 0,
	MaterialType.VEIN_CRYSTAL: 0,
}

# === 矿石引用 ===
var ore_fragments: int = 0

func _ready() -> void:
	pass

func set_ore_count(count: int) -> void:
	ore_fragments = count

func get_material_count(mat_type: int) -> int:
	return materials.get(mat_type, 0)

func add_material(mat_type: int, count: int = 1) -> void:
	if materials.has(mat_type):
		materials[mat_type] += count

func can_craft(recipe_index: int) -> bool:
	if recipe_index < 0 or recipe_index >= RECIPES.size():
		return false
	var recipe: Dictionary = RECIPES[recipe_index]
	# 检查是否已拥有
	if GameState.owned_equipment.has(recipe["id"]):
		return false
	# 检查矿石
	if ore_fragments < recipe["ore_cost"]:
		return false
	# 检查材料
	for mat_type: int in recipe["materials"]:
		var needed: int = recipe["materials"][mat_type]
		if materials.get(mat_type, 0) < needed:
			return false
	return true

func craft(recipe_index: int) -> bool:
	if not can_craft(recipe_index):
		return false
	var recipe: Dictionary = RECIPES[recipe_index]
	# 消耗矿石
	ore_fragments -= recipe["ore_cost"]
	# 消耗材料
	for mat_type: int in recipe["materials"]:
		materials[mat_type] -= recipe["materials"][mat_type]
	# 添加到拥有列表
	GameState.owned_equipment.append(recipe["id"])
	# 注册到装备系统 - 添加到对应装备字典
	_register_crafted_equipment(recipe)
	# 自动装备
	if recipe["type"] == "weapon":
		GameState.equip_weapon(recipe["id"])
	else:
		GameState.equip_armor(recipe["id"])
	return true

func _register_crafted_equipment(recipe: Dictionary) -> void:
	"""将打造的装备注册到game_state的装备属性映射中"""
	# 这些装备的属性已通过get_equipment_stats直接查询RECIPES
	# 无需额外注册，game_state会通过crafting系统查询
	pass

func get_recipe_status(recipe_index: int) -> String:
	"""获取配方状态文本"""
	if recipe_index < 0 or recipe_index >= RECIPES.size():
		return ""
	var recipe: Dictionary = RECIPES[recipe_index]
	if GameState.owned_equipment.has(recipe["id"]):
		var equipped_id: String = GameState.equipped_weapon if recipe["type"] == "weapon" else GameState.equipped_armor
		if recipe["id"] == equipped_id:
			return "已装备"
		else:
			return "已拥有"
	if can_craft(recipe_index):
		return "可打造"
	return "材料不足"

func get_missing_materials_text(recipe_index: int) -> String:
	"""获取缺少的材料描述"""
	if recipe_index < 0 or recipe_index >= RECIPES.size():
		return ""
	var recipe: Dictionary = RECIPES[recipe_index]
	var missing: String = ""
	if ore_fragments < recipe["ore_cost"]:
		missing += "矿石x" + str(recipe["ore_cost"] - ore_fragments) + " "
	for mat_type: int in recipe["materials"]:
		var needed: int = recipe["materials"][mat_type]
		var have: int = materials.get(mat_type, 0)
		if have < needed:
			var info: Dictionary = MATERIAL_INFO[mat_type]
			missing += info["name"] + "x" + str(needed - have) + " "
	return missing.strip_edges()

func get_save_data() -> Dictionary:
	"""获取存档数据"""
	return {
		"beetle_shell": materials[MaterialType.BEETLE_SHELL],
		"lava_core": materials[MaterialType.LAVA_CORE],
		"shadow_essence": materials[MaterialType.SHADOW_ESSENCE],
		"vein_crystal": materials[MaterialType.VEIN_CRYSTAL],
	}

func load_save_data(data: Dictionary) -> void:
	"""加载存档数据"""
	materials[MaterialType.BEETLE_SHELL] = int(data.get("beetle_shell", 0))
	materials[MaterialType.LAVA_CORE] = int(data.get("lava_core", 0))
	materials[MaterialType.SHADOW_ESSENCE] = int(data.get("shadow_essence", 0))
	materials[MaterialType.VEIN_CRYSTAL] = int(data.get("vein_crystal", 0))

func reset() -> void:
	materials[MaterialType.BEETLE_SHELL] = 0
	materials[MaterialType.LAVA_CORE] = 0
	materials[MaterialType.SHADOW_ESSENCE] = 0
	materials[MaterialType.VEIN_CRYSTAL] = 0

# 静态方法：获取打造装备的属性（供game_state调用）
static func get_crafted_weapon_stats(weapon_id: String) -> Dictionary:
	for recipe in RECIPES:
		if recipe["id"] == weapon_id and recipe["type"] == "weapon":
			return recipe["stats"]
	return {}

static func get_crafted_armor_stats(armor_id: String) -> Dictionary:
	for recipe in RECIPES:
		if recipe["id"] == armor_id and recipe["type"] == "armor":
			return recipe["stats"]
	return {}

static func get_all_recipe_ids() -> Array:
	var ids: Array = []
	for recipe in RECIPES:
		ids.append(recipe["id"])
	return ids
