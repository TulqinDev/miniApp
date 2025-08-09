import os
from typing import TYPE_CHECKING

from telegram import (
    InlineKeyboardButton,
    WebAppInfo,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    filters,
)

from data.customer.models import Customer

if TYPE_CHECKING:
    from data.bot.models import BotUser
    from data.user.models import User

NAME, CONTACT = range(2)


class Bot:
    USER_MINI_APP_URL = "https://youtu.be/user_link"
    CUSTOMER_MINI_APP_URL = "https://youtu.be/customer_link"

    def __init__(self):
        TOKEN = os.environ.get("TOKEN")
        self.app = ApplicationBuilder().token(TOKEN).build()

        conv_handler = ConversationHandler(
            entry_points=[CommandHandler("start", self.start)],
            states={
                NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, self.get_name)],
                CONTACT: [
                    MessageHandler(filters.CONTACT, self.get_contact),
                    MessageHandler(filters.TEXT & ~filters.COMMAND, self.ask_contact_again),
                ],
            },
            fallbacks=[CommandHandler("cancel", self.cancel)],
        )

        self.app.add_handler(conv_handler)

    def run(self):
        self.app.run_polling()

    async def send_mini_app_button(self, update, user_type="customer"):

        """Mini app tugmasini yuborish. user_type = 'user' yoki 'customer'"""

        if user_type == "user":
            url = self.USER_MINI_APP_URL
        else:
            url = self.CUSTOMER_MINI_APP_URL

        button = [[InlineKeyboardButton(text="Dasturga kirish", web_app=WebAppInfo(url=url))]]
        reply_markup = InlineKeyboardMarkup(button)
        await update.message.reply_text("Dasturga kirish uchun pastdagi tugmani bosing!", reply_markup=reply_markup)

    def link_bot_user(self, chat_id, tg_name, username, user_obj=None, customer_obj=None):

        """BotUser obyektini yaratish yoki bog‘lash."""

        from data.bot.models import BotUser
        defaults = {"tg_name": tg_name, "username": username}
        if user_obj:
            defaults["user"] = user_obj
        if customer_obj:
            defaults["customer"] = customer_obj
        BotUser.objects.get_or_create(chat_id=chat_id, defaults=defaults)

    async def start(self, update, context):
        from data.bot.models import BotUser

        user = update.effective_user
        bot_user = BotUser.objects.filter(chat_id=user.id).first()

        if bot_user:
            if bot_user.user:
                await self.send_mini_app_button(update, user_type="user")
            elif bot_user.customer:
                await self.send_mini_app_button(update, user_type="customer")
            return ConversationHandler.END  # Ro‘yxatdan o‘tgan bo‘lsa, to‘xtatamiz

        await update.message.reply_text("Ism sharifingizni kiriting:")
        return NAME

    async def get_name(self, update, context):
        context.user_data["name"] = update.message.text
        button = [[KeyboardButton(text="📱 Kontakt yuborish", request_contact=True)]]
        reply_markup = ReplyKeyboardMarkup(button, resize_keyboard=True)
        await update.message.reply_text("Pastdagi tugma orqali telefon raqamingizni yuboring!",
                                        reply_markup=reply_markup)
        return CONTACT

    async def ask_contact_again(self, update, context):
        await update.message.reply_text("❗ Iltimos, tugma orqali telefon raqamingizni yuboring.")
        return CONTACT

    async def get_contact(self, update, context):
        from data.user.models import User

        user = update.effective_user
        phone_number = update.message.contact.phone_number.lstrip("+")
        name = context.user_data.get("name")

        # Avval User tekshiramiz
        user_obj = User.objects.filter(phone_number=phone_number).first()
        if user_obj:
            self.link_bot_user(user.id, user.full_name, user.username, user_obj=user_obj)
            await self.send_mini_app_button(update, user_type="user")
            return ConversationHandler.END

        # Agar User bo‘lmasa, Customer yaratamiz
        customer_obj, _ = Customer.objects.get_or_create(name=name, phone_number=phone_number)
        self.link_bot_user(user.id, user.full_name, user.username, customer_obj=customer_obj)
        await self.send_mini_app_button(update, user_type="customer")
        return ConversationHandler.END

    async def cancel(self, update, context):
        await update.message.reply_text("❌ Ro‘yxatdan o‘tish bekor qilindi.")
        return ConversationHandler.END
