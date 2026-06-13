from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

PRICE_PER_GB = 10000

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 به ربات خرید VPN خوش آمدید\n\n"
        "💰 قیمت هر گیگ: 10,000 تومان\n"
        "📦 حداقل خرید: 10 گیگ\n\n"
        "🔢 لطفاً حجم مورد نظر خود را وارد کنید:"
    )

async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text.isdigit():
        gb = int(text)

        if gb < 10:
            await update.message.reply_text(
                "❌ حداقل خرید 10 گیگ می‌باشد."
            )
            return

        price = gb * PRICE_PER_GB

        await update.message.reply_text(
            f"📦 حجم انتخابی: {gb} گیگ\n"
            f"💵 مبلغ قابل پرداخت: {price:,} تومان\n\n"
            "🏦 بانک‌نو\n"
            "5859471024750675\n\n"
            "🏦 بانک شهر\n"
            "5047061661170361\n\n"
            "🏦 بانک پاسارگاد\n"
            "5022291618890436\n\n"
            "📸 پس از پرداخت، عکس رسید را ارسال کنید."
        )
    else:
        await update.message.reply_text(
            "⚠️ لطفاً فقط عدد وارد کنید."
        )

async def photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ رسید شما با موفقیت ثبت شد.\n\n"
        "⏳ رسید شما توسط ادمین بررسی می‌شود.\n\n"
        "🔐 پس از تأیید، کانفیگ برای شما ارسال خواهد شد.\n\n"
        "👤 پشتیبانی: @soli_9491"
    )

TOKEN = "8832044335:AAF7DQ935xg2yJUTknCt8xMVKF7aLl_FxrY"

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message))
app.add_handler(MessageHandler(filters.PHOTO, photo))

print("Bot Started...")
app.run_polling()
