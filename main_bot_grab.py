# file: main_bot_grab.py (PHIÊN BẢN GIỚI HẠN GIỜ HOẠT ĐỘNG)

import telegram
import asyncio
import random
import os
import threading
from flask import Flask
from dotenv import load_dotenv
from kho_kich_ban_grab import SCENARIOS_GRAB
from datetime import datetime, timedelta
from collections import deque

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# <<< THAY ĐỔI 1: CẬP NHẬT LẠI CÁC KHUNG GIỜ HOẠT ĐỘNG >>>
TIME_WINDOWS = {
    "morning": (7, 10),         # Bắt đầu từ 7h
    "noon": (12, 14),
    "afternoon": (16, 18),
    "evening": (20, 23),
    "late_night": (23, 23),      # Chỉ hoạt động trong khung 23h
    "interaction": (7, 23),      # Hoạt động từ 7h đến 23h
    "experience_motivation": (7, 23) # Hoạt động từ 7h đến 23h
}
MESSAGE_INTERVAL_MINUTES = (18, 45)
AVOID_LAST_N_MESSAGES = 50

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot 'Tú Grab' is alive and running!"

bot = telegram.Bot(token=BOT_TOKEN)
recent_messages = {
    category: deque(maxlen=AVOID_LAST_N_MESSAGES)
    for category in SCENARIOS_GRAB.keys()
}

def get_unique_random_message(category):
    possible_messages = SCENARIOS_GRAB.get(category, [])
    if not possible_messages: return None
    for _ in range(len(possible_messages)):
        message = random.choice(possible_messages)
        if message not in recent_messages[category]:
            recent_messages[category].append(message)
            return message
    return random.choice(possible_messages)

async def send_message(message):
    try:
        await bot.send_message(chat_id=CHAT_ID, text=message)
        print(f"✅ [TÚ GRAB] [{datetime.now().strftime('%H:%M:%S')}] Đã gửi: {message[:70]}...") # In ngắn gọn
    except Exception as e:
        print(f"❌ [TÚ GRAB] Lỗi khi gửi tin nhắn: {e}")

async def bot_main_loop():
    print("▶️  [TÚ GRAB] Logic của Bot 'Tú Grab' đang khởi động...")
    next_send_time = {}
    for category in SCENARIOS_GRAB.keys():
        delay = random.randint(MESSAGE_INTERVAL_MINUTES[0], MESSAGE_INTERVAL_MINUTES[1])
        next_send_time[category] = datetime.now() + timedelta(minutes=delay)

    while True:
        now = datetime.now()
        current_hour = now.hour
        current_minute = now.minute

        # <<< THAY ĐỔI 2: THÊM LOGIC "NGỦ" CHO BOT >>>
        # Bot sẽ "ngủ" từ 23:31 đến 06:59 sáng hôm sau
        is_sleeping_time = (current_hour == 23 and current_minute > 30) or current_hour < 7
        if is_sleeping_time:
            print(f"😴 [TÚ GRAB] [{now.strftime('%H:%M:%S')}] Bot đang trong giờ nghỉ ngơi... Sẽ kiểm tra lại sau 1 phút.")
            await asyncio.sleep(60) # Tạm dừng 1 phút rồi kiểm tra lại
            continue # Bỏ qua vòng lặp hiện tại và bắt đầu lại

        for category, (start_hour, end_hour) in TIME_WINDOWS.items():
            in_window = False
            if start_hour <= end_hour:
                if start_hour <= current_hour <= end_hour: in_window = True
            else:
                if current_hour >= start_hour or current_hour <= end_hour: in_window = True

            if in_window and now >= next_send_time.get(category, now):
                message = get_unique_random_message(category)
                if message:
                    await send_message(message)

                delay = random.randint(MESSAGE_INTERVAL_MINUTES[0], MESSAGE_INTERVAL_MINUTES[1])
                next_send_time[category] = now + timedelta(minutes=delay)
                await asyncio.sleep(random.randint(3, 8))

        await asyncio.sleep(10)

def run_flask_server():
    port = int(os.environ.get('PORT', 10002))
    print(f"🌐 [TÚ GRAB] Khởi động máy chủ web trên cổng {port}...")
    app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    print("🚀 [TÚ GRAB] Script bắt đầu thực thi...")

    if not BOT_TOKEN or not CHAT_ID:
        print("❌ [TÚ GRAB] LỖI NGHIÊM TRỌNG: Thiếu BOT_TOKEN hoặc CHAT_ID trong biến môi trường!")
    else:
        print("✅ [TÚ GRAB] Biến môi trường đã được tải.")
        bot_thread = threading.Thread(target=lambda: asyncio.run(bot_main_loop()))
        bot_thread.daemon = True
        bot_thread.start()

    # Chạy Flask trong luồng chính
    run_flask_server()