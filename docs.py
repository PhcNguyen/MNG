import gspread
import datetime
from constants import data

gc = gspread.service_account_from_dict(data)
sh = gc.open_by_key("1TCEXbeUdEsonC62bk9sPj55nemMD_hHN5HN4uzIQCSY")
wks = sh.sheet1
def time_set():
  current_time = datetime.datetime.now()
  formatted_time = current_time.strftime("%H:%M")
  return formatted_time
def date_set():
  current_time = datetime.datetime.now()
  formatted_date = current_time.strftime("%Y-%m-%d ")
  return formatted_date
def list_data():
  list_of_lists = wks.get_all_values()
  return list_of_lists
def UpdateSheet(data):
  data = data.split()
  del data[0]
  list_of_lists = list_data()
  current = len(list_of_lists) + 1
  MC = len(data) - 1
  String = ''
  X = 2
  for X in range(MC):
    String += ' '+ data[X]
  row = wks.cell(current, 1)
  row.value = String
  wks.update_cell(row.row, row.col, row.value)
  row_1 = wks.cell(current, 2)
  row_1.value = data[MC]
  wks.update_cell(row_1.row, row_1.col, row_1.value)
  formatted_date = date_set()
  row_2 = wks.cell(current, 3)
  row_2.value = formatted_date
  wks.update_cell(row_2.row, row_2.col, row_2.value)
def GetData():
  list_of_lists = list_data()
  NameIteam = []
  MoneyIteam = []
  MsgID = []
  MsgID2 = []
  for ID in range(len(list_of_lists)):
    NameIteam.append(list_of_lists[ID][0])
    MoneyIteam.append(list_of_lists[ID][1])
  print(NameIteam)
  for I in range(len(NameIteam)):
    if I == 0:
      continue
    Money = MoneyIteam[I]
    Money = int(Money)
    Msg = f"\n[{I}] Iteam: {NameIteam[I]} \n      Money: {Money:,} VNÐ\n"
    MsgID = ''.join(Msg)
    MsgID2.append(MsgID)
  return MsgID2
def DeleteData(ID):
  
  ID = int(ID) + 1
  wks.delete_row(ID)
  return True
def SumData():
  list_of_lists = list_data()
  Sum = 0
  for ID in range(len(list_of_lists)):
    if (ID == 0):
      continue
    Money = list_of_lists[ID][1]
    Sum += int(Money)
  return Sum