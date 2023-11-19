# [IMPORT]
import telebot
from KEY import API_KEY
from threading import Thread
from telebot import types
from keep_alive import keep_alive
from CoreSystem import UpdataSheet, DeleteSheet, SeeList

# [CODE]
bot = telebot.TeleBot(API_KEY, parse_mode=None)
keep_alive()
print("[SYSTEM] Start Bot")

def CmdSever(msg):
	user = msg.from_user.id
	text = msg.text
	print(f"\nUser: {user}\nChat: {text}")
	
@bot.callback_query_handler(func=lambda callback:True)
def callback_inline(callback):
	bot.delete_message(callback.message.chat.id, callback.message.message_id)
	
@bot.message_handler(commands=['a'])
def Update(msg):
	CmdSever(msg)
	UpdataSheet(msg)
	
@bot.message_handler(commands=['del'])
def Delete(msg):
	CmdSever(msg)
	DeleteSheet(msg)

@bot.message_handler(commands=['list'])
def List(msg):
	CmdSever(msg)
	SeeList(msg)

if (__name__ == "__main__"):
	Thread(target=callback_inline, args=(bot.infinity_polling())).start()