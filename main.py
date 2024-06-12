import discord
from requests_html import AsyncHTMLSession
from bs4 import BeautifulSoup
import nest_asyncio
client = discord.Client()

async def get_data():
    asession = AsyncHTMLSession()
    r = await asession.get('https://money18.on.cc/')
    #r = await asession.get('https://money18.on.cc/info/hk/liveinfo_quote_02382.html')
    await r.html.arender()
    # print(r.html.html)
    soup = BeautifulSoup(r.html.html, 'html.parser')
    print(soup.prettify())
    filter = soup.find("div", class_="stock stockDn")
    filter2 = filter.find("div", class_="value")
    # print(filter)
    #print(filter2)
    result = "" + filter2.get_text()
    #print(result)
    return result

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('恒指'):
        await message.channel.send(await get_data())
        #await get_data()
client.run('Discord Bot Token')
