#!/usr/bin/env python3
"""
《代号：传说》像素风精灵图生成器
- 所有精灵图均使用 RGBA 模式，透明背景
- 统一像素画风：战士、木桩、特效
- 64x64 单帧，组合成精灵图表
"""

from PIL import Image, ImageDraw
import os

OUTPUT_DIR = "/home/z/my-project/godot/legend/assets/sprites"

# === 颜色调色板 ===
class Palette:
    # 铠甲 - 暗金色系
    ARMOR_DARK = (60, 45, 30, 255)
    ARMOR_MID = (95, 75, 45, 255)
    ARMOR_LIGHT = (140, 115, 65, 255)
    ARMOR_HIGHLIGHT = (190, 165, 95, 255)
    # 头盔
    HELM_DARK = (50, 40, 30, 255)
    HELM_MID = (80, 65, 45, 255)
    HELM_LIGHT = (120, 100, 60, 255)
    HELM_CREST = (180, 50, 30, 255)
    # 皮肤
    SKIN = (210, 175, 135, 255)
    SKIN_SHADOW = (175, 140, 100, 255)
    # 剑
    BLADE_LIGHT = (200, 210, 220, 255)
    BLADE_MID = (160, 170, 180, 255)
    BLADE_DARK = (100, 110, 120, 255)
    HILT = (100, 70, 35, 255)
    HILT_WRAP = (140, 100, 50, 255)
    # 盾
    SHIELD_DARK = (70, 55, 35, 255)
    SHIELD_MID = (110, 90, 50, 255)
    SHIELD_LIGHT = (150, 125, 70, 255)
    SHIELD_RIM = (180, 155, 90, 255)
    # 靴子
    BOOT_DARK = (40, 30, 20, 255)
    BOOT_MID = (65, 50, 30, 255)
    # 斗篷
    CLOAK_DARK = (80, 30, 25, 255)
    CLOAK_MID = (120, 45, 35, 255)
    CLOAK_LIGHT = (160, 60, 45, 255)
    # 木桩
    WOOD_DARK = (80, 55, 30, 255)
    WOOD_MID = (120, 85, 45, 255)
    WOOD_LIGHT = (155, 115, 65, 255)
    WOOD_HIGHLIGHT = (185, 150, 90, 255)
    ROPE = (150, 130, 90, 255)
    # 特效
    SPARK_WHITE = (255, 255, 240, 255)
    SPARK_YELLOW = (255, 230, 100, 255)
    SPARK_ORANGE = (255, 180, 60, 255)
    PARRY_BLUE = (100, 180, 255, 255)
    PARRY_WHITE = (200, 230, 255, 255)
    RAGE_RED = (255, 80, 40, 255)
    RAGE_ORANGE = (255, 160, 50, 255)


def new_sprite(w=64, h=64):
    return Image.new('RGBA', (w, h), (0, 0, 0, 0))


def fill_rect(img, x, y, w, h, color):
    d = img.load()
    for py in range(y, y + h):
        for px in range(x, x + w):
            if 0 <= px < img.width and 0 <= py < img.height:
                d[px, py] = color


