import json
import os, sys
import random
from discord.ext import commands

if not os.path.isfile('config.json'):
    with open('config.json', "w") as conf_file:
        data = {}
        data['Key'] = 'KeyHere'
        data['Prefix'] = '>'
        
        json.dump(data, conf_file, indent=2)
        print('New Config Made, go change settings and return.')
        sys.exit()
    
global key
global prefix
with open('config.json') as conf_file:
    data = json.load(conf_file)
    key = data['Key']
    prefix = data['Prefix']

bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print("Ready with {}".format(bot.user))

bot.run(key)