import discord
from discord.ext import commands
import asyncio
import os
import time
from colorama import init, Fore, Style

init(convert=True)
class DiscordRaid:
	def __init__(self, token , prefix= '?', loop=None, bot_count=1, channel_spam= None, messages_to_spam= None):
		self.channel_spam = channel_spam
		self.bot_count = bot_count
		self.loop = loop
		self.prefix = prefix
		self.token = token
		self.messages_to_spam = messages_to_spam
		self.bot = commands.Bot(command_prefix= self.prefix, loop = self.loop)

	async def run(self):
		@self.bot.event
		async def on_ready():
			print(f'[{self.bot_count}] {self.bot.user.name}#{self.bot.user.discriminator} id: {self.bot.user.id}')
		
		@self.bot.event
		async def on_message(message):
			if message.channel.id == self.channel_spam: 

				for x in self.messages_to_spam:
					await message.channel.send(x)	

		await self.bot.start(self.token, bot=False)


def main():

	menu()	

	print(Style.RESET_ALL)
	tokens = []
	with open("tokens.txt", "r") as tokens_file:
		lines = tokens_file.readlines()
		for l in lines:
			tokens.append(l.replace('\n', ''))

	channel_id  = int(input("[!] Enter ID of the channel you want to raid >"))


	messages_to_spam = []

	while True:
		os.system('cls')
		message_spam = input("[!] Enter messages to spam [enter q to exit] >  ")
		if message_spam == "q":
			break
		messages_to_spam.append(message_spam)

	os.system('cls')
	print(f"The following messages will be spammed to the channel id {channel_id} \n")

	for mes in messages_to_spam:
		print(mes)

	print('\n')
	input("Hit enter to continue.")

	os.system('title EZ Raider [Nightfall#2512] ^| ')
	os.system('cls')

	print("Close the application or hit Control+C to stop spamming. \n")
	print('[*] ~ TOKEN INFORMATION ~ \n')

	main_loop = asyncio.new_event_loop()
	bot_count = 1 
	new_var = {}

	for i, input_token in zip(range(len(tokens)), tokens):
		new_var[i] = DiscordRaid(input_token, loop=main_loop, bot_count= bot_count, channel_spam= channel_id, messages_to_spam= messages_to_spam)
		bot_count += 1

	for z in range(len(tokens)):
		main_loop.create_task(new_var[z].run())

	main_loop.run_forever()
		

def menu():
	os.system('cls')
	os.system('From Genesis Intelligence Team ^| A simple discord server raider.')
	print(f'''
{Fore.LIGHTBLACK_EX} V0.01 Glory to TGT
		{Fore.RED}
		
████████╗░░░░██████╗░░░░████████╗
╚══██╔══╝░░░██╔════╝░░░░╚══██╔══╝
░░░██║░░░░░░██║░░██╗░░░░░░░██║░░░
░░░██║░░░░░░██║░░╚██╗░░░░░░██║░░░
░░░██║░░░██╗╚██████╔╝██╗░░░██║░░░
░░░╚═╝░░░╚═╝░╚═════╝░╚═╝░░░╚═╝░░░
		                            ▀      "We always comeback" -TGT                 
''')
if __name__ == "__main__":
	main()
