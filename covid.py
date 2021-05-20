    # coding=utf8

import discord
from random import seed
from random import randint
import datetime
import random
from datetime import date
from discord.ext import commands
import aiohttp
import asyncio
import requests
import json
import os
import pandas as pd
import time
import schedule


client = discord.Client()



@client.event
async def on_ready():
    print("OK")


@client.event
async def on_message(message, ctx=None):

    if message.author == client.user:
        return

    if ("!covid") in message.content:

        channel = client.get_channel(813713177941770253)
        headers = {
        	'accept': 'application/json'
        }
        response = requests.get('https://covid-19-greece.herokuapp.com/all', headers=headers)
       	output = json.loads(response.text)
       	cases = output['cases']
       	array_length = len(cases)
       	last_element = cases[array_length - 1]

       	embedVar = discord.Embed(title=f"Covid 19 Bot", description="©️petersid202", color=0x00ff00)
       	embedVar.add_field(name="Ημερομηνία:", value=last_element["date"], inline=False)
       	embedVar.add_field(name="Επιβεβαιωμένα Κρούσματα:", value=last_element["confirmed"], inline=False)
       	embedVar.add_field(name="Θάνατοι:", value=last_element["deaths"], inline=False)
       	await channel.send(embed=embedVar)

    if ("!region") in message.content:
        channel = client.get_channel(813713177941770253)
        headers = {
        	'accept': 'application/json'
        }
        response = requests.get('https://covid-19-greece.herokuapp.com/regions', headers=headers)
       	output = json.loads(response.text)
       	regions = output['regions']
       	print(regions[0])
       	#array_length = len(regions)
       	#last_element = regions[array_length - 1]

       	file = discord.File("nomoi.png")
       	embed = discord.Embed(title="Για ποιο νομό θες να μάθεις πληροφορίες;")
       	embed.set_image(url="attachment://nomoi.png")
       	await channel.send(file=file, embed=embed)
       	
       	nomoi = ["ΑΓΙΟ ΟΡΟΣ","ΑΙΤΩΛΟΑΚΑΡΝΑΝΙΑΣ","ΑΡΓΟΛΙΔΑΣ","ΑΡΚΑΔΙΑΣ","ΑΡΤΑΣ","ΑΤΤΙΚΗΣ","ΑΧΑΪΑΣ","ΒΟΙΩΤΙΑΣ","ΓΡΕΒΕΝΩΝ","ΔΡΑΜΑΣ","ΔΩΔΕΚΑΝΗΣΩΝ","ΕΒΡΟΥ","ΕΥΒΟΙΑΣ","ΕΥΡΥΤΑΝΙΑΣ","ΖΑΚΥΝΘΟΥ","ΗΛΕΙΑΣ","ΗΜΑΘΙΑΣ","ΗΡΑΚΛΕΙΟΥ","ΘΕΣΠΡΩΤΙΑΣ","ΘΕΣΣΑΛΟΝΙΚΗΣ","ΙΩΑΝΝΙΝΩΝ","ΚΑΒΑΛΑΣ","ΚΑΡΔΙΤΣΑΣ","ΚΑΣΤΟΡΙΑΣ","ΚΕΡΚΥΡΑΣ","ΚΕΦΑΛΛΟΝΙΑΣ","ΚΙΛΚΙΣ","ΚΟΖΑΝΗΣ","ΚΟΡΙΝΘΟΥ","ΚΟΡΙΝΘΟΥ","ΛΑΚΩΝΙΑΣ","ΛΑΡΙΣΑΣ","ΛΑΣΙΘΙΟΥ","ΛΕΣΒΟΥ","ΛΕΥΚΑΔΑΣ","ΜΑΓΝΗΣΙΑΣ","ΜΕΣΣΗΝΙΑΣ","ΞΑΝΘΗΣ","ΠΕΛΛΑΣ","ΠΙΕΡΙΑΣ","ΠΡΕΒΕΖΑΣ","ΡΕΘΥΜΝΟΥ","ΡΟΔΟΠΗΣ","ΣΑΜΟΥ","ΣΕΡΡΩΝ","ΤΡΙΚΑΛΩΝ","ΦΘΙΩΤΙΔΑΣ","ΦΛΩΡΙΝΑΣ","ΦΩΚΙΔΑΣ","ΧΑΛΚΙΔΙΚΗΣ","ΧΑΝΙΩΝ","ΧΙΟΥ"]
       	arithmoi = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52"]
       	
       	def check(msg):
       		return msg.content.lower() in arithmoi and msg.channel == channel

       	msg = await client.wait_for("message", check=check)

       	if msg.content.lower() == "1":
       		nomos = nomoi[0]
       	elif  msg.content.lower()=="2":
       		nomos = nomoi[1]
       	elif  msg.content.lower() =="3":
       		nomos = nomoi[2]
       	elif  msg.content.lower() == "4":
       		nomos = nomoi[3]
       	elif  msg.content.lower() =="5":
       		nomos = nomoi[4]
       	elif msg.content.lower() == "6":
       		nomos = nomoi[5]
       	elif  msg.content.lower()=="7":
       		nomos = nomoi[6]
       	elif  msg.content.lower() =="8":
       		nomos = nomoi[7]
       	elif  msg.content.lower() == "9":
       		nomos = nomoi[8]
       	elif  msg.content.lower() =="10":
       		nomos = nomoi[9]	
       	elif msg.content.lower() == "11":
       		nomos = nomoi[10]
       	elif  msg.content.lower()=="12":
       		nomos = nomoi[11]
       	elif  msg.content.lower() =="13":
       		nomos = nomoi[12]
       	elif  msg.content.lower() == "14":
       		nomos = nomoi[13]
       	elif  msg.content.lower() =="15":
       		nomos = nomoi[14]
       	elif msg.content.lower() == "16":
       		nomos = nomoi[15]
       	elif  msg.content.lower()=="17":
       		nomos = nomoi[16]
       	elif  msg.content.lower() =="18":
       		nomos = nomoi[17]
       	elif  msg.content.lower() == "19":
       		nomos = nomoi[18]
       	elif  msg.content.lower() =="20":
       		nomos = nomoi[19]
       	elif msg.content.lower() == "21":
       		nomos = nomoi[20]
       	elif  msg.content.lower()=="22":
       		nomos = nomoi[21]
       	elif  msg.content.lower() =="23":
       		nomos = nomoi[22]
       	elif  msg.content.lower() == "24":
       		nomos = nomoi[23]
       	elif  msg.content.lower() =="25":
       		nomos = nomoi[24]
       	elif msg.content.lower() == "26":
       		nomos = nomoi[25]
       	elif  msg.content.lower()=="27":
       		nomos = nomoi[26]
       	elif  msg.content.lower() =="28":
       		nomos = nomoi[27]
       	elif  msg.content.lower() == "29":
       		nomos = nomoi[28]
       	elif  msg.content.lower() =="30":
       		nomos = nomoi[29]	
       	elif msg.content.lower() == "31":
       		nomos = nomoi[30]
       	elif  msg.content.lower()=="32":
       		nomos = nomoi[31]
       	elif  msg.content.lower() =="33":
       		nomos = nomoi[32]
       	elif  msg.content.lower() == "34":
       		nomos = nomoi[33]
       	elif  msg.content.lower() =="35":
       		nomos = nomoi[34]
       	elif msg.content.lower() == "36":
       		nomos = nomoi[35]
       	elif  msg.content.lower()=="37":
       		nomos = nomoi[36]
       	elif  msg.content.lower() =="38":
       		nomos = nomoi[37]
       	elif  msg.content.lower() == "39":
       		nomos = nomoi[38]
       	elif  msg.content.lower() =="40":
       		nomos = nomoi[39]
       	elif  msg.content.lower() =="41":
       		nomos = nomoi[40]
       	elif  msg.content.lower() == "42":
       		nomos = nomoi[41]
       	elif  msg.content.lower() =="43":
       		nomos = nomoi[42]	
       	elif msg.content.lower() == "44":
       		nomos = nomoi[43]
       	elif  msg.content.lower()=="45":
       		nomos = nomoi[44]
       	elif  msg.content.lower() =="46":
       		nomos = nomoi[45]
       	elif  msg.content.lower() == "47":
       		nomos = nomoi[46]
       	elif  msg.content.lower() =="48":
       		nomos = nomoi[47]
       	elif msg.content.lower() == "49":
       		nomos = nomoi[48]
       	elif  msg.content.lower()=="50":
       		nomos = nomoi[49]
       	elif  msg.content.lower() =="51":
       		nomos = nomoi[50]
       	elif  msg.content.lower() == "52":
       		nomos = nomoi[51]

       	print(nomos)
       	if nomos in nomoi:
       		hello = regions[int(msg.content.lower())-1]
       		embedVar = discord.Embed(title=f"Covid 19 Bot", description="©️petersid202", color=0x00ff00)
       		embedVar.add_field(name="Ημερομηνία:", value=hello["last_updated_at"], inline=False)
       		embedVar.add_field(name="Περιοχή:", value=nomos, inline=False)
       		embedVar.add_field(name="Κρούσματα ανά 100 χιλιάδες άτομα:", value=hello["cases_per_100000_people"], inline=False)
       		embedVar.add_field(name="Συνολικά Κρούσματα:", value=hello["total_cases"], inline=False)
       		await channel.send(embed=embedVar)



client.run('NzgwMzg1MDE0MzM2MTkyNTMy.X7uULg.EjgXt7HMo65vjgBg5764QuO2-2I')