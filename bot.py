import telebot
from telebot import types
import os

TOKEN = os.getenv("TOKEN")
if not TOKEN:
    TOKEN = "8320654489:AAFNgRdPMRlaclabDNm7bqRsFvVMJcpkHq8"

bot = telebot.TeleBot(TOKEN)

# ================== كل المباني من الـ Excel الجديد (version 3) ==================
BUILDINGS = {
    "PS.28": {
        "معماري": "https://drive.google.com/drive/u/0/folders/1aVGq1TIlw8WAtmFtX9pULo_b4WrvOhVI",
        "إنشائي": "https://drive.google.com/drive/u/0/folders/1JqG-YZJlNeB9w-Wt7LiqV5PSh5zXmHxR"
    },
    "PS.29": {
        "معماري": "https://drive.google.com/drive/u/0/folders/1T5uG1QXoCJW61U5zMbfp2NL9BVPozaGt",
        "إنشائي": "https://drive.google.com/drive/u/0/folders/1K377AX5ykH-zJTkDAW6bIsdPMNN57zFW"
    },
    "PS.31": {
        "معماري": "https://drive.google.com/drive/u/0/folders/1Oad9src7ALeZQPSrQf93VTKlgAfXT1Jf",
        "إنشائي": "https://drive.google.com/drive/u/0/folders/1NJFUX7nvdltmekXFUkrhIGBk9R-nHCsn"
    },
    "PS.32": {
        "معماري": "https://drive.google.com/drive/u/0/folders/18X9Wv7g1KxYdCwjfWLREDefMrsBm_DXk",
        "إنشائي": "https://drive.google.com/drive/u/0/folders/12dndrWg2MGZ-CXq4ZGCWXngBoVZhgfb5"
    },
    "PS.62": {
        "معماري": "https://drive.google.com/drive/u/0/folders/1zn6mnWDHmpMR9jCn4ZIUUoWWUJqrIgZn",
        "إنشائي": "https://drive.google.com/drive/u/0/folders/1wv6sBCXQynO2fV_0lMZXMhSTaNbCssJc"
    },
    "PS.69": {
        "معماري": "https://drive.google.com/drive/u/0/folders/1mxWT75bzXTj0eejLAEYNnhOBTQwj_SU0",
        "إنشائي": "https://drive.google.com/drive/u/0/folders/1Xis7X5Peitbp53iR8Upzy5afUcFpPSh5"
    },
    "PS.29 Interlock": {
        "معماري": "https://drive.google.com/drive/u/0/folders/1eqjo8vrnGyVwZWVPaKkTrMi1fqw9Df-p",
        "إنشائي": "لا يوجد انشائي"
    },
    "PS.31-32-69-62 Interlock": {
        "معماري": "https://drive.google.com/drive/u/0/folders/1aa8IM5SrUVEPNp_VjmwhRxs7O4Yv99Lh",
        "إنشائي": "لا يوجد انشائي"
    },
    "Admin": {
        "معماري": "https://drive.google.com/drive/u/0/folders/1OPcdo_omU3GHkm73IXo0wFaigl2FxOAU",
        "إنشائي": "https://drive.google.com/drive/u/0/folders/1NFpnP9ldMa8vfoY1Fnh4pMSenvUw0SHj"
    },
    "Farmer Traditional": {
        "معماري": "https://drive.google.com/drive/u/0/folders/1i-9sDaLfK5Jvp9LULlUgrgczisFgs_7e",
        "إنشائي": "https://drive.google.com/drive/u/0/folders/1d20105FgUF6cfgnd0tjqUaaeQ8Tmvjgi"
    },
    "Farmer precast": {
        "معماري": "https://drive.google.com/drive/u/0/folders/1WAQvTZ1hybUOPsiTeabr_TsRy5-CWsuH",
        "إنشائي": "https://drive.google.com/drive/u/0/folders/1NgYiP8w8NtEoH2TgD-oYUWiGVa90LVGy"
    },
    "Distributer": {
        "معماري": "https://drive.google.com/drive/u/0/folders/1npIf_uAfDmbUq4emLJp92qKnk-WatvW-",
        "إنشائي": "https://drive.google.com/drive/u/0/folders/16u7qxcyU50fTriPoyPKiI3T_v9y9Pi_n"
    },
    "Substation": {
        "معماري": "https://drive.google.com/drive/u/0/folders/1WufXTr5Psade3sHjQN-c2qZA9E5k6ewr",
        "إنشائي": "https://drive.google.com/drive/u/0/folders/1deF_wf-vzNCXJvyask_xpDSVeBBzwV38"
    },
    "Fire Tank": {
        "معماري": "لا يوجد معماري",
        "إنشائي": "https://drive.google.com/drive/u/0/folders/1LX9KiWZi9AhZxNxCVTdKJbtqsACGIPSJ"
    },
    "Septic Tank": {
        "معماري": "لا يوجد معماري",
        "إنشائي": "https://drive.google.com/drive/u/0/folders/1pb_3Ov4EMuZiYDHsZA9A6LV8c7BxqyBa"
    },
    "غرفة Bypass رقم 1": {
        "معماري": "لا يوجد معماري",
        "إنشائي": "https://drive.google.com/drive/u/0/folders/1X6a476n6SAYsTQZOJPAlyAEm4PvY9_VL"
    },
    "غرفة Bypass رقم 2": {
        "معماري": "لا يوجد معماري",
        "إنشائي": "https://drive.google.com/drive/u/0/folders/1WAsP4BVGqgLV2HOHfV944us_acmzXPPB"
    },
    "Thru.Wall": {
        "معماري": "لا يوجد معماري",
        "إنشائي": "https://drive.google.com/drive/u/0/folders/1KiQVKiZ1-PZisLLehH8vlJCy58mbo5cq"
    },
    "Thru.Block": {
        "معماري": "لا يوجد معماري",
        "إنشائي": "https://drive.google.com/drive/u/0/folders/1fRpU62Qf5d7YWbAWxj55Hl2SQf_2Xoyi"
    },
    "Off-take Thru.Block": {
        "معماري": "لا يوجد معماري",
        "إنشائي": "https://drive.google.com/drive/u/0/folders/1_R3bAwZuadWJ1J50yrrlyfKUGVbOMfAg"
    },
    "Off-take Valve Pads": {
        "معماري": "لا يوجد معماري",
        "إنشائي": "https://drive.google.com/drive/u/0/folders/1ZdkCEvkgmZTf-EVA5NV4HmVE3d17Nyc-"
    },
    "Thru.Block -(S)": {
        "معماري": "لا يوجد معماري",
        "إنشائي": "https://drive.google.com/drive/u/0/folders/1JlVQwB2Icwb4rJG7zd9ugnI7arjlxjjR"
    },
    "بادات التنصيص والمناورة": {
        "معماري": "لا يوجد معماري",
        "إنشائي": "https://drive.google.com/drive/u/0/folders/1G_zS2FgRWfIrliz9c93K7JnAyvm-0s-Z"
    },
    "Electrical Manhole": {
        "معماري": "لا يوجد معماري",
        "إنشائي": "https://drive.google.com/drive/u/0/folders/1852XDFvWfR1JStKfDDJpB40a0ST5nfFc"
    },
    "Steel Doors -PS": {
        "معماري": "لا يوجد معماري",
        "إنشائي": "https://drive.google.com/drive/u/0/folders/1OYnaGDYD86ogQTUjRz8k0OfH2t5G6Vf5"
    },
    "Steel Doors -Distr": {
        "معماري": "لا يوجد معماري",
        "إنشائي": "https://drive.google.com/drive/u/0/folders/1qs0bJG9O-z-nG3sQ7QwhXKH8e_pVQ8ON"
    },
    "B.Steel Doors -Dis": {
        "معماري": "لا يوجد معماري",
        "إنشائي": "https://drive.google.com/drive/u/0/folders/1qxay63Aqa7d9rIeVFHd5hkfMJWhwS7fe"
    },
    "مظلة خزان الحريق": {
        "معماري": "لا يوجد معماري",
        "إنشائي": "https://drive.google.com/drive/u/0/folders/1n5NnA9aIhsB9SoY835wh0zE85rcIG15W"
    }
}

