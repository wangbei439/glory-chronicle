# 《代号：传说》无装备素体角色提示词 v1.0

> 核心原则：素体 = 无职业装备、仅穿朴素衣物、仅靠职业主色丝带/腰带辨识
> 性别强化：使用 Danbooru 标签 `(1boy:1.5)` / `(1girl:1.5)` 强制性别，正面+负面双保险

---

## 一、通用模板

### 1.1 男性正面提示词骨架

```
(pixel art, dithering, pixelated, sprite art, 8-bit:1.2), masterpiece, best quality, (1boy:1.5), solo, male, full body full length sprite of {职业} base character, chibi, 2-head tall, A-pose, standing on ground with feet visible, front 3/4 angle viewed from left, face and chest clearly visible facing camera, body oriented toward right side of frame, boyish face, flat chest, broad shoulders, masculine features, no breasts, {发型}, {朴素衣物描述}, {职业主色丝带/腰带}, stubby boots visible, dark fantasy style, black background, high contrast, clear silhouette
```

### 1.2 女性正面提示词骨架

```
(pixel art, dithering, pixelated, sprite art, 8-bit:1.2), masterpiece, best quality, (1girl:1.5), solo, female, full body full length sprite of {职业} base character, chibi, 2-head tall, A-pose, standing on ground with feet visible, front 3/4 angle viewed from left, face and chest clearly visible facing camera, body oriented toward right side of frame, feminine face, slender build, {发型}, {朴素衣物描述}, {职业主色丝带/腰带}, stubby boots visible, dark fantasy style, black background, high contrast, clear silhouette
```

### 1.3 通用负面提示词（男女共用）

```
modern, recent, anime, illustration, cartoon, graphic, text, painting, abstract, glitch, deformed, mutated, ugly, disfigured, long body, lowres, bad anatomy, bad hands, missing fingers, extra digits, cropped, very displeasing, (worst quality, bad quality:1.2), sketch, jpeg artifacts, signature, watermark, username, simple background, conjoined, bad ai-generated, back view, rear view, facing away, from behind, showing back, half body, upper body only, cropped body, cut off, no legs, no feet, close-up, portrait, head shot, bust shot, waist up, weapon, sword, axe, bow, staff, shield, armor, helmet, plate armor, chainmail, heavy armor, weapon on back
```

### 1.4 男性专用负面提示词（追加到通用负面之后）

```
1girl, female, woman, girl, breasts, feminine, girly, long eyelashes, lipstick, curvy, hourglass figure, feminine hips, makeup, dress, skirt, long flowing hair on male
```

### 1.5 女性专用负面提示词（追加到通用负面之后）

```
1boy, male, man, boy, muscular, broad shoulders, flat chest, masculine, facial hair, beard, mustache, stubble, macho
```

---

## 二、8职业 × 2性别 无装备素体提示词

> 素体原则：
> - 仅穿最朴素衣物（亚麻上衣+长裤+短靴）
> - 唯一职业辨识 = 腰间系一条职业主色丝带/腰带
> - 无武器、无盔甲、无帽子、无职业专属装备
> - 男女仅发型/体型/性别锚点不同，衣物款式基本一致

---

### 2.1 战士 Warrior — 主色：深红 #cc3333

**男性**：
```
(pixel art, dithering, pixelated, sprite art, 8-bit:1.2), masterpiece, best quality, (1boy:1.5), solo, male, full body full length sprite of warrior base character, chibi, 2-head tall, A-pose, standing on ground with feet visible, front 3/4 angle viewed from left, face and chest clearly visible facing camera, body oriented toward right side of frame, boyish face, flat chest, broad shoulders, masculine features, no breasts, short spiky red-tinted hair, determined eyes, plain linen shirt in off-white, simple brown trousers, crimson red sash tied at waist, leather belt, stubby brown boots visible, bare hands no gloves, no weapon, no armor, dark fantasy style, black background, high contrast, vibrant crimson accent on sash, clear silhouette
```

