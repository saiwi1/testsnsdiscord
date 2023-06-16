import discord 
import datetime
import sqlite3

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

  
    if message.content.startswith("/out_"):
        
        await message.channel.send(f'金額を入力してください')        
        wait_message2 = await client.wait_for("message", check=check)
        await message.channel.send(f'科目を入力してください')
        wait_message0 = await client.wait_for("message", check=check)
        await message.channel.send(f'支払先を入力してください')
        wait_message1 = await client.wait_for("message", check=check)
        
        await message.channel.send(f'摘要を入力してください')
        wait_message3 = await client.wait_for("message", check=check)
       
        dt= datetime.datetime.now()
        dt_now =dt.strftime('%Y年%m月%d日%H:%M')
        dt_y = int(dt.strftime('%Y'))
        dt_m = int(dt.strftime('%m'))
        dt_d = int(dt.strftime('%d'))
        dt_ym = dt.strftime('%Y年%m月')
        kamoku = wait_message0.content
        saki = wait_message1.content
        kinngaku = wait_message2.content
        tekiyo = wait_message3.content

        memberid = message.author.id
        membername = str(message.author)

        conn = sqlite3.connect("syushi.db")
        cur = conn.cursor()
        cur.execute('create table IF NOT EXISTS pyment(id text,year int,month int,day int,yearmonth text,kamoku text,buyer text,out_Money integer,tekiyou text,Author_id int,Author_name text,primary key(id))')
        # データの挿入
        dt = datetime.datetime.now()
        dt_now = dt.strftime('%Y%m%d%H%M%S')
        data = [(dt_now,dt_y,dt_m,dt_d,dt_ym,kamoku,saki,kinngaku,tekiyo,memberid,membername)]
        cur.executemany('INSERT INTO pyment VALUES(?,?,?,?,?,?,?,?,?,?,?)',data)
        cur.close()
        conn.commit()
        conn.close()
        await message.channel.send(f'終わりました')
    elif message.content.startswith("/in_"):
        
        await message.channel.send(f'金額を入力してください')        
        wait_message2 = await client.wait_for("message", check=check)
        await message.channel.send(f'科目を入力してください')
        wait_message0 = await client.wait_for("message", check=check)
        await message.channel.send(f'収入元を入力してください')
        wait_message1 = await client.wait_for("message", check=check)
        
        await message.channel.send(f'摘要を入力してください')
        wait_message3 = await client.wait_for("message", check=check)
       
        dt= datetime.datetime.now()
        dt_now =dt.strftime('%Y年%m月%d日%H:%M')
        dt_y = int(dt.strftime('%Y'))
        dt_m = int(dt.strftime('%m'))
        dt_d = int(dt.strftime('%d'))
        dt_ym = dt.strftime('%Y年%m月')
        kamoku = wait_message0.content
        moto = wait_message1.content
        kinngaku = wait_message2.content
        tekiyo = wait_message3.content

        memberid = message.author.id
        membername = str(message.author)

        conn = sqlite3.connect("syushi.db")
        cur = conn.cursor()
        cur.execute('create table IF NOT EXISTS income(id text,year int,month int,day int,yearmonth text,kamoku text,income text,receipt_Money integer,tekiyou text,Author_id int,Author_name text,primary key(id))')
        # データの挿入
        dt = datetime.datetime.now()
        dt_now = dt.strftime('%Y%m%d%H%M%S')
        data = [(dt_now,dt_y,dt_m,dt_d,dt_ym,kamoku,moto,kinngaku,tekiyo,memberid,membername)]
        cur.executemany('INSERT INTO income VALUES(?,?,?,?,?,?,?,?,?,?,?)',data)
        cur.close()
        conn.commit()
        conn.close()
        await message.channel.send(f'終わりました')
client.run(TOKEN)