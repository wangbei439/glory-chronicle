#!/usr/bin/env python3
"""
Generate pixel art sprite sheets for 远古熔岩龟 (Ancient Lava Turtle) boss.
640x360 pixel-perfect resolution, Nearest filtering, RGBA transparent backgrounds.
Each frame is 128x64 pixels.
"""

from PIL import Image, ImageDraw
import math
import random

# ── Color Palette ──────────────────────────────────────────────────────────────
PALETTE = {
    # Shell rock
    "shell_dark":      (55, 38, 28),
    "shell_mid":       (70, 48, 35),
    "shell_light":     (88, 62, 42),
    "shell_highlight": (100, 72, 50),

    # Lava cracks
    "lava_dark":       (180, 50, 10),
    "lava_mid":        (220, 80, 20),
    "lava_bright":     (255, 130, 30),
    "lava_hot":        (255, 180, 60),
    "lava_white":      (255, 230, 140),

    # Body skin
    "body_dark":       (72, 52, 40),
    "body_mid":        (88, 65, 48),
    "body_light":      (105, 78, 55),
    "body_highlight":  (115, 88, 62),

    # Eyes
    "eye_core":        (255, 120, 30),
    "eye_glow":        (255, 200, 80),
    "eye_white":       (255, 240, 200),
    "eye_pupil":       (60, 20, 5),

    # Legs
    "leg_dark":        (65, 45, 32),
    "leg_mid":         (78, 55, 38),
    "leg_light":       (92, 65, 45),

    # Tail
    "tail_body":       (75, 55, 40),
    "tail_lava":       (240, 90, 20),

    # Effects
    "star_yellow":     (255, 255, 100),
    "star_white":      (255, 255, 220),

    # Mouth interior
    "mouth_inner":     (50, 20, 10),
    "mouth_lava":      (230, 70, 15),

    # Damage flash
    "hurt_flash":      (255, 200, 180),
}

BG_ALPHA = 0  # Fully transparent background


def rgba(color_tuple, alpha=255):
    """Convert RGB tuple to RGBA."""
    return color_tuple + (alpha,)


def fill_rect(draw, x, y, w, h, color, alpha=255):
    """Draw a filled rectangle on an RGBA image."""
    if w <= 0 or h <= 0:
        return
    draw.rectangle([x, y, x + w - 1, y + h - 1], fill=rgba(color, alpha))


def fill_ellipse(draw, cx, cy, rx, ry, color, alpha=255):
    """Draw a filled ellipse centered at (cx, cy)."""
    if rx <= 0 or ry <= 0:
        return
    draw.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=rgba(color, alpha))


def fill_circle(draw, cx, cy, r, color, alpha=255):
    """Draw a filled circle centered at (cx, cy)."""
    fill_ellipse(draw, cx, cy, r, r, color, alpha)


