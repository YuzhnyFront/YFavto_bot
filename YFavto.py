import telebot

TOKEN = "7784925961:AAFSm8-hQRDSc1qrxpJ3UUGVJS2v4gshCPM"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, "Спасибо. Ваше сообщение получено! Скоро оно появится в ленте канала")
    bot.forward_message(543018537, message.chat.id, message.message_id)

bot.polling()
