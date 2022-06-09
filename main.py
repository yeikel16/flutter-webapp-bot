"""
Basic example for a bot that uses inline keyboards. For an in-depth explanation, check out
 https://github.com/python-telegram-bot/python-telegram-bot/wiki/InlineKeyboard-Example.
"""
import logging
import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackContext, CallbackQueryHandler, CommandHandler

from dotenv import load_dotenv

load_dotenv()

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

link_webapp = 'https://taupe-tulumba-027376.netlify.app/'


async def start(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [
            InlineKeyboardButton("Open WebApp", web_app={'url': link_webapp}),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("WebApp made in Flutter", reply_markup=reply_markup)


async def button(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()

    # keyboard = [
    #     [
    #         InlineKeyboardButton("Flutter", url='https://flutter.dev/')
    #     ], 
    #     [
    #         InlineKeyboardButton("Dart", url='https://dart.dev/')
    #     ]
    # ]

    # reply_markup = InlineKeyboardMarkup(keyboard)

    # await update.message.reply_text("Your favorite color is:", reply_markup=reply_markup)
    await query.edit_message_text(text=f"Your favorite color is: {query.data}")


async def help_command(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    """Displays info on how to use the bot."""
    await update.message.reply_text("Use /start to test this bot.")


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    # application.add_handler(CallbackQueryHandler(button))
    # application.add_handler(CommandHandler("help", help_command))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()