def warrior_idle(frame=0):
    img = new_sprite()
    p = Palette
    breath = [0, -1, 0, 1][frame % 4]
    
    # 靴子
    fill_rect(img, 24, 54, 6, 5, p.BOOT_DARK)
    fill_rect(img, 25, 54, 4, 5, p.BOOT_MID)
    fill_rect(img, 34, 54, 6, 5, p.BOOT_DARK)
    fill_rect(img, 35, 54, 4, 5, p.BOOT_MID)
    
    # 腿甲
    fill_rect(img, 24, 44, 6, 10, p.ARMOR_DARK)
    fill_rect(img, 25, 44, 4, 10, p.ARMOR_MID)
    fill_rect(img, 34, 44, 6, 10, p.ARMOR_DARK)
    fill_rect(img, 35, 44, 4, 10, p.ARMOR_MID)
    fill_rect(img, 23, 44, 2, 3, p.ARMOR_LIGHT)
    fill_rect(img, 33, 44, 2, 3, p.ARMOR_LIGHT)
    
    # 躯干
    fill_rect(img, 22, 28+breath, 20, 16, p.ARMOR_DARK)
    fill_rect(img, 24, 28+breath, 16, 15, p.ARMOR_MID)
    fill_rect(img, 26, 29+breath, 12, 13, p.ARMOR_LIGHT)
    fill_rect(img, 31, 29+breath, 2, 13, p.ARMOR_MID)
    # 肩甲
    fill_rect(img, 18, 28+breath, 6, 6, p.ARMOR_DARK)
    fill_rect(img, 19, 29+breath, 4, 4, p.ARMOR_LIGHT)
    fill_rect(img, 40, 28+breath, 6, 6, p.ARMOR_DARK)
    fill_rect(img, 41, 29+breath, 4, 4, p.ARMOR_LIGHT)
    # 腰带
    fill_rect(img, 22, 42+breath, 20, 2, p.HILT)
    fill_rect(img, 30, 42+breath, 4, 2, p.ARMOR_HIGHLIGHT)
    
    # 头盔
    fill_rect(img, 25, 12+breath, 14, 16, p.HELM_DARK)
    fill_rect(img, 27, 13+breath, 10, 14, p.HELM_MID)
    fill_rect(img, 29, 14+breath, 6, 12, p.HELM_LIGHT)
    fill_rect(img, 29, 19+breath, 6, 2, (20, 15, 10, 255))
    fill_rect(img, 30, 19+breath, 2, 1, (200, 180, 100, 255))
    fill_rect(img, 33, 19+breath, 2, 1, (200, 180, 100, 255))
    # 盔缨
    fill_rect(img, 29, 10+breath, 6, 3, p.HELM_CREST)
    fill_rect(img, 30, 8+breath, 4, 3, p.HELM_CREST)
    fill_rect(img, 31, 7+breath, 2, 2, (200, 70, 50, 255))
    
    # 右臂+剑
    fill_rect(img, 44, 30+breath, 4, 10, p.ARMOR_MID)
    fill_rect(img, 45, 31+breath, 2, 8, p.SKIN)
    fill_rect(img, 45, 40+breath, 2, 4, p.HILT)
    fill_rect(img, 44, 41+breath, 4, 1, p.HILT_WRAP)
    fill_rect(img, 45, 44+breath, 2, 10, p.BLADE_MID)
    fill_rect(img, 45, 44+breath, 1, 10, p.BLADE_LIGHT)
    
    # 左臂
    fill_rect(img, 16, 30+breath, 4, 10, p.ARMOR_MID)
    fill_rect(img, 17, 31+breath, 2, 8, p.SKIN)
    
    # 斗篷
    cloak_sway = [0, 1, 0, -1][frame % 4]
    fill_rect(img, 20+cloak_sway, 34+breath, 3, 12, p.CLOAK_DARK)
    fill_rect(img, 41+cloak_sway, 34+breath, 3, 12, p.CLOAK_DARK)
    
    return img


def warrior_run(frame=0):
    img = new_sprite()
    p = Palette
    
    leg_offsets = [
        (-2, 0, 4, -2),
        (0, -1, 2, 0),
        (4, -2, -2, 0),
        (2, 0, 0, -1),
    ]
    lo = leg_offsets[frame % 4]
    lean = [1, 0, 1, 0][frame % 4]
    
    # 脚
    fill_rect(img, 23+lo[0], 54+lo[1], 6, 5, p.BOOT_DARK)
    fill_rect(img, 24+lo[0], 54+lo[1], 4, 5, p.BOOT_MID)
    fill_rect(img, 33+lo[2], 54+lo[3], 6, 5, p.BOOT_DARK)
    fill_rect(img, 34+lo[2], 54+lo[3], 4, 5, p.BOOT_MID)
    
    # 腿
    fill_rect(img, 24+lo[0], 44+lo[1], 5, 10, p.ARMOR_DARK)
    fill_rect(img, 25+lo[0], 44+lo[1], 3, 10, p.ARMOR_MID)
    fill_rect(img, 34+lo[2], 44+lo[3], 5, 10, p.ARMOR_DARK)
    fill_rect(img, 35+lo[2], 44+lo[3], 3, 10, p.ARMOR_MID)
    
    # 躯干
    fill_rect(img, 22+lean, 28, 20, 16, p.ARMOR_DARK)
    fill_rect(img, 24+lean, 29, 16, 14, p.ARMOR_MID)
    fill_rect(img, 26+lean, 30, 12, 12, p.ARMOR_LIGHT)
    fill_rect(img, 18+lean, 28, 6, 6, p.ARMOR_DARK)
    fill_rect(img, 40+lean, 28, 6, 6, p.ARMOR_DARK)
    
    # 头盔
    fill_rect(img, 25+lean, 12, 14, 16, p.HELM_DARK)
    fill_rect(img, 27+lean, 13, 10, 14, p.HELM_MID)
    fill_rect(img, 29+lean, 14, 6, 12, p.HELM_LIGHT)
    fill_rect(img, 29+lean, 19, 6, 2, (20, 15, 10, 255))
    fill_rect(img, 30+lean, 19, 2, 1, (200, 180, 100, 255))
    fill_rect(img, 33+lean, 19, 2, 1, (200, 180, 100, 255))
    fill_rect(img, 29+lean, 10, 6, 3, p.HELM_CREST)
    fill_rect(img, 30+lean, 8, 4, 3, p.HELM_CREST)
    
    # 右臂+剑
    fill_rect(img, 44+lean, 30, 4, 8, p.ARMOR_MID)
    fill_rect(img, 45+lean, 38, 2, 3, p.HILT)
    fill_rect(img, 45+lean, 41, 2, 8, p.BLADE_MID)
    fill_rect(img, 45+lean, 41, 1, 8, p.BLADE_LIGHT)
    
    # 左臂
    fill_rect(img, 16+lean, 30, 4, 8, p.ARMOR_MID)
    
    # 斗篷
    cloak = [2, 3, 1, 2][frame % 4]
    fill_rect(img, 20+lean-cloak, 34, 3, 14, p.CLOAK_DARK)
    fill_rect(img, 41+lean+cloak, 34, 3, 14, p.CLOAK_DARK)
    
    return img


