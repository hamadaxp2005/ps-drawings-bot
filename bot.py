import time
import telebot
from telebot import types
from keep_alive import keep_alive

keep_alive()

TOKEN = "8320654489:AAFNgRdPMRlaclabDNm7bqRsFvVMJcpkHq8"
bot = telebot.TeleBot(TOKEN)

# ================== كل المباني (النسخة المحدثة) ==================
BUILDINGS = {
    "PS.28": {
        "معماري": "https://drive.google.com/drive/u/0/folders/1Ti4CUiut8geB7J5A3vmK1TU8ha8JRMMQ",
        "إنشائي": "https://drive.google.com/drive/u/0/folders/1tUaMeaudHYu9EiiIWxbH3FvH5N3QzNtX"
    },
    "PS.29": {
        "معماري": "https://drive.google.com/drive/folders/1nIDNYcMgAgA5_JBNTn3vAWYk_c5y-cUM",
        "إنشائي": "https://drive.google.com/drive/folders/15lA77eQB523MfVIif07Lfi9Jzruau_tP?usp=drive"
    },
    "PS.31": {
        "معماري": "https://drive.google.com/drive/folders/1JXay96a02F_RLod7gynkd4quhCMcH9OA?usp=drive",
        "إنشائي": "https://drive.google.com/drive/folders/1dYsPGO8ZhMagA6plGLBl5hdbXOXe7wK_?usp=drive"
    },
    "PS.32": {
        "معماري": "https://drive.google.com/drive/folders/18Zr9aR6vqsFMiCQcYD9ciCMwWLWb5qXH?usp=drive",
        "إنشائي": "https://drive.google.com/drive/folders/1lPGJeqPI_XZziEFmxVhYsnNjaYMb6niT"
    },
    "PS.62": {
        "معماري": "https://drive.google.com/drive/u/0/folders/1oMx4AQnRF6MT9MRr_B2oUsTSDXL6h-Yc",
        "إنشائي": "https://drive.google.com/drive/u/0/folders/1wkoDRIVlfsm8fSaY8BDMJ0azLomeXCEK"
    },
    "PS.69": {
        "معماري": "https://drive.google.com/drive/u/0/folders/1IS4k7a6FvV3fYZ-LgL5Q-LzGDdKgD0mi",
        "إنشائي": "https://drive.google.com/drive/u/0/folders/1ilQCTQ-mroSS51BG2TVyNyN--hyAZFDH"
    },
    "Admin": {
        "معماري": "https://drive.google.com/drive/u/0/folders/1pRrUjKQDQO1IdVutLAQPOVyeBfG-gVJs",
        "إنشائي": "https://drive.google.com/drive/u/0/folders/1jFubc7QYjYGCFtg7IR862T4XfxD3aH86"
    },
    "Distributer": {
        "معماري": "https://drive.google.com/drive/u/0/folders/1X67-YS-ak9mEfq3bfLKckwtjEM5KZjnt",
        "إنشائي": "https://drive.google.com/drive/u/0/folders/1jOSa1EIPr6RK5cRTikG819LGN6tU7tgQ"
    },
    "Substation": {
        "معماري": "https://drive.google.com/drive/folders/1rN-2yYYjw5RVMajXKQPpuRR6m15H30WP",
        "إنشائي": "https://drive.google.com/drive/folders/14hKytYP0A9BqmYmZClK7u-QNCcHluSLk"
    },
    "Fire Tank": {
        "معماري": "لا يوجد معماري",
        "إنشائي": "https://drive.google.com/drive/u/0/folders/1_mzDHMxNBKUlo22L20XRWYhs8TfYTUsd"
    },
    "Septic Tank": {
        "معماري": "لا يوجد معماري",
        "إنشائي": "https://drive.google.com/drive/u/0/folders/1dUcmhlPMARuJdvU1WK6zh1iWQzskgQ_y"
    },
    "غرفة Bypass رقم 1": {
        "معماري": "لا يوجد معماري",
        "إنشائي": "https://drive.google.com/drive/folders/1lZEm9KowJDFX0KPWp4oXDb24-023g22D?usp=drive"
    },
    "غرفة Bypass رقم 2": {
        "معماري": "لا يوجد معماري",
        "إنشائي": "https://drive.google.com/drive/folders/1vJLJwhF54ZnxzrvVtwqWgDzpT4mBdaO_?usp=drive"
    },
    "Thru.Wall": {
        "معماري": "لا يوجد معماري",
        "إنشائي": "https://drive.google.com/drive/folders/1vLGUCWzaehlN8z9ACq8aiNECrX1St27v"
    },
    "Thru.Block": {
        "معماري": "لا يوجد معماري",
        "إنشائي": "https://drive.google.com/drive/u/0/folders/1N5_MmHR1p9ao3Vy-M1GL6jqG4KnrEZ1Y"
    },
    "Off-take Thru.Block": {
        "معماري": "لا يوجد معماري",
        "إنشائي": "https://drive.google.com/drive/folders/1Gw2GIOafhozlcSsTVOJEVnwYNzgblV_8"
    },
    "Off-take Valve Pads": {
        "معماري": "لا يوجد معماري",
        "إنشائي": "https://drive.google.com/drive/u/0/folders/1sS_pgudRjWo-3RaXoFRQVZ2i8J5rsIiF"
    },
    "Thru.Block -(S)": {
        "معماري": "لا يوجد معماري",
        "إنشائي": "https://drive.google.com/drive/u/0/folders/1oU09YfxIvptFleOKxc3vHChj960pJice"
    },
    "بادات التنصيص والمناورة": {
        "معماري": "لا يوجد معماري",
        "إنشائي": "https://drive.google.com/drive/folders/1xf26Rxompb01SrfWaYbsbihMuYJLwQ7U"
    },
    "Electrical Manhole": {
        "معماري": "لا يوجد معماري",
        "إنشائي": "https://drive.google.com/drive/folders/1eqKFwzJRbiHXLhdbAs5dJrI2GW_9mzjA?usp=drive"
    },
    "Steel Doors -PS": {
        "معماري": "لا يوجد معماري",
        "إنشائي": "https://drive.google.com/drive/u/0/folders/1jktwC8G6o3x30MdkwnMmlpZ-0B6TfQFN"
    },
    "Steel Doors -Distr": {
        "معماري": "لا يوجد معماري",
        "إنشائي": "https://drive.google.com/drive/u/0/folders/1sj3kraV97QWT-Fna7_KxhKKdlF8nTs_i"
    },
    "B.Steel Doors -Dis": {
        "معماري": "لا يوجد معماري",
        "إنشائي": "https://drive.google.com/drive/u/0/folders/1rN4uUqgap4Aqw5exZc2ekOJTjZxsSUgc"
    },
}

