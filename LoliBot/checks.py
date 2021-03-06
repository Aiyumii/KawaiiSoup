from discord.ext import commands
from LoliBot import load_config
from LoliBot.settings import guild_settings as gs

def is_owner_or_admin():
	def predicate(ctx):
		if ctx.author.id == load_config.owner:
			return True
		else:
			for role in ctx.author.roles:
				if role.id in gs.get(ctx.guild).perm_roles["admin"]:
					return True
		return False
	return commands.check(predicate)

def is_admin_or_mod():
	def predicate(ctx):
		if ctx.message.author.id == load_config.owner:
			return True
		else:
			admin_roles =  gs.get(ctx.guild).perm_roles["admin"]
			mod_roles = gs.get(ctx.guild).perm_roles["mod"]
			for role in ctx.author.roles:
				if role.id in mod_roles or role.id in admin_roles:
					return True
		return False
	return commands.check(predicate)

def nsfw_predicate(ctx):
	nsfw = gs.get(ctx.guild).nsfw
	if not nsfw["channels"] and nsfw["enabled"]:
		return nsfw["enabled"] == 1
	elif nsfw["enabled"] and nsfw["channels"]:
		return ctx.channel.id in nsfw["channels"]
	else:
		return False

def is_nfsw_enabled():
	return commands.check(lambda ctx: nsfw_predicate(ctx))

def isnt_anal():
	return commands.check(lambda ctx: gs.get(ctx.guild).is_anal["y/n"] and nsfw_predicate(ctx) or not gs.get(ctx.guild).is_anal["y/n"])