def warrior_attack(frame=0):
    img = new_sprite()
    p = Palette
    
    lean = [0, 1, 2, 1][frame]
    
    # 脚
    fill_rect(img, 22, 54, 6, 5, p.BOOT_DARK)
    fill_rect(img, 23, 54, 4, 5, p.BOOT_MID)
    fill_rect(img, 34, 54, 6, 5, p.BOOT_DARK)
    fill_rect(img, 35, 54, 4, 5, p.BOOT_MID)
    
    # 腿
    fill_rect(img, 23, 44, 5, 10, p.ARMOR_DARK)
    fill_rect(img, 24, 44, 3, 10, p.ARMOR_MID)
    fill_rect(img, 35, 44, 5, 10, p.ARMOR_DARK)
    fill_rect(img, 36, 44, 3, 10, p.ARMOR_MID)
    
    # 躯干
    fill_rect(img, 22+lean, 28, 20, 16, p.ARMOR_DARK)
    fill_rect(img, 24+lean, 29, 16, 14, p.ARMOR_MID)
    fill_rect(img, 26+lean, 30, 12, 12, p.ARMOR_LIGHT)
    fill_rect(img, 18+lean, 28, 6, 6, p.ARMOR_DARK)
    fill_rect(img, 19+lean, 29, 4, 4, p.ARMOR_LIGHT)
    fill_rect(img, 40+lean, 28, 6, 6, p.ARMOR_DARK)
    fill_rect(img, 41+lean, 29, 4, 4, p.ARMOR_LIGHT)
    
    # 头盔
    fill_rect(img, 25+lean, 12, 14, 16, p.HELM_DARK)
    fill_rect(img, 27+lean, 13, 10, 14, p.HELM_MID)
    fill_rect(img, 29+lean, 14, 6, 12, p.HELM_LIGHT)
    fill_rect(img, 29+lean, 19, 6, 2, (20, 15, 10, 255))
    fill_rect(img, 30+lean, 19, 2, 1, (200, 180, 100, 255))
    fill_rect(img, 33+lean, 19, 2, 1, (200, 180, 100, 255))
    fill_rect(img, 29+lean, 10, 6, 3, p.HELM_CREST)
    fill_rect(img, 30+lean, 8, 4, 3, p.HELM_CREST)
    
    # 右臂+剑 - 不同攻击帧
    if frame == 0:
        fill_rect(img, 44+lean, 24, 4, 6, p.ARMOR_MID)
        fill_rect(img, 44+lean, 20, 4, 4, p.SKIN)
        fill_rect(img, 45, 6, 2, 14, p.BLADE_MID)
        fill_rect(img, 45, 6, 1, 14, p.BLADE_LIGHT)
        fill_rect(img, 44, 18, 4, 2, p.HILT_WRAP)
    elif frame == 1:
        fill_rect(img, 44+lean, 24, 4, 8, p.ARMOR_MID)
        fill_rect(img, 47, 20, 4, 4, p.SKIN)
        fill_rect(img, 49, 18, 2, 14, p.BLADE_MID)
        fill_rect(img, 49, 18, 1, 14, p.BLADE_LIGHT)
        fill_rect(img, 48, 30, 4, 2, p.HILT_WRAP)
    elif frame == 2:
        fill_rect(img, 44+lean, 28, 4, 6, p.ARMOR_MID)
        fill_rect(img, 47, 29, 4, 4, p.SKIN)
        fill_rect(img, 49, 30, 14, 2, p.BLADE_MID)
        fill_rect(img, 49, 30, 14, 1, p.BLADE_LIGHT)
        fill_rect(img, 61, 29, 2, 4, p.BLADE_LIGHT)
        fill_rect(img, 48, 31, 2, 2, p.HILT_WRAP)
        for i in range(3):
            fill_rect(img, 52+i*4, 28, 2, 1, p.SPARK_WHITE)
            fill_rect(img, 54+i*4, 32, 2, 1, p.SPARK_YELLOW)
    else:
        fill_rect(img, 44+lean, 30, 4, 6, p.ARMOR_MID)
        fill_rect(img, 46, 34, 4, 3, p.SKIN)
        fill_rect(img, 48, 36, 2, 10, p.BLADE_MID)
        fill_rect(img, 48, 36, 1, 10, p.BLADE_LIGHT)
        fill_rect(img, 47, 37, 3, 1, p.HILT_WRAP)
    
    # 左臂
    fill_rect(img, 16+lean, 30, 4, 8, p.ARMOR_MID)
    fill_rect(img, 17+lean, 31, 2, 6, p.SKIN)
    
    return img


