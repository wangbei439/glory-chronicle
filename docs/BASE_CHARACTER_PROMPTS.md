# 《代号：传说》无装备素体角色提示词 v2.0

> 严格遵循 Nova Pixels XL v3.0 官方推荐模板，仅在 {Prompt} 槽位做最小改动
> 改动点：① 性别用 Danbooru 标签 `(1boy:1.5)`/`(1girl:1.5)` ② 描述改为无装备素体 ③ 负面追加性别反制+装备反制

---

## 一、官方模板（不可修改部分）

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

## 二、{Prompt} 槽位写法规则

1. **性别标签放最前**：`(1boy:1.5), solo,` 或 `(1girl:1.5), solo,`
2. **角色描述精简**：只写必要信息，不堆砌
3. **素体 = 朴素衣物 + 职业色丝带**，无武器无盔甲
4. **全身+方向**：保留之前验证通过的 `full body`, `feet visible`, `facing camera` 修正

---

## 三、8职业 × 2性别 无装备素体

---

### 3.1 战士 Warrior — 红色丝带 #cc3333

**男性 {Prompt}**：
```
(1boy:1.5), solo, full body sprite of adventurer, short spiky hair, plain white shirt, brown trousers, crimson sash at waist, brown boots, bare hands, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character
```

**完整正面**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), (1boy:1.5), solo, full body sprite of adventurer, short spiky hair, plain white shirt, brown trousers, crimson sash at waist, brown boots, bare hands, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character, BREAK, depth of field, volumetric lighting
```

**女性 {Prompt}**：
```
(1girl:1.5), solo, full body sprite of adventurer, short hair in ponytail, plain white shirt, brown trousers, crimson sash at waist, brown boots, bare hands, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character
```

**完整正面**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), (1girl:1.5), solo, full body sprite of adventurer, short hair in ponytail, plain white shirt, brown trousers, crimson sash at waist, brown boots, bare hands, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character, BREAK, depth of field, volumetric lighting
```

**负面（男性追加）**：
```
modern, recent, old, oldest, anime, illustration, cartoon, graphic, text, painting, crayon, graphite, abstract, glitch, deformed, mutated, ugly, disfigured, long body, lowres, bad anatomy, bad hands, missing fingers, extra digits, fewer digits, cropped, very displeasing, (worst quality, bad quality:1.2), sketch, jpeg artifacts, signature, watermark, username, signature, simple background, conjoined, bad ai-generated, 1girl, breasts, feminine, weapon, sword, armor, shield, helmet, back view, half body
```

**负面（女性追加）**：
```
modern, recent, old, oldest, anime, illustration, cartoon, graphic, text, painting, crayon, graphite, abstract, glitch, deformed, mutated, ugly, disfigured, long body, lowres, bad anatomy, bad hands, missing fingers, extra digits, fewer digits, cropped, very displeasing, (worst quality, bad quality:1.2), sketch, jpeg artifacts, signature, watermark, username, signature, simple background, conjoined, bad ai-generated, 1boy, muscular, beard, weapon, sword, armor, shield, helmet, back view, half body
```

---

### 3.2 游侠 Ranger — 绿色丝带 #33aa55

**男性 {Prompt}**：
```
(1boy:1.5), solo, full body sprite of adventurer, short messy brown hair, plain tan shirt, dark green trousers, green sash at waist, brown boots, bare hands, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character
```

**完整正面**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), (1boy:1.5), solo, full body sprite of adventurer, short messy brown hair, plain tan shirt, dark green trousers, green sash at waist, brown boots, bare hands, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character, BREAK, depth of field, volumetric lighting
```

**女性 {Prompt}**：
```
(1girl:1.5), solo, full body sprite of adventurer, long brown hair in braid, plain tan shirt, dark green trousers, green sash at waist, brown boots, bare hands, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character
```

**完整正面**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), (1girl:1.5), solo, full body sprite of adventurer, long brown hair in braid, plain tan shirt, dark green trousers, green sash at waist, brown boots, bare hands, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character, BREAK, depth of field, volumetric lighting
```