**女性**：
```
(pixel art, dithering, pixelated, sprite art, 8-bit:1.2), masterpiece, best quality, (1girl:1.5), solo, female, full body full length sprite of warrior base character, chibi, 2-head tall, A-pose, standing on ground with feet visible, front 3/4 angle viewed from left, face and chest clearly visible facing camera, body oriented toward right side of frame, feminine face, slender build, short red-tinted hair in ponytail, determined eyes, plain linen shirt in off-white, simple brown trousers, crimson red sash tied at waist, leather belt, stubby brown boots visible, bare hands no gloves, no weapon, no armor, dark fantasy style, black background, high contrast, vibrant crimson accent on sash, clear silhouette
```

---

### 2.2 游侠 Ranger — 主色：翠绿 #33aa55

**男性**：
```
(pixel art, dithering, pixelated, sprite art, 8-bit:1.2), masterpiece, best quality, (1boy:1.5), solo, male, full body full length sprite of ranger base character, chibi, 2-head tall, A-pose, standing on ground with feet visible, front 3/4 angle viewed from left, face and chest clearly visible facing camera, body oriented toward right side of frame, boyish face, flat chest, lean athletic build, no breasts, short messy brown hair with green tint, keen eyes, plain linen shirt in light tan, simple dark green trousers, forest green sash tied at waist, leather belt, stubby brown boots visible, bare hands no gloves, no weapon, no armor, no bow, no quiver, dark fantasy style, black background, high contrast, vibrant green accent on sash, clear silhouette
```

**女性**：
```
(pixel art, dithering, pixelated, sprite art, 8-bit:1.2), masterpiece, best quality, (1girl:1.5), solo, female, full body full length sprite of ranger base character, chibi, 2-head tall, A-pose, standing on ground with feet visible, front 3/4 angle viewed from left, face and chest clearly visible facing camera, body oriented toward right side of frame, feminine face, slender build, long brown hair in braid with green ribbon, keen eyes, plain linen shirt in light tan, simple dark green trousers, forest green sash tied at waist, leather belt, stubby brown boots visible, bare hands no gloves, no weapon, no armor, no bow, no quiver, dark fantasy style, black background, high contrast, vibrant green accent on sash, clear silhouette
```

---

### 2.3 刺客 Assassin — 主色：暗紫 #7733cc

**男性**：
```
(pixel art, dithering, pixelated, sprite art, 8-bit:1.2), masterpiece, best quality, (1boy:1.5), solo, male, full body full length sprite of assassin base character, chibi, 2-head tall, A-pose, standing on ground with feet visible, front 3/4 angle viewed from left, face and chest clearly visible facing camera, body oriented toward right side of frame, boyish face, flat chest, slim agile build, no breasts, short dark hair with purple tint covering one eye, sharp eyes, plain dark linen shirt in charcoal, simple black trousers, dark purple sash tied at waist, leather belt, stubby dark boots visible, bare hands no gloves, no weapon, no daggers, no armor, no mask, no hood, dark fantasy style, black background, high contrast, vibrant purple accent on sash, clear silhouette
```

**女性**：
```
(pixel art, dithering, pixelated, sprite art, 8-bit:1.2), masterpiece, best quality, (1girl:1.5), solo, female, full body full length sprite of assassin base character, chibi, 2-head tall, A-pose, standing on ground with feet visible, front 3/4 angle viewed from left, face and chest clearly visible facing camera, body oriented toward right side of frame, feminine face, slender build, long dark hair with purple tint in twin tails, sharp eyes, plain dark linen shirt in charcoal, simple black trousers, dark purple sash tied at waist, leather belt, stubby dark boots visible, bare hands no gloves, no weapon, no daggers, no armor, no mask, no hood, dark fantasy style, black background, high contrast, vibrant purple accent on sash, clear silhouette
```

---

### 2.4 法师 Mage — 主色：宝蓝 #3388ff