def warrior_guard(frame=0):
    img = new_sprite()
    p = Palette
    shake = 0 if frame == 0 else 1
    
    # 脚
    fill_rect(img, 22+shake, 54, 6, 5, p.BOOT_DARK)
    fill_rect(img, 23+shake, 54, 4, 5, p.BOOT_MID)
    fill_rect(img, 34+shake, 54, 6, 5, p.BOOT_DARK)
    fill_rect(img, 35+shake, 54, 4, 5, p.BOOT_MID)
    
    # 腿
    fill_rect(img, 23+shake, 44, 5, 10, p.ARMOR_DARK)
    fill_rect(img, 24+shake, 44, 3, 10, p.ARMOR_MID)
    fill_rect(img, 35+shake, 44, 5, 10, p.ARMOR_DARK)
    fill_rect(img, 36+shake, 44, 3, 10, p.ARMOR_MID)
    
    # 躯干
    fill_rect(img, 21+shake, 28, 20, 16, p.ARMOR_DARK)
    fill_rect(img, 23+shake, 29, 16, 14, p.ARMOR_MID)
    fill_rect(img, 25+shake, 30, 12, 12, p.ARMOR_LIGHT)
    fill_rect(img, 17+shake, 28, 6, 6, p.ARMOR_DARK)
    fill_rect(img, 39+shake, 28, 6, 6, p.ARMOR_DARK)
    
    # 头盔
    fill_rect(img, 24+shake, 12, 14, 16, p.HELM_DARK)
    fill_rect(img, 26+shake, 13, 10, 14, p.HELM_MID)
    fill_rect(img, 28+shake, 14, 6, 12, p.HELM_LIGHT)
    fill_rect(img, 28+shake, 19, 6, 2, (20, 15, 10, 255))
    fill_rect(img, 29+shake, 19, 2, 1, (200, 180, 100, 255))
    fill_rect(img, 32+shake, 19, 2, 1, (200, 180, 100, 255))
    fill_rect(img, 28+shake, 10, 6, 3, p.HELM_CREST)
    fill_rect(img, 29+shake, 8, 4, 3, p.HELM_CREST)
    
    # 盾牌
    fill_rect(img, 14+shake, 22, 8, 18, p.SHIELD_DARK)
    fill_rect(img, 15+shake, 23, 6, 16, p.SHIELD_MID)
    fill_rect(img, 16+shake, 24, 4, 14, p.SHIELD_LIGHT)
    fill_rect(img, 17+shake, 25, 2, 12, p.SHIELD_RIM)
    fill_rect(img, 14+shake, 22, 8, 1, p.SHIELD_RIM)
    fill_rect(img, 14+shake, 39, 8, 1, p.SHIELD_RIM)
    
    # 右臂+剑
    fill_rect(img, 42+shake, 26, 4, 8, p.ARMOR_MID)
    fill_rect(img, 43+shake, 27, 2, 6, p.SKIN)
    fill_rect(img, 43+shake, 33, 2, 3, p.HILT)
    fill_rect(img, 43+shake, 36, 2, 8, p.BLADE_MID)
    fill_rect(img, 43+shake, 36, 1, 8, p.BLADE_LIGHT)
    
    # 完美格挡火花
    if frame == 1:
        fill_rect(img, 12, 20, 3, 2, p.PARRY_BLUE)
        fill_rect(img, 10, 22, 2, 2, p.PARRY_WHITE)
        fill_rect(img, 13, 18, 2, 2, p.PARRY_WHITE)
    
    return img


