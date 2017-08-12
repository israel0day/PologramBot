#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telebot
from telebot import types
import os
from forex_python.bitcoin import BtcConverter
from decimal import *
import time
# Coded By: @Uservzk80
# Github: https://github.com/uservzk80


TOKEN = "Your Token" # Telegram Token
USERS_LOCATED = {'Your_Name':'Your Telegram ID', 'Pedro_Example':'00000000'} # Add all authorized users to use the bot

userProc = {}
BotUsers = []

commands = {
              'start': 'Start the bot',
              'help': 'Commands available',
              'balance': 'Show poloniex balance',
              'trades': 'Show last trades'
}

# TEXT COLOR
class color:
    RED = '\033[91m'
    ENDC = '\033[0m'


# USER STEP
def get_user_step(uid):
    if uid in userProc:
        return userProc[uid]
    else:
        BotUsers.append(uid)
        userProc[uid] = 0
        print(color.RED + " [+] !!NEW USER!!" + color.ENDC)

# LISTENER
def listener(messages):
    for m in messages:
        if m.content_type == 'text':
            print("[" + str(m.chat.id) + "] " + str(m.chat.first_name) + ": " + m.text)

bot = telebot.TeleBot(TOKEN)
bot.set_update_listener(listener)


# START
@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    userProc[cid] = 0
    bot.send_message(cid, "Hi " + str(m.chat.first_name) + " I'm a Telegram Bot for Poloniex")
    time.sleep(1)
    bot.send_message(cid, "I hope I can help you")
    time.sleep(1)


# HELP
@bot.message_handler(commands=['help'])
def command_help(m):

    cid = m.chat.id
    help_text = "This is my commands ;)\n"
    for key in commands:
        help_text += "/" + key + ": "
        help_text += commands[key] + "\n"
    bot.send_message(cid, help_text)


@bot.message_handler(commands=['balance'])
def balance(m):

    cid = m.chat.id

    if str(cid) in USERS_LOCATED.values():

        bot.send_chat_action(cid, 'typing')

        infile = open('balance', 'r')
        infile = infile.read()

        bot.send_message(cid, "I am calculating the balance...")
        bot.send_message(cid, "The total balance is: " + infile[:9])

    else:
        bot.send_message(cid, "You are not authorized.")


@bot.message_handler(commands=['trades'])
def trades(m):

    cid = m.chat.id

    if str(cid) in USERS_LOCATED.values():

        bot.send_chat_action(cid, 'typing')

        infile = open('trades', 'r')
        infile = infile.read()

	if len(infile) == 0:
		bot.send_message(cid, "There are no trades")
        else:

		bot.send_message(cid, "I'm recovering the trades ...")
        	bot.send_message(cid, "Last Trades:\n\n " + infile)

    else:
        bot.send_message(cid, "You are not authorized.")


@bot.message_handler(func=lambda message: True, content_types=['text'])
def command_text(m):
    cid = m.chat.id
    if (m.text.lower() in ['hellow', 'hi', 'hola']):
        bot.send_message(cid, 'Hi, ' + str(m.from_user.first_name) + '. Im glad to see you.', parse_mode="Markdown")
    elif (m.text.lower() in ['bye', 'goodbye', 'adios']):
        bot.send_message(cid, 'Bye, ' + str(m.from_user.first_name), parse_mode="Markdown")

    elif (m.text.lower() in ['ayuda', 'help', 'aiuda']):
        bot.send_message(cid, 'It seems that you have problems ' + str(m.from_user.first_name) + '. Type /help.', parse_mode="Markdown")

    elif (m.text.lower() in ['balace', 'trades']):
        bot.send_message(cid, 'It seems that you have problems ' + str(m.from_user.first_name) + '. Type /+command. Example: /help', parse_mode="Markdown")

    else:
        bot.send_message(cid, 'I do not understand you ' + str(m.from_user.first_name) + '. You re talking to a bot and will not talk /help', parse_mode="Markdown")

print 'Starting...'
bot.polling(none_stop=True)