**男性**：
```
(pixel art, dithering, pixelated, sprite art, 8-bit:1.2), masterpiece, best quality, (1boy:1.5), solo, male, full body full length sprite of mage base character, chibi, 2-head tall, A-pose, standing on ground with feet visible, front 3/4 angle viewed from left, face and chest clearly visible facing camera, body oriented toward right side of frame, boyish face, flat chest, slender tall frame, no breasts, medium length blue-tinted hair tied back in small ponytail, thoughtful eyes, plain linen robe-shirt in pale grey, simple dark blue trousers, royal blue sash tied at waist, leather belt, stubby dark boots visible, bare hands no gloves, no weapon, no staff, no spellbook, no hat, no armor, dark fantasy style, black background, high contrast, vibrant blue accent on sash, clear silhouette
```

**女性**：
```
(pixel art, dithering, pixelated, sprite art, 8-bit:1.2), masterpiece, best quality, (1girl:1.5), solo, female, full body full length sprite of mage base character, chibi, 2-head tall, A-pose, standing on ground with feet visible, front 3/4 angle viewed from left, face and chest clearly visible facing camera, body oriented toward right side of frame, feminine face, slender build, long blue-tinted hair in flowing style with hairpin, thoughtful eyes, plain linen robe-shirt in pale grey, simple dark blue trousers, royal blue sash tied at waist, leather belt, stubby dark boots visible, bare hands no gloves, no weapon, no staff, no spellbook, no hat, no armor, dark fantasy style, black background, high contrast, vibrant blue accent on sash, clear silhouette
```

---

### 2.5 武僧 Monk — 主色：金黄 #ddaa22

**男性**：
```
(pixel art, dithering, pixelated, sprite art, 8-bit:1.2), masterpiece, best quality, (1boy:1.5), solo, male, full body full length sprite of monk base character, chibi, 2-head tall, A-pose, standing on ground with feet visible, front 3/4 angle viewed from left, face and chest clearly visible facing camera, body oriented toward right side of frame, boyish face, flat chest, toned muscular build, no breasts, short buzz cut with golden headband, calm resolute eyes, plain sleeveless linen top in off-white, simple dark brown trousers, golden yellow sash tied at waist, leather belt, bare feet with ankle wraps visible, bare hands no gloves, no weapon, no gauntlets, no armor, dark fantasy style, black background, high contrast, vibrant gold accent on sash and headband, clear silhouette
```

**女性**：
```
(pixel art, dithering, pixelated, sprite art, 8-bit:1.2), masterpiece, best quality, (1girl:1.5), solo, female, full body full length sprite of monk base character, chibi, 2-head tall, A-pose, standing on ground with feet visible, front 3/4 angle viewed from left, face and chest clearly visible facing camera, body oriented toward right side of frame, feminine face, toned slender build, short hair tied in topknot with golden headband, calm resolute eyes, plain sleeveless linen top in off-white, simple dark brown trousers, golden yellow sash tied at waist, leather belt, bare feet with ankle wraps visible, bare hands no gloves, no weapon, no gauntlets, no armor, dark fantasy style, black background, high contrast, vibrant gold accent on sash and headband, clear silhouette
```

---

### 2.6 骑士 Knight — 主色：银白 #ddddee

**男性**：
```
(pixel art, dithering, pixelated, sprite art, 8-bit:1.2), masterpiece, best quality, (1boy:1.5), solo, male, full body full length sprite of knight base character, chibi, 2-head tall, A-pose, standing on ground with feet visible, front 3/4 angle viewed from left, face and chest clearly visible facing camera, body oriented toward right side of frame, boyish face, flat chest, strong broad build, no breasts, short neat silver-white hair, noble eyes, plain linen shirt in pale white, simple grey trousers, silver-white sash tied at waist, leather belt, stubby grey boots visible, bare hands no gloves, no weapon, no lance, no shield, no armor, no helmet, dark fantasy style, black background, high contrast, vibrant silver-white accent on sash, clear silhouette
```