def warrior_jump(frame=0):
    img = new_sprite()
    p = Palette
    
    if frame == 0:
        leg_y = 46
        leg_spread = 0
    else:
        leg_y = 48
        leg_spread = 2
    
    # 脚
    fill_rect(img, 24-leg_spread, leg_y+6, 5, 4, p.BOOT_DARK)
    fill_rect(img, 25-leg_spread, leg_y+6, 3, 4, p.BOOT_MID)
    fill_rect(img, 35+leg_spread, leg_y+6, 5, 4, p.BOOT_DARK)
    fill_rect(img, 36+leg_spread, leg_y+6, 3, 4, p.BOOT_MID)
    
    # 腿
    fill_rect(img, 24-leg_spread, leg_y, 5, 6, p.ARMOR_DARK)
    fill_rect(img, 25-leg_spread, leg_y, 3, 6, p.ARMOR_MID)
    fill_rect(img, 35+leg_spread, leg_y, 5, 6, p.ARMOR_DARK)
    fill_rect(img, 36+leg_spread, leg_y, 3, 6, p.ARMOR_MID)
    
    # 躯干
    fill_rect(img, 22, 26, 20, 16, p.ARMOR_DARK)
    fill_rect(img, 24, 27, 16, 14, p.ARMOR_MID)
    fill_rect(img, 26, 28, 12, 12, p.ARMOR_LIGHT)
    fill_rect(img, 18, 26, 6, 6, p.ARMOR_DARK)
    fill_rect(img, 40, 26, 6, 6, p.ARMOR_DARK)
    
    # 头盔
    fill_rect(img, 25, 10, 14, 16, p.HELM_DARK)
    fill_rect(img, 27, 11, 10, 14, p.HELM_MID)
    fill_rect(img, 29, 12, 6, 12, p.HELM_LIGHT)
    fill_rect(img, 29, 17, 6, 2, (20, 15, 10, 255))
    fill_rect(img, 30, 17, 2, 1, (200, 180, 100, 255))
    fill_rect(img, 33, 17, 2, 1, (200, 180, 100, 255))
    fill_rect(img, 29, 8, 6, 3, p.HELM_CREST)
    fill_rect(img, 30, 6, 4, 3, p.HELM_CREST)
    
    # 右臂+剑
    if frame == 0:
        fill_rect(img, 44, 20, 4, 6, p.ARMOR_MID)
        fill_rect(img, 45, 10, 2, 12, p.BLADE_MID)
        fill_rect(img, 45, 10, 1, 12, p.BLADE_LIGHT)
        fill_rect(img, 44, 20, 4, 2, p.HILT_WRAP)
    else:
        fill_rect(img, 44, 28, 4, 6, p.ARMOR_MID)
        fill_rect(img, 46, 34, 2, 12, p.BLADE_MID)
        fill_rect(img, 46, 34, 1, 12, p.BLADE_LIGHT)
    
    # 左臂
    fill_rect(img, 16, 28, 4, 8, p.ARMOR_MID)
    
    # 斗篷
    fill_rect(img, 20, 32, 3, 12, p.CLOAK_DARK)
    fill_rect(img, 41, 32, 3, 12, p.CLOAK_DARK)
    
    return img


def warrior_hurt(frame=0):
    img = new_sprite()
    p = Palette
    knockback = 2 if frame == 0 else 3
    
    # 脚
    fill_rect(img, 22+knockback, 54, 6, 5, p.BOOT_DARK)
    fill_rect(img, 23+knockback, 54, 4, 5, p.BOOT_MID)
    fill_rect(img, 34+knockback, 54, 6, 5, p.BOOT_DARK)
    fill_rect(img, 35+knockback, 54, 4, 5, p.BOOT_MID)
    
    # 腿
    fill_rect(img, 23+knockback, 44, 5, 10, p.ARMOR_DARK)
    fill_rect(img, 24+knockback, 44, 3, 10, p.ARMOR_MID)
    fill_rect(img, 35+knockback, 44, 5, 10, p.ARMOR_DARK)
    fill_rect(img, 36+knockback, 44, 3, 10, p.ARMOR_MID)
    
    # 躯干
    fill_rect(img, 22+knockback, 30, 20, 14, p.ARMOR_DARK)
    fill_rect(img, 24+knockback, 31, 16, 12, p.ARMOR_MID)
    fill_rect(img, 26+knockback, 32, 12, 10, p.ARMOR_LIGHT)
    fill_rect(img, 18+knockback, 30, 6, 6, p.ARMOR_DARK)
    fill_rect(img, 40+knockback, 30, 6, 6, p.ARMOR_DARK)
    
    # 头盔
    fill_rect(img, 25+knockback, 14, 14, 16, p.HELM_DARK)
    fill_rect(img, 27+knockback, 15, 10, 14, p.HELM_MID)
    fill_rect(img, 29+knockback, 16, 6, 12, p.HELM_LIGHT)
    fill_rect(img, 29+knockback, 21, 3, 2, (255, 200, 100, 255))
    fill_rect(img, 33+knockback, 21, 3, 2, (255, 200, 100, 255))
    fill_rect(img, 29+knockback, 12, 6, 3, p.HELM_CREST)
    fill_rect(img, 30+knockback, 10, 4, 3, p.HELM_CREST)
    
    # 手臂
    fill_rect(img, 14+knockback, 32, 5, 8, p.ARMOR_MID)
    fill_rect(img, 45+knockback, 32, 5, 8, p.ARMOR_MID)
    if frame == 1:
        fill_rect(img, 52+knockback, 38, 2, 10, p.BLADE_MID)
        fill_rect(img, 52+knockback, 38, 1, 10, p.BLADE_LIGHT)
    
    return img


