from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Define multiple buttons
    keyboard = [
        [InlineKeyboardButton("👉 Start Swiping", url="https://trade.griffy.app")],
        [InlineKeyboardButton("🫂 Refer a Friend",callback_data="refer_friend")],
        [InlineKeyboardButton("🐦 Follow us on X",url="https://x.com/GriffyCommunity")],
        [InlineKeyboardButton("🤳 Join Telegram Community",url="https://t.me/griffycommunity")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send the message with the buttons
    await update.message.reply_text(
        f"Welcome to GriffyBot! \n\n"
        f"Predict crypto prices with a swipe. Think Tinder, but for trading.🚀🎉",
        reply_markup=reply_markup
    )
    
async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # Acknowledge the button press

    if query.data == "refer_friend":
        # Generate or provide the referral code
            referral_code = "IBWBLR"
    await query.message.reply_text(
            f"🥳Copy the text ,`{referral_code}` share it with your friends \n\n"
            f"and watch your rewards EXPLODE!🚀",
            parse_mode="Markdown"
        )    

def main():
    # Replace with your bot token
    TOKEN = "7574414681:AAGxV0wWdeYOxQlZptsRfu8QBfPxSOPiKkE"


    # Create the application
    application = Application.builder().token(TOKEN).build()

    # Add the command and callback handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_callback))

    # Run the bot
    application.run_polling()


if __name__ == "__main__":
    main()
