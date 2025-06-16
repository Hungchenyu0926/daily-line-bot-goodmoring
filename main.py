import requests, random
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import os

# --------------CONFIG--------------
TOKEN = os.getenv("LINE_NOTIFY_TOKEN")  # 由 GitHub Secret 提供
API_URL = "https://notify-api.line.me/api/notify"

# 讀取語錄
with open("quotes.txt", encoding="utf-8") as f:
    quotes = [line.strip() for line in f if line.strip()]

# 隨機選一句
quote = random.choice(quotes)

# 產生圖片
img = Image.new("RGB", (1080, 1080), color=(255, 248, 240))
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("font/NotoSansTC-Regular.otf",  Forty=48)
# 自動換行處理（若需要可擴充）
draw.text((60, 400), quote, fill=(60, 60, 60), font=font)
output_path = "output.jpg"
img.save(output_path)

# 傳送 LINE Notify
headers = {"Authorization": f"Bearer {TOKEN}"}
payload = {"message": f"☀️ {datetime.now().strftime('%Y/%m/%d')} 的正能量語錄"}
files = {"imageFile": open(output_path, "rb")}
resp = requests.post(API_URL, headers=headers, data=payload, files=files)
if resp.status_code == 200:
    print("✅ 成功發送", quote)
else:
    print("❌ 發送失敗", resp.status_code, resp.text)

