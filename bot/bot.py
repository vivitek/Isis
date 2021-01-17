import discord
import os
import psycopg2
from discord.utils import get

try:
    conn = psycopg2.connect("host={} dbname={} password={} user={}".format(os.getenv(
        "POSTGRES_URL", "localhost"), os.getenv("POSTGRES_DB"), os.getenv("POSTGRES_PWD"), os.getenv("POSTGRES_USER")))
except psycopg2.Error as err:
    print("[-] Error psql: {}".format(err.pgerror))
    quit(1)

conn.autocommit = True
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS site(url CHAR(200) NOT NULL,category CHAR(200) NOT NULL,id INT PRIMARY KEY NOT NULL)")

HOOK_ID = os.getenv("HOOK_ID")
XANA_CHANNEL = os.getenv("XANA_CHANNEL")


def add_record(url, category):
    cur.execute(
        "INSERT INTO site(url, category) values {},{}".format(url, category))


async def create_embed(url, category, reactions):
    pros = get(reactions, emoji="✅")
    against = get(reactions, emoji="❌")
    pros_name = ""
    against_name = ""
    embed: discord.Embed = discord.Embed(title="Results for {}".format(url))
    embed.add_field(name="Url", value=url)
    embed.add_field(name="Category", value=category)
    embed.add_field(name="For", value=pros.count - 1, inline=False)
    pro_users = await pros.users().flatten()
    for p in pro_users:
        pros_name += p.mention + "\n"
    embed.add_field(name="Nominations For", value=pros_name, inline=True)
    against_users = await against.users().flatten()
    for p in against_users:
        against_name += p.mention + "\n"
    embed.add_field(name="Against", value=against.count - 1, inline=False)
    embed.add_field(name="Nominations Against",
                    value=against_name, inline=True)
    return embed


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        await self.change_presence(activity=discord.Activity(name="Urls", type=3))
        self.channel: discord.TextChannel = self.get_channel(int(XANA_CHANNEL))

    async def on_message(self, message: discord.Message):
        if str(message.author.id) != HOOK_ID or str(message.channel.id) != XANA_CHANNEL:
            return
        # await message.add_reaction("✅")
        # await message.add_reaction("❌")

    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        if str(payload.user_id) == HOOK_ID or str(payload.user_id) == self.user.id or payload.channel_id != int(XANA_CHANNEL):
            return
        message: discord.Message = await self.channel.fetch_message(payload.message_id)
        if payload.emoji.name != '✅' and payload.emoji.name != '❌':
            member: discord.Member = await self.fetch_user(payload.user_id)
            if not member:
                return
            await message.remove_reaction(payload.emoji, member)
        reaction: discord.Reaction = get(
            message.reactions, emoji=payload.emoji.name)
        if reaction and reaction.count == 2:
            data_embed = message.embeds[0].to_dict()
            url = None
            category = None
            for f in data_embed["fields"]:
                if f["name"] == "Url":
                    url = f["value"]
                if f["name"] == "Category":
                    category = f["value"]
            if (payload.emoji.name == "✅"):
                add_record(url, category)
            embed = await create_embed(url, category, message.reactions)
            await self.channel.send(embed=embed)
            await message.delete()


client = MyClient()
client.run(os.getenv("DISCORD_TOKEN"))