def warrior_skill_war_cry(frame=0):
    img = new_sprite()
    p = Palette
    
    # 基础身体
    fill_rect(img, 24, 54, 6, 5, p.BOOT_DARK)
    fill_rect(img, 25, 54, 4, 5, p.BOOT_MID)
    fill_rect(img, 34, 54, 6, 5, p.BOOT_DARK)
    fill_rect(img, 35, 54, 4, 5, p.BOOT_MID)
    fill_rect(img, 24, 44, 6, 10, p.ARMOR_DARK)
    fill_rect(img, 25, 44, 4, 10, p.ARMOR_MID)
    fill_rect(img, 34, 44, 6, 10, p.ARMOR_DARK)
    fill_rect(img, 35, 44, 4, 10, p.ARMOR_MID)
    
    # 躯干
    fill_rect(img, 22, 28, 20, 16, p.ARMOR_DARK)
    fill_rect(img, 24, 29, 16, 14, p.ARMOR_MID)
    fill_rect(img, 26, 30, 12, 12, p.ARMOR_LIGHT)
    fill_rect(img, 18, 28, 6, 6, p.ARMOR_DARK)
    fill_rect(img, 40, 28, 6, 6, p.ARMOR_DARK)
    
    # 头盔
    fill_rect(img, 25, 10, 14, 16, p.HELM_DARK)
    fill_rect(img, 27, 11, 10, 14, p.HELM_MID)
    fill_rect(img, 29, 12, 6, 12, p.HELM_LIGHT)
    fill_rect(img, 29, 17, 6, 3, (30, 20, 15, 255))
    fill_rect(img, 30, 17, 4, 1, (255, 100, 80, 255))
    fill_rect(img, 29, 8, 6, 3, p.HELM_CREST)
    fill_rect(img, 30, 6, 4, 3, (200, 60, 40, 255))
    
    # 双臂举起
    fill_rect(img, 14, 18, 5, 12, p.ARMOR_MID)
    fill_rect(img, 15, 16, 3, 4, p.SKIN)
    fill_rect(img, 45, 18, 5, 12, p.ARMOR_MID)
    fill_rect(img, 46, 16, 3, 4, p.SKIN)
    
    # 战吼光环
    if frame == 0:
        for i in range(4):
            fill_rect(img, 20+i*4, 24, 2, 2, p.RAGE_ORANGE)
            fill_rect(img, 40-i*4, 24, 2, 2, p.RAGE_RED)
    else:
        for i in range(6):
            fill_rect(img, 16+i*3, 20, 2, 2, p.RAGE_ORANGE)
            fill_rect(img, 44-i*3, 20, 2, 2, p.RAGE_RED)
            fill_rect(img, 22+i*3, 14, 2, 2, p.SPARK_YELLOW)
            fill_rect(img, 38-i*3, 14, 2, 2, p.SPARK_YELLOW)
    
    return img


