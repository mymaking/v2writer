import os
from pyrogram import Client, idle
from lib.env import tokens, config_tool

bot = Client("writer",
             tokens()[0],
             tokens()[1],
             bot_token=tokens()[2],
             plugins={"root": "plugins"})

bot.start()
os.system('echo V2Writer')
idle()
