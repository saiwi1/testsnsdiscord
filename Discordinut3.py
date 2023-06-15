
import discord 
import datetime


intents = discord.Intents.default()
intents.message_content = True


client = discord.Client(intents=intents)


TOKEN = ''


@client.event
async def on_ready():
    print('ログインしました')


@client.event
async def on_message(message): 


    if message.author.bot:
        return


    def check(msg):
        return msg.author == message.author

  
    if message.content.startswith("/in_"):

        wait_message0 = await client.wait_for("message", check=check)

        wait_message1 = await client.wait_for("message", check=check)

        wait_message2 = await client.wait_for("message", check=check)

       
        dt= datetime.datetime.now()
        dt_now =dt.strftime('%Y年%m月%d日%H:%M')

        ded = wait_message0.content
        ded0 = wait_message1.content
        ded1 = wait_message2.content

        ddss = message.author.id
        qqqst = str(message.author)

        lis = [dt_now,ded,ded0,ded1,ddss,qqqst]

        await message.channel.send("完了")

    elif message.content.startswith("/su_"):


        wait_message0 = await client.wait_for("message", check=check)

        wait_message1 = await client.wait_for("message", check=check)

        wait_message2 = await client.wait_for("message", check=check)

 
        dt= datetime.datetime.now()
        dt_now =dt.strftime('%Y年%m月%d日%H:%M')

        ded = wait_message0.content
        ded0 = wait_message1.content
        ded1 = wait_message2.content

        ddss = message.author.id
        qqqst = str(message.author)

        lis = [dt_now,ded,ded0,ded1,ddss,qqqst]
        suu= int(ded)+int(ded0)+int(ded1)
        print(lis)

        await message.channel.send(f'計算結果は{suu}です')

client.run(TOKEN)