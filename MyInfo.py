# -*- coding: utf-8 -*-

from telegram.ext import Updater , CommandHandler
import telegram

def myInfo (Update , context ) :

    chat_id = Update.message.chat.id
    name = Update.effective_user.first_name
    id = Update.effective_user.id
    username = Update.effective_user.username

    list_id = open ("id_list.txt" , "a" , encoding = "utf-8")
    list_id.write(str(id) + "\n")
    list_id.close()

#Método send_chat_action
    bot.send_chat_action(chat_id = chat_id , action = "TYPING" )

    Update.message.reply_text("Nombre: " + name + "\nID: " + str(id) + "\nUsername: @" + username )

def start(Update , context) :

    chat_id = Update.message.chat.id

    name = Update.effective_user.first_name

#Método send_chat_action
    bot.send_chat_action(chat_id = chat_id , action = "TYPING" )
    
    
    Update.message.reply_text("_Hola " + name +    " , yo soy un Bot_" , "markdown" , reply_markup = telegram.InlineKeyboardMarkup ([[ telegram.InlineKeyboardButton(text = "Mi Creador" , url = "https://t.me/Ragnar_l14")] , [ telegram.InlineKeyboardButton (text ="📚Doc. Libreria" , url="https://python-telegram-bot.readthedocs.io/en/stable/index.html ")]]))




if __name__ == '__main__':

	bot = telegram.Bot(token= "1693944849:AAFNL00kv8rA4mYvZZ_jlCEWo-ruahyQEsY")
	updater = Updater(token= "1693944849:AAFNL00kv8rA4mYvZZ_jlCEWo-ruahyQEsY" ,  use_context=True)

	update = Updater
	dp = updater.dispatcher

	dp.add_handler(CommandHandler('start', start))
	dp.add_handler(CommandHandler("myInfo" , myInfo))

	updater.start_polling()
	print("Esta Corriendo")
	updater.idle()
