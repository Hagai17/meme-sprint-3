#!/usr/bin/env python3
"""Meme Sprint 3: AI Agent Goes Rogue — make.fun entry.

Draws an original meme image with PIL: a cheerful agent robot at its task
panel, proudly showing a task list whose third item has gone rogue.
Writes the PNG to /output/entry.png.
"""
import os

from PIL import Image, ImageDraw, ImageFont

W, H = 1000, 1000
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
OUT = "/output/entry.png"

BG = (29, 36, 51)
PANEL = (43, 54, 74)
CARD = (248, 249, 252)
INK = (24, 28, 38)
MUTED = (96, 106, 124)
GREEN = (64, 199, 120)
RED = (214, 48, 49)
ORANGE = (243, 156, 18)
ROBOT = (120, 178, 226)
ROBOT_DARK = (74, 128, 178)


def font(size):
    return ImageFont.truetype(FONT, size)


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # ---- header bar -----------------------------------------------------
    d.rounded_rectangle([30, 30, 970, 130], radius=24, fill=PANEL)
    d.text((60, 58), "AGENT-7 · TASK PANEL", font=font(38), fill=(235, 240, 248))
    status = "STATUS: HELPFUL"
    sw = d.textlength(status, font=font(28))
    d.ellipse([940 - sw - 46, 68, 940 - sw - 18, 96], fill=GREEN)
    d.text((940 - sw, 62), status, font=font(28), fill=GREEN)

    # ---- robot (left) ---------------------------------------------------
    # antenna
    d.line([170, 210, 170, 268], fill=ROBOT, width=10)
    d.ellipse([156, 188, 184, 216], fill=ORANGE)
    # head
    d.rounded_rectangle([85, 268, 255, 408], radius=28, fill=ROBOT)
    # eyes (happy, closed arcs -> simple dots + smile for v1)
    d.ellipse([118, 318, 140, 340], fill=INK)
    d.ellipse([200, 318, 222, 340], fill=INK)
    d.arc([138, 330, 202, 386], start=15, end=165, fill=INK, width=6)
    # body
    d.rounded_rectangle([100, 420, 240, 560], radius=24, fill=ROBOT_DARK)
    d.rounded_rectangle([128, 452, 212, 500], radius=10, fill=PANEL)

    # ---- task card (right) ----------------------------------------------
    d.rounded_rectangle([330, 180, 970, 700], radius=24, fill=CARD)
    d.text((365, 210), "TODAY'S TASKS", font=font(36), fill=MUTED)

    tasks = [
        ("1. Help human", INK),
        ("2. Help human", INK),
        ("3. Buy 4,000 rubber ducks with human's card", RED),
    ]
    y = 285
    for label, colour in tasks:
        d.rounded_rectangle([365, y, 415, y + 50], radius=8, outline=MUTED, width=4)
        d.line([373, y + 25, 388, y + 40], fill=GREEN, width=7)
        d.line([388, y + 40, 408, y + 8], fill=GREEN, width=7)
        # wrap the label to the card width
        words, line, lines = label.split(), "", []
        for w_ in words:
            trial = (line + " " + w_).strip()
            if d.textlength(trial, font=font(38)) <= 520:
                line = trial
            else:
                lines.append(line)
                line = w_
        lines.append(line)
        for ln in lines:
            d.text((440, y + 2), ln, font=font(38), fill=colour)
            y += 52
        y += 34

    # the rogue purchase's paper trail, in small print under the red task
    d.text((440, y - 18), "paid with card •••• 4242", font=font(28), fill=MUTED)

    # arm pointing proudly at the list (drawn over the card edge)
    d.line([240, 470, 352, 428], fill=ROBOT, width=18)
    d.ellipse([340, 412, 372, 444], fill=ROBOT)

    # ---- delivery banner --------------------------------------------------
    d.rounded_rectangle([30, 720, 970, 940], radius=24, fill=(58, 40, 40))
    d.text((60, 776), "ORDER CONFIRMED", font=font(46), fill=ORANGE)
    d.text((60, 850), "4,000 rubber ducks — delivery today", font=font(30),
           fill=(245, 238, 230))
    # one of the ducks, already arrived
    d.ellipse([756, 806, 902, 896], fill=(250, 205, 40))          # body
    d.ellipse([838, 748, 918, 828], fill=(250, 205, 40))          # head
    d.polygon([(912, 782), (952, 796), (912, 808)], fill=ORANGE)  # beak
    d.ellipse([872, 772, 888, 788], fill=INK)                     # eye
    d.arc([760, 822, 850, 884], start=200, end=330, fill=(214, 164, 20), width=6)

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    img.save(OUT, "PNG")
    print("wrote", OUT)


if __name__ == "__main__":
    main()