**女性**：
```
(pixel art, dithering, pixelated, sprite art, 8-bit:1.2), masterpiece, best quality, (1girl:1.5), solo, female, full body full length sprite of knight base character, chibi, 2-head tall, A-pose, standing on ground with feet visible, front 3/4 angle viewed from left, face and chest clearly visible facing camera, body oriented toward right side of frame, feminine face, strong slender build, long silver-white hair in neat braid, noble eyes, plain linen shirt in pale white, simple grey trousers, silver-white sash tied at waist, leather belt, stubby grey boots visible, bare hands no gloves, no weapon, no lance, no shield, no armor, no helmet, dark fantasy style, black background, high contrast, vibrant silver-white accent on sash, clear silhouette
```

---

### 2.7 召唤师 Summoner — 主色：幽青 #22aaaa

**男性**：
```
(pixel art, dithering, pixelated, sprite art, 8-bit:1.2), masterpiece, best quality, (1boy:1.5), solo, male, full body full length sprite of summoner base character, chibi, 2-head tall, A-pose, standing on ground with feet visible, front 3/4 angle viewed from left, face and chest clearly visible facing camera, body oriented toward right side of frame, boyish face, flat chest, thin pale frame, no breasts, medium length teal-tinted hair messy and covering forehead, eerie calm eyes, plain dark linen shirt in dark grey, simple black trousers, dark teal sash tied at waist, leather belt, stubby dark boots visible, bare hands no gloves, no weapon, no staff, no lantern, no skull, no armor, no cloak, dark fantasy style, black background, high contrast, vibrant teal accent on sash, clear silhouette
```

**女性**：
```
(pixel art, dithering, pixelated, sprite art, 8-bit:1.2), masterpiece, best quality, (1girl:1.5), solo, female, full body full length sprite of summoner base character, chibi, 2-head tall, A-pose, standing on ground with feet visible, front 3/4 angle viewed from left, face and chest clearly visible facing camera, body oriented toward right side of frame, feminine face, slender pale build, long teal-tinted hair loose and messy, eerie calm eyes, plain dark linen shirt in dark grey, simple black trousers, dark teal sash tied at waist, leather belt, stubby dark boots visible, bare hands no gloves, no weapon, no staff, no lantern, no skull, no armor, no cloak, dark fantasy style, black background, high contrast, vibrant teal accent on sash, clear silhouette
```

---

### 2.8 机关师 Engineer — 主色：古铜 #cc8822

**男性**：
```
(pixel art, dithering, pixelated, sprite art, 8-bit:1.2), masterpiece, best quality, (1boy:1.5), solo, male, full body full length sprite of engineer base character, chibi, 2-head tall, A-pose, standing on ground with feet visible, front 3/4 angle viewed from left, face and chest clearly visible facing camera, body oriented toward right side of frame, boyish face, flat chest, stocky broad build, no breasts, short scruffy brown hair with amber tint, inventive eyes, plain linen shirt in tan brown, simple dark brown trousers, bronze-orange sash tied at waist, leather belt, stubby heavy brown boots visible, bare hands no gloves, no weapon, no toolbox, no goggles, no mechanical arm, no gear, no armor, dark fantasy style, black background, high contrast, vibrant bronze-orange accent on sash, clear silhouette
```

**女性**：
```
(pixel art, dithering, pixelated, sprite art, 8-bit:1.2), masterpiece, best quality, (1girl:1.5), solo, female, full body full length sprite of engineer base character, chibi, 2-head tall, A-pose, standing on ground with feet visible, front 3/4 angle viewed from left, face and chest clearly visible facing camera, body oriented toward right side of frame, feminine face, compact slender build, medium brown hair with amber tint in messy bun held by gear pin, inventive eyes, plain linen shirt in tan brown, simple dark brown trousers, bronze-orange sash tied at waist, leather belt, stubby heavy brown boots visible, bare hands no gloves, no weapon, no toolbox, no goggles, no mechanical arm, no gear, no armor, dark fantasy style, black background, high contrast, vibrant bronze-orange accent on sash, clear silhouette
```

