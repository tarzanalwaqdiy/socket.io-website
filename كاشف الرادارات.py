import logging
import requests
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# إعداد تسجيل الأخطاء
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# دالة لبدء البوت
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_location_button = KeyboardButton("موقعي", request_location=True)
    reply_markup = ReplyKeyboardMarkup([[user_location_button]], one_time_keyboard=True)
    await update.message.reply_text('يرجى مشاركة موقعك:', reply_markup=reply_markup)

# دالة للتعامل مع الموقع
async def location(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_location = update.message.location
    location = f"{user_location.latitude},{user_location.longitude}"

    await update.message.reply_text("جاري البحث عن مواقع الرادارات...")

    # يمكنك استبدال هذه القائمة بمواقع الرادارات الفعلية
    radars = [
        (24.7136, 46.6753),  # مثال على إحداثيات الرادار
        (24.7137, 46.6755),  # مثال على إحداثيات الرادار
    ]

    radar_locations = ""
    for lat, lon in radars:
        radar_locations += f"رادار موجود في: خط العرض: {lat}, خط الطول: {lon}\n"

    await update.message.reply_text(radar_locations)

    # إذا كنت تريد تخطيط طريق يمكنك استخدام جوجل مابس
    await update.message.reply_text(f"يمكنك استخدام هذا الرابط لتخطيط الطريق: "
                                     f"https://www.google.com/maps/dir/?api=1&origin={location}&destination={radars[0][0]},{radars[0][1]}")

# إعداد البوت
def main():
    application = ApplicationBuilder().token('8148083182:AAFijSroNpcoWtIRCWvjIlhhy9qzLxH-Nk8').build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.LOCATION, location))

    # بدء البوت
    application.run_polling()

# تنفيذ الكود
if __name__ == '__main__':
    main()