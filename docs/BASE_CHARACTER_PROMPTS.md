# 《代号：传说》角色资产工作流 v4.0

> 核心管线：ComfyUI立绘 → 混元3D图生3D → Blender调整/装备分件/动画 → Blender To Pixels渲染 → Godot
> 提示词严格遵循 Nova Pixels XL v3.0 官方推荐模板

---

## 一、完整工作流

```
① ComfyUI 生成穿装备的角色立绘（8职业×2性别=16张）
         ↓
② 混元3D 图生3D → 下载GLB
         ↓
③ Blender 导入GLB → 拆分装备mesh/摆动画
         ↓
④ Blender To Pixels 渲染像素精灵
         ↓
⑤ 导入 Godot (Sprite3D + LoongBones骨骼)
```

**为什么不再用"基础体+HY扩展"？**

| 方案 | 问题 |
|------|------|
| 基础体 → HY Instruct加装备 | HY是图生图，会重绘整张图，旧衣物残留/身体变形/性别偏移 |
| 直接生成穿装备的完整角色 ✅ | 混元3D从一张完整图生3D，装备天然贴合身体 |

**基础体图片的作用**：作为混元3D的参考底图，让你知道这个职业的身体比例/姿势应该是什么样的。最终生成的是穿装备的完整角色。

---

## 二、官方模板（不可修改）

### 正面模板
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), {Prompt}, BREAK, depth of field, volumetric lighting
```

### 负面模板
```
modern, recent, old, oldest, anime, illustration, cartoon, graphic, text, painting, crayon, graphite, abstract, glitch, deformed, mutated, ugly, disfigured, long body, lowres, bad anatomy, bad hands, missing fingers, extra digits, fewer digits, cropped, very displeasing, (worst quality, bad quality:1.2), sketch, jpeg artifacts, signature, watermark, username, signature, simple background, conjoined, bad ai-generated
```

### 参数
```
Sampler: Euler a
Steps: 25
Clip Skip: 2
CFG Scale: 5
Size: 1024x1024
```

---

## 三、8职业×2性别 穿装备立绘提示词

> 每个提示词 = 官方模板 + 性别标签 + 完整角色描述（含装备）
> 生成后直接上传混元3D转3D模型

### 3.1 战士 Warrior — 深红 #cc3333

**男性完整正面**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), (1boy:1.5), solo, full body sprite of male warrior, heavy plate armor in dark steel with crimson trim, horned helmet with red plume, greatsword on back, gauntlets with spiked knuckles, steel-toed boots, head up looking forward, upright posture, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character, BREAK, depth of field, volumetric lighting
```

**女性完整正面**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), (1girl:1.5), solo, full body sprite of female warrior, heavy plate armor in dark steel with crimson trim, horned helmet with red plume, greatsword on back, gauntlets with spiked knuckles, steel-toed boots, head up looking forward, upright posture, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character, BREAK, depth of field, volumetric lighting
```

---

### 3.2 游侠 Ranger — 翠绿 #33aa55

**男性完整正面**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), (1boy:1.5), solo, full body sprite of male ranger, leather armor in forest green and brown, longbow on back, quiver with green-fletched arrows, feathered cap, leather bracers, brown boots, head up looking forward, upright posture, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character, BREAK, depth of field, volumetric lighting
```

**女性完整正面**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), (1girl:1.5), solo, full body sprite of female ranger, leather armor in forest green and brown, longbow on back, quiver with green-fletched arrows, feathered cap, leather bracers, brown boots, head up looking forward, upright posture, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character, BREAK, depth of field, volumetric lighting
```

---

### 3.3 刺客 Assassin — 暗紫 #7733cc

**男性完整正面**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), (1boy:1.5), solo, full body sprite of male assassin, dark leather armor in deep purple and black, twin daggers at waist, dark hood with purple inner lining, shadow wrappings on arms, dark boots, head up looking forward, upright posture, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character, BREAK, depth of field, volumetric lighting
```

**女性完整正面**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), (1girl:1.5), solo, full body sprite of female assassin, dark leather armor in deep purple and black, twin daggers at waist, dark hood with purple inner lining, shadow wrappings on arms, dark boots, head up looking forward, upright posture, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character, BREAK, depth of field, volumetric lighting
```

---

### 3.4 法师 Mage — 宝蓝 #3388ff

**男性完整正面**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), (1boy:1.5), solo, full body sprite of male mage, arcane robes in royal blue and silver, staff with glowing blue crystal orb, pointed hat with star pattern, spellbook at hip, dark boots, head up looking forward, upright posture, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character, BREAK, depth of field, volumetric lighting
```

**女性完整正面**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), (1girl:1.5), solo, full body sprite of female mage, arcane robes in royal blue and silver, staff with glowing blue crystal orb, pointed hat with star pattern, spellbook at hip, dark boots, head up looking forward, upright posture, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character, BREAK, depth of field, volumetric lighting
```

---

### 3.5 武僧 Monk — 金黄 #ddaa22

**男性完整正面**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), (1boy:1.5), solo, full body sprite of male monk, martial arts robes in golden yellow and dark brown, fighting gloves with golden knuckles, golden headband, prayer beads on wrist, bare feet with ankle wraps, head up looking forward, upright posture, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character, BREAK, depth of field, volumetric lighting
```

