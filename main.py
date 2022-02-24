from discord.ext import commands
from AntiScam import AntiScam

whitelist = [435976390551273485] # Here you can add the IDs of the users allowed to bypass the AntiScam system.
logs_channel = ''# Here you can add the ID of the channel where the logs will be sent.

killerBot = commands.Bot(command_prefix='>')
killerBot.remove_command('help') # Remove this line if you want to use the help command.

@killerBot.listen()
async def on_message(message):
    await AntiScam(message, bot = killerBot, whitelist = whitelist, muted_role='Muted', verified_role='Verificado', logs_channel=[454452587920621568]) # Here you can change the names of the roles.

killerBot.run('OTQ2NDMwMTY0NTQyMzIwNjQw.Yhelxw.cFw0tnIlY8A2Nzdj3Tr6JEwGH0o')