def warrior_skill_earth_shatter(frame=0):
    img = new_sprite()
    p = Palette
    
    # 脚
    fill_rect(img, 22, 54, 6, 5, p.BOOT_DARK)
    fill_rect(img, 23, 54, 4, 5, p.BOOT_MID)
    fill_rect(img, 34, 54, 6, 5, p.BOOT_DARK)
    fill_rect(img, 35, 54, 4, 5, p.BOOT_MID)
    
    # 腿
    fill_rect(img, 23, 44, 5, 10, p.ARMOR_DARK)
    fill_rect(img, 24, 44, 3, 10, p.ARMOR_MID)
    fill_rect(img, 35, 44, 5, 10, p.ARMOR_DARK)
    fill_rect(img, 36, 44, 3, 10, p.ARMOR_MID)
    
    if frame == 0:
        # 蓄力
        fill_rect(img, 22, 24, 20, 16, p.ARMOR_DARK)
        fill_rect(img, 24, 25, 16, 14, p.ARMOR_MID)
        fill_rect(img, 26, 26, 12, 12, p.ARMOR_LIGHT)
        fill_rect(img, 25, 8, 14, 16, p.HELM_DARK)
        fill_rect(img, 27, 9, 10, 14, p.HELM_MID)
        fill_rect(img, 29, 10, 6, 12, p.HELM_LIGHT)
        fill_rect(img, 29, 6, 6, 3, p.HELM_CREST)
        fill_rect(img, 44, 12, 4, 6, p.ARMOR_MID)
        fill_rect(img, 45, 0, 2, 14, p.BLADE_MID)
        fill_rect(img, 45, 0, 1, 14, p.BLADE_LIGHT)
        fill_rect(img, 44, 2, 4, 2, p.SPARK_YELLOW)
        fill_rect(img, 44, 6, 4, 2, p.RAGE_ORANGE)
    else:
        # 劈下
        fill_rect(img, 22, 28, 20, 16, p.ARMOR_DARK)
        fill_rect(img, 24, 29, 16, 14, p.ARMOR_MID)
        fill_rect(img, 26, 30, 12, 12, p.ARMOR_LIGHT)
        fill_rect(img, 25, 12, 14, 16, p.HELM_DARK)
        fill_rect(img, 27, 13, 10, 14, p.HELM_MID)
        fill_rect(img, 29, 14, 6, 12, p.HELM_LIGHT)
        fill_rect(img, 29, 10, 6, 3, p.HELM_CREST)
        fill_rect(img, 44, 30, 4, 6, p.ARMOR_MID)
        fill_rect(img, 45, 36, 2, 20, p.BLADE_MID)
        fill_rect(img, 45, 36, 1, 20, p.BLADE_LIGHT)
        for i in range(5):
            fill_rect(img, 20+i*6, 56, 3, 3, p.RAGE_ORANGE)
            fill_rect(img, 22+i*6, 54, 2, 2, p.SPARK_YELLOW)
            fill_rect(img, 18+i*6, 58, 2, 2, p.RAGE_RED)
    
    return img


def training_dummy(frame=0):
    img = new_sprite()
    p = Palette
    shake = 1 if frame == 1 else 0
    
    # 底座
    fill_rect(img, 22+shake, 52, 20, 6, p.WOOD_DARK)
    fill_rect(img, 24+shake, 53, 16, 4, p.WOOD_MID)
    
    # 主干
    fill_rect(img, 28+shake, 16, 8, 36, p.WOOD_DARK)
    fill_rect(img, 29+shake, 17, 6, 34, p.WOOD_MID)
    fill_rect(img, 30+shake, 18, 4, 32, p.WOOD_LIGHT)
    
    # 横梁
    fill_rect(img, 18+shake, 24, 28, 4, p.WOOD_DARK)
    fill_rect(img, 19+shake, 25, 26, 2, p.WOOD_MID)
    fill_rect(img, 20+shake, 25, 24, 1, p.WOOD_LIGHT)
    
    # 头部
    fill_rect(img, 26+shake, 8, 12, 10, p.WOOD_DARK)
    fill_rect(img, 27+shake, 9, 10, 8, p.WOOD_MID)
    fill_rect(img, 28+shake, 10, 8, 6, p.WOOD_LIGHT)
    fill_rect(img, 30+shake, 10, 4, 2, p.WOOD_HIGHLIGHT)
    
    # 靶心
    fill_rect(img, 30+shake, 28, 4, 4, p.ROPE)
    fill_rect(img, 31+shake, 29, 2, 2, (200, 60, 40, 255))
    
    # 绳索
    fill_rect(img, 30+shake, 20, 1, 4, p.ROPE)
    fill_rect(img, 33+shake, 20, 1, 4, p.ROPE)
    
    # 受击特效
    if frame == 1:
        fill_rect(img, 14, 22, 4, 2, p.SPARK_YELLOW)
        fill_rect(img, 38, 26, 3, 2, p.SPARK_ORANGE)
        fill_rect(img, 16, 28, 2, 2, p.SPARK_WHITE)
    
    return img


def create_spritesheet(frames, frame_size=64, cols=4):
    count = len(frames)
    rows = (count + cols - 1) // cols
    sheet_w = cols * frame_size
    sheet_h = rows * frame_size
    sheet = Image.new('RGBA', (sheet_w, sheet_h), (0, 0, 0, 0))
    for i, frame in enumerate(frames):
        col = i % cols
        row = i // cols
        sheet.paste(frame, (col * frame_size, row * frame_size))
    return sheet