# متغير عشان نحفظ آخر رسالة لكل يوزر
user_messages = {}

def edit_or_send_message(chat_id, text, markup=None):
    """دالة ذكية: تعدل الرسالة لو موجودة، أو تبعت واحدة جديدة"""
    try:
        if chat_id in user_messages:
            bot.edit_message_text(
                chat_id=chat_id,
                message_id=user_messages[chat_id],
                text=text,
                reply_markup=markup,
                parse_mode="Markdown"
            )
        else:
            msg = bot.send_message(
                chat_id=chat_id,
                text=text,
                reply_markup=markup,
                parse_mode="Markdown"
            )
            user_messages[chat_id] = msg.message_id
    except:
        msg = bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode="Markdown")
        user_messages[chat_id] = msg.message_id

def show_buildings(chat_id):
    keyboard = []
    row = []
    for building in BUILDINGS.keys():
        row.append(
            types.InlineKeyboardButton(text=building, callback_data=f"b:{building}")
        )
        if len(row) == 2:
            keyboard.append(row)
            row = []
    if row:
        keyboard.append(row)
    keyboard.append(
        [types.InlineKeyboardButton(text="🔄 تحديث", callback_data="refresh")]
    )
    markup = types.InlineKeyboardMarkup(keyboard)
    edit_or_send_message(chat_id, "🏗️ **اختر المبنى:**", markup)

def show_types(chat_id, building):
    data = BUILDINGS.get(building, {})
    keyboard = []

    if data.get("معماري") and data["معماري"] and "لا يوجد معماري" not in data["معماري"]:
        keyboard.append(
            [types.InlineKeyboardButton(text="📐 لوحات معمارية", url=data["معماري"])]
        )

    if data.get("إنشائي") and data["إنشائي"] and "لا يوجد معماري" not in data["إنشائي"]:
        keyboard.append(
            [types.InlineKeyboardButton(text="🏗️ لوحات إنشائية", url=data["إنشائي"])]
        )

    keyboard.append([types.InlineKeyboardButton(text="🔙 رجوع", callback_data="back")])
    markup = types.InlineKeyboardMarkup(keyboard)

    text = f"📁 **{building}**\nاختر نوع اللوحات:"

    if not any(
        data.get(k) and "لا يوجد" not in str(data.get(k)) 
        for k in ["معماري", "إنشائي"]
    ):
        text = f"⚠️ **لسه مفيش لوحات مسجلة لـ {building}**"

    edit_or_send_message(chat_id, text, markup)

@bot.message_handler(commands=["start", "menu"])
def start(message):
    show_buildings(message.chat.id)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    bot.answer_callback_query(call.id)
    if call.data == "back" or call.data == "refresh":
        show_buildings(call.message.chat.id)
    elif call.data.startswith("b:"):
        building = call.data[2:]
        show_types(call.message.chat.id, building)

print("✅ البوت شغال بنجاح!")
bot.infinity_polling()