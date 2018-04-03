import configparser

settings = configparser.ConfigParser() 
settings.read("LoliBot/preferences.ini")

command_prefix = settings["LoliBot"]["Command_Prefix"]
token = settings["LoliBot"]["Token"]
owner = int(settings["LoliBot"]["OwnerID"])
tat_token = settings["LoliBot"]["Tatsumaki_Token"]


__description__ = """LoliBot, A Discord Bot made by a anime fan. Built with love (and discord.py) by MoonAlicesu ☪#1100.

[Github link](https://github.com/Aiyumii/KawaiiSoup)
[Changelog](https://github.com/Aiyumii/KawaiiSoup#v100)
[Found a bug or need to report an issue? Report it here](https://github.com/Aiyumii/KawaiiSoup/issues/new)"""
__author__ = "MoonAlice"
__version__ = "1.5.0"
embedcolour = 0xDEADBF

# IF YOU ARE TESTING OR NOT IN THE GSS DISCORD, REMOVE "cogs.gss" FROM THE LIST

cogs = [
	"LoliBot.cogs.admin",
	"LoliBot.cogs.customcommands",
	"LoliBot.cogs.fun",
	"LoliBot.cogs.joinleave",
	"LoliBot.cogs.nsfw",
	"LoliBot.cogs.reddit",
	"LoliBot.cogs.selfassign",
	"LoliBot.cogs.trivia",
	"LoliBot.cogs.twitch",
	"LoliBot.cogs.util",
	#"LoliBot.cogs.gss"
]
