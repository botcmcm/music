
import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint


@app.on_message(
    command(["سورس","سورس ليون","السورس"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/95f9a021664ed46050d63.jpg",
        caption=f"• 𝗧𝗵𝗲 𝗕𝗲𝘀𝘁 𝗦𝗼𝘂𝗿𝗰𝗲 𝗢𝗻 𝗧𝗲𝗹𝗲𝗴𝗮𝗺 🎸 .",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " تحديثات سم .", url=f"https://t.me/a_re_aa"), 
                 InlineKeyboardButton(
                    " ♡ ",       url=f"https://t.me/a_re_aa"), 
                 
             ],[ 
            InlineKeyboardButton(
                        " ᴅᴇᴠᴇʟᴏᴘᴇʀ", url=f"https://t.me/Mab_1p"), 
                      
             ],[ 
                  InlineKeyboardButton(
                text=" أضفني الى مجموعتك",
                url=f"https://t.me/{app.username}?startgroup=true"),
                ],

            ]

        ),

    )