def create_full_sheet():
    animations = {
        'idle': [warrior_idle(i) for i in range(4)],
        'run': [warrior_run(i) for i in range(4)],
        'attack': [warrior_attack(i) for i in range(4)],
        'guard': [warrior_guard(i) for i in range(2)],
        'jump': [warrior_jump(i) for i in range(2)],
        'hurt': [warrior_hurt(i) for i in range(2)],
        'war_cry': [warrior_skill_war_cry(i) for i in range(2)],
        'earth_shatter': [warrior_skill_earth_shatter(i) for i in range(2)],
    }
    
    total_frames = sum(len(v) for v in animations.values())
    cols = 8
    rows = (total_frames + cols - 1) // cols
    
    full_sheet = Image.new('RGBA', (cols * 64, rows * 64), (0, 0, 0, 0))
    
    frame_idx = 0
    meta = {}
    
    for anim_name, frames in animations.items():
        start_frame = frame_idx
        for frame in frames:
            col = frame_idx % cols
            row = frame_idx // cols
            full_sheet.paste(frame, (col * 64, row * 64))
            frame_idx += 1
        meta[anim_name] = {
            'start_frame': start_frame,
            'frame_count': len(frames),
            'col': start_frame % cols,
            'row': start_frame // cols,
        }
    
    return full_sheet, meta, animations


def main():
    print("=== 《代号：传说》像素精灵图生成器 ===")
    print()
    
    animations = {
        'idle': [warrior_idle(i) for i in range(4)],
        'run': [warrior_run(i) for i in range(4)],
        'attack': [warrior_attack(i) for i in range(4)],
        'guard': [warrior_guard(i) for i in range(2)],
        'jump': [warrior_jump(i) for i in range(2)],
        'hurt': [warrior_hurt(i) for i in range(2)],
        'war_cry': [warrior_skill_war_cry(i) for i in range(2)],
        'earth_shatter': [warrior_skill_earth_shatter(i) for i in range(2)],
    }
    
    player_dir = os.path.join(OUTPUT_DIR, "player")
    enemy_dir = os.path.join(OUTPUT_DIR, "enemy")
    
    for anim_name, frames in animations.items():
        sheet = create_spritesheet(frames, 64, len(frames))
        path = os.path.join(player_dir, f"warrior_{anim_name}_sheet.png")
        sheet.save(path)
        print(f"  保存: warrior_{anim_name}_sheet.png ({sheet.size[0]}x{sheet.size[1]})")
        frames[0].save(os.path.join(player_dir, f"warrior_{anim_name}_64.png"))
    
    full_sheet, meta, _ = create_full_sheet()
    full_path = os.path.join(player_dir, "warrior_full_sheet.png")
    full_sheet.save(full_path)
    print(f"\n  完整精灵图表: warrior_full_sheet.png ({full_sheet.size[0]}x{full_sheet.size[1]})")
    
    meta_path = os.path.join(player_dir, "warrior_sheet_meta.txt")
    with open(meta_path, 'w') as f:
        f.write("# Warrior Sprite Sheet Metadata\n")
        f.write(f"# Sheet size: {full_sheet.size[0]}x{full_sheet.size[1]}\n")
        f.write("# Frame size: 64x64\n\n")
        for name, m in meta.items():
            f.write(f"{name}={m['start_frame']},{m['frame_count']},{m['col']},{m['row']}\n")
    print(f"  元数据: warrior_sheet_meta.txt")
    
    # 训练木桩
    dummy_frames = [training_dummy(i) for i in range(2)]
    dummy_sheet = create_spritesheet(dummy_frames, 64, 2)
    dummy_sheet.save(os.path.join(enemy_dir, "training_dummy_sheet.png"))
    dummy_frames[0].save(os.path.join(enemy_dir, "training_dummy_64.png"))
    print(f"\n  训练木桩: training_dummy_sheet.png (128x64)")
    
    # 验证透明度
    print("\n=== 透明度验证 ===")
    for anim_name, frames in animations.items():
        alpha = frames[0].getchannel('A')
        transparent = sum(1 for p in alpha.getdata() if p == 0)
        total = alpha.width * alpha.height
        pct = transparent / total * 100
        print(f"  {anim_name}: 透明度={pct:.1f}%")
    
    alpha = full_sheet.getchannel('A')
    transparent = sum(1 for p in alpha.getdata() if p == 0)
    total = alpha.width * alpha.height
    print(f"\n  完整图表: 透明度={transparent/total*100:.1f}%")
    
    print("\n=== 生成完成! ===")


if __name__ == '__main__':
    main()
