!pip3 install adafruit.io
from Adafruit_IO import RequestError, Client, Feed
from Adafruit_IO import Data

username = 'Sagar_jairaj'                   
code = 'aio_iimD058JCLdEBS9uqMc3E3Wtazsi'  
aio = Client(username,code)

!pip install python-telegram-bot
from telegram.ext import Updater,CommandHandler
import requests
import time

def on(bot,update):
    chat_id = update.message.chat_id
    txt = 'light is turning on'              #to display the message that light is turning on
    pic = 'https://assets.bose.com/content/dam/Bose_DAM/Web/consumer_electronics/support/articles/speakers/solo_10_series_ii/system_settings/solo_volume_max_green.psd/_jcr_content/renditions/cq5dam.web.320.320.jpeg'       #to display the green indication image
    time.sleep(2)
    bot.send_message(chat_id,txt)
    time.sleep(1)
    bot.send_photo(chat_id,pic)
    value = Data(value=1)
    value_send = aio.create_data('lit',value)  #sending value to a feed with key 'lit' which is already created

def off(bot,update):
    chat_id = update.message.chat_id
    txt = 'light is turning off'              #to display the message that light is turning off
    pic = 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTYcNq48qvRya6UCjHWkjCRQiqoxJRnYUSQ4w&usqp=CAU'     #to display the green indication image 
    time.sleep(2)
    bot.send_message(chat_id,txt)
    time.sleep(1)
    bot.send_photo(chat_id,pic)
    value = Data(value=0)
    value_send = aio.create_data('lit',value)   #sending value to a feed with key 'lit' which is already created

u = Updater('1359440014:AAFjnCIX9k0wpY9_NGGe1c5MDq6l6o4fa54')  
dp = u.dispatcher
dp.add_handler(CommandHandler('on',on))
dp.add_handler(CommandHandler('off',off))
u.start_polling()
u.idle()
