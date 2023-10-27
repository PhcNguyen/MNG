import telebot
from keep_alive import keep_alive
from time import sleep
from docs import UpdateSheet, GetData, DeleteData, SumData

keep_alive()
#keep_alive để bot 24/24 khi bạn sài replit
API_KEY = "key bot telegram cua ban"
bot = telebot.TeleBot(API_KEY, parse_mode=None)
@bot.message_handler(commands=['help'])
def start(msg):
  bot.send_message(msg.chat.id, '/s - Thêm Dữ Liệu.\n/g - Hiển Thị Dữ Liệu.\n/sum - Tính Tổng Dữ Liệu.')
  
@bot.message_handler(commands=["s"])
def update(msg):
  msgChat = "Bạn đã nhập sai Cú Pháp !\n  /s <Tên> <Giá>"
  data = msg.text
  CompareData = msg.text
  CompareData = CompareData.split()
  MC = len(CompareData) - 1
  try:
    Money = int(CompareData[MC])
    print(Money)
    text=bot.send_message(msg.chat.id, ".")
    bot.edit_message_text("..", chat_id=msg.chat.id, message_id=text.message_id)
    bot.edit_message_text("...", chat_id=msg.chat.id, message_id=text.message_id)
    UpdateSheet(data)
    bot.edit_message_text("Done !", chat_id=msg.chat.id, message_id=text.message_id)
  except:
    id=bot.send_message(msg.chat.id, msgChat)
    sleep(5)
    bot.delete_message(msg.chat.id, id.message_id)
    
@bot.message_handler(commands=["g"])
def getData(msg):
  MsgID2 = GetData()
  print(MsgID2)
  for I in range(len(MsgID2)):
    bot.send_message(msg.chat.id, MsgID2[I])
@bot.message_handler(commands=["sum"])
def SumMoney(msg):
  Sum = SumData()
  bot.send_message(msg.chat.id, f"Tồng: {Sum:,} !")
@bot.message_handler(commands=["delete"])
def Delete(msg):
  data = msg.text
  data = data.split()
  try:
    ID=bot.send_message(msg.chat.id, "...")
    DeleteData(data[-1])
    bot.edit_message_text("Done !", chat_id=msg.chat.id, message_id=ID.message_id)
  except:
    bot.send_message(msg.chat.id, "Bạn đã nhập sai Cú Pháp!\n/delete <ID>")
    
bot.polling()