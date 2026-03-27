"""生成范蠡研讨会微信分享封面图 (300x300 正方形，微信分享小图标规格)"""
from PIL import Image, ImageDraw, ImageFont
import os, math

W, H = 300, 300
img = Image.new('RGB', (W, H), color=(10, 14, 26))
draw = ImageDraw.Draw(img)

# 渐变背景
for y in range(H):
    r = int(10 + (20 - 10) * y / H)
    g = int(14 + (18 - 14) * y / H)
    b = int(26 + (40 - 26) * y / H)
    draw.line([(0, y), (W, y)], fill=(r, g, b))

# 金色边框
gold = (201, 168, 76)
gold_light = (232, 201, 122)
draw.rectangle([8, 8, W-9, H-9], outline=gold, width=2)
draw.rectangle([12, 12, W-13, H-13], outline=(201, 168, 76, 80), width=1)

# 四角装饰
corner = 20
for cx, cy, dx, dy in [(16, 16, 1, 1), (W-16, 16, -1, 1), (16, H-16, 1, -1), (W-16, H-16, -1, -1)]:
    draw.line([(cx, cy), (cx + dx*corner, cy)], fill=gold_light, width=2)
    draw.line([(cx, cy), (cx, cy + dy*corner)], fill=gold_light, width=2)

# 顶部英文小标
try:
    font_sm = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 11)
except:
    font_sm = ImageFont.load_default()

draw.text((W//2, 38), "2026 · FANLI SUMMIT", fill=(201, 168, 76, 180), font=font_sm, anchor="mm")

# 分割线
draw.line([(40, 52), (W-40, 52)], fill=gold, width=1)

# 主标题（中文）
try:
    font_title = ImageFont.truetype("C:/Windows/Fonts/msyh.ttc", 22)
    font_sub   = ImageFont.truetype("C:/Windows/Fonts/msyh.ttc", 14)
    font_desc  = ImageFont.truetype("C:/Windows/Fonts/msyh.ttc", 11)
    font_date  = ImageFont.truetype("C:/Windows/Fonts/msyh.ttc", 12)
except:
    font_title = ImageFont.load_default()
    font_sub = font_title
    font_desc = font_title
    font_date = font_title

# 范蠡 大字
draw.text((W//2, 90), "范 蠡", fill=gold_light, font=font_title, anchor="mm")

# 副标题
draw.text((W//2, 120), "消费互联网共创研讨会", fill=(240, 230, 204), font=font_sub, anchor="mm")

# 中间分割线 + 装饰
draw.line([(50, 140), (W-50, 140)], fill=(201, 168, 76, 120), width=1)

# 描述文字
draw.text((W//2, 162), "消费筑产权 · 链上享未来", fill=(201, 168, 76), font=font_desc, anchor="mm")
draw.text((W//2, 182), "探索消费互联网新范式", fill=(180, 160, 120), font=font_desc, anchor="mm")

# 底部分割线
draw.line([(40, 210), (W-40, 210)], fill=gold, width=1)

# 日期地点
draw.text((W//2, 228), "2026年·深圳", fill=(201, 168, 76), font=font_date, anchor="mm")

# 报名提示
draw.text((W//2, 252), "▶  点击查看详情并报名", fill=(29, 233, 182), font=font_desc, anchor="mm")

# 底部小字
draw.text((W//2, 278), "扫码 / 点击链接参与", fill=(120, 110, 90), font=font_desc, anchor="mm")

out = os.path.join(os.path.dirname(__file__), "share-cover.png")
img.save(out, "PNG", optimize=True)
print(f"saved: {out}")
