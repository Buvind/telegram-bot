import os
import telebot

bot = telebot.TeleBot("5118421027:AAE-6sbVuM4HVdGLzLRHKRemZuRv86O_Rxg")

@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message,"Hey I am arman.my creater D.A.B.N.G.")
  
@bot.message_handler(commands=["GroupHp"])
def send_message(message):
  bot.send_message(message,"Please add me in your group.😊")
  
bot.polling()