负面同3.1

---

### 3.3 刺客 Assassin — 紫色丝带 #7733cc

**男性 {Prompt}**：
```
(1boy:1.5), solo, full body sprite of adventurer, short dark hair, plain charcoal shirt, black trousers, purple sash at waist, dark boots, bare hands, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character
```

**完整正面**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), (1boy:1.5), solo, full body sprite of adventurer, short dark hair, plain charcoal shirt, black trousers, purple sash at waist, dark boots, bare hands, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character, BREAK, depth of field, volumetric lighting
```

**女性 {Prompt}**：
```
(1girl:1.5), solo, full body sprite of adventurer, long dark hair in twin tails, plain charcoal shirt, black trousers, purple sash at waist, dark boots, bare hands, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character
```

**完整正面**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), (1girl:1.5), solo, full body sprite of adventurer, long dark hair in twin tails, plain charcoal shirt, black trousers, purple sash at waist, dark boots, bare hands, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character, BREAK, depth of field, volumetric lighting
```

负面同3.1

---

### 3.4 法师 Mage — 蓝色丝带 #3388ff

**男性 {Prompt}**：
```
(1boy:1.5), solo, full body sprite of adventurer, medium blue-tinted hair tied back, plain grey shirt, dark blue trousers, blue sash at waist, dark boots, bare hands, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character
```

**完整正面**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), (1boy:1.5), solo, full body sprite of adventurer, medium blue-tinted hair tied back, plain grey shirt, dark blue trousers, blue sash at waist, dark boots, bare hands, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character, BREAK, depth of field, volumetric lighting
```

**女性 {Prompt}**：
```
(1girl:1.5), solo, full body sprite of adventurer, long blue-tinted hair flowing, plain grey shirt, dark blue trousers, blue sash at waist, dark boots, bare hands, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character
```

**完整正面**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), (1girl:1.5), solo, full body sprite of adventurer, long blue-tinted hair flowing, plain grey shirt, dark blue trousers, blue sash at waist, dark boots, bare hands, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character, BREAK, depth of field, volumetric lighting
```

负面同3.1

---

### 3.5 武僧 Monk — 金色丝带 #ddaa22

**男性 {Prompt}**：
```
(1boy:1.5), solo, full body sprite of adventurer, short buzz cut with golden headband, plain sleeveless white top, dark brown trousers, golden sash at waist, bare feet with ankle wraps, bare hands, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character
```

**完整正面**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), (1boy:1.5), solo, full body sprite of adventurer, short buzz cut with golden headband, plain sleeveless white top, dark brown trousers, golden sash at waist, bare feet with ankle wraps, bare hands, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character, BREAK, depth of field, volumetric lighting
```

**女性 {Prompt}**：
```
(1girl:1.5), solo, full body sprite of adventurer, short hair in topknot with golden headband, plain sleeveless white top, dark brown trousers, golden sash at waist, bare feet with ankle wraps, bare hands, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character
```

**完整正面**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), (1girl:1.5), solo, full body sprite of adventurer, short hair in topknot with golden headband, plain sleeveless white top, dark brown trousers, golden sash at waist, bare feet with ankle wraps, bare hands, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character, BREAK, depth of field, volumetric lighting
```

负面同3.1

---

### 3.6 骑士 Knight — 银白丝带 #ddddee

**男性 {Prompt}**：
```
(1boy:1.5), solo, full body sprite of adventurer, short neat silver-white hair, plain white shirt, grey trousers, silver-white sash at waist, grey boots, bare hands, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character
```

**完整正面**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), (1boy:1.5), solo, full body sprite of adventurer, short neat silver-white hair, plain white shirt, grey trousers, silver-white sash at waist, grey boots, bare hands, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character, BREAK, depth of field, volumetric lighting
```

**女性 {Prompt}**：
```
(1girl:1.5), solo, full body sprite of adventurer, long silver-white hair in braid, plain white shirt, grey trousers, silver-white sash at waist, grey boots, bare hands, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character
```

**完整正面**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), (1girl:1.5), solo, full body sprite of adventurer, long silver-white hair in braid, plain white shirt, grey trousers, silver-white sash at waist, grey boots, bare hands, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character, BREAK, depth of field, volumetric lighting
```

负面同3.1

---

### 3.7 召唤师 Summoner — 青色丝带 #22aaaa

**男性 {Prompt}**：
```
(1boy:1.5), solo, full body sprite of adventurer, medium teal-tinted messy hair, plain dark grey shirt, black trousers, teal sash at waist, dark boots, bare hands, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character
```

**完整正面**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), (1boy:1.5), solo, full body sprite of adventurer, medium teal-tinted messy hair, plain dark grey shirt, black trousers, teal sash at waist, dark boots, bare hands, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character, BREAK, depth of field, volumetric lighting
```

**女性 {Prompt}**：
```
(1girl:1.5), solo, full body sprite of adventurer, long teal-tinted hair loose, plain dark grey shirt, black trousers, teal sash at waist, dark boots, bare hands, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character
```

**完整正面**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), (1girl:1.5), solo, full body sprite of adventurer, long teal-tinted hair loose, plain dark grey shirt, black trousers, teal sash at waist, dark boots, bare hands, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character, BREAK, depth of field, volumetric lighting
```

负面同3.1

---

### 3.8 机关师 Engineer — 古铜丝带 #cc8822

**男性 {Prompt}**：
```
(1boy:1.5), solo, full body sprite of adventurer, short scruffy brown hair, plain tan shirt, dark brown trousers, bronze-orange sash at waist, heavy brown boots, bare hands, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character
```

**完整正面**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), (1boy:1.5), solo, full body sprite of adventurer, short scruffy brown hair, plain tan shirt, dark brown trousers, bronze-orange sash at waist, heavy brown boots, bare hands, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character, BREAK, depth of field, volumetric lighting
```

**女性 {Prompt}**：
```
(1girl:1.5), solo, full body sprite of adventurer, medium brown hair in messy bun, plain tan shirt, dark brown trousers, bronze-orange sash at waist, heavy brown boots, bare hands, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character
```

**完整正面**：
```
masterpiece, best quality, amazing quality, 4k, very aesthetic, ultra-detailed, (pixel art, dithering, pixelated, sprite art, 8-bit:1.2), (1girl:1.5), solo, full body sprite of adventurer, medium brown hair in messy bun, plain tan shirt, dark brown trousers, bronze-orange sash at waist, heavy brown boots, bare hands, A-pose, standing with feet visible, front 3/4 angle facing camera, dark fantasy character, BREAK, depth of field, volumetric lighting
```

负面同3.1

---

## 四、性别强化速查

| 问题 | 修复 |
|------|------|
| 男性出女性 | 正面加 `(1boy:1.5)`, 负面加 `1girl, breasts, feminine` |
| 权重不够 | `(1boy:1.5)` → `(1boy:1.8)` |
| 还是不行 | 追加 `(flat chest:1.3), (no breasts:1.3)` |

## 五、男女差异对照

| 职业 | 男性 | 女性 |
|------|------|------|
| 战士 | short spiky hair | short hair in ponytail |
| 游侠 | short messy brown hair | long brown hair in braid |
| 刺客 | short dark hair | long dark hair in twin tails |
| 法师 | medium blue-tinted hair tied back | long blue-tinted hair flowing |
| 武僧 | short buzz cut + headband | short hair in topknot + headband |
| 骑士 | short neat silver-white hair | long silver-white hair in braid |
| 召唤师 | medium teal-tinted messy hair | long teal-tinted hair loose |
| 机关师 | short scruffy brown hair | medium brown hair in messy bun |

## 六、后处理管线

```
1. ComfyUI 生成 1024×1024
2. Python 降采样至 128×128 (LANCZOS)
3. 最近邻上采样至 512×512 (NEAREST)
4. 抠图去背景
5. 添加 1px 深色轮廓
6. 6 部位分件 (head/body/right_arm/left_arm/right_leg/left_leg)
7. LoongBones 骨骼绑定
```
