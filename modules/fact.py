import json
import random
from telegram import Update
from telegram.ext import CallbackContext

def random_fact():
    with open("data/facts.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return random.choice(data["facts"])

async def fact(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(f"***Random bir fakt:***\n\n{random_fact()}", parse_mode="Markdown")

