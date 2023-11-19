# [IMPORT]
import gspread
import telebot
from KEY import API_KEY, DATA, OPEN_KEY
from threading import Thread
from telebot import types
from time import sleep
from datetime import datetime

# [OPEN SHEET]
gc = gspread.service_account_from_dict(DATA)
sh = gc.open_by_key(OPEN_KEY)
wks = sh.sheet1
crossbar = '_______________'

# [API TELEGRAM]
bot = telebot.TeleBot(API_KEY, parse_mode=None)

# [CODE]
def Delete(msg):
	chat_id = msg.chat.id
	message_id = msg.message_id
	bot.delete_message(chat_id=chat_id, message_id=message_id)
	return 0
	
def SendDel(msg):
	user = msg.from_user.id
	chat_id_to_send = str(user)
	message_to_send = f"{crossbar}\nHoàn Thành !"
	delay_seconds = 10
	sent_message = bot.send_message(chat_id_to_send, message_to_send)
	sleep(delay_seconds)
	bot.delete_message(chat_id_to_send, sent_message.message_id)
	return 0
	
def Error(msg):
	now = datetime.now()
	user = msg.from_user.id
	chat_id_to_send = f'{user}'
	message_to_send = f"{crossbar}\nERROR!"
	delay_seconds = 10
	sent_message = bot.send_message(chat_id_to_send, message_to_send)
	sleep(delay_seconds)
	bot.delete_message(chat_id_to_send, sent_message.message_id)
	return 0
	
def Send(msg, text):
	markup = types.InlineKeyboardMarkup()
	box = types.InlineKeyboardButton(text="Delete", callback_data="1")
	markup.row(box)
	bot.send_message(msg.chat.id, text, reply_markup=markup)
	return 0
	
def ListSheet():
	list_lists = wks.get_all_values()
	del list_lists[0]
	return list_lists
	
def UpdataSheet(msg):
	def Data(text, coin):
		list_lists = ListSheet()
		current = len(list_lists) + 2
		wks.update_cell(current, 1, text)
		wks.update_cell(current, 2, coin)
		return 0
		
	def Main(msg):
		text = msg.text.split()
		coin = text[-1]
		del text[0]
		del text[-1]
		text = " ".join(text)
		Delete(msg)
		
		threads = [
		Thread(target=Data, args=(text, coin)),
		Thread(target=SendDel, args=(msg,))
		]
		
		[thread.start() for thread in threads]
		
	Main(msg)
	
def DeleteSheet(msg):
	try:
		Delete(msg)
		ID = int(msg.text.split()[-1]) + 1
		wks.delete_row(ID)
		SendDel(msg)
	except:
		Error(msg)
		
def SeeList(msg):
	list_lists = ListSheet()
	Delete(msg)
	if len(list_lists) == 0:
		Error(msg)
		return 0
	MSG = []
	for ID, (iteam, coin) in enumerate(list_lists, start=1):
		coin = int(coin)
		formatted_coin = f"{coin:,}" if coin >= 1000 else str(coin)
		text = f"{ID}: {iteam} {formatted_coin}\n"
		MSG.append(text)
	MSG = ''.join(MSG)
	Send(msg, MSG)