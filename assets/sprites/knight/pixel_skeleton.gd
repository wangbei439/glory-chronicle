## 像素骨骼动画系统 - 《代号：传说》
## 使用6个独立Sprite3D部件实现代码驱动动画
## 部件切分自AI生成的A-Pose骑士角色
extends Node3D

# ========== 部件节点 ==========
@onready var left_leg:  Sprite3D = $LeftLeg
@onready var left_arm:  Sprite3D = $LeftArm
@onready var body:      Sprite3D = $Body
@onready var head:      Sprite3D = $Head
@onready var right_arm: Sprite3D = $RightArm
@onready var right_leg: Sprite3D = $RightLeg

# ========== 配置 ==========
## Sprite3D参数
const PIXEL_SIZE: float = 0.05
const CANVAS_W: int = 126  ## 缩放后画布宽
const CANVAS_H: int = 128  ## 缩放后画布高

## 部件偏移（相对于角色根节点，基于pivot点）
## 格式: [offset_x, offset_y, z_index]
const PART_OFFSETS: Dictionary = {
	"head":      {"offset": Vector2(-32, -32), "z": 3},
	"body":      {"offset": Vector2(-28, 3),   "z": 2},
	"right_arm": {"offset": Vector2(-2, 20),   "z": 4},
	"left_arm":  {"offset": Vector2(-33, 1),   "z": 1},
	"left_leg":  {"offset": Vector2(-42, -4),  "z": 0},
	"right_leg": {"offset": Vector2(-8, -7),   "z": 5},
}

## 动画速度
var anim_time: float = 0.0
var current_state: String = "idle"
var facing_right: bool = true

## 动画参数
const IDLE_BREATHE: float = 1.5     ## 呼吸幅度（像素）
const IDLE_SPEED: float = 2.0       ## 呼吸速度
const WALK_BOB: float = 2.0         ## 行走上下摆动
const WALK_LEG_SWING: float = 8.0   ## 腿摆动角度
const WALK_ARM_SWING: float = 6.0   ## 手臂摆动角度
const WALK_SPEED: float = 8.0       ## 行走动画速度
const ATTACK_SWING: float = 90.0    ## 攻击挥剑角度
const ATTACK_DURATION: float = 0.3  ## 攻击动画时长
const DODGE_SHIFT: float = 15.0     ## 闪避位移
const DODGE_DURATION: float = 0.4   ## 闪避动画时长
const HURT_SHAKE: float = 3.0       ## 受击抖动
const HURT_DURATION: float = 0.2    ## 受击动画时长

## 攻击/闪避/受击计时器
var attack_timer: float = 0.0
var dodge_timer: float = 0.0
var hurt_timer: float = 0.0

func _ready() -> void:
	_setup_sprites()

func _setup_sprites() -> void:
	"""初始化所有Sprite3D节点"""
	var parts: Dictionary = {
		"head": head, "body": body,
		"right_arm": right_arm, "left_arm": left_arm,
		"left_leg": left_leg, "right_leg": right_leg,
	}
	for part_name: String in parts:
		var sprite: Sprite3D = parts[part_name]
		if sprite == null:
			continue
		sprite.pixel_size = PIXEL_SIZE
		sprite.texture_filter = BaseMaterial3D.TEXTURE_FILTER_NEAREST
		sprite.billboard_mode = BaseMaterial3D.BILLBOARD_FIXED_Y
		sprite.centered = false  # 左上角对齐，方便用offset定位
		# 加载纹理（路径根据你的项目结构调整）
		sprite.texture = load("res://assets/sprites/knight/%s_godot.png" % part_name)
		# 应用偏移
		var info: Dictionary = PART_OFFSETS[part_name]
		sprite.position = Vector3(info["offset"].x * PIXEL_SIZE, -info["offset"].y * PIXEL_SIZE, info["z"] * 0.01)
		sprite.z_index = info["z"]

func _process(delta: float) -> void:
	anim_time += delta
	
	# 更新各动画计时器
	if attack_timer > 0:
		attack_timer = max(0, attack_timer - delta)
	if dodge_timer > 0:
		dodge_timer = max(0, dodge_timer - delta)
	if hurt_timer > 0:
		hurt_timer = max(0, hurt_timer - delta)
	
	# 确定当前动画状态
	if hurt_timer > 0:
		current_state = "hurt"
	elif dodge_timer > 0:
		current_state = "dodge"
	elif attack_timer > 0:
		current_state = "attack"
	else:
		current_state = "idle"  # 默认idle，外部脚本会设为walk
	
	# 执行动画
	match current_state:
		"idle":   _animate_idle()
		"walk":   _animate_walk()
		"attack": _animate_attack()
		"dodge":  _animate_dodge()
		"hurt":   _animate_hurt()
		"jump":   _animate_jump()

# ========== IDLE 呼吸动画 ==========
func _animate_idle() -> void:
	var breathe: float = sin(anim_time * IDLE_SPEED) * IDLE_BREATHE
	var head_bob: float = sin(anim_time * IDLE_SPEED) * 0.8
	
	_reset_legs()
	_reset_arms()
	
	# 身体微微上下呼吸
	body.position.y = _base_y("body") - breathe * PIXEL_SIZE
	# 头部跟随
	head.position.y = _base_y("head") - breathe * PIXEL_SIZE - head_bob * PIXEL_SIZE
	# 手臂微微下垂摆动
	left_arm.rotation_degrees.z = sin(anim_time * IDLE_SPEED * 0.7) * 1.5
	right_arm.rotation_degrees.z = -sin(anim_time * IDLE_SPEED * 0.7) * 1.5

