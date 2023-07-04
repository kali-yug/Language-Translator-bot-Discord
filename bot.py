import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from lingua import Language, LanguageDetectorBuilder
import config
# import translators as ts
from deep_translator import (GoogleTranslator, single_detection)

load_dotenv()

# bot = commands.Bot(command_prefix="$")

intents = discord.Intents.all()
intents.message_content = True

client = discord.Client(intents=intents)
token = config.params['TOKEN']

langs = [Language.ENGLISH, Language.HINDI, Language.RUSSIAN, Language.FRENCH, Language.SPANISH, Language.GERMAN]
detector = LanguageDetectorBuilder.from_languages(*langs).build()



@client.event
async def on_ready():
    print('Online')

@client.event
async def on_message(message):
    user_message = str(message.content)

    if message.author == client.user:
        return

    # user_lang = detector.detect_language_of(user_message)
    # print(user_lang)
    
    lang = single_detection(user_message, api_key='7135c93b9322b1acc1c75d5e366b7c1b')
    print(lang)

    if lang != "en":
        # detected_language = detector.detect(user_message)
        # translation = ts.translate_text(user_message)
        translated = GoogleTranslator(source='auto', target='en').translate(text=user_message)
        await message.channel.send(translated)
        print(translated)
client.run(token)
DISCORD_TOKEN = config.params['TOKEN']