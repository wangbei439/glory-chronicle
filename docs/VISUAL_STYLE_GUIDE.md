# 《代号：传说》视觉风格标准 v1.0

> 基于 Beta v0.37 设计文档制定 | 引擎：Godot 4.6.2 | 类型：2.5D 动作 RPG

---

## 一、整体风格定义

**风格关键词**：奇幻史诗 · 暗调霓彩 · 像素精工

本游戏采用"暗调霓彩"美术风格——整体画面偏暗、饱和度偏低的环境氛围中，角色和关键元素以高饱和色彩和发光效果凸显。这种风格既保持了暗黑奇幻的沉浸感，又通过鲜明色彩区分确保2.5D视角下的战斗可读性。

**核心原则**：
1. **暗底亮角**：场景暗沉，角色/特效/交互物高饱和高亮度，确保战斗层次清晰
2. **区域色温**：6大区域各有独立色温体系，玩家进入即感知环境变化
3. **职业辨识**：8职业通过主色+轮廓光+武器形态三重辨识，混战中0.5秒可识别
4. **像素一致**：所有精灵统一走 1024→128→512 像素化管线，保证像素密度一致

---

## 二、调色板体系

### 2.1 全局基础色

| 用途 | 色值 | 说明 |
|------|------|------|
| UI底色 | #1a1a2e | 深蓝黑，所有UI面板底色 |
| UI边框 | #3a3a5c | 暗紫灰，面板/窗口边框 |
| 文字主色 | #e8e8f0 | 冷白，正文/标题 |
| 文字副色 | #8888aa | 灰紫，描述/次要信息 |
| 品质白 | #cccccc | 普通品质 |
| 品质绿 | #44cc44 | 优秀品质 |
| 品质蓝 | #4488ff | 稀有品质 |
| 品质紫 | #aa44ff | 史诗品质 |
| 品质橙 | #ff8800 | 传说品质 |
| 品质红 | #ff2244 | 神话品质 |

### 2.2 职业主色

| 职业 | 主色 | 辅色 | 轮廓光色 | 色感关键词 |
|------|------|------|----------|-----------|
| 战士 | #cc3333 深红 | #ff6644 橙红 | 红橙暖光 | 血性·力量 |
| 游侠 | #33aa55 翠绿 | #88dd44 黄绿 | 绿色自然光 | 敏锐·自然 |
| 刺客 | #7733cc 暗紫 | #bb44ff 亮紫 | 紫色暗光 | 暗影·致命 |
| 法师 | #3388ff 宝蓝 | #44ddff 冰蓝 | 蓝白冷光 | 奥术·深邃 |
| 武僧 | #ddaa22 金黄 | #ffcc44 亮金 | 金色暖光 | 炽热·修练 |
| 骑士 | #ddddee 银白 | #ffffcc 圣金 | 白金圣光 | 圣洁·守护 |
| 召唤师 | #22aaaa 幽青 | #44ffcc 翠青 | 青绿灵光 | 亡灵·冥界 |
| 机关师 | #cc8822 古铜 | #ffaa33 琥珀 | 橙黄火光 | 机械·锻造 |

### 2.3 区域色温

| 区域 | 色温 | 主色调 | 氛围关键词 | 饱和度 |
|------|------|--------|-----------|--------|
| 幽暗森林 | 冷绿偏暗 | #1a3322 深墨绿 | 迷雾·腐化·幽寂 | 低(40%) |
| 云中城 | 冷蓝偏亮 | #4466aa 天蓝 | 空灵·圣洁·高处 | 中(60%) |
| 铁匠谷 | 暖橙偏暗 | #442211 深红棕 | 熔炉·锻造·炽热 | 中(55%) |
| 龙脊山脉 | 冷蓝白 | #334466 冰蓝 | 极寒·巍峨·苍凉 | 低(35%) |
| 深渊裂隙 | 冷紫偏暗 | #1a1133 深紫黑 | 虚无·混沌·恐惧 | 极低(25%) |
| 试炼之塔 | 中性灰蓝 | #2a2a44 暗蓝灰 | 神秘·考验·庄严 | 低(30%) |

---

## 三、角色精灵规范

### 3.1 角色生成规范

