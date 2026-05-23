#!/usr/bin/env python3
"""生成《代号：传说》开发路线图 PDF — 从设计到原型的执行计划"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus.flowables import Flowable

# ═══ Fonts ═══
FD = "/usr/share/fonts/truetype"
pdfmetrics.registerFont(TTFont('SansSC', f'{FD}/chinese/SarasaMonoSC-Regular.ttf'))
pdfmetrics.registerFont(TTFont('SansSC-Bold', f'{FD}/chinese/SarasaMonoSC-Bold.ttf'))
pdfmetrics.registerFont(TTFont('SerifSC', f'{FD}/noto-serif-sc/NotoSerifSC-Regular.ttf'))
pdfmetrics.registerFont(TTFont('SerifSC-Bold', f'{FD}/noto-serif-sc/NotoSerifSC-Bold.ttf'))
pdfmetrics.registerFont(TTFont('SerifSC-Black', f'{FD}/noto-serif-sc/NotoSerifSC-Black.ttf'))

# ═══ Colors ═══
CP = HexColor('#1a1a2e')       # 主色-深蓝紫
CS = HexColor('#16213e')       # 副色
CA = HexColor('#e94560')       # 强调色-红
CD = HexColor('#2c2c2c')       # 正文
CW = HexColor('#ffffff')       # 白
CTA = HexColor('#fafafa')      # 交替行
C_M1 = HexColor('#1565c0')    # 里程碑1 蓝
C_M2 = HexColor('#2e7d32')    # 里程碑2 绿
C_M3 = HexColor('#e65100')    # 里程碑3 橙
C_M4 = HexColor('#6a1b9a')    # 里程碑4 紫
C_RISK = HexColor('#b71c1c')  # 风险 红
C_TODO = HexColor('#00695c')  # 待办 青

# ═══ Styles ═══
s_title = ParagraphStyle('T', fontName='SerifSC-Black', fontSize=26, textColor=CP, alignment=TA_CENTER, spaceAfter=4*mm, leading=34)
s_sub = ParagraphStyle('Sub', fontName='SansSC', fontSize=10.5, textColor=HexColor('#666'), alignment=TA_CENTER, spaceAfter=8*mm, leading=15)
s_h1 = ParagraphStyle('H1', fontName='SerifSC-Bold', fontSize=18, textColor=CP, spaceBefore=8*mm, spaceAfter=3*mm, leading=26)
s_h2 = ParagraphStyle('H2', fontName='SerifSC-Bold', fontSize=14, textColor=CS, spaceBefore=5*mm, spaceAfter=2.5*mm, leading=20)
s_h3 = ParagraphStyle('H3', fontName='SerifSC-Bold', fontSize=11.5, textColor=CD, spaceBefore=4*mm, spaceAfter=2*mm, leading=17)
s_body = ParagraphStyle('B', fontName='SansSC', fontSize=9.5, textColor=CD, alignment=TA_JUSTIFY, leading=16, spaceBefore=1*mm, spaceAfter=2*mm, firstLineIndent=19)
s_th = ParagraphStyle('TH', fontName='SansSC', fontSize=8.5, textColor=CW, alignment=TA_CENTER, leading=13)
s_td = ParagraphStyle('TD', fontName='SansSC', fontSize=8.5, textColor=CD, alignment=TA_LEFT, leading=13)
s_cap = ParagraphStyle('Cap', fontName='SansSC', fontSize=8, textColor=HexColor('#888'), spaceBefore=1*mm, spaceAfter=3*mm)
s_m1 = ParagraphStyle('M1', fontName='SerifSC-Bold', fontSize=14, textColor=C_M1, spaceBefore=5*mm, spaceAfter=2*mm, leading=20)
s_m2 = ParagraphStyle('M2', fontName='SerifSC-Bold', fontSize=14, textColor=C_M2, spaceBefore=5*mm, spaceAfter=2*mm, leading=20)
s_m3 = ParagraphStyle('M3', fontName='SerifSC-Bold', fontSize=14, textColor=C_M3, spaceBefore=5*mm, spaceAfter=2*mm, leading=20)
s_m4 = ParagraphStyle('M4', fontName='SerifSC-Bold', fontSize=14, textColor=C_M4, spaceBefore=5*mm, spaceAfter=2*mm, leading=20)
s_risk = ParagraphStyle('Risk', fontName='SerifSC-Bold', fontSize=13, textColor=C_RISK, spaceBefore=5*mm, spaceAfter=2*mm, leading=19)
s_todo = ParagraphStyle('Todo', fontName='SerifSC-Bold', fontSize=13, textColor=C_TODO, spaceBefore=5*mm, spaceAfter=2*mm, leading=19)
s_bullet = ParagraphStyle('Bul', fontName='SansSC', fontSize=9.5, textColor=CD, alignment=TA_LEFT, leading=16, spaceBefore=0.5*mm, spaceAfter=1*mm, leftIndent=20, bulletIndent=8)
s_note = ParagraphStyle('Note', fontName='SansSC', fontSize=8.5, textColor=HexColor('#555'), alignment=TA_LEFT, leading=14, spaceBefore=1*mm, spaceAfter=1*mm, leftIndent=15, borderColor=HexColor('#ccc'), borderWidth=0.5, borderPadding=4)

pw = A4[0] - 40*mm

class ColorBar(Flowable):
    def __init__(self, color, width=500, height=3):
        Flowable.__init__(self)
        self.color = color; self.bw = width; self.height = height
    def draw(self):
        self.canv.setFillColor(self.color)
        self.canv.rect(0, 0, self.bw, self.height, fill=1, stroke=0)

def mk_table(headers, rows, col_widths=None, hdr_color=CP):
    h = [Paragraph(x, s_th) for x in headers]
    data = [h] + [[Paragraph(str(c), s_td) for c in r] for r in rows]
    t = Table(data, colWidths=col_widths, repeatRows=1)
    cmds = [
        ('BACKGROUND', (0,0), (-1,0), hdr_color), ('TEXTCOLOR', (0,0), (-1,0), CW),
        ('FONTNAME', (0,0), (-1,0), 'SansSC'), ('FONTSIZE', (0,0), (-1,-1), 8.5),
        ('ALIGN', (0,0), (-1,0), 'CENTER'), ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.5, HexColor('#ccc')),
        ('TOPPADDING', (0,0), (-1,-1), 3), ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 4), ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]
    for i in range(2, len(data), 2):
        cmds.append(('BACKGROUND', (0,i), (-1,i), CTA))
    t.setStyle(TableStyle(cmds))
    return t


def build_doc():
    output = "/home/z/my-project/download/代号传说_开发路线图.pdf"
    doc = SimpleDocTemplate(output, pagesize=A4, leftMargin=20*mm, rightMargin=20*mm, topMargin=18*mm, bottomMargin=18*mm)
    story = []

    # ═══ COVER ═══
    story.append(Spacer(1, 35*mm))
    story.append(ColorBar(CA, pw, 4))
    story.append(Spacer(1, 6*mm))
    story.append(Paragraph('代号：传说', s_title))
    story.append(Spacer(1, 2*mm))
    story.append(Paragraph('从设计到原型的开发执行路线图', ParagraphStyle('SubT', fontName='SerifSC-Bold', fontSize=16, textColor=CS, alignment=TA_CENTER, spaceAfter=6*mm, leading=22)))
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph('基于Godot 4.6.2引擎 | 2.5D动作RPG | 4个里程碑 | 12个冲刺周期', s_sub))
    story.append(Spacer(1, 10*mm))
    ct = Table([
        ['设计文档版本', 'Beta v0.37 (99页/14.2万字)'],
        ['目标引擎', 'Godot 4.6.2'],
        ['开发范式', '2.5D (3D场景+2D像素+Z轴)'],
        ['路线图版本', 'v1.0'],
    ], colWidths=[40*mm, 70*mm])
    ct.setStyle(TableStyle([
        ('FONTNAME',(0,0),(-1,-1),'SansSC'),('FONTSIZE',(0,0),(-1,-1),10),
        ('TEXTCOLOR',(0,0),(0,-1),HexColor('#888')),('TEXTCOLOR',(1,0),(1,-1),CD),
        ('ALIGN',(0,0),(0,-1),'RIGHT'),('ALIGN',(1,0),(1,-1),'LEFT'),
        ('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4),
        ('LINEBELOW',(0,0),(-1,-2),0.5,HexColor('#eee')),
    ]))
    story.append(ct)
    story.append(Spacer(1, 15*mm))
    story.append(ColorBar(CA, pw, 4))
    story.append(PageBreak())

    # ═══ 一、路线图总览 ═══
    story.append(Paragraph('一、路线图总览', s_h1))
    story.append(ColorBar(CP, pw, 2))
    story.append(Paragraph('本路线图将《代号：传说》的开发过程拆解为4个递进式里程碑，每个里程碑聚焦一个核心验证目标。整体遵循"先验证核心乐趣，再扩展内容广度"的原则——如果2.5D战斗不好玩，后面的一切都没有意义。因此里程碑1是整个项目的生死线，必须优先完成并反复迭代。每个里程碑内部再细分为2-3个冲刺（Sprint），每个冲刺约1-1.5周，交付可运行的增量版本。', s_body))
    story.append(Paragraph('总预估周期约12-16周（单人开发节奏），如果多人协作可压缩至8-10周。每个里程碑末尾设有"质量门"——必须通过验证标准才能进入下一阶段，避免在根基不稳时仓促推进。', s_body))

    story.append(mk_table(
        ['里程碑', '核心目标', '周期', '验证标准'],
        [
            ['M1 核心战斗原型', '2.5D战斗"好玩"', '2-3周', '能流畅操作战士打1怪+1Boss'],
            ['M2 职业与装备', '8职业可玩+装备有效', '3-4周', '8职业各有手感+装备改变数值'],
            ['M3 世界与剧情', '能走完第一章主线', '3-4周', '从散人到一转完整体验'],
            ['M4 完整Demo', '可发布的演示版本', '4-5周', '含副本/PVP/新手引导的闭环'],
        ],
        col_widths=[30*mm, 35*mm, 20*mm, pw-85*mm],
        hdr_color=CP
    ))
    story.append(Paragraph('表1-1 开发里程碑总览', s_cap))

    # ═══ 二、里程碑1：核心战斗原型 ═══
    story.append(Paragraph('二、里程碑1：核心战斗原型', s_m1))
    story.append(ColorBar(C_M1, pw, 2))
    story.append(Paragraph('这是整个项目的生死线。如果2.5D战斗手感不好玩，后面铺再多内容也没有意义。本里程碑的目标极简：在Godot中搭建2.5D场景，实现战士这一个职业的基础战斗，加上一个小怪和一个Boss，验证"3D场景+2D像素角色+Z轴"这套技术方案是否成立。不需要UI美化，不需要音效，不需要剧情——只需要证明核心循环"移动-攻击-闪避-受击"有操作快感。', s_body))

    # Sprint 1.1
    story.append(Paragraph('2.1 Sprint 1.1：2.5D基础框架（第1-2周）', s_h2))
    story.append(Paragraph('本冲刺搭建2.5D技术框架，是最关键的基础工作。Godot中实现2.5D有多种方案，需要根据实际效果选择。推荐的方案是使用Node3D作为场景根节点，用3D TileMap铺设地形，角色使用Sprite3D渲染2D像素图，通过Z轴坐标模拟高度。这套方案的好处是3D场景天然支持透视和光照，2D角色可以保持像素风格，Z轴物理由引擎直接处理。', s_body))

    story.append(mk_table(
        ['任务', 'Godot节点/资源', '产出物', '参考设计文档章节'],
        [
            ['创建3D场景根节点', 'Node3D (root) + Camera3D', 'main_scene.tscn', '第二章 技术架构'],
            ['搭建测试地形', 'TileMap (3D) + StaticBody3D', 'test_arena.tscn', '第六章 世界设定'],
            ['2D像素角色渲染', 'Sprite3D + AnimationPlayer', 'player_sprite.tscn', '第二章 2.5D渲染方案'],
            ['Z轴物理系统', 'CharacterBody3D + 自定义重力', 'z_physics.gd', '第二章 Z轴物理'],
            ['输入系统', 'InputMap + 自定义InputController', 'input_controller.gd', '第二十三章 UI/UX'],
            ['基础移动+跳跃', 'move_and_slide() + Z轴跳跃', 'player_move.gd', '第四章 战士基础'],
        ],
        col_widths=[30*mm, 40*mm, 35*mm, pw-105*mm],
        hdr_color=C_M1
    ))
    story.append(Paragraph('表2-1 Sprint 1.1任务清单', s_cap))

    story.append(Paragraph('关键技术决策：角色使用CharacterBody3D而非CharacterBody2D，因为需要引擎原生的3D物理来处理Z轴碰撞。Sprite3D的billboard模式设为Y-Billboard，确保角色始终面向摄像机但保留上下朝向。角色像素图的渲染需要关闭纹理过滤（filter = nearest），保持像素锐利感。', s_body))

    # Sprint 1.2
    story.append(Paragraph('2.2 Sprint 1.2：战士战斗系统（第2-3周）', s_h2))
    story.append(Paragraph('在2.5D框架之上实现战士的完整战斗循环。战士的核心机制是怒气系统——受击和攻击都会积累怒气，怒气越高伤害越高，这要求怒气条必须非常直观地呈现在屏幕上。本冲刺需要实现战士的4个基础技能（重击、战吼、格挡反击、旋风斩）和怒气资源管理，确保技能释放有打击感和策略性。', s_body))

    story.append(mk_table(
        ['任务', 'Godot节点/资源', '产出物', '关键参数'],
        [
            ['怒气资源系统', 'Resource (RageBar)', 'rage_resource.tres', '最大100，受击+8/攻击+5'],
            ['重击技能', 'Area3D + Timer', 'skill_heavy_strike.gd', '150%物伤，耗20怒+50%'],
            ['战吼技能', 'Area3D(范围检测)', 'skill_war_cry.gd', '嘲讽+自防+20%持续8秒'],
            ['格挡反击', 'RayCast3D + Signal', 'skill_block_counter.gd', '格挡成功反击80%+10怒'],
            ['旋风斩', 'Area3D(旋转碰撞)', 'skill_whirlwind.gd', '周围360%伤害3秒'],
            ['伤害数字浮动', 'Label3D + Tween', 'damage_number.gd', '暴击放大+变色'],
            ['受击反馈', 'Shader (闪白) + Shake', 'hit_feedback.gd', '0.1秒闪白+0.05秒震屏'],
        ],
        col_widths=[28*mm, 35*mm, 38*mm, pw-101*mm],
        hdr_color=C_M1
    ))
    story.append(Paragraph('表2-2 Sprint 1.2任务清单', s_cap))

    story.append(Paragraph('打击感实现要点：伤害数字使用Label3D漂浮在受击位置上方，暴击时字号放大1.5倍并变为红色。受击闪白通过Shader实现（uniform控制mix系数），配合Camera2D的轻微震动（0.05秒随机偏移2-3像素），这三个要素叠加就能产生明显的打击反馈。', s_body))

    # Sprint 1.3
    story.append(Paragraph('2.3 Sprint 1.3：敌人与Boss验证（第3周）', s_h2))
    story.append(Paragraph('实现1个小怪和1个Boss，验证战斗系统的完整循环。小怪选择设计文档中的"源脉哨兵"（第一章区域），Boss选择"裂隙守卫"（第一章Boss）。Boss必须有多阶段机制，否则无法验证Z轴战斗的深度。', s_body))

    story.append(mk_table(
        ['任务', '敌人', '核心AI', '设计文档参考'],
        [
            ['源脉哨兵 AI', '源脉哨兵(Lv.2)', '巡逻->追击->近战攻击', '第八章 小怪设计'],
            ['裂隙守卫 Boss', '裂隙守卫(Lv.6)', '三阶段：普攻->召唤+跳跃->狂暴', '第九章 Boss设计'],
            ['Boss血条UI', 'TextureProgressBar', 'boss_hp_bar.tscn', '第二十三章 UI/UX'],
            ['战利品掉落', 'RigidBody3D(掉落物)', 'loot_drop.gd', '第十章 装备掉落'],
        ],
        col_widths=[30*mm, 30*mm, 40*mm, pw-100*mm],
        hdr_color=C_M1
    ))
    story.append(Paragraph('表2-3 Sprint 1.3任务清单', s_cap))

    story.append(Paragraph('Boss三阶段设计：阶段一（HP 100%-60%）为地面普攻模式，缓慢横扫+重击；阶段二（HP 60%-30%）召唤2只源脉哨兵+开始使用Z轴跳跃攻击（跳到高处平台再俯冲）；阶段三（HP 30%以下）进入狂暴，攻速+50%+地面震击产生AOE。这个三阶段设计能充分验证Z轴战斗的立体感。', s_body))

    # M1 质量门
    story.append(Paragraph('2.4 里程碑1质量门', s_h2))
    story.append(mk_table(
        ['验证项', '通过标准', '失败处理'],
        [
            ['2.5D渲染效果', '3D场景有纵深感，2D角色不违和，Z轴跳跃可见高度差', '调整Camera FOV/Sprite3D缩放'],
            ['战斗手感', '攻击有反馈，闪避有意义，怒气管理有策略', '调整打击感参数/技能数值'],
            ['Boss体验', '3-5次尝试可通关，每阶段机制可辨识', '调整Boss数值/AI行为树'],
            ['性能', '60fps稳定（小怪5只+Boss同屏）', '优化渲染/减少drawcall'],
        ],
        col_widths=[30*mm, 55*mm, pw-85*mm],
        hdr_color=C_M1
    ))
    story.append(Paragraph('表2-4 里程碑1质量门验证标准', s_cap))

    # ═══ 三、里程碑2：职业与装备 ═══
    story.append(Paragraph('三、里程碑2：职业与装备体系', s_m2))
    story.append(ColorBar(C_M2, pw, 2))
    story.append(Paragraph('里程碑1验证了"好不好玩"，里程碑2要验证"有没有深度"。8个职业各自拥有独一无二的核心机制（怒气/蓄力/暗杀/元素共鸣/搓招/圣盾/召唤物AI/部署），这些机制能否各自产生不同的操作乐趣？装备系统是否真正影响数值和玩法？本里程碑结束时，玩家应该能用8个职业分别打同一个Boss，体验到截然不同的战斗方式。', s_body))

    # Sprint 2.1
    story.append(Paragraph('3.1 Sprint 2.1：8职业核心机制（第4-6周）', s_h2))
    story.append(Paragraph('每个职业实现核心机制+3-4个基础技能。不需要实现一转/二转分支，只做初始形态。优先级按机制复杂度排序：战士（已有）>法师（元素共鸣）>骑士（圣盾守护）>刺客（暗杀判定）>武僧（搓招系统）>召唤师（召唤物AI）>游侠（蓄力射击）>机关师（部署系统）。', s_body))

    story.append(mk_table(
        ['职业', '核心机制资源', '关键脚本', '机制验证要点'],
        [
            ['战士', 'rage_resource.tres', 'warrior_controller.gd', '怒气积累/消耗循环'],
            ['法师', 'element_stack_resource.tres', 'mage_controller.gd', '三系交替触发共鸣'],
            ['骑士', 'shield_guard_resource.tres', 'knight_controller.gd', '为队友分伤+嘲讽'],
            ['刺客', 'assassinate_resource.tres', 'assassin_controller.gd', '背击/隐身触发暗杀'],
            ['武僧', 'combo_sequence_resource.tres', 'monk_controller.gd', '方向+按键出招表'],
            ['召唤师', 'summon_ai_controller.gd', 'summoner_controller.gd', '召唤物独立AI作战'],
            ['游侠', 'charge_shot_resource.tres', 'ranger_controller.gd', '蓄力时间与伤害/穿透'],
            ['机关师', 'deploy_system.gd', 'mechanic_controller.gd', '放置炮台/陷阱/傀儡'],
        ],
        col_widths=[18*mm, 35*mm, 35*mm, pw-88*mm],
        hdr_color=C_M2
    ))
    story.append(Paragraph('表3-1 8职业核心机制开发清单', s_cap))

    story.append(Paragraph('散人职业的特殊处理：散人可使用所有职业技能但效果仅50%，等级上限30级。实现方式是在SkillComponent中添加一个职业系数（class_modifier），散人设为0.5，其他职业设为1.0。散人的角色不在本里程碑实现，而是放在里程碑3的转职流程中作为初始形态出现。', s_body))

    # Sprint 2.2
    story.append(Paragraph('3.2 Sprint 2.2：装备与属性系统（第6-7周）', s_h2))
    story.append(Paragraph('装备系统的核心原则是"装备管数值，天赋管机制"——装备只改变攻击力、防御力、生命值等数值属性，不改变技能行为；技能行为的质变由天赋词条系统负责。这种分离让数值平衡更容易调试，也让装备掉落时的预期更清晰。', s_body))

    story.append(mk_table(
        ['任务', 'Godot实现', '产出物', '数据参考'],
        [
            ['装备数据结构', 'Resource (EquipmentData)', 'equipment_data.gd', '第十章 装备系统'],
            ['装备槽位管理', 'Node (EquipmentManager)', 'equipment_manager.gd', '6槽：武器/头/身/手/脚/饰品'],
            ['属性计算引擎', 'Node (StatCalculator)', 'stat_calculator.gd', '第十五章 数值框架'],
            ['品质系统', 'Enum (White/Green/Blue/Purple/Orange)', 'quality_system.gd', '第十章 品质等级'],
            ['装备掉落', 'LootTable Resource', 'loot_table.gd', '第十章 掉落规则'],
            ['背包UI', 'Control (GridContainer)', 'inventory_ui.tscn', '第二十三章 UI/UX'],
        ],
        col_widths=[28*mm, 38*mm, 35*mm, pw-101*mm],
        hdr_color=C_M2
    ))
    story.append(Paragraph('表3-2 装备系统开发清单', s_cap))

    story.append(Paragraph('属性计算的核心公式来自设计文档第十五章：角色总属性 = 基础属性 x (1 + 装备加成%) + 装备固定加成。基础属性由等级和职业决定（约占满级总属性的30%-40%），装备加成约占50%-60%，天赋加成约占10%-15%。这种分配确保装备是最主要的成长来源，但不会让无装备角色完全无法战斗。', s_body))

    # Sprint 2.3
    story.append(Paragraph('3.3 Sprint 2.3：天赋词条系统（第7-8周）', s_h2))
    story.append(Paragraph('天赋词条系统是"装备管数值，天赋管机制"的后半段。天赋不增加攻击力数值，而是改变技能行为——比如战士的"怒气获取+50%"让怒气循环加速，刺客的"暗杀判定范围+30%"让背击更容易触发。天赋以树状结构呈现，每个职业有3条路线（对应3个一转分支的前置），玩家每5级获得1个天赋点。', s_body))

    story.append(mk_table(
        ['任务', '实现方式', '产出物'],
        [
            ['天赋数据结构', 'Resource (TalentNode) 含前置/效果/层级', 'talent_data.gd'],
            ['天赋树UI', 'Control (GraphEdit自定义)', 'talent_tree_ui.tscn'],
            ['天赋效果注册', '信号总线 + 效果字典', 'talent_effects.gd'],
            ['5个核心天赋实现', '每职业1个验证性天赋', 'talent_warrior.gd 等'],
        ],
        col_widths=[35*mm, 55*mm, pw-90*mm],
        hdr_color=C_M2
    ))
    story.append(Paragraph('表3-3 天赋系统开发清单', s_cap))

    # M2 质量门
    story.append(Paragraph('3.4 里程碑2质量门', s_h2))
    story.append(mk_table(
        ['验证项', '通过标准'],
        [
            ['职业差异化', '8职业打同一Boss的操作方式有明显不同，至少5个职业机制有意义'],
            ['装备感知', '白装换绿装有约30%伤害提升可感知，紫装换橙装有质变感'],
            ['天赋感知', '点天赋前后技能行为有可见变化（不是纯数值）'],
            ['数值平衡', '8职业打同一Boss通关时间差异不超过50%'],
        ],
        col_widths=[35*mm, pw-35*mm],
        hdr_color=C_M2
    ))
    story.append(Paragraph('表3-4 里程碑2质量门验证标准', s_cap))

    # ═══ 四、里程碑3：世界与剧情 ═══
    story.append(Paragraph('四、里程碑3：世界与剧情原型', s_m3))
    story.append(ColorBar(C_M3, pw, 2))
    story.append(Paragraph('里程碑1和2在"竞技场"里验证了战斗，里程碑3要把战场搬到"世界"里。本里程碑的目标是让玩家能从散人出发，走过云中城的街道，走出城门进入野外区域，与NPC对话、接取任务、完成第一章"初入云中"的全部主线流程，最终完成一转。这是从"战斗原型"到"游戏体验"的关键跨越。', s_body))

    # Sprint 3.1
    story.append(Paragraph('4.1 Sprint 3.1：世界场景与移动（第8-9周）', s_h2))
    story.append(Paragraph('搭建两个可探索区域：云中城（安全区/主城）和一个野外区域（源脉荒原，Lv.1-6怪物区）。场景切换使用Godot的SceneTree切换，区域之间通过传送点连接。云中城需要至少3个功能区域：源脉广场（主线NPC）、铁匠街（装备NPC）、佣兵酒馆（支线NPC）。', s_body))

    story.append(mk_table(
        ['任务', '产出物', '设计文档参考'],
        [
            ['云中城场景', 'yuncheng.tscn (3D TileMap)', '第六章 云中城'],
            ['源脉荒原场景', 'yuanmo_wasteland.tscn', '第六章 六大区域'],
            ['场景切换管理', 'scene_manager.gd', '第二章 场景管理'],
            ['小地图', 'minimap.tscn (SubViewport)', '第二十三章 UI/UX'],
            ['3种小怪分布', '源脉哨兵/游荡灵体/碎骨蛛', '第八章 小怪设计'],
        ],
        col_widths=[35*mm, 45*mm, pw-80*mm],
        hdr_color=C_M3
    ))
    story.append(Paragraph('表4-1 Sprint 3.1任务清单', s_cap))

    # Sprint 3.2
    story.append(Paragraph('4.2 Sprint 3.2：NPC与对话系统（第9-10周）', s_h2))
    story.append(Paragraph('NPC系统是剧情的基础设施。本冲刺实现NPC放置、对话树、好感度基础框架。对话系统使用JSON驱动的对话树，支持分支选择和条件判断。好感度系统先实现5个核心NPC（老铁匠洪、源脉守卫长、猎人会长鹰眼、药草师青幽、流浪者雁回），每个NPC有6级好感度。', s_body))

    story.append(mk_table(
        ['任务', '产出物', '设计文档参考'],
        [
            ['NPC控制器', 'npc_controller.gd (StateChart)', '第十四章 NPC系统'],
            ['对话树引擎', 'dialog_tree.gd (JSON驱动)', '第十三章 任务剧情'],
            ['对话UI', 'dialog_ui.tscn (RichTextLabel)', '第二十三章 UI/UX'],
            ['好感度数据', 'affinity_resource.tres', '第十四章 好感度系统'],
            ['5个核心NPC', 'npc_hong.tscn 等', '第十四章 关键NPC'],
            ['NPC记忆系统', 'npc_memory.gd', '第十四章 NPC记忆'],
        ],
        col_widths=[30*mm, 45*mm, pw-75*mm],
        hdr_color=C_M3
    ))
    story.append(Paragraph('表4-2 Sprint 3.2任务清单', s_cap))

    # Sprint 3.3
    story.append(Paragraph('4.3 Sprint 3.3：第一章主线流程（第10-11周）', s_h2))
    story.append(Paragraph('将前面所有系统串联起来，实现从散人创建角色到完成一转的完整流程。第一章"初入云中"分为三节：第一节"起航"（Lv.1-6，学习移动/攻击/闪避，击败裂隙守卫）；第二节"抉择"（Lv.7-14，选择3个一转分支之一，学习分支技能）；第三节"守护"（Lv.15-20，使用一转技能守护云中城，完成转职仪式）。', s_body))

    story.append(mk_table(
        ['任务', '产出物', '关键流程'],
        [
            ['任务系统框架', 'quest_manager.gd', '接取/追踪/完成/奖励'],
            ['第一章任务链', 'ch1_quests.json', '起航->抉择->守护'],
            ['转职仪式场景', 'class_change.tscn', '散人->一转分支'],
            ['转职技能解锁', 'class_unlock.gd', '分支技能树开放'],
            ['新手引导集成', 'tutorial_sequencer.gd', '第二十一章 引导节奏'],
            ['过场演出', 'cutscene_player.gd', '关键剧情动画'],
        ],
        col_widths=[30*mm, 40*mm, pw-70*mm],
        hdr_color=C_M3
    ))
    story.append(Paragraph('表4-3 Sprint 3.3任务清单', s_cap))

    # M3 质量门
    story.append(Paragraph('4.4 里程碑3质量门', s_h2))
    story.append(mk_table(
        ['验证项', '通过标准'],
        [
            ['流程完整', '从创建角色到完成一转，全程无软锁/死锁，约30-45分钟流程'],
            ['对话有意义', 'NPC对话有分支选择，选择影响好感度和任务走向'],
            ['转职有仪式感', '转职时获得新技能有明显的手感变化和视觉反馈'],
            ['新手友好', '不读任何说明也能在引导下完成第一章'],
        ],
        col_widths=[35*mm, pw-35*mm],
        hdr_color=C_M3
    ))
    story.append(Paragraph('表4-4 里程碑3质量门验证标准', s_cap))

    # ═══ 五、里程碑4：完整Demo ═══
    story.append(Paragraph('五、里程碑4：完整Demo', s_m4))
    story.append(ColorBar(C_M4, pw, 2))
    story.append(Paragraph('前三个里程碑证明了核心战斗好玩、职业有深度、世界能走通。里程碑4的目标是把这些串联成一个"可发布的Demo"——不是内部测试版，而是可以给玩家试玩并收集反馈的版本。需要补齐副本系统、PVP基础模式、社交框架和UI打磨，确保整个体验从开始到结束有完整的闭环。', s_body))

    # Sprint 4.1
    story.append(Paragraph('5.1 Sprint 4.1：副本与组队（第11-13周）', s_h2))
    story.append(Paragraph('实现1个小规模副本（暗影矿坑，2-3人）和1个中型副本（源脉深渊，3-5人）。副本的核心价值是利用2.5D的Z轴做独特地形机制——暗影矿坑的矿车沿轨道在多层矿道穿行，玩家需要跳上移动的矿车躲避熔岩；源脉深渊的雾气从低处向上弥漫，需要高低交替站位。', s_body))

    story.append(mk_table(
        ['任务', '产出物', '设计文档参考'],
        [
            ['副本管理器', 'dungeon_manager.gd', '第十七章 副本系统'],
            ['暗影矿坑副本', 'dungeon_shadow_mine.tscn', '第十七章 小型副本'],
            ['源脉深渊副本', 'dungeon_source_abyss.tscn', '第十七章 中型副本'],
            ['组队匹配UI', 'party_ui.tscn', '第十七章 组队系统'],
            ['副本机制脚本', 'minecart_track.gd / fog_system.gd', '第十七章 地形机制'],
            ['副本奖励', 'dungeon_loot_table.tres', '第十七章 奖励规则'],
        ],
        col_widths=[30*mm, 50*mm, pw-80*mm],
        hdr_color=C_M4
    ))
    story.append(Paragraph('表5-1 Sprint 4.1任务清单', s_cap))

    # Sprint 4.2
    story.append(Paragraph('5.2 Sprint 4.2：PVP与社交框架（第13-14周）', s_h2))
    story.append(Paragraph('PVP系统实现1v1竞技场模式和3v3模式的基础版本。PVP的核心设计原则是"装备管下限，操作管上限"——PVP中装备属性会被压缩到合理区间，确保装备差距不会成为碾压因素。PVP数值与PVE完全分离，使用独立的伤害系数表。社交系统实现好友列表和公会基础框架，不做完整社交功能。', s_body))

    story.append(mk_table(
        ['任务', '产出物', '设计文档参考'],
        [
            ['PVP竞技场', 'pvp_arena.tscn', '第二十章 PVP系统'],
            ['PVP数值压缩', 'pvp_stat_scaler.gd', '第二十章 独立调参'],
            ['1v1匹配', 'pvp_match_1v1.gd', '第二十章 竞技场'],
            ['3v3模式', 'pvp_match_3v3.gd', '第二十章 3v3'],
            ['好友列表', 'friend_list_ui.tscn', '第二十二章 社交系统'],
            ['公会框架', 'guild_manager.gd', '第二十二章 公会'],
        ],
        col_widths=[30*mm, 45*mm, pw-75*mm],
        hdr_color=C_M4
    ))
    story.append(Paragraph('表5-2 Sprint 4.2任务清单', s_cap))

    # Sprint 4.3
    story.append(Paragraph('5.3 Sprint 4.3：UI打磨与音效（第14-16周）', s_h2))
    story.append(Paragraph('这是最后的打磨冲刺。将所有临时UI替换为正式UI，实现设计文档第二十三章描述的界面风格——深色主题+金色强调+信息密度高。添加基础音效（攻击/受击/技能/BGM），实现设置菜单（画面/音量/按键绑定），确保游戏可以在不同分辨率下正常运行。', s_body))

    story.append(mk_table(
        ['任务', '产出物', '说明'],
        [
            ['主菜单UI', 'main_menu.tscn', '开始/继续/设置/退出'],
            ['HUD正式版', 'hud.tscn', 'HP/MP/怒气/技能栏/小地图'],
            ['全屏背包UI', 'inventory_full.tscn', '装备/材料/任务物品分页'],
            ['角色面板UI', 'character_panel.tscn', '属性/天赋/装备一览'],
            ['音效管理器', 'audio_manager.gd', 'SFX/BGM分层控制'],
            ['设置菜单', 'settings_ui.tscn', '画面/音量/按键绑定'],
            ['分辨率适配', 'viewport_scaler.gd', '16:9/16:10/21:9'],
        ],
        col_widths=[30*mm, 40*mm, pw-70*mm],
        hdr_color=C_M4
    ))
    story.append(Paragraph('表5-3 Sprint 4.3任务清单', s_cap))

    # ═══ 六、技术风险与应对 ═══
    story.append(Paragraph('六、技术风险与应对', s_risk))
    story.append(ColorBar(C_RISK, pw, 2))

    story.append(mk_table(
        ['风险', '影响', '概率', '应对方案'],
        [
            ['2.5D渲染不协调', '3D场景与2D角色视觉割裂', '中', '早期原型多方案对比：Sprite3D vs Viewport贴图 vs Shader混合；调整FOV/光照/像素密度'],
            ['Z轴物理穿模', '角色穿墙/浮空/卡地形', '高', 'CharacterBody3D + move_and_slide()；设置安全边距；自定义碰撞检测回调'],
            ['搓招系统延迟', '武僧搓招输入响应慢', '中', '使用Input事件缓冲区+帧窗口判定；参考格斗游戏输入系统实现'],
            ['召唤物AI卡顿', '多召唤物同时运算导致帧率下降', '中', '召唤物使用简化状态机；远离玩家时降级为巡逻AI；限制同屏召唤物数量'],
            ['像素角色动画量大', '8职业x多技能帧动画资源过多', '高', '骨架动画+部件替换方案：通用身体+职业特征部件；减少每技能帧数至6-8帧'],
            ['PVP同步问题', '网络延迟导致命中判定不一致', '低', 'Demo阶段做本地PVP；正式版使用回滚式网络代码(rollback netcode)'],
        ],
        col_widths=[30*mm, 40*mm, 13*mm, pw-83*mm],
        hdr_color=C_RISK
    ))
    story.append(Paragraph('表6-1 技术风险清单与应对', s_cap))

    # ═══ 七、Godot项目结构建议 ═══
    story.append(Paragraph('七、Godot项目结构建议', s_h2))
    story.append(Paragraph('以下是推荐的Godot项目目录结构，按功能模块组织而非按资源类型。这种结构在项目规模扩大后更容易维护和协作，也方便版本控制时定位变更。每个文件夹内包含对应的场景(.tscn)、脚本(.gd)和资源(.tres)文件。', s_body))

    story.append(Paragraph('glory_chronicle/<br/>'
        '  project.godot<br/>'
        '  scenes/<br/>'
        '    main/             # 主场景、启动画面<br/>'
        '    characters/       # 角色（player/ + enemies/ + npcs/）<br/>'
        '    combat/           # 技能、伤害区域、buff<br/>'
        '    world/            # 区域场景（yuncheng/ + wasteland/ + dungeons/）<br/>'
        '    ui/               # 所有UI界面<br/>'
        '  scripts/<br/>'
        '    core/             # 核心系统（input/scene_manager/stat_calculator）<br/>'
        '    combat/           # 战斗逻辑（skill_component/damage_system）<br/>'
        '    world/            # 世界逻辑（quest_manager/dialog_system）<br/>'
        '    ai/               # AI行为（enemy_ai/npc_ai/summon_ai）<br/>'
        '    network/          # 网络相关（pvp匹配/社交）<br/>'
        '  resources/<br/>'
        '    data/             # 数据资源（equipment/loot_tables/quest_json）<br/>'
        '    sprites/          # 像素图（characters/effects/tilesets）<br/>'
        '    audio/            # 音效和音乐<br/>'
        '    shaders/          # 自定义Shader', s_note))

    # ═══ 八、每个冲刺结束时的检查清单 ═══
    story.append(Paragraph('八、每个冲刺结束时的检查清单', s_todo))
    story.append(ColorBar(C_TODO, pw, 2))
    story.append(Paragraph('每个冲刺结束时（约1-1.5周），需要执行以下检查清单。这不是官僚流程，而是确保增量交付质量的实用工具。如果某项检查未通过，下一个冲刺的第一优先级就是修复它，而不是继续推进新功能。', s_body))

    story.append(mk_table(
        ['检查项', '标准', '工具/方法'],
        [
            ['版本控制', '所有变更已提交，commit信息清晰', 'git status + git log'],
            ['场景可运行', '从main_scene启动无报错，核心流程无崩溃', '手动测试5分钟'],
            ['帧率达标', '测试场景稳定60fps', 'Godot性能监视器'],
            ['无回归', '上一冲刺的功能仍然正常', '手动回归测试清单'],
            ['代码规范', '无硬编码魔法数字，关键参数导出为export', '代码审查'],
            ['文档同步', '设计文档有变更则更新对应章节', '设计文档版本号更新'],
        ],
        col_widths=[28*mm, 50*mm, pw-78*mm],
        hdr_color=C_TODO
    ))
    story.append(Paragraph('表8-1 冲刺检查清单', s_cap))

    # ═══ 九、下一步行动 ═══
    story.append(Paragraph('九、立即开始的行动', s_h2))
    story.append(Paragraph('路线图已经铺好，现在最重要的是迈出第一步。以下是本周就应该开始的具体行动项，按照优先级排列。不要试图一次性搭建所有东西，而是先完成第一项，确认能运行后再进入下一项。', s_body))

    story.append(mk_table(
        ['序号', '行动', '预计耗时', '完成标志'],
        [
            ['1', '创建Godot项目，设置Git仓库', '30分钟', 'project.godot可运行，git push成功'],
            ['2', '搭建2.5D测试场景（3D地面+Camera3D）', '2小时', '能旋转视角看到3D地面'],
            ['3', '放置Sprite3D角色到场景中', '1小时', '2D像素角色出现在3D场景中'],
            ['4', '实现角色左右移动+跳跃', '3小时', 'WASD移动，空格跳跃，Z轴跳跃可见'],
            ['5', '添加攻击动画+伤害区域', '2小时', '按J键播放攻击动画，Area3D检测碰撞'],
            ['6', '添加源脉哨兵小怪', '3小时', '小怪巡逻+追击+攻击'],
            ['7', '添加怒气条UI', '1小时', '受击/攻击时怒气条可见增长'],
        ],
        col_widths=[12*mm, 55*mm, 20*mm, pw-87*mm],
        hdr_color=CP
    ))
    story.append(Paragraph('表9-1 本周行动项', s_cap))

    story.append(Paragraph('以上7项全部完成后，就拥有了里程碑1 Sprint 1.1的核心产出物——一个在3D场景中可以移动、跳跃、攻击的2D像素角色。这是整个项目最关键的第一步，走完这一步之后，后续的技能、敌人、Boss都是在同一个框架上叠加。', s_body))

    # Build
    doc.build(story)
    print(f"PDF generated: {output}")


if __name__ == '__main__':
    build_doc()