# ========== WALK 行走动画 ==========
func _animate_walk() -> void:
	var t: float = anim_time * WALK_SPEED
	var bob: float = abs(sin(t)) * WALK_BOB
	var leg_swing: float = sin(t) * WALK_LEG_SWING
	var arm_swing: float = sin(t) * WALK_ARM_SWING
	
	# 身体上下摆动
	body.position.y = _base_y("body") - bob * PIXEL_SIZE
	head.position.y = _base_y("head") - bob * PIXEL_SIZE
	
	# 腿前后摆动
	left_leg.rotation_degrees.z = leg_swing
	right_leg.rotation_degrees.z = -leg_swing
	
	# 手臂反向摆动
	left_arm.rotation_degrees.z = -arm_swing
	right_arm.rotation_degrees.z = arm_swing

# ========== ATTACK 攻击动画 ==========
func _animate_attack() -> void:
	var progress: float = 1.0 - (attack_timer / ATTACK_DURATION)
	progress = clamp(progress, 0.0, 1.0)
	
	_reset_legs()
	left_arm.rotation_degrees.z = 0
	
	# 右臂挥剑：从后方举起到前方劈下
	if progress < 0.3:
		# 蓄力：举剑
		right_arm.rotation_degrees.z = lerp(0.0, -ATTACK_SWING * 0.6, progress / 0.3)
	elif progress < 0.6:
		# 劈下
		right_arm.rotation_degrees.z = lerp(-ATTACK_SWING * 0.6, ATTACK_SWING * 0.8, (progress - 0.3) / 0.3)
	else:
		# 回收
		right_arm.rotation_degrees.z = lerp(ATTACK_SWING * 0.8, 0.0, (progress - 0.6) / 0.4)
	
	# 身体前倾
	body.rotation_degrees.z = sin(progress * PI) * 5.0
	head.rotation_degrees.z = sin(progress * PI) * 3.0

func start_attack() -> void:
	attack_timer = ATTACK_DURATION

# ========== DODGE 闪避动画 ==========
func _animate_dodge() -> void:
	var progress: float = 1.0 - (dodge_timer / DODGE_DURATION)
	progress = clamp(progress, 0.0, 1.0)
	
	# 整体下蹲+位移
	var crouch: float = sin(progress * PI) * 8.0
	var shift: float = sin(progress * PI) * DODGE_SHIFT
	
	# 身体下蹲
	body.position.y = _base_y("body") + crouch * PIXEL_SIZE
	head.position.y = _base_y("head") + crouch * PIXEL_SIZE
	
	# 腿弯曲
	left_leg.rotation_degrees.z = sin(progress * PI) * 15.0
	right_leg.rotation_degrees.z = -sin(progress * PI) * 10.0
	
	# 手臂收紧
	left_arm.rotation_degrees.z = sin(progress * PI) * 10.0
	right_arm.rotation_degrees.z = -sin(progress * PI) * 10.0

func start_dodge() -> void:
	dodge_timer = DODGE_DURATION

# ========== HURT 受击动画 ==========
func _animate_hurt() -> void:
	var progress: float = 1.0 - (hurt_timer / HURT_DURATION)
	progress = clamp(progress, 0.0, 1.0)
	
	# 抖动
	var shake: float = sin(progress * PI * 8) * HURT_SHAKE * (1.0 - progress)
	position.x += shake * PIXEL_SIZE
	
	# 受击闪白（配合modulate使用）
	# 外部脚本设置 modulate = Color(10, 10, 10) 然后渐变回白色
	
	# 身体后仰
	body.rotation_degrees.z = sin(progress * PI) * -8.0
	head.rotation_degrees.z = sin(progress * PI) * -10.0

func start_hurt() -> void:
	hurt_timer = HURT_DURATION

# ========== JUMP 跳跃动画 ==========
func _animate_jump() -> void:
	# 腿收起
	left_leg.rotation_degrees.z = 15.0
	right_leg.rotation_degrees.z = -10.0
	
	# 手臂上扬
	left_arm.rotation_degrees.z = -15.0
	right_arm.rotation_degrees.z = 15.0
	
	# 身体微缩（蜷缩感）
	body.position.y = _base_y("body") + 2.0 * PIXEL_SIZE

# ========== 工具函数 ==========
func _base_y(part_name: String) -> float:
	"""获取部件的基础Y位置"""
	return -PART_OFFSETS[part_name]["offset"].y * PIXEL_SIZE

func _reset_legs() -> void:
	left_leg.rotation_degrees.z = 0.0
	right_leg.rotation_degrees.z = 0.0

func _reset_arms() -> void:
	left_arm.rotation_degrees.z = 0.0
	right_arm.rotation_degrees.z = 0.0

func set_facing(right: bool) -> void:
	"""设置朝向（翻转整个骨骼）"""
	facing_right = right
	scale.x = -1.0 if not right else 1.0

func set_walk_state(is_walking: bool) -> void:
	"""外部调用：设置是否在走路"""
	if is_walking and current_state == "idle":
		current_state = "walk"
	elif not is_walking and current_state == "walk":
		current_state = "idle"
