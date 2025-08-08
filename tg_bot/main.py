import os

from telegram.ext import ApplicationBuilder, MessageHandler, filters


class Bot:

    def __init__(self):
        TOKEN = os.environ.get("TOKEN")
        self.app = ApplicationBuilder().token(TOKEN).build()
        self.app.add_handler(MessageHandler(filters.TEXT, self.start))

    def run(self):
        self.app.run_polling()

    async def start(self, update, context):
        user = update.effective_user
        text = f"Salom {user.full_name}"
        await update.message.reply_text(text=text)
