from flask import Flask
from threading import Thread

# Mọi người xoá file này nếu sài vps nha
# Này mình làm cho replit
app = Flask(__name__)
@app.route('/')
def index():
  return "I am alive!"
  
def run():
  app.run(host='0.0.0.0', port=8080)
  
def keep_alive():
  t = Thread(target = run)
  t.start()