from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
🇹🇷 Merhaba {}

• **Hos geldiniz** {}

✍🏻 **Ben Fısıldayanların Efendisiyim** . . .

» **Gruplarda ve kanallarda arkadaşınıza fısıltı göndermek için beni kullanabilirsiniz ( Grubta olmasam bile )! **

» **Diğerleri aynı grupta olsa bile sadece o arkadaşınızin mesajını siz okuyabileceksiniz !** 

`By` @ByWolk
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔒 𝖡𝗂𝗋 𝖥𝗂𝗌𝗂𝗅𝗍𝗂 𝖦𝗈𝗇𝖽𝖾𝗋 🔒", switch_inline_query="")],
        [InlineKeyboardButton(text="🏠 𝖦𝖾𝗋𝗂 𝖦𝗂𝗍 🏠", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("🔒 𝖡𝗂𝗋 𝖥𝗂𝗌𝗂𝗅𝗍𝗂 𝖦𝗈𝗇𝖽𝖾𝗋 🔒", switch_inline_query="")
        ],

        [InlineKeyboardButton("✍🏻 𝖭𝖺𝗌𝗂𝗅 𝖪𝗎𝗅𝗅𝖺𝗇𝗂𝗋𝗂𝗆 ?", callback_data="help")],
        [InlineKeyboardButton("🇹🇷 𝖱𝖾𝗌𝗆𝗂 𝖪𝖺𝗇𝖺𝗅", url="https://t.me/StarBotKanal")],
    ]

    # Help Message
    HELP = """
»**Herhangi bir Grubta mesajı aşağıdaki gibi yazmanız yeterlidir **.

» @StarWhisperBot **Mesajiniz** `Kullanıcı Adı`
    """

    # About Message
    ABOUT = """
**About This Bot** 

Bot created by @StarkBots

Source Code : [Click Here](https://github.com/StarkBotsIndustries/WhisperBot)

Inspired By : nnbbot

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @StarkProgrammer
    """