**女性完整正面**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), (1girl:1.5), solo, full body sprite of female monk, martial arts robes in golden yellow and dark brown, fighting gloves with golden knuckles, golden headband, prayer beads on wrist, bare feet with ankle wraps, head up looking forward, upright posture, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character, BREAK, depth of field, volumetric lighting
```

---

### 3.6 骑士 Knight — 银白 #ddddee

**男性完整正面**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), (1boy:1.5), solo, full body sprite of male paladin knight, full plate armor in silver white and holy gold, winged helmet with gold trim, lance on back, kite shield with cross emblem on left arm, white cape with golden border, grey boots, head up looking forward, upright posture, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character, BREAK, depth of field, volumetric lighting
```

**女性完整正面**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), (1girl:1.5), solo, full body sprite of female paladin knight, full plate armor in silver white and holy gold, winged helmet with gold trim, lance on back, kite shield with cross emblem on left arm, white cape with golden border, grey boots, head up looking forward, upright posture, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character, BREAK, depth of field, volumetric lighting
```

---

### 3.7 召唤师 Summoner — 幽青 #22aaaa

**男性完整正面**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), (1boy:1.5), solo, full body sprite of male summoner, necromancer robes in dark teal and ghostly cyan, tattered hooded cloak, soul lantern on chain in right hand, spirit staff with skull orb in left hand, ghostly chains on arms, dark boots, head up looking forward, upright posture, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character, BREAK, depth of field, volumetric lighting
```

**女性完整正面**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), (1girl:1.5), solo, full body sprite of female summoner, necromancer robes in dark teal and ghostly cyan, tattered hooded cloak, soul lantern on chain in right hand, spirit staff with skull orb in left hand, ghostly chains on arms, dark boots, head up looking forward, upright posture, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character, BREAK, depth of field, volumetric lighting
```

---

### 3.8 机关师 Engineer — 古铜 #cc8822

**男性完整正面**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), (1boy:1.5), solo, full body sprite of male engineer, mechanical armor in bronze and amber, toolbox on back, mechanical arm gauntlet on right hand, goggles on forehead, gear decorations, steam vents on shoulders, heavy brown boots, head up looking forward, upright posture, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character, BREAK, depth of field, volumetric lighting
```

**女性完整正面**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), (1girl:1.5), solo, full body sprite of female engineer, mechanical armor in bronze and amber, toolbox on back, mechanical arm gauntlet on right hand, goggles on forehead, gear decorations, steam vents on shoulders, heavy brown boots, head up looking forward, upright posture, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character, BREAK, depth of field, volumetric lighting
```

---

### 通用负面（男性）
```
modern, recent, old, oldest, anime, illustration, cartoon, graphic, text, painting, crayon, graphite, abstract, glitch, deformed, mutated, ugly, disfigured, long body, lowres, bad anatomy, bad hands, missing fingers, extra digits, fewer digits, cropped, very displeasing, (worst quality, bad quality:1.2), sketch, jpeg artifacts, signature, watermark, username, signature, simple background, conjoined, bad ai-generated, 1girl, breasts, feminine, back view, half body, looking down, head down, hunched, slouching
```

### 通用负面（女性）
```
modern, recent, old, oldest, anime, illustration, cartoon, graphic, text, painting, crayon, graphite, abstract, glitch, deformed, mutated, ugly, disfigured, long body, lowres, bad anatomy, bad hands, missing fingers, extra digits, fewer digits, cropped, very displeasing, (worst quality, bad quality:1.2), sketch, jpeg artifacts, signature, watermark, username, signature, simple background, conjoined, bad ai-generated, 1boy, muscular, beard, back view, half body, looking down, head down, hunched, slouching
```

---

## 四、装备分层架构（Blender 3D端实现）

```
穿装备的完整角色3D模型（从混元3D生成）
    ↓ Blender拆分
├── 身体 mesh（基础体，不变）
├── 头盔 mesh（可替换）
├── 胸甲 mesh（可替换）
├── 武器 mesh（可替换）
├── 护腿 mesh（可替换）
├── 鞋子 mesh（可替换）
└── 特效（粒子/发光，饰品）
```

**换装流程**：
1. 混元3D生成"穿A套装"的角色3D
2. Blender里拆分装备mesh
3. 想换B套装 → 生成"穿B套装"的角色3D → 拆出B装备mesh → 替换A装备mesh
4. 身体mesh始终不变（或从基础体3D获取）

---

## 五、混元3D操作步骤

1. 打开 `3d.hunyuan.tencent.com`
2. 选择「图生3D」
3. 上传 ComfyUI 生成的穿装备角色立绘
4. 等待生成（约1-2分钟）
5. 下载 GLB 格式

---

## 六、性别强化速查

| 问题 | 修复 |
|------|------|
| 男性出女性 | 正面加 `(1boy:1.5)`, 负面加 `1girl, breasts, feminine` |
| 权重不够 | `(1boy:1.5)` → `(1boy:1.8)` |
| 还是不行 | 追加 `(flat chest:1.3), (no breasts:1.3)` |

---

## 七、后处理管线

```
1. ComfyUI 生成 1024×1024 立绘
2. 上传混元3D → 下载GLB
3. Blender 导入GLB → 拆分装备mesh / 摆动画
4. Blender To Pixels 渲染像素精灵
5. 6 部位分件 (head/body/right_arm/left_arm/right_leg/left_leg)
6. LoongBones 骨骼绑定
7. 导入 Godot (Sprite3D)
```
