# 《代号：传说》角色资产工作流 v3.0

> 核心管线：ComfyUI立绘 → 混元3D图生3D → Blender调整/装备分件/动画 → Blender To Pixels渲染 → Godot
> 提示词严格遵循 Nova Pixels XL v3.0 官方推荐模板

---

## 一、完整工作流

```
① ComfyUI + Nova Pixels XL v3.0 生成立绘
         ↓
② 混元3D 2.5 图生3D → 下载GLB
         ↓
③ Blender 导入GLB → 装备分件/摆动画/Q版调整
         ↓
④ Blender To Pixels 插件 → 渲染成像素精灵
         ↓
⑤ 导入 Godot (Sprite3D + LoongBones骨骼)
```

| 步骤 | 工具 | 解决的问题 | 一致性 |
|------|------|-----------|--------|
| ① 立绘 | ComfyUI + Nova Pixels XL | 概念设计、风格定义 | ⭐⭐⭐ |
| ② 图生3D | 混元3D 2.5 (3d.hunyuan.tencent.com) | 立绘→3D模型，解决AI随机性 | ⭐⭐⭐⭐⭐ |
| ③ 3D调整 | Blender | 装备分件、摆姿势、做动画 | ⭐⭐⭐⭐⭐ |
| ④ 像素渲染 | Blender To Pixels (免费插件) | 3D→像素精灵，统一风格 | ⭐⭐⭐⭐⭐ |

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

## 三、基础体提示词（1男 + 1女）

> 核心思路：8职业共用2个基础体（裸模/内衣），职业差异全靠装备层叠加
> 生成后上传混元3D转3D模型，之后所有换装/动画都在Blender里做

### 3.1 男·基础体

**{Prompt}**：
```
(1boy:1.5), solo, full body sprite of male human, plain linen underwear, bare arms and legs, short brown hair, head up looking forward, upright posture, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character
```

**完整正面**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), (1boy:1.5), solo, full body sprite of male human, plain linen underwear, bare arms and legs, short brown hair, head up looking forward, upright posture, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character, BREAK, depth of field, volumetric lighting
```

**负面（官方 + 性别反制 + 姿势反制 + 装备反制）**：
```
modern, recent, old, oldest, anime, illustration, cartoon, graphic, text, painting, crayon, graphite, abstract, glitch, deformed, mutated, ugly, disfigured, long body, lowres, bad anatomy, bad hands, missing fingers, extra digits, fewer digits, cropped, very displeasing, (worst quality, bad quality:1.2), sketch, jpeg artifacts, signature, watermark, username, signature, simple background, conjoined, bad ai-generated, 1girl, breasts, feminine, back view, half body, looking down, head down, hunched, slouching, armor, weapon, helmet, cape, boots, gauntlet, shield, equipment, decoration
```

### 3.2 女·基础体

**{Prompt}**：
```
(1girl:1.5), solo, full body sprite of female human, plain linen underwear, bare arms and legs, long brown hair, head up looking forward, upright posture, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character
```

**完整正面**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), (1girl:1.5), solo, full body sprite of female human, plain linen underwear, bare arms and legs, long brown hair, head up looking forward, upright posture, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character, BREAK, depth of field, volumetric lighting
```

**负面（官方 + 性别反制 + 姿势反制 + 装备反制）**：
```
modern, recent, old, oldest, anime, illustration, cartoon, graphic, text, painting, crayon, graphite, abstract, glitch, deformed, mutated, ugly, disfigured, long body, lowres, bad anatomy, bad hands, missing fingers, extra digits, fewer digits, cropped, very displeasing, (worst quality, bad quality:1.2), sketch, jpeg artifacts, signature, watermark, username, signature, simple background, conjoined, bad ai-generated, 1boy, muscular, beard, back view, half body, looking down, head down, hunched, slouching, armor, weapon, helmet, cape, boots, gauntlet, shield, equipment, decoration
```

---

## 四、装备层提示词（独立生成，叠加到基础体）

> 每个装备只画对应部位，不含角色身体，上传混元3D后作为独立3D部件

### 4.1 头盔