def draw_dome(draw, x, y, w, h, color, alpha=255):
    """Draw a dome (half-ellipse on top of a rectangle)."""
    fill_rect(draw, x, y + h // 2, w, h // 2, color, alpha)
    fill_ellipse(draw, x + w // 2, y + h // 2, w // 2, h // 2, color, alpha)


def draw_pixel_line(draw, x1, y1, x2, y2, color, alpha=255):
    """Draw a line of pixels (Bresenham-like, but via PIL)."""
    draw.line([(x1, y1), (x2, y2)], fill=rgba(color, alpha), width=1)


def lerp_color(c1, c2, t):
    """Linearly interpolate between two RGB colors."""
    t = max(0.0, min(1.0, t))
    return tuple(int(a + (b - a) * t) for a, b in zip(c1, c2))


def lava_crack_pattern(draw, x, y, w, h, frame, intensity=1.0):
    """Draw lava crack lines on the shell. frame modulates pulsing."""
    pulse = 0.6 + 0.4 * math.sin(frame * math.pi / 2)
    bright = intensity * pulse

    # Define crack paths as sequences of (x_offset, y_offset) relative to shell
    cracks = [
        # Main central crack
        [(0.5, 0.15), (0.45, 0.3), (0.52, 0.5), (0.48, 0.7), (0.5, 0.85)],
        # Left branch
        [(0.3, 0.2), (0.35, 0.35), (0.25, 0.5), (0.2, 0.65)],
        # Right branch
        [(0.7, 0.25), (0.65, 0.4), (0.72, 0.55), (0.78, 0.7)],
        # Top-left small
        [(0.38, 0.1), (0.32, 0.25)],
        # Top-right small
        [(0.62, 0.12), (0.68, 0.22)],
        # Bottom-center
        [(0.5, 0.7), (0.55, 0.82), (0.48, 0.92)],
    ]

    for crack_idx, crack in enumerate(cracks):
        for i in range(len(crack) - 1):
            x1 = int(x + crack[i][0] * w)
            y1 = int(y + crack[i][1] * h)
            x2 = int(x + crack[i + 1][0] * w)
            y2 = int(y + crack[i + 1][1] * h)

            # Outer glow (wider, dimmer)
            glow_color = lerp_color(PALETTE["shell_dark"], PALETTE["lava_dark"], bright * 0.5)
            draw_pixel_line(draw, x1 - 1, y1, x2 - 1, y2, glow_color, int(160 * bright))
            draw_pixel_line(draw, x1 + 1, y1, x2 + 1, y2, glow_color, int(160 * bright))

            # Core crack line
            if bright > 0.3:
                core_color = lerp_color(PALETTE["lava_dark"], PALETTE["lava_bright"], bright)
                draw_pixel_line(draw, x1, y1, x2, y2, core_color, int(220 * bright))

            # Hot center (thinner, brighter)
            if bright > 0.5:
                hot_color = lerp_color(PALETTE["lava_bright"], PALETTE["lava_hot"], bright)
                mid_x = (x1 + x2) // 2
                mid_y = (y1 + y2) // 2
                fill_rect(draw, mid_x, mid_y, 1, 1, hot_color, int(200 * bright))


def draw_shell_base(draw, sx, sy, sw, sh, lava_frame=0, lava_intensity=1.0):
    """Draw the volcanic shell with lava cracks."""
    # Shell base - darker bottom layer
    draw_dome(draw, sx, sy, sw, sh, PALETTE["shell_dark"])

    # Shell mid-tone overlay (slightly smaller)
    draw_dome(draw, sx + 2, sy + 1, sw - 4, sh - 2, PALETTE["shell_mid"])

    # Shell highlight on top
    draw_dome(draw, sx + 6, sy + 2, sw - 12, sh // 2 + 2, PALETTE["shell_light"])

    # Shell top specular highlight
    fill_ellipse(draw, sx + sw // 2, sy + sh // 4, sw // 6, sh // 6,
                 PALETTE["shell_highlight"], 180)

    # Rocky texture bumps on shell
    random.seed(42)  # Deterministic for consistency
    for _ in range(12):
        bx = sx + random.randint(4, sw - 5)
        by = sy + random.randint(2, sh - 4)
        bw = random.randint(2, 4)
        bh = random.randint(1, 3)
        c = random.choice([PALETTE["shell_dark"], PALETTE["shell_mid"], PALETTE["shell_light"]])
        fill_rect(draw, bx, by, bw, bh, c, 200)

    # Lava cracks
    lava_crack_pattern(draw, sx, sy, sw, sh, lava_frame, lava_intensity)

    # Lava seepage at bottom edge of shell
    pulse = 0.5 + 0.5 * math.sin(lava_frame * math.pi / 2)
    for i in range(4):
        seep_x = sx + sw // 5 + i * (sw // 5)
        seep_h = int(2 + 2 * pulse)
        fill_rect(draw, seep_x, sy + sh - 1, 3, seep_h,
                  lerp_color(PALETTE["lava_dark"], PALETTE["lava_mid"], pulse),
                  int(180 * pulse))


def draw_head_base(draw, hx, hy, hw, hh, mouth_open=0, facing_left=True):
    """Draw the turtle head. mouth_open: 0=closed, 1=full open."""
    # Neck
    neck_w = hw // 2
    neck_h = hh // 3
    fill_rect(draw, hx + hw // 4, hy + hh - neck_h, neck_w, neck_h + 2,
              PALETTE["body_dark"])
    fill_rect(draw, hx + hw // 4 + 1, hy + hh - neck_h, neck_w - 2, neck_h,
              PALETTE["body_mid"])

    # Head base (rectangular with rounded top)
    fill_rect(draw, hx, hy + 2, hw, hh - 2, PALETTE["body_mid"])
    fill_rect(draw, hx + 1, hy, hw - 2, 3, PALETTE["body_mid"])
    fill_rect(draw, hx + 2, hy - 1, hw - 4, 2, PALETTE["body_light"])

    # Jaw / mouth area
    jaw_y = hy + hh * 2 // 3
    if mouth_open > 0:
        # Open mouth
        mouth_h = max(2, int(4 * mouth_open))
        fill_rect(draw, hx + 2, jaw_y, hw - 4, mouth_h, PALETTE["mouth_inner"])
        # Lava drool inside mouth
        fill_rect(draw, hx + 4, jaw_y + 1, 3, max(1, mouth_h - 2), PALETTE["mouth_lava"],
                  int(200 * mouth_open))
        # Upper jaw line
        fill_rect(draw, hx + 1, jaw_y - 1, hw - 2, 1, PALETTE["body_dark"])
        # Lower jaw
        fill_rect(draw, hx + 2, jaw_y + mouth_h, hw - 5, 3, PALETTE["body_mid"])
        fill_rect(draw, hx + 3, jaw_y + mouth_h, hw - 7, 2, PALETTE["body_dark"])
    else:
        # Closed mouth - just a line
        fill_rect(draw, hx + 2, jaw_y, hw - 5, 1, PALETTE["body_dark"])

    # Nostril
    nostril_x = hx + 3 if facing_left else hx + hw - 5
    fill_rect(draw, nostril_x, hy + 4, 2, 1, PALETTE["body_dark"])

    # Eye
    eye_x = hx + hw // 3 if facing_left else hx + hw * 2 // 3
    eye_y = hy + hh // 3
    # Eye socket (darker)
    fill_rect(draw, eye_x - 2, eye_y - 2, 5, 4, PALETTE["body_dark"])
    # Eye glow aura
    fill_circle(draw, eye_x, eye_y, 3, PALETTE["lava_dark"], 80)
    # Eye core
    fill_rect(draw, eye_x - 1, eye_y - 1, 3, 3, PALETTE["eye_core"])
    # Pupil
    fill_rect(draw, eye_x, eye_y, 1, 1, PALETTE["eye_pupil"])
    # Eye highlight
    fill_rect(draw, eye_x - 1, eye_y - 1, 1, 1, PALETTE["eye_glow"], 200)

    # Brow ridge
    fill_rect(draw, hx + 1, hy + hh // 3 - 3, hw - 3, 1, PALETTE["body_dark"])
    fill_rect(draw, hx + 2, hy + hh // 3 - 2, hw - 5, 1, PALETTE["body_dark"], 150)

    # Top of head texture
    fill_rect(draw, hx + 3, hy + 1, hw - 6, 1, PALETTE["body_highlight"], 120)


def draw_leg_base(draw, lx, ly, lw, lh, phase=0):
    """Draw a single leg with rocky texture. phase: 0-3 for walk animation."""
    # Offset for walk animation
    lift = 0
    if phase == 1:
        lift = -2
    elif phase == 3:
        lift = -1

    adjusted_y = ly + lift

    # Leg body
    fill_rect(draw, lx, adjusted_y, lw, lh, PALETTE["leg_mid"])
    # Darker edges
    fill_rect(draw, lx, adjusted_y, 1, lh, PALETTE["leg_dark"])
    fill_rect(draw, lx + lw - 1, adjusted_y, 1, lh, PALETTE["leg_dark"])
    fill_rect(draw, lx, adjusted_y, lw, 1, PALETTE["leg_dark"])

    # Toe/claw details
    for i in range(3):
        toe_x = lx + 1 + i * (lw // 3)
        fill_rect(draw, toe_x, adjusted_y + lh - 1, 2, 1, PALETTE["leg_dark"])
        fill_rect(draw, toe_x, adjusted_y + lh - 2, 1, 1, PALETTE["leg_light"], 180)

    # Rocky texture spots
    random.seed(lx * 100 + ly)  # Deterministic per leg position
    for _ in range(3):
        rx = lx + random.randint(1, lw - 3)
        ry = adjusted_y + random.randint(1, lh - 3)
        fill_rect(draw, rx, ry, 2, 1, PALETTE["leg_light"], 150)


def draw_tail_base(draw, tx, ty, tw, th, lava_tip=True):
    """Draw the tail with optional lava tip."""
    # Tail body - tapered shape
    for i in range(tw):
        taper = max(1, th - (i * th) // tw)
        y_off = (th - taper) // 2
        c = PALETTE["tail_body"] if i < tw - 3 else PALETTE["body_mid"]
        fill_rect(draw, tx + i, ty + y_off, 1, taper, c)

    # Lava tip
    if lava_tip:
        fill_rect(draw, tx + tw - 3, ty + th // 2 - 1, 3, 3, PALETTE["tail_lava"])
        fill_rect(draw, tx + tw - 2, ty + th // 2, 1, 1, PALETTE["lava_bright"], 200)


def draw_lava_turtle_base(draw, ox, oy, frame=0, anim="idle", anim_frame=0):
    """
    Draw a complete lava turtle boss frame.
    ox, oy: origin offset within the frame
    frame: global frame counter for lava pulsing
    anim: animation name
    anim_frame: frame within this animation
    """
    # ── Layout Constants ──
    # Shell
    SHELL_X = ox + 22
    SHELL_Y = oy + 4
    SHELL_W = 76
    SHELL_H = 30

    # Head
    HEAD_X = ox + 2
    HEAD_Y = oy + 20
    HEAD_W = 22
    HEAD_H = 16

    # Legs (4 legs - 2 near, 2 far with slight offset)
    LEG_W = 10
    LEG_H = 14

    # Front near leg
    FL_X = ox + 28
    FL_Y = oy + 40

    # Front far leg (slightly behind)
    FFL_X = ox + 24
    FFL_Y = oy + 42

    # Back near leg
    BL_X = ox + 80
    BL_Y = oy + 40

    # Back far leg
    BFL_X = ox + 84
    BFL_Y = oy + 42

    # Tail
    TAIL_X = ox + 96
    TAIL_Y = oy + 28
    TAIL_W = 14
    TAIL_H = 6

    # ── Animation Modifications ──
    head_offset_x = 0
    head_offset_y = 0
    mouth_open = 0.0
    shell_offset_y = 0
    leg_phases = [0, 0, 0, 0]  # FL, FFL, BL, BFL
    lava_intensity = 1.0
    tail_offset_x = 0
    alpha_mult = 255
    extra_lava = False

    if anim == "idle":
        # Breathing - shell bobs slightly
        breath = [0, -1, 0, 1][anim_frame % 4]
        shell_offset_y = breath
        head_offset_y = breath
        lava_intensity = 0.7 + 0.3 * (anim_frame % 4) / 3.0

    elif anim == "walk":
        # Heavy walk cycle
        walk_cycle = anim_frame % 4
        shell_offset_y = [0, -1, 0, -1][walk_cycle]
        head_offset_y = [0, -1, 0, -1][walk_cycle]
        # Alternating leg pairs
        if walk_cycle == 0:
            leg_phases = [0, 2, 2, 0]  # FL, FFL, BL, BFL
        elif walk_cycle == 1:
            leg_phases = [1, 3, 3, 1]
        elif walk_cycle == 2:
            leg_phases = [2, 0, 0, 2]
        else:
            leg_phases = [3, 1, 1, 3]

    elif anim == "attack":
        # Head lunge bite
        if anim_frame == 0:
            head_offset_x = 0
            head_offset_y = 0
            mouth_open = 0.0
        elif anim_frame == 1:
            head_offset_x = -3
            head_offset_y = 1
            mouth_open = 0.3
        elif anim_frame == 2:
            head_offset_x = -8
            head_offset_y = 2
            mouth_open = 1.0
        elif anim_frame == 3:
            head_offset_x = -5
            head_offset_y = 1
            mouth_open = 0.5

    elif anim == "shell_spin":
        # Retract into shell
        if anim_frame == 0:
            # Starting to retract
            shell_offset_y = 0
            head_offset_y = 3
            head_offset_x = 6
            lava_intensity = 1.3
        else:
            # Fully retracted, spinning (no head visible, shell slightly different)
            shell_offset_y = -2
            head_offset_y = 20  # Hidden
            lava_intensity = 1.5

    elif anim == "lava_spit":
        # Open mouth, spit lava
        if anim_frame == 0:
            mouth_open = 0.8
            head_offset_y = -1
            lava_intensity = 1.4
            extra_lava = True
        else:
            mouth_open = 1.0
            head_offset_x = -2
            head_offset_y = -2
            lava_intensity = 1.5
            extra_lava = True

    elif anim == "stunned":
        # Dazed
        lava_intensity = 0.3
        if anim_frame == 0:
            head_offset_y = -2
        else:
            head_offset_y = -1
            head_offset_x = 1

    elif anim == "hurt":
        # Recoil
        if anim_frame == 0:
            head_offset_x = 4
            head_offset_y = -2
            shell_offset_y = -1
            lava_intensity = 1.5
        else:
            head_offset_x = 2
            head_offset_y = -1
            lava_intensity = 1.2

    elif anim == "death":
        # Shell cracks, lava spills, collapses
        progress = anim_frame / 3.0
        lava_intensity = 1.0 + progress * 0.5
        if anim_frame == 0:
            # Initial hit
            head_offset_y = -2
            lava_intensity = 1.5
        elif anim_frame == 1:
            # Cracking
            head_offset_y = 2
            shell_offset_y = 1
            lava_intensity = 1.8
        elif anim_frame == 2:
            # Lava spilling
            head_offset_y = 5
            shell_offset_y = 4
            lava_intensity = 2.0
            extra_lava = True
        elif anim_frame == 3:
            # Collapsed
            head_offset_y = 8
            shell_offset_y = 8
            lava_intensity = 1.5
            extra_lava = True

    # ── Draw Order (back to front) ──

    # Far legs (drawn first, slightly darker)
    draw_leg_base(draw, FFL_X, FFL_Y + shell_offset_y, LEG_W - 1, LEG_H - 1,
                  leg_phases[1])
    # Re-draw far legs with darker tint
    fill_rect(draw, FFL_X, FFL_Y + shell_offset_y, LEG_W - 1, LEG_H - 1,
              PALETTE["leg_dark"], 220)

    draw_leg_base(draw, BFL_X, BFL_Y + shell_offset_y, LEG_W - 1, LEG_H - 1,
                  leg_phases[3])
    fill_rect(draw, BFL_X, BFL_Y + shell_offset_y, LEG_W - 1, LEG_H - 1,
              PALETTE["leg_dark"], 220)

    # Tail
    draw_tail_base(draw, TAIL_X + tail_offset_x, TAIL_Y + shell_offset_y,
                   TAIL_W, TAIL_H, lava_tip=(anim != "stunned"))

    # Body (under shell, connecting legs)
    body_y = SHELL_Y + SHELL_H - 2 + shell_offset_y
    body_h = 14
    fill_rect(draw, SHELL_X - 4, body_y, SHELL_W + 8, body_h, PALETTE["body_dark"])
    fill_rect(draw, SHELL_X - 2, body_y + 1, SHELL_W + 4, body_h - 2, PALETTE["body_mid"])
    # Belly highlight
    fill_rect(draw, SHELL_X + 5, body_y + 2, SHELL_W - 10, 3, PALETTE["body_light"], 140)

    # Near legs
    draw_leg_base(draw, FL_X, FL_Y + shell_offset_y, LEG_W, LEG_H,
                  leg_phases[0])
    draw_leg_base(draw, BL_X, BL_Y + shell_offset_y, LEG_W, LEG_H,
                  leg_phases[2])

    # Shell
    draw_shell_base(draw, SHELL_X, SHELL_Y + shell_offset_y,
                    SHELL_W, SHELL_H,
                    lava_frame=frame + anim_frame,
                    lava_intensity=min(lava_intensity, 2.0))

    # Extra lava effects for certain animations
    if extra_lava:
        draw_extra_lava(draw, SHELL_X, SHELL_Y + shell_offset_y,
                        SHELL_W, SHELL_H, anim, anim_frame)

    # Shell spin special: draw rotation lines
    if anim == "shell_spin" and anim_frame == 1:
        draw_spin_lines(draw, SHELL_X + SHELL_W // 2, SHELL_Y + SHELL_H // 2 + shell_offset_y)

    # Head (may be hidden for shell_spin)
    if anim != "shell_spin" or anim_frame == 0:
        draw_head_base(draw,
                       HEAD_X + head_offset_x,
                       HEAD_Y + head_offset_y,
                       HEAD_W, HEAD_H,
                       mouth_open=mouth_open,
                       facing_left=True)

    # Stunned stars
    if anim == "stunned":
        draw_stun_stars(draw, HEAD_X + HEAD_W // 2 + head_offset_x,
                        HEAD_Y - 8 + head_offset_y, anim_frame)

    # Death cracks and lava pool
    if anim == "death":
        draw_death_effects(draw, ox, oy, SHELL_X, SHELL_Y + shell_offset_y,
                           SHELL_W, SHELL_H, anim_frame)

    # Hurt flash overlay
    if anim == "hurt" and anim_frame == 0:
        # Brief white flash on the whole body area
        fill_rect(draw, ox + 5, oy + 5, 110, 50, PALETTE["hurt_flash"], 40)


def draw_extra_lava(draw, sx, sy, sw, sh, anim, anim_frame):
    """Draw additional lava effects for special attacks."""
    if anim == "lava_spit":
        # Lava dripping from shell
        for i in range(3):
            drip_x = sx + 15 + i * 20
            drip_y = sy + sh
            fill_rect(draw, drip_x, drip_y, 2, 4, PALETTE["lava_mid"], 200)
            fill_rect(draw, drip_x, drip_y + 3, 2, 2, PALETTE["lava_bright"], 180)

        # Lava spit projectile in front of mouth
        spit_x = sx - 18 if anim_frame == 1 else sx - 10
        spit_y = sy + sh // 2 + 5
        fill_circle(draw, spit_x, spit_y, 4, PALETTE["lava_bright"], 220)
        fill_circle(draw, spit_x, spit_y, 2, PALETTE["lava_hot"], 240)
        fill_rect(draw, spit_x - 1, spit_y - 1, 3, 3, PALETTE["lava_white"], 200)
        # Trail
        for t in range(3):
            tx = spit_x + 5 + t * 4
            ty = spit_y + t
            r = max(1, 3 - t)
            fill_circle(draw, tx, ty, r, PALETTE["lava_mid"], int(180 - t * 50))

    elif anim == "death":
        # Lava overflowing from shell
        for i in range(5):
            flow_x = sx + 8 + i * 14
            flow_y = sy + sh - 2
            flow_h = 3 + anim_frame * 2
            fill_rect(draw, flow_x, flow_y, 3, flow_h, PALETTE["lava_mid"], 200)
            fill_rect(draw, flow_x + 1, flow_y + 1, 1, flow_h - 1, PALETTE["lava_bright"], 180)


def draw_spin_lines(draw, cx, cy):
    """Draw motion blur lines for shell spin."""
    for angle_offset in range(0, 360, 45):
        rad = math.radians(angle_offset)
        x1 = cx + int(25 * math.cos(rad))
        y1 = cy + int(15 * math.sin(rad))
        x2 = cx + int(38 * math.cos(rad))
        y2 = cy + int(22 * math.sin(rad))
        draw_pixel_line(draw, x1, y1, x2, y2, PALETTE["shell_highlight"], 120)


def draw_stun_stars(draw, cx, cy, frame):
    """Draw spinning stars above head for stun effect."""
    positions = [(-8, -2), (0, -6), (8, -2), (-4, -8), (4, -8)]
    for i, (dx, dy) in enumerate(positions):
        # Rotate position based on frame
        angle = (frame * 30 + i * 72) * math.pi / 180
        rx = int(dx * math.cos(angle) - dy * math.sin(angle))
        ry = int(dx * math.sin(angle) + dy * math.cos(angle))
        sx = cx + rx
        sy = cy + ry
        # Draw a small star (cross shape)
        c = PALETTE["star_yellow"] if i % 2 == 0 else PALETTE["star_white"]
        fill_rect(draw, sx - 1, sy, 3, 1, c, 220)
        fill_rect(draw, sx, sy - 1, 1, 3, c, 220)


def draw_death_effects(draw, ox, oy, sx, sy, sw, sh, frame):
    """Draw death animation effects - cracks, lava spills, collapse."""
    if frame >= 1:
        # Shell cracks (thick jagged lines)
        crack_lines = [
            ((sx + sw // 3, sy + sh // 4), (sx + sw // 3 + 5, sy + sh // 2)),
            ((sx + sw * 2 // 3, sy + sh // 3), (sx + sw // 2, sy + sh * 3 // 4)),
        ]
        if frame >= 2:
            crack_lines.extend([
                ((sx + sw // 4, sy + sh // 2), (sx + sw // 2, sy + sh - 2)),
                ((sx + sw * 3 // 4, sy + sh // 4), (sx + sw // 2 + 8, sy + sh * 2 // 3)),
            ])

        for (x1, y1), (x2, y2) in crack_lines:
            draw_pixel_line(draw, x1, y1, x2, y2, PALETTE["lava_bright"], 230)
            draw_pixel_line(draw, x1 - 1, y1, x2 - 1, y2, PALETTE["lava_mid"], 180)

    if frame >= 2:
        # Lava pool spreading underneath
        pool_y = oy + 56
        pool_w = 60 + (frame - 2) * 30
        pool_x = ox + 64 - pool_w // 2
        fill_rect(draw, pool_x, pool_y, pool_w, 4, PALETTE["lava_dark"], 200)
        fill_rect(draw, pool_x + 2, pool_y + 1, pool_w - 4, 2, PALETTE["lava_mid"], 220)
        fill_rect(draw, pool_x + pool_w // 3, pool_y, pool_w // 3, 3, PALETTE["lava_bright"], 180)

    if frame >= 3:
        # Collapsed - lower alpha, more lava
        fill_rect(draw, ox + 20, oy + 48, 88, 6, PALETTE["lava_mid"], 160)
        fill_rect(draw, ox + 30, oy + 49, 68, 4, PALETTE["lava_bright"], 180)


def apply_alpha_target(img, target_alpha_pct=0.80):
    """Scale non-zero alpha values to target percentage (78-82%)."""
    import numpy as np
    arr = np.array(img)
    alpha = arr[:, :, 3]
    mask = alpha > 0
    # Scale existing alpha values relative to target (preserve relative variation)
    # target_alpha_pct of 0.80 means max alpha becomes 204 (80% of 255)
    scale = target_alpha_pct  # 0.78-0.82 range
    alpha[mask] = np.clip(alpha[mask].astype(float) * scale, 0, 255).astype(np.uint8)
    arr[:, :, 3] = alpha
    return Image.fromarray(arr)


def create_sprite_sheet(anim_name, frame_count, frame_w, frame_h, output_path):
    """Create a complete sprite sheet for one animation."""
    total_w = frame_w * frame_count
    sheet = Image.new("RGBA", (total_w, frame_h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(sheet)

    for f in range(frame_count):
        ox = f * frame_w
        draw_lava_turtle_base(draw, ox, 0, frame=f, anim=anim_name, anim_frame=f)

    # Apply target alpha scaling (78-82% range)
    sheet = apply_alpha_target(sheet, target_alpha_pct=0.80)

    sheet.save(output_path, "PNG")
    print(f"  Saved: {output_path} ({total_w}x{frame_h})")


def create_single_frame(output_path, frame_w=128, frame_h=64):
    """Create a single-frame fallback sprite."""
    img = Image.new("RGBA", (frame_w, frame_h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw_lava_turtle_base(draw, 0, 0, frame=0, anim="idle", anim_frame=0)

    # Apply target alpha scaling (78-82% range)
    img = apply_alpha_target(img, target_alpha_pct=0.80)

    img.save(output_path, "PNG")
    print(f"  Saved: {output_path} ({frame_w}x{frame_h})")


def main():
    output_dir = "/home/z/my-project/godot/legend/assets/sprites/enemy/"

    print("=== Generating 远古熔岩龟 (Ancient Lava Turtle) Boss Sprite Sheets ===\n")
    print(f"Output directory: {output_dir}\n")

    FRAME_W = 128
    FRAME_H = 64

    # 1. Idle - 4 frames (512x64)
    print("[1/9] Generating idle sheet...")
    create_sprite_sheet("idle", 4, FRAME_W, FRAME_H,
                        output_dir + "boss_lava_turtle_idle_sheet.png")

    # 2. Walk - 4 frames (512x64)
    print("[2/9] Generating walk sheet...")
    create_sprite_sheet("walk", 4, FRAME_W, FRAME_H,
                        output_dir + "boss_lava_turtle_walk_sheet.png")

    # 3. Attack (bite) - 4 frames (512x64)
    print("[3/9] Generating attack sheet...")
    create_sprite_sheet("attack", 4, FRAME_W, FRAME_H,
                        output_dir + "boss_lava_turtle_attack_sheet.png")

    # 4. Shell spin - 2 frames (256x64)
    print("[4/9] Generating shell spin sheet...")
    create_sprite_sheet("shell_spin", 2, FRAME_W, FRAME_H,
                        output_dir + "boss_lava_turtle_shell_spin_sheet.png")

    # 5. Lava spit - 2 frames (256x64)
    print("[5/9] Generating lava spit sheet...")
    create_sprite_sheet("lava_spit", 2, FRAME_W, FRAME_H,
                        output_dir + "boss_lava_turtle_lava_spit_sheet.png")

    # 6. Stunned - 2 frames (256x64)
    print("[6/9] Generating stunned sheet...")
    create_sprite_sheet("stunned", 2, FRAME_W, FRAME_H,
                        output_dir + "boss_lava_turtle_stunned_sheet.png")

    # 7. Hurt - 2 frames (256x64)
    print("[7/9] Generating hurt sheet...")
    create_sprite_sheet("hurt", 2, FRAME_W, FRAME_H,
                        output_dir + "boss_lava_turtle_hurt_sheet.png")

    # 8. Death - 4 frames (512x64)
    print("[8/9] Generating death sheet...")
    create_sprite_sheet("death", 4, FRAME_W, FRAME_H,
                        output_dir + "boss_lava_turtle_death_sheet.png")

    # 9. Single frame fallback (128x64)
    print("[9/9] Generating single-frame fallback...")
    create_single_frame(output_dir + "boss_lava_turtle_idle_128.png")

    print("\n=== All sprite sheets generated successfully! ===")
    print(f"\nFiles saved to: {output_dir}")

    # Print summary
    files = [
        ("boss_lava_turtle_idle_sheet.png", 512, 64, 4),
        ("boss_lava_turtle_walk_sheet.png", 512, 64, 4),
        ("boss_lava_turtle_attack_sheet.png", 512, 64, 4),
        ("boss_lava_turtle_shell_spin_sheet.png", 256, 64, 2),
        ("boss_lava_turtle_lava_spit_sheet.png", 256, 64, 2),
        ("boss_lava_turtle_stunned_sheet.png", 256, 64, 2),
        ("boss_lava_turtle_hurt_sheet.png", 256, 64, 2),
        ("boss_lava_turtle_death_sheet.png", 512, 64, 4),
        ("boss_lava_turtle_idle_128.png", 128, 64, 1),
    ]
    print(f"\n{'File':<45} {'Size':<12} {'Frames'}")
    print("-" * 72)
    for name, w, h, frames in files:
        print(f"{name:<45} {w}x{h:<8} {frames}")


if __name__ == "__main__":
    main()
