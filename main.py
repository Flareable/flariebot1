import discord
from discord.ext import commands
from keep_alive import keep_alive

keep_alive()

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Kata-kata yang dianggap toxic
banned_words = ["nigga", "nigg4", "fuck", "stfu", "kontol"]

@bot.event
async def on_ready():
    print(f"Bot {bot.user} aktif dan siap nge-BAN orang toxic!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    msg_content = message.content.lower()

    # Cek apakah ada kata terlarang
    if any(word in msg_content for word in banned_words):
        try:
            await message.author.ban(reason="Menggunakan kata-kata terlarang.")
            await message.channel.send(
                f"{message.author.mention} telah **dilarang (banned)** karena menggunakan kata-kata toxic!\n"
                f"**User has been banned** for using offensive language!"
            )
        except discord.Forbidden:
            await message.channel.send(
                "Aku nggak punya izin buat nge-ban orang ini.\n"
                "I don't have permission to ban this person."
            )
        except Exception as e:
            print(f"Error saat ban: {e}")

    await bot.process_commands(message)

bot.run(TOKEN)