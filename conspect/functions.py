
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я бот, который будет поздравлять участников группы с днем рождения.')

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Отправь мне дату рождения, и я буду поздравлять тебя каждый год!')

def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def main():
    updater = Updater("YOUR_TOKEN", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()