**战士·角盔**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), horned helmet in crimson red and dark steel, red plume on top, front 3/4 angle facing camera, dark background, no face no body, equipment overlay sprite, BREAK, depth of field, volumetric lighting
```

**法师·尖帽**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), royal blue pointed hat with silver star pattern, front 3/4 angle facing camera, dark background, no face no body, equipment overlay sprite, BREAK, depth of field, volumetric lighting
```

**游侠·羽帽**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), feathered cap in forest green with brown leather band, front 3/4 angle facing camera, dark background, no face no body, equipment overlay sprite, BREAK, depth of field, volumetric lighting
```

**刺客·暗兜**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), dark hood with purple inner lining, front 3/4 angle facing camera, dark background, no face no body, equipment overlay sprite, BREAK, depth of field, volumetric lighting
```

**武僧·金箍**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), golden headband with engraved rune, front 3/4 angle facing camera, dark background, no face no body, equipment overlay sprite, BREAK, depth of field, volumetric lighting
```

**骑士·翼盔**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), winged helmet in silver white with gold trim, front 3/4 angle facing camera, dark background, no face no body, equipment overlay sprite, BREAK, depth of field, volumetric lighting
```

**召唤师·魂兜**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), tattered hood in dark teal with ghostly cyan glow, front 3/4 angle facing camera, dark background, no face no body, equipment overlay sprite, BREAK, depth of field, volumetric lighting
```

**机关师·护目**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), brass goggles on forehead with amber lenses and gear decorations, front 3/4 angle facing camera, dark background, no face no body, equipment overlay sprite, BREAK, depth of field, volumetric lighting
```

### 4.2 胸甲

**战士·板甲**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), heavy plate armor in dark steel with crimson trim, front 3/4 angle facing camera, dark background, no head no arms no legs, torso equipment overlay, BREAK, depth of field, volumetric lighting
```

**法师·奥术袍**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), arcane robes in royal blue and silver, front 3/4 angle facing camera, dark background, no head no arms no legs, torso equipment overlay, BREAK, depth of field, volumetric lighting
```

**游侠·皮甲**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), leather armor in forest green and brown, front 3/4 angle facing camera, dark background, no head no arms no legs, torso equipment overlay, BREAK, depth of field, volumetric lighting
```

**刺客·暗皮甲**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), dark leather armor in deep purple and black, front 3/4 angle facing camera, dark background, no head no arms no legs, torso equipment overlay, BREAK, depth of field, volumetric lighting
```

**武僧·武袍**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), martial arts sleeveless top in golden yellow and dark brown, front 3/4 angle facing camera, dark background, no head no arms no legs, torso equipment overlay, BREAK, depth of field, volumetric lighting
```

**骑士·圣甲**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), full plate armor in silver white and holy gold, front 3/4 angle facing camera, dark background, no head no arms no legs, torso equipment overlay, BREAK, depth of field, volumetric lighting
```

**召唤师·冥袍**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), necromancer robes in dark teal and ghostly cyan, front 3/4 angle facing camera, dark background, no head no arms no legs, torso equipment overlay, BREAK, depth of field, volumetric lighting
```

**机关师·机甲**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), mechanical armor in bronze and amber, front 3/4 angle facing camera, dark background, no head no arms no legs, torso equipment overlay, BREAK, depth of field, volumetric lighting
```

### 4.3 武器

**战士·巨剑**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), large iron greatsword with red leather grip and steel crossguard, front 3/4 angle facing camera, dark background, no character, weapon sprite, BREAK, depth of field, volumetric lighting
```

**法师·法杖**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), wooden staff with glowing blue crystal orb top, front 3/4 angle facing camera, dark background, no character, weapon sprite, BREAK, depth of field, volumetric lighting
```

**游侠·长弓**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), curved wooden longbow with green vine wrapping, front 3/4 angle facing camera, dark background, no character, weapon sprite, BREAK, depth of field, volumetric lighting
```

**刺客·双匕**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), twin daggers with curved dark blades and purple gem pommel, front 3/4 angle facing camera, dark background, no character, weapon sprite, BREAK, depth of field, volumetric lighting
```

