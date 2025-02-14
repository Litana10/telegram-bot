pip install pyTelegramBotAPI
import telebot
TOKEN = "8095260181:AAHztRFzwSOxtGwM4I_jog9YHozHqVk2OuA"
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(func=lambda message: True)
def echo_all(message): 

bot.reply_to(message, f"Ты написал: {message.text}")
bot.polling()
