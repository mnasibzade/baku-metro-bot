import json
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

# Read JSON
def load_st_data():
    with open("data/stations.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("stations", {})

async def stations(update: Update, context: CallbackContext) -> None:
    if len(context.args) == 0:
        await update.message.reply_text("Stansiya adı daxil edin!\n\nMəsələn: /station 28 May")
        return

    station_name = " ".join(context.args)
    station_data = load_st_data()
    station = station_data.get(station_name)

    if not station:
        await update.message.reply_text("Bu adda stansiya tapılmadı. Zəhmət olmasa düzgün ad daxil edin.")
        return

    message = (
        f"📍 Stansiya: {station['name']}\n"
        f"📅 Açılış tarixi: {station['opened']}\n"
        f"🧭 İstiqamətlər: {', '.join(station['directions'])}\n"
        f"🚇 Xətt: {', '.join(station['lines'])}\n"
        f"🔁 Keçid: {station['transfer'] or 'Yoxdur'}\n"
        f"📌 Yerləşdiyi yer: {station['location']}\n"
        f"🚪 Çıxış sayı: {station['exits']}\n"
        f"⏱️ Interval: {station['interval']}\n"
        f"ℹ️ Haqqında: {station['description']}"
    )

    keyboard = [
        [
            InlineKeyboardButton("📍 Xəritədə bax", url=station["location_url"]),
            InlineKeyboardButton("📢 İnformator", callback_data=f"info_{station['informator_url']}")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(message, parse_mode="Markdown", reply_markup=reply_markup)