**武僧·拳套**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), fighting gauntlets with golden knuckle plates, front 3/4 angle facing camera, dark background, no character, weapon sprite, BREAK, depth of field, volumetric lighting
```

**骑士·圣枪**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), holy lance in silver with gold tip, front 3/4 angle facing camera, dark background, no character, weapon sprite, BREAK, depth of field, volumetric lighting
```

**召唤师·魂灯**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), soul lantern on chain with spectral teal flame, front 3/4 angle facing camera, dark background, no character, weapon sprite, BREAK, depth of field, volumetric lighting
```

**机关师·机械臂**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), mechanical arm gauntlet in bronze with amber glow, front 3/4 angle facing camera, dark background, no character, weapon sprite, BREAK, depth of field, volumetric lighting
```

### 4.4 盾牌（骑士专属）

**骑士·鸢盾**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), kite shield with silver cross emblem and gold border, front 3/4 angle facing camera, dark background, no character, shield sprite, BREAK, depth of field, volumetric lighting
```

### 4.5 装备层通用负面

```
modern, recent, old, oldest, anime, illustration, cartoon, graphic, text, painting, crayon, graphite, abstract, glitch, deformed, mutated, ugly, disfigured, long body, lowres, bad anatomy, bad hands, missing fingers, extra digits, fewer digits, cropped, very displeasing, (worst quality, bad quality:1.2), sketch, jpeg artifacts, signature, watermark, username, signature, simple background, conjoined, bad ai-generated, full character, face, skin, body, person, character wearing equipment, hands, legs, feet
```

---

## 五、装备分层架构

```
基础身体（裸模/内衣）→ 固定不变，1男+1女
    + 头盔层          → 替换 head 分件
    + 胸甲层          → 替换 body 分件
    + 武器层          → 替换 right_arm 分件
    + 盾牌层          → 替换 left_arm 分件（骑士）
    + 护腿层          → 替换 right_leg + left_leg 分件
    + 鞋子层          → 替换 legs 下部分件
    + 特效层          → 粒子/发光（饰品，不换贴图）
```

### 资产量对比

| | 旧方案 | 新方案 |
|---|---|---|
| 角色 | 16个完整角色 | 2个基础体 |
| 装备 | 绑定在角色上 | N套独立装备层 |
| 换装 | 重画角色 | 换overlay |
| 一致性 | 每次AI生成不同 | 3D模型完全一致 |

---

## 六、混元3D操作步骤

### 第1步：立绘→3D
1. 打开 `3d.hunyuan.tencent.com`
2. 选择「图生3D」
3. 上传 ComfyUI 生成的角色立绘
4. 等待生成（约1-2分钟）
5. 下载 GLB 格式

### 第2步：Blender处理
1. Blender 导入 GLB
2. 安装 **Blender To Pixels** 插件（`astropulse.itch.io/blender-to-pixels`）
3. 摄像机角度设为 3/4 侧视角（匹配2.5D）
4. 像素化参数设为 128×128 等效
5. 逐帧渲染 idle/walk/attack 等动画
6. 导出 sprite sheet

### 第3步：装备系统
1. Blender 里按 head/body/arms/legs 分组
2. 换装备 = 换对应部件的3D模型 → 重新渲染
3. 天然分件，纹理替换，像素级一致

---

## 七、性别强化速查

| 问题 | 修复 |
|------|------|
| 男性出女性 | 正面加 `(1boy:1.5)`, 负面加 `1girl, breasts, feminine` |
| 权重不够 | `(1boy:1.5)` → `(1boy:1.8)` |
| 还是不行 | 追加 `(flat chest:1.3), (no breasts:1.3)` |

---

## 八、后处理管线

```
1. ComfyUI 生成 1024×1024 立绘
2. 上传混元3D → 下载GLB
3. Blender 导入GLB → 装备分件/摆动画
4. Blender To Pixels 渲染像素精灵
5. 6 部位分件 (head/body/right_arm/left_arm/right_leg/left_leg)
6. LoongBones 骨骼绑定
7. 导入 Godot (Sprite3D)
```
