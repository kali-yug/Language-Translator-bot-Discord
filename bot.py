import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from lingua import Language, LanguageDetectorBuilder
import config
import translators as ts

load_dotenv()


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

    user_lang = detector.detect_language_of(user_message)
    print(user_lang)

    if user_lang != Language.ENGLISH:
        translation = ts.translate_text(user_message)
        await message.channel.send(translation)
        print(translation)
client.run(token)
DISCORD_TOKEN = config.params['TOKEN']