---

## 三、ComfyUI 参数设置

| 参数 | 值 | 说明 |
|------|-----|------|
| 模型 | Nova Pixels XL v3.0 | Illustrious 架构 |
| 采样器 | Euler a | - |
| 步数 | 25 | - |
| Clip Skip | 2 | - |
| CFG Scale | 5 | - |
| 尺寸 | 1024×1024 | - |

---

## 四、性别强化关键要点

### 4.1 为什么之前的 "male" 不起作用？

| 问题 | 原因 | 修复 |
|------|------|------|
| 写 male 还是出女性 | Illustrious 用 Danbooru 标签，`male` 不是有效性别标签 | 改用 `(1boy:1.5)` |
| 男性角色有胸部 | 模型默认给角色加女性特征 | 正面加 `flat chest, no breasts`，负面加 `breasts, feminine` |
| 男性角色像女孩脸 | 训练集中男性样本太少 | 正面加 `boyish face, angular jaw, masculine features` |
| 男性角色长发裙装 | 模型倾向于女性化设计 | 明确指定 `short hair` + `trousers`，负面加 `dress, skirt` |

### 4.2 权重调整建议

如果仍然偏女性，可逐步加大权重：
- 轻度偏女：`(1boy:1.5)` → `(1boy:1.8)`
- 严重偏女：额外加 `(flat chest:1.3), (no breasts:1.3), (masculine:1.2)`
- 极端情况：CFG 从5提到7，增加性别标签权重

### 4.3 男女发型对照表

| 职业 | 男性发型 | 女性发型 |
|------|----------|----------|
| 战士 | short spiky red-tinted hair | short red-tinted hair in ponytail |
| 游侠 | short messy brown hair with green tint | long brown hair in braid with green ribbon |
| 刺客 | short dark hair with purple tint covering one eye | long dark hair with purple tint in twin tails |
| 法师 | medium length blue-tinted hair tied back in small ponytail | long blue-tinted hair flowing with hairpin |
| 武僧 | short buzz cut | short hair tied in topknot |
| 骑士 | short neat silver-white hair | long silver-white hair in neat braid |
| 召唤师 | medium length teal-tinted hair messy | long teal-tinted hair loose and messy |
| 机关师 | short scruffy brown hair with amber tint | medium brown hair in messy bun with gear pin |

---

## 五、素体设计理念

### 5.1 为什么素体只保留丝带/腰带？

装备分层系统的核心是：**角色素体 + 装备层 = 最终显示**。如果素体本身就穿了职业装备（盔甲、武器、帽子），那么装备层就无法替换——换装时旧装备和新装备会叠加。

素体的唯一辨识来源：
1. **腰间丝带颜色** = 职业主色（不可更换，代表角色本质）
2. **发色微调** = 职业辅色偏移（极其微妙，几乎看不出）
3. 其他一切 = 朴素通用衣物，可被装备层完全覆盖

### 5.2 装备层追加提示词（后续使用）

素体生成完成后，装备层独立生成，格式如下：

```
(pixel art, dithering, pixelated, sprite art, 8-bit:1.2), masterpiece, best quality, item sprite, {装备名称}, {装备描述}, {品质色}, transparent background, centered, no character, equipment piece only
```

示例——战士铁甲胸甲：
```
(pixel art, dithering, pixelated, sprite art, 8-bit:1.2), masterpiece, best quality, item sprite, iron chest plate armor, heavy steel breastplate with crimson trim, faint green shimmer, transparent background, centered, no character, equipment piece only
```

---

## 六、后处理管线

素体角色走统一管线：

```
1. ComfyUI 生成 1024×1024
2. Python 降采样至 128×128 (LANCZOS)
3. 最近邻上采样至 512×512 (NEAREST)
4. 抠图去背景
5. 添加 1px 深色轮廓
6. 6 部位分件 (head/body/right_arm/left_arm/right_leg/left_leg)
7. LoongBones 骨骼绑定
```