# متغير لحفظ آخر رسالة لكل مستخدم (عشان نعدلها في مكانها)
user_messages = {}

def edit_or_send_message(chat_id, text, markup=None):
    """دالة ذكية: تعدل الرسالة لو موجودة أو ترسل واحدة جديدة"""
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
    except Exception:
        # لو حصل أي خطأ، نرسل رسالة جديدة
        msg = bot.send_message(chat_id=chat_id, text=text, reply_markup=markup, parse_mode="Markdown")
        user_messages[chat_id] = msg.message_id

def show_buildings(chat_id):
    keyboard = []
    row = []
    for building in BUILDINGS.keys():
        row.append(types.InlineKeyboardButton(text=building, callback_data=f"b:{building}"))
        if len(row) == 2:
            keyboard.append(row)
            row = []
    if row:
        keyboard.append(row)
    keyboard.append([types.InlineKeyboardButton(text="🔄 تحديث", callback_data="refresh")])
    markup = types.InlineKeyboardMarkup(keyboard)
    edit_or_send_message(chat_id, "🏗️ **اختر المبنى:**", markup)

def show_types(chat_id, building):
    data = BUILDINGS.get(building, {})
    keyboard = []
    
    # عرض زرار معماري فقط لو فيه رابط حقيقي
    if data.get("معماري") and data["معماري"] and "لا يوجد" not in data["معماري"].lower():
        keyboard.append([types.InlineKeyboardButton(text="📐 لوحات معمارية", url=data["معماري"])])
    
    # عرض زرار إنشائي فقط لو فيه رابط حقيقي
    if data.get("إنشائي") and data["إنشائي"] and "لا يوجد" not in data["إنشائي"].lower():
        keyboard.append([types.InlineKeyboardButton(text="🏗️ لوحات إنشائية", url=data["إنشائي"])])
    
    keyboard.append([types.InlineKeyboardButton(text="🔙 رجوع", callback_data="back")])
    markup = types.InlineKeyboardMarkup(keyboard)
    
    text = f"📁 **{building}**\nاختر نوع اللوحات:"
    
    # لو مفيش أي لوحات
    if len(keyboard) <= 1:
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
