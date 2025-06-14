from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "7508326547:AAHq1BCI3UcIYL0kyZbSelPdr5XPxqC-LLo"  # Замените на токен от @BotFather

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    button = InlineKeyboardButton(
        text="🐍 Играть в Змейку",
        web_app={"url": "https://ваш-ник.github.io/snake-game/snake.html"}
    )
    await update.message.reply_text(
        "Нажмите кнопку, чтобы начать игру!",
        reply_markup=InlineKeyboardMarkup([[button]])
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == '__main__':
    main()