| 参数 | 标准值 | 说明 |
|------|--------|------|
| 生成分辨率 | 1024×1024 | ComfyUI初始生成尺寸 |
| 目标像素密度 | 128×128 等效 | 降采样后像素密度 |
| 最终输出尺寸 | 512×512 | nearest-exact上采样 |
| 姿势 | A-Pose / T-Pose | 骨骼绑定用，手臂展开 |
| 朝向 | 面朝右 (3/4侧视) | 2.5D侧视角标准 |
| 背景 | 纯色 (#000000 或 #00ff00) | 便于自动抠图 |
| 描边 | 1px深色轮廓 | 像素化后处理添加 |
| 调色板 | 对应职业主色+辅色 | 见2.2职业主色表 |

### 3.2 角色分件规范（LoongBones骨骼动画）

| 部位 | 分件名 | 说明 |
|------|--------|------|
| 头部 | head | 含头盔/帽子/头发 |
| 躯干 | body | 含胸甲/衣服 |
| 右臂 | right_arm | 含肩甲+手部+武器握持 |
| 左臂 | left_arm | 含肩甲+手部+盾牌(骑士) |
| 右腿 | right_leg | 含护腿+靴子 |
| 左腿 | left_leg | 含护腿+靴子 |

### 3.3 装备分层规范

装备更换只替换对应分件纹理，不重建完整精灵：
- **武器**：替换 right_arm 纹理（部分职业替换 left_arm）
- **胸甲**：替换 body 纹理
- **护腿**：替换 right_leg + left_leg 纹理
- **鞋子**：替换 right_leg + left_leg 下部纹理
- **头盔**：替换 head 纹理
- **饰品**：添加发光/粒子效果，不替换纹理

---

## 四、场景精灵规范

### 4.1 背景规范

| 参数 | 标准值 | 说明 |
|------|--------|------|
| 视差层数 | 3层 (远/中/近) | 横向卷轴视差 |
| 单层分辨率 | 960×540 | 2倍于游戏视口 |
| 像素化处理 | 同角色管线 | 保持风格一致 |
| 色温 | 对应区域色温 | 见2.3区域色温表 |

### 4.2 地砖/平台规范

| 参数 | 标准值 |
|------|--------|
| 基础地砖尺寸 | 32×32 px |
| 平台地砖尺寸 | 32×8 px |
| 接缝处理 | 无缝拼接，边缘1px暗线 |

### 4.3 环境装饰规范

| 类型 | 尺寸 | 说明 |
|------|------|------|
| 小型(蘑菇/矿石/水晶) | 32×32 | 可交互采集物 |
| 中型(火把/蛛网/钟乳石) | 32×64 | 场景装饰 |
| 大型(链条/矿脉) | 64×128 | 场景装饰 |

---

## 五、敌人精灵规范

### 5.1 小怪规范

| 参数 | 标准值 | 说明 |
|------|--------|------|
| 生成尺寸 | 1024×1024 | 同角色 |
| 像素化处理 | 同角色管线 | 1024→128→512 |
| 朝向 | 面朝左 (与玩家对峙) | 2.5D侧视角 |
| 骨骼类型 | 按6套基础骨骼分类 | 植物/野兽/飞行/人形/元素/构造 |

### 5.2 Boss规范

| 参数 | 标准值 | 说明 |
|------|--------|------|
| 生成尺寸 | 1024×1024 | 大型Boss可出多张拼接 |
| 尺寸倍率 | 1.5x~3x 角色体型 | 按设计文档Boss描述 |
| 多阶段 | 每阶段独立精灵 | 阶段转换换贴图 |

### 5.3 美术复用规则

同类怪物共享基础骨骼，通过以下方式区域差异化：
- **颜色替换**：森林狼(绿) → 霜狼(蓝白) → 暗影狼(紫)
- **装饰添加**：基础骨架+区域特征装饰
- **体型缩放**：精英1.3x，稀有1.5x

---

## 六、UI精灵规范

| 元素 | 尺寸 | 风格 |
|------|------|------|
| 血条框 | 200×20 | 暗底+品质色边框 |
| Boss血条框 | 400×24 | 同上+装饰花纹 |
| 技能图标 | 64×64 | 暗底+职业主色图标 |
| 物品图标 | 64×64 | 暗底+品质色边框+物品图 |
| 面板框架 | 按需 | 暗底半透明+紫灰边框 |

---

## 七、ComfyUI 通用提示词模板

### 7.1 模型与基础设置

```
模型：Nova Pixels XL v3.0 (Illustrious架构)
采样器：Euler a
步数：25-30
CFG：7
尺寸：1024×1024
```

### 7.2 通用正面提示词骨架

```
(pixel art, dithering, pixelated, sprite art, 8-bit:1.2), masterpiece, best quality, {性别标签}, solo, full body full length sprite of {角色描述}, A-pose, standing on ground with feet visible, front 3/4 angle viewed from left, face and chest clearly visible facing camera, body oriented toward right side of frame, {装备/衣物描述}, dark fantasy style, black background, high contrast, vibrant {职业主色} accent, clear silhouette
```

### 7.3 性别强化标签（Illustrious/Danbooru 体系）

**⚠️ 重要：必须使用 Danbooru 性别标签，自然语言的 male/female 对 Illustrious 架构几乎无效！**

| 性别 | 正面标签 | 追加负面标签 |
|------|----------|-------------|
| 男性 | `(1boy:1.5), solo, male, boyish face, flat chest, broad shoulders, masculine features, no breasts` | `1girl, female, woman, girl, breasts, feminine, girly, long eyelashes, lipstick, curvy, hourglass figure, feminine hips, makeup, dress, skirt` |
| 女性 | `(1girl:1.5), solo, female, feminine face, slender build` | `1boy, male, man, boy, muscular, broad shoulders, flat chest, masculine, facial hair, beard, mustache, stubble` |

**权重调整**：如果仍偏女性，逐步加大 `(1boy:1.5)` → `(1boy:1.8)` → 额外加 `(flat chest:1.3), (no breasts:1.3)`

### 7.4 通用负面提示词

```
modern, recent, anime, illustration, cartoon, graphic, text, painting, abstract, glitch, deformed, mutated, ugly, disfigured, long body, lowres, bad anatomy, bad hands, missing fingers, extra digits, cropped, very displeasing, (worst quality, bad quality:1.2), sketch, jpeg artifacts, signature, watermark, username, simple background, conjoined, bad ai-generated, back view, rear view, facing away, from behind, showing back, half body, upper body only, cropped body, cut off, no legs, no feet, close-up, portrait, head shot, bust shot, waist up
```

### 7.5 无装备素体负面追加（生成素体时追加到通用负面）

```
weapon, sword, axe, bow, staff, shield, armor, helmet, plate armor, chainmail, heavy armor, weapon on back, quiver, cloak, hood, mask, goggles
```

---

## 八、角色提示词（8职业 A-Pose）

### 8.1 战士 Warrior

**正面**：
```
masterpiece, best quality, pixel art, sprite, male warrior character, A-pose, facing right, 3/4 side view, heavy plate armor in deep crimson red and dark steel, large greatsword on back, horned helmet with red plume, scarred face, muscular build, gauntlets with spiked knuckles, dark fantasy style, dark background, high contrast, vibrant red accent, clear silhouette, detailed equipment, battle-hardened veteran look
```

**负面**：
```
lowres, bad anatomy, bad hands, blurry, realistic, photograph, 3d render, text, watermark, signature, jpeg artifacts, extra limbs, deformed, messy lines, anti-aliased, smooth edges, gradient, soft shading
```

### 8.2 游侠 Ranger

**正面**：
```
masterpiece, best quality, pixel art, sprite, male ranger character, A-pose, facing right, 3/4 side view, leather armor in forest green and brown, longbow on back, quiver with green-fletched arrows, hooded cloak with leaf patterns, lean athletic build, leather bracers, forest green cape, dark fantasy style, dark background, high contrast, vibrant green accent, clear silhouette, detailed equipment, keen-eyed hunter look
```

**负面**：同通用负面

### 8.3 刺客 Assassin

**正面**：
```
masterpiece, best quality, pixel art, sprite, male assassin character, A-pose, facing right, 3/4 side view, dark leather armor in deep purple and black, twin daggers at waist, half-mask covering lower face, dark hood with purple inner lining, slim agile build, shadow wrappings on arms, purple glow edges, dark fantasy style, dark background, high contrast, vibrant purple accent, clear silhouette, detailed equipment, shadow stalker look
```

**负面**：同通用负面

### 8.4 法师 Mage

**正面**：
```
masterpiece, best quality, pixel art, sprite, male mage character, A-pose, facing right, 3/4 side view, arcane robes in royal blue and silver, staff with glowing blue crystal orb, spellbook at hip, pointed hat with star pattern, flowing beard, mystical aura, blue magical runes floating around, dark fantasy style, dark background, high contrast, vibrant blue accent, clear silhouette, detailed equipment, wise scholar look
```

**负面**：同通用负面

### 8.5 武僧 Monk

**正面**：
```
masterpiece, best quality, pixel art, sprite, male monk character, A-pose, facing right, 3/4 side view, martial arts robes in golden yellow and dark brown,拳套 fighting gloves with golden knuckles, prayer beads on wrist, shaved head with golden headband, muscular toned build, barefoot with leg wraps, golden chi aura around fists, dark fantasy style, dark background, high contrast, vibrant gold accent, clear silhouette, detailed equipment, disciplined fighter look
```

**负面**：同通用负面

### 8.6 骑士 Knight

**正面**：
```
masterpiece, best quality, pixel art, sprite, male paladin knight character, A-pose, facing right, 3/4 side view, full plate armor in silver white and holy gold, lance on back, kite shield with cross emblem on left arm, winged helmet with gold trim, holy aura glow, white cape with golden border, sacred sigils on armor, dark fantasy style, dark background, high contrast, vibrant silver-gold accent, clear silhouette, detailed equipment, divine guardian look
```

**负面**：同通用负面

### 8.7 召唤师 Summoner

**正面**：
```
masterpiece, best quality, pixel art, sprite, male summoner character, A-pose, facing right, 3/4 side view, necromancer robes in dark teal and ghostly cyan, soul lantern on chain in right hand, spirit staff with skull orb in left hand, tattered hooded cloak, ghostly chains wrapped around arms, spectral wisps floating nearby, cyan spirit flames, dark fantasy style, dark background, high contrast, vibrant cyan accent, clear silhouette, detailed equipment, necromancer look
```

**负面**：同通用负面

### 8.8 机关师 Engineer

**正面**：
```
masterpiece, best quality, pixel art, sprite, male engineer mechanic character, A-pose, facing right, 3/4 side view, mechanical armor in bronze and amber, toolbox on back, mechanical arm gauntlet on right hand, goggles on forehead, gear decorations, steam vents on shoulders, wrench and cog accessories, amber glow from mechanical parts, dark fantasy style, dark background, high contrast, vibrant orange-bronze accent, clear silhouette, detailed equipment, steampunk inventor look
```

**负面**：同通用负面

---

## 九、区域场景提示词

### 9.1 幽暗森林 Dark Forest

**远景**：
```
masterpiece, best quality, pixel art, dark forest background, distant view, dense canopy blocking sky, foggy ground, twisted dead trees, eerie green glow from mushrooms, deep moss green atmosphere, mysterious shadows, parallax layer, dark fantasy, low saturation, horror undertone
```

**中景**：
```
masterpiece, best quality, pixel art, dark forest background, midground, giant tree trunks, hanging vines and moss, bioluminescent mushrooms, stone ruins overgrown, fog patches, faint purple corruption veins on trees, deep green-teal atmosphere, parallax layer, dark fantasy
```

**近景/地面**：
```
masterpiece, best quality, pixel art, dark forest ground tiles, stone floor with moss, twisted roots, small glowing mushrooms, fallen leaves, puddles reflecting dim light, 32px tile size, dark fantasy, seamless tileable
```

### 9.2 云中城 Sky City

**远景**：
```
masterpiece, best quality, pixel art, sky city background, distant view, floating islands among clouds, waterfalls cascading into void, sunset sky gradient, marble towers with blue roofs, ethereal light rays, bright blue-white atmosphere, heavenly realm, parallax layer, dark fantasy
```

**中景**：
```
masterpiece, best quality, pixel art, sky city background, midground, cloud bridges, floating stone platforms, crystal pylons, wind sails, angelic statues, bright sky blue atmosphere, parallax layer, dark fantasy
```

**近景/地面**：
```
masterpiece, best quality, pixel art, sky city ground tiles, white marble floor, cloud patterns, golden inlay decorations, 32px tile size, dark fantasy, seamless tileable
```

### 9.3 铁匠谷 Blacksmith Valley

**远景**：
```
masterpiece, best quality, pixel art, volcanic forge valley background, distant view, smoke-filled sky with orange glow, volcanic peaks, molten rivers, giant chimneys and foundries, sparks rising, dark red-brown atmosphere, industrial forge realm, parallax layer, dark fantasy
```

**中景**：
```
masterpiece, best quality, pixel art, forge valley background, midground, massive forge buildings, anvils and bellows, ore carts on rails, lava channels, glowing cracks in ground, dark orange-brown atmosphere, parallax layer, dark fantasy
```

**近景/地面**：
```
masterpiece, best quality, pixel art, forge valley ground tiles, dark stone floor with lava cracks, metal grating, scattered cinders, hot coals, 32px tile size, dark fantasy, seamless tileable
```

### 9.4 龙脊山脉 Dragon Ridge

**远景**：
```
masterpiece, best quality, pixel art, snowy mountain background, distant view, towering ice peaks, blizzard clouds, frozen waterfalls, dragon silhouettes in mist, icy blue-white atmosphere, desolate grandeur, parallax layer, dark fantasy
```

**中景**：
```
masterpiece, best quality, pixel art, snowy mountain background, midground, ice caves, frozen stalactites, dragon bones embedded in cliff, ancient carved steps, aurora in sky, cold blue atmosphere, parallax layer, dark fantasy
```

**近景/地面**：
```
masterpiece, best quality, pixel art, snowy mountain ground tiles, icy stone floor, snow patches, frost crystals, frozen puddles, 32px tile size, dark fantasy, seamless tileable
```

### 9.5 深渊裂隙 Abyss Rift

**远景**：
```
masterpiece, best quality, pixel art, abyssal rift background, distant view, twisted void space, purple dimensional cracks, floating debris, distant screaming faces in darkness, purple-black atmosphere, cosmic horror, parallax layer, dark fantasy
```

**中景**：
```
masterpiece, best quality, pixel art, abyssal rift background, midground, corrupted architecture, void portals with purple glow, chains from ceiling, floating platforms in void, dark purple atmosphere, parallax layer, dark fantasy
```

**近景/地面**：
```
masterpiece, best quality, pixel art, abyssal rift ground tiles, dark void stone, purple veins of corruption, skull motifs, cracked reality, 32px tile size, dark fantasy, seamless tileable
```

### 9.6 试炼之塔 Trial Tower

**远景**：
```
masterpiece, best quality, pixel art, mystical tower interior background, distant view, endless spiral staircase, magical runes on walls, floating crystals, gothic arches, blue-grey atmosphere, sacred trial ground, parallax layer, dark fantasy
```

**中景**：
```
masterpiece, best quality, pixel art, tower interior background, midground, enchanted pillars, weapon racks, magical barrier doors, elemental symbols on floor, dark blue-grey atmosphere, parallax layer, dark fantasy
```

**近景/地面**：
```
masterpiece, best quality, pixel art, tower ground tiles, dark marble floor with rune circles, mystical engravings, 32px tile size, dark fantasy, seamless tileable
```

---

## 十、小怪提示词（按区域×骨骼类型）

### 10.1 幽暗森林（等级1-10）

**蘑菇怪 Mushroom** (植物骨骼)
```
masterpiece, best quality, pixel art, sprite, enemy monster, mushroom creature, walking mushroom with angry face, toxic spore clouds around cap, stubby root legs, bioluminescent green spots, dark forest setting, facing left, 3/4 side view, dark fantasy, low saturation green atmosphere
```

**树精 Tree Spirit** (植物骨骼)
```
masterpiece, best quality, pixel art, sprite, enemy monster, tree creature, humanoid tree with branch arms, bark armor, glowing eyes in hollow trunk, roots as feet, moss and mushrooms growing on body, dark forest setting, facing left, 3/4 side view, dark fantasy
```

**森林狼 Forest Wolf** (野兽骨骼)
```
masterpiece, best quality, pixel art, sprite, enemy monster, dark green furred wolf, glowing green eyes, snarling fangs, thick fur with moss and leaves, pack predator stance, dark forest setting, facing left, 3/4 side view, dark fantasy
```

**毒蛛 Poison Spider** (虫类骨骼)
```
masterpiece, best quality, pixel art, sprite, enemy monster, giant spider, green toxic abdomen, multiple red eyes, dripping venom from fangs, web strands trailing, dark forest setting, facing left, 3/4 side view, dark fantasy
```

**幽暗蝙蝠 Dark Bat** (飞行骨骼)
```
masterpiece, best quality, pixel art, sprite, enemy monster, large bat, tattered dark wings, glowing red eyes, sonar waves visual, hanging upside down pose alternate, dark forest setting, facing left, 3/4 side view, dark fantasy
```

**藤蔓蛇 Vine Snake** (野兽骨骼)
```
masterpiece, best quality, pixel art, sprite, enemy monster, snake creature made of vines, camouflaged in green, thorny scales, venomous fangs, coiled striking pose, dark forest setting, facing left, 3/4 side view, dark fantasy
```

**古树守卫 Ancient Tree Guardian** (植物骨骼·精英1.3x)
```
masterpiece, best quality, pixel art, sprite, elite enemy monster, massive tree guardian, ancient treant with glowing core, bark shield arms, root tentacles, moss-covered crown, larger than normal, dark forest setting, facing left, 3/4 side view, dark fantasy, imposing presence
```

**毒蛛女王 Spider Queen** (虫类骨骼·精英1.3x)
```
masterpiece, best quality, pixel art, sprite, elite enemy monster, queen spider, large abdomen with egg sac, crown-like markings on head, multiple eyes glowing purple, web-producing spinnerets, regal threatening pose, dark forest setting, facing left, 3/4 side view, dark fantasy
```

**精灵鹿 Spirit Deer** (灵兽骨骼·稀有1.5x)
```
masterpiece, best quality, pixel art, sprite, rare enemy monster, ethereal spirit deer, translucent glowing body, antlers with light particles, healing aura emanating outward, gentle but alert stance, dark forest setting, facing left, 3/4 side view, dark fantasy, mystical presence
```

### 10.2 云中城周边（等级5-15）

**云鸦 Cloud Crow** (飞行骨骼)
```
masterpiece, best quality, pixel art, sprite, enemy monster, large crow made of clouds and wind, wind blade feathers, stormy eyes, aerial predator, sky setting, facing left, 3/4 side view, dark fantasy, bright blue-white atmosphere
```

**雾灵 Fog Spirit** (元素骨骼)
```
masterpiece, best quality, pixel art, sprite, enemy monster, ghostly fog spirit, semi-transparent icy body, cold blue glow, reaching frost hands, barely visible in mist, sky setting, facing left, 3/4 side view, dark fantasy
```

**浮岛石人 Floating Golem** (构造骨骼)
```
masterpiece, best quality, pixel art, sprite, enemy monster, stone golem on floating island, chunky rock body, embedded crystals, throwing boulder pose, cannot move, sky setting, facing left, 3/4 side view, dark fantasy
```

**风蛇 Wind Serpent** (龙族骨骼)
```
masterpiece, best quality, pixel art, sprite, enemy monster, serpentine wind dragon, sleek blue-silver scales, wing fins, wind blade breath, coiled flying pose, sky setting, facing left, 3/4 side view, dark fantasy
```

**暴风骑士 Storm Knight** (人形骨骼·精英1.3x)
```
masterpiece, best quality, pixel art, sprite, elite enemy monster, storm knight riding cloud beast, lightning lance, storm armor crackling with electricity, cloud mount, sky setting, facing left, 3/4 side view, dark fantasy, imposing
```

**虹羽鸟 Rainbow Bird** (灵兽骨骼·稀有1.5x)
```
masterpiece, best quality, pixel art, sprite, rare enemy monster, iridescent rainbow bird, feathers shimmering with spectrum light, blinding light beam attack pose, fast erratic flight, sky setting, facing left, 3/4 side view, dark fantasy, mystical
```

### 10.3 铁匠谷周边（等级8-18）

**矿魂 Ore Spirit** (元素骨骼)
```
masterpiece, best quality, pixel art, sprite, enemy monster, mineral elemental, body made of floating ore chunks, glowing crystal core, heavy iron fists, rocky fragments orbiting, forge valley setting, facing left, 3/4 side view, dark fantasy, warm orange-brown atmosphere
```

**焰蜥 Fire Salamander** (龙族骨骼)
```
masterpiece, best quality, pixel art, sprite, enemy monster, small fire lizard, flame-tipped tail, glowing orange belly scales, fire breath, embers trailing, forge valley setting, facing left, 3/4 side view, dark fantasy
```

**铁甲蝎 Iron Scorpion** (虫类骨骼)
```
masterpiece, best quality, pixel art, sprite, enemy monster, armored scorpion, metal-plated carapace, stinger dripping venom, crushing pincers, forged metal look, forge valley setting, facing left, 3/4 side view, dark fantasy
```

**熔渣泥人 Slag Mudman** (构造骨骼)
```
masterpiece, best quality, pixel art, sprite, enemy monster, lava mud golem, molten core visible through cracks, slow heavy body, slag and cinders falling, burning footprints, forge valley setting, facing left, 3/4 side view, dark fantasy
```

**锻炉守卫 Forge Guardian** (构造骨骼·精英1.3x)
```
masterpiece, best quality, pixel art, sprite, elite enemy monster, giant forge guardian construct, massive iron hammer, furnace in chest glowing red, steam vents on shoulders, protective stance, forge valley setting, facing left, 3/4 side view, dark fantasy, imposing
```

**赤金蝶 Crimson Gold Butterfly** (灵兽骨骼·稀有1.5x)
```
masterpiece, best quality, pixel art, sprite, rare enemy monster, golden butterfly with crimson edges, sparkling gold dust trail, blinding wing flash, delicate but dangerous, forge valley setting, facing left, 3/4 side view, dark fantasy, mystical
```

### 10.4 龙脊山脉（等级10-20）

**霜狼 Frost Wolf** (野兽骨骼·森林狼换色)
```
masterpiece, best quality, pixel art, sprite, enemy monster, white-blue frost wolf, ice crystal fur, frozen breath mist, glowing ice-blue eyes, pack predator stance, snowy mountain setting, facing left, 3/4 side view, dark fantasy, cold blue atmosphere
```

**熔岩史莱姆 Lava Slime** (元素骨骼)
```
masterpiece, best quality, pixel art, sprite, enemy monster, lava slime, molten rock body, glowing orange cracks, splitting into two smaller copies, fire droplets, snowy mountain setting, facing left, 3/4 side view, dark fantasy
```

**山石巨人 Mountain Giant** (构造骨骼)
```
masterpiece, best quality, pixel art, sprite, enemy monster, huge rock giant, boulder body, stone shield front, throwing rocks, earthquake stomp, extremely slow but massive, snowy mountain setting, facing left, 3/4 side view, dark fantasy
```

**霜雪蜥蜴 Frost Lizard** (龙族骨骼)
```
masterpiece, best quality, pixel art, sprite, enemy monster, ice-breathing lizard, frost-covered blue-white scales, ice crystal spines, freezing breath cone, ice skating movement, snowy mountain setting, facing left, 3/4 side view, dark fantasy
```

**雷鹰 Thunder Eagle** (飞行骨骼)
```
masterpiece, best quality, pixel art, sprite, enemy monster, lightning eagle, crackling electric feathers, storm cloud trailing, diving attack pose, thunder in talons, snowy mountain setting, facing left, 3/4 side view, dark fantasy
```

**矿洞矮人 Mine Dwarf** (人形骨骼)
```
masterpiece, best quality, pixel art, sprite, enemy monster, stocky dwarf miner, pickaxe weapon, mining helmet with lamp, ore bag on back, underground burrowing, snowy mountain setting, facing left, 3/4 side view, dark fantasy
```

**山巅龙人 Peak Dragonkin** (龙族骨骼·精英1.3x)
```
masterpiece, best quality, pixel art, sprite, elite enemy monster, dragon-man hybrid, dragon wings, fire breath, scaled armor in red-gold, dragon rage glowing eyes, snowy mountain setting, facing left, 3/4 side view, dark fantasy, imposing
```

**暴风雪元素 Blizzard Element** (元素骨骼·精英1.3x)
```
masterpiece, best quality, pixel art, sprite, elite enemy monster, blizzard elemental, swirling ice and wind, icicle projectiles, freezing aura, cold blue-white body, snowy mountain setting, facing left, 3/4 side view, dark fantasy
```

**冰晶凤凰 Ice Phoenix** (灵兽骨骼·稀有1.5x)
```
masterpiece, best quality, pixel art, sprite, rare enemy monster, ice phoenix, crystalline ice feathers, frozen flame aura, resurrection glow, ice coffin ability, snowy mountain setting, facing left, 3/4 side view, dark fantasy, mystical
```

### 10.5 深渊裂隙（等级20-30）

**深渊蠕虫 Abyss Worm** (异形骨骼)
```
masterpiece, best quality, pixel art, sprite, enemy monster, abyssal worm, segmented purple-black body, acid dripping maw, underground burrowing, multiple eyes, abyss rift setting, facing left, 3/4 side view, dark fantasy, deep purple-black atmosphere
```

**虚空行者 Void Walker** (异界骨骼)
```
masterpiece, best quality, pixel art, sprite, enemy monster, void walker, humanoid dark matter, purple portal effects, teleporting pose, shadow bolt in hand, abyss rift setting, facing left, 3/4 side view, dark fantasy
```

**暗影猎手 Shadow Hunter** (人形骨骼)
```
masterpiece, best quality, pixel art, sprite, enemy monster, shadow assassin, cloaked in darkness, twin dark blades, faint purple outline when stealthed, backstab stance, abyss rift setting, facing left, 3/4 side view, dark fantasy
```

**噬魂者 Soul Devourer** (异形骨骼)
```
masterpiece, best quality, pixel art, sprite, enemy monster, soul devourer, spectral tentacles, draining green soul energy, growing larger with each drain, hollow eye sockets, abyss rift setting, facing left, 3/4 side view, dark fantasy
```

**深渊信徒 Abyss Cultist** (人形骨骼)
```
masterpiece, best quality, pixel art, sprite, enemy monster, abyss cultist, dark robes with purple runes, chanting pose, buff aura around allies, scroll in hand, non-aggressive stance, abyss rift setting, facing left, 3/4 side view, dark fantasy
```

**裂隙爬行者 Rift Crawler** (异形骨骼)
```
masterpiece, best quality, pixel art, sprite, enemy monster, ceiling crawler, insectoid limbs, clinging to walls, dropping poison, multiple legs, abyss rift setting, facing left, 3/4 side view, dark fantasy
```

**裂隙守卫 Rift Guardian** (构造骨骼·精英1.3x)
```
masterpiece, best quality, pixel art, sprite, elite enemy monster, rift guardian construct, portal frame body, summoning void portals, dark energy core, protective barrier, abyss rift setting, facing left, 3/4 side view, dark fantasy, imposing
```

**深渊法师 Abyss Mage** (人形骨骼·精英1.3x)
```
masterpiece, best quality, pixel art, sprite, elite enemy monster, dark mage, cycling fire ice lightning spells, magic reflection shield, floating grimoire, spell circles, abyss rift setting, facing left, 3/4 side view, dark fantasy
```

**混沌之眼 Chaos Eye** (异界骨骼·稀有1.5x)
```
masterpiece, best quality, pixel art, sprite, rare enemy monster, chaos eye entity, giant floating eye, chaos ray beam, tentacles beneath, reality distorting aura, abyss rift setting, facing left, 3/4 side view, dark fantasy, mystical
```

---

## 十一、Boss提示词（11个Boss × 多阶段）

### 11.1 枯木领主（幽暗森林·主线Boss）

**阶段一 - 腐化树精**：
```
masterpiece, best quality, pixel art, sprite, boss monster, corrupted treant lord, massive tree creature, rotted bark armor, toxic mushroom growths on body, glowing green decay core in chest, root tentacles as arms, withered crown of branches, dark forest setting, facing left, 3/4 side view, dark fantasy, imposing 2x size, purple corruption veins
```

**阶段二 - 狂暴树人**：
```
masterpiece, best quality, pixel art, sprite, boss monster, enraged treant lord, trunk split open revealing pulsing green decay core, roots writhing wildly, thorn walls, faster aggressive pose, mushrooms exploding, dark forest setting, facing left, 3/4 side view, dark fantasy, imposing 2x size, green glow from cracked trunk
```

### 11.2 精灵女王（幽暗森林·隐藏Boss）

**阶段一 - 自然守护**：
```
masterpiece, best quality, pixel art, sprite, boss monster, elf queen, ethereal beauty, flower crown, vine dress, glowing green wings, rapid movement trails, nature magic circles, dark forest garden setting, facing left, 3/4 side view, dark fantasy, elegant but deadly
```

**阶段二 - 自然之怒**：
```
masterpiece, best quality, pixel art, sprite, boss monster, elf queen nature fury, floating with wild thorny aura, ground covered in jagged thorns, three safe islands visible, moonlight rain, thorn storm, dark forest garden setting, facing left, 3/4 side view, dark fantasy, divine wrath
```

### 11.3 风暴巨像（云中城·主线Boss）

**阶段一 - 风之守卫**：
```
masterpiece, best quality, pixel art, sprite, boss monster, storm colossus, giant construct of stone and wind, wind core in chest, massive stone fists, storm clouds swirling around body, floating platform arena, sky setting, facing left, 3/4 side view, dark fantasy, imposing 3x size
```

**阶段二 - 暴风觉醒**：
```
masterpiece, best quality, pixel art, sprite, boss monster, storm colossus awakened, wind core exploding with lightning, platform edges crumbling, tornado pulling inward, lightning strikes, storm vortex, sky setting, facing left, 3/4 side view, dark fantasy, imposing 3x size, blue-white storm glow
```

### 11.4 炎魔锻匠（铁匠谷·主线Boss）

**阶段一 - 熔炉之主**：
```
masterpiece, best quality, pixel art, sprite, boss monster, forge demon, massive fire demon blacksmith, giant red-hot hammer, molten metal body, furnace in belly, forge workshop setting with anvils and crucibles, facing left, 3/4 side view, dark fantasy, imposing 2.5x size
```

**阶段二 - 炎魔觉醒**：
```
masterpiece, best quality, pixel art, sprite, boss monster, forge demon awakened, pure flame form, no hammer, molten body shifting, fire tornadoes, lava ring expanding, workshop burning, facing left, 3/4 side view, dark fantasy, imposing 2.5x size, intense orange-red glow
```

### 11.5 冰霜巨龙·赫拉格（龙脊山脉·主线Boss）

**阶段一 - 地面龙兽**：
```
masterpiece, best quality, pixel art, sprite, boss monster, frost dragon Hrag, massive ice dragon on ground, four-legged stance, ice crystal scales, frozen breath, tail sweeping, blizzard aura, snowy mountain peak arena, facing left, 3/4 side view, dark fantasy, imposing 3x size, blue-white ice glow
```

**阶段二 - 升空冰龙**：
```
masterpiece, best quality, pixel art, sprite, boss monster, frost dragon Hrag airborne, flying ice dragon, massive wings spread, diving from sky, ice wall breath sweeping ground, icicle rain, snowy mountain peak arena, facing left, 3/4 side view, dark fantasy, imposing 3x size, using Z-axis height
```

### 11.6 雪山贤者（龙脊山脉·隐藏Boss）

**阶段一 - 三系轮换**：
```
masterpiece, best quality, pixel art, sprite, boss monster, mountain sage, elderly wizard, fire ice lightning elements cycling, elemental color changing, staff with triple crystal, ancient robes, icy cave setting, facing left, 3/4 side view, dark fantasy
```

**阶段二 - 三系融合**：
```
masterpiece, best quality, pixel art, sprite, boss monster, mountain sage fusion, three elements combined, steam explosions, ice-lightning chains, fire-thunder meltdown, chaotic elemental aura, icy cave setting, facing left, 3/4 side view, dark fantasy, tri-color glow
```

### 11.7 深渊领主·虚无（深渊裂隙·主线Boss）

**阶段一 - 暗影形态**：
```
masterpiece, best quality, pixel art, sprite, boss monster, abyss lord Void, humanoid shadow form, constantly shifting dark matter, purple core deep inside, shadow blade combos, void portals, abyss setting, facing left, 3/4 side view, dark fantasy, imposing 2x size
```

**阶段二 - 混沌形态**：
```
masterpiece, best quality, pixel art, sprite, boss monster, abyss lord Void chaos form, amorphous chaos entity, eight tentacles, gravity anomaly effects, void devour ability, purple core more visible, abyss setting, facing left, 3/4 side view, dark fantasy, imposing 2.5x size
```

**阶段三 - 终焉形态**：
```
masterpiece, best quality, pixel art, sprite, boss monster, abyss lord Void final form, pure darkness with exposed core, apocalyptic energy, arena shrinking, final desperation attack, annihilation light wave, abyss setting, facing left, 3/4 side view, dark fantasy, imposing 2.5x size, ultimate threat
```

### 11.8 堕落天使·路西菲尔（深渊裂隙·隐藏Boss）

**阶段一 - 审判天使**：
```
masterpiece, best quality, pixel art, sprite, boss monster, fallen angel Lucifel, six white wings, golden holy spear, radiant armor, divine judgment pose, light-based attacks, holy aura, abyss altar setting, facing left, 3/4 side view, dark fantasy, imposing 2x size, white-gold glow
```

**阶段二 - 堕落天使**：
```
masterpiece, best quality, pixel art, sprite, boss monster, fallen angel Lucifel dark, blackened wings, shattered spear becomes dark scythe, dark halo, corrupted divine power, shadow-light mixed attacks, abyss altar setting, facing left, 3/4 side view, dark fantasy, imposing 2x size, dark-purple glow
```

### 11.9 武器大师（试炼之塔·5F一转Boss）

```
masterpiece, best quality, pixel art, sprite, boss monster, weapon master, masked warrior, wielding all 8 weapon types simultaneously, 8 arms with different weapons, trial tower arena, facing left, 3/4 side view, dark fantasy, mysterious
```

### 11.10 影之镜像（试炼之塔·10F二转Boss）

```
masterpiece, best quality, pixel art, sprite, boss monster, shadow mirror, dark reflection of player character, mirror-like surface body, copying player abilities, doppelganger, trial tower arena, facing left, 3/4 side view, dark fantasy, unsettling
```

### 11.11 传说守卫（试炼之塔·15F三转Boss）

```
masterpiece, best quality, pixel art, sprite, boss monster, legendary guardian, ancient construct knight, three-phase mechanism fusion, glowing trial runes, ultimate challenge presence, trial tower arena, facing left, 3/4 side view, dark fantasy, imposing 2.5x size, tri-color glow
```

---

## 十二、装备图标提示词

### 12.1 武器图标

**战士·巨剑**：
```
masterpiece, best quality, pixel art, item icon, greatsword, heavy iron blade, red leather grip, steel crossguard, 64x64, dark background, centered, item sprite
```

**战士·战斧**：
```
masterpiece, best quality, pixel art, item icon, battle axe, double-bladed axe head, ironwood handle, crimson steel, 64x64, dark background, centered, item sprite
```

**游侠·长弓**：
```
masterpiece, best quality, pixel art, item icon, longbow, curved wooden bow, green vine wrapping, string taut, 64x64, dark background, centered, item sprite
```

**刺客·双匕**：
```
masterpiece, best quality, pixel art, item icon, twin daggers, curved dark blades, purple gem pommel, paired weapons, 64x64, dark background, centered, item sprite
```

**法师·法杖**：
```
masterpiece, best quality, pixel art, item icon, magic staff, blue crystal orb top, silver shaft with runes, 64x64, dark background, centered, item sprite
```

**武僧·拳套**：
```
masterpiece, best quality, pixel art, item icon, fighting gauntlets, golden knuckle plates, leather straps, 64x64, dark background, centered, item sprite
```

**骑士·长枪+圣盾**：
```
masterpiece, best quality, pixel art, item icon, holy lance and shield, silver spear with gold tip, kite shield with cross emblem, 64x64, dark background, centered, item sprite
```

**召唤师·魂灯**：
```
masterpiece, best quality, pixel art, item icon, soul lantern, spectral teal flame, chain handle, skull decoration, 64x64, dark background, centered, item sprite
```

**机关师·工具箱**：
```
masterpiece, best quality, pixel art, item icon, engineer toolbox, brass and bronze box, gear decorations, steam vents, 64x64, dark background, centered, item sprite
```

### 12.2 防具图标模板

**胸甲**：
```
masterpiece, best quality, pixel art, item icon, chest armor plate, {材质描述}, {品质色描述}, 64x64, dark background, centered, item sprite
```

**护腿**：
```
masterpiece, best quality, pixel art, item icon, leg armor greaves, {材质描述}, {品质色描述}, 64x64, dark background, centered, item sprite
```

**鞋子**：
```
masterpiece, best quality, pixel art, item icon, boots, {材质描述}, {品质色描述}, 64x64, dark background, centered, item sprite
```

### 12.3 品质色关键词

| 品质 | 关键词 |
|------|--------|
| 普通(白) | plain iron, simple design, no glow |
| 优秀(绿) | refined steel, faint green shimmer |
| 稀有(蓝) | enchanted, blue magical glow, rune inscriptions |
| 史诗(紫) | legendary, purple arcane aura, intricate engravings |
| 传说(橙) | mythical, blazing orange fire aura, divine patterns |
| 神话(红) | godlike, crimson reality-bending aura, cosmic patterns |

---

## 十三、材料图标提示词

**通用材料**：
```
masterpiece, best quality, pixel art, item icon, {材料名}, {材质描述}, 64x64, dark background, centered, item sprite, soft glow
```

具体示例：
- **强化石**：`enhancement stone, glowing crystal shard, warm white light`
- **蘑菇孢子**：`mushroom spore pod, green bioluminescent, forest material`
- **矿魂碎片**：`ore spirit fragment, floating rock crystal, orange mineral glow`
- **霜牙**：`frost fang, ice-crystal wolf tooth, cold blue glow`
- **虚空碎片**：`void fragment, purple-black dimensional shard, reality distortion`
- **龙人之鳞**：`dragonkin scale, red-gold metallic sheen, fire resistance`
- **枯木之心**：`withered tree heart, dark wood with green decay pulse, rare material`
- **炎魔之心**：`demon forge heart, molten core with fire aura, legendary material`
- **虚无之心**：`void lord heart, pure darkness with purple core, mythic material`

---

## 十四、UI元素提示词

**血条框**：
```
masterpiece, best quality, pixel art, UI element, health bar frame, dark metal border, red fill bar, fantasy RPG style, 200x20, dark background
```

**技能图标模板**：
```
masterpiece, best quality, pixel art, skill icon, {技能描述}, {职业主色} glow, 64x64, dark circular frame, centered
```

**品质框**：
```
masterpiece, best quality, pixel art, UI element, item slot frame, {品质色} border glow, dark center, fantasy RPG inventory, 64x64
```

---

## 十五、像素化后处理管线

所有AI生成的精灵必须经过统一后处理管线确保风格一致：

```python
# 管线步骤：
# 1. AI生成 1024×1024
# 2. 降采样至 128×128 (LANCZOS)
# 3. 最近邻上采样至 512×512 (NEAREST)
# 4. 抠图去背景
# 5. 添加1px深色轮廓 (颜色=主色RGB各-40)
# 6. 保存为PNG

# ComfyUI设置：
# - 采样器：Euler a
# - 步数：25-30
# - CFG：7
# - 尺寸：1024×1024
# - 降采样在ComfyUI外用Python处理
```

---

## 十六、资产生成优先级

| 优先级 | 资产类型 | 数量 | 说明 |
|--------|----------|------|------|
| P0 | 8职业A-Pose角色 | 8 | 骨骼动画基础 |
| P1 | 幽暗森林全场景 | 3层×1 | 第一个关卡 |
| P1 | 幽暗森林小怪 | 8+1+1=10 | 含精英/稀有 |
| P1 | 枯木领主Boss | 2阶段 | 第一个Boss |
| P2 | 铁匠谷全场景 | 3层×1 | 第二关卡 |
| P2 | 铁匠谷小怪 | 4+1+1=6 | |
| P2 | 炎魔锻匠Boss | 2阶段 | |
| P2 | 基础装备图标 | ~20 | 初始装备 |
| P3 | 云中城/龙脊山脉 | - | 逐步扩展 |
| P4 | 深渊裂隙/试炼塔 | - | 高级内容 |
