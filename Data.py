from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
اهلا بك {}

• **مرحبا بك في** {}

✍🏻 **يمكنك كتابه رسائل خاصه لاشخاص** . . .

» **ايضا يمكنك استعمالي في ارسال الرسائل في الكروبات من دون وجودي**

» **فقط عليك كتابه يوزر البوت ومن ثم الرساله وبعدها يةزر الشخص المراد الارسال له !** 

`المطور` @K_8_U
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔒 كتابه همسه 🔒", switch_inline_query="")],
        [InlineKeyboardButton(text="🏠 رجوع 🏠", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("🔒 كتابه همسه 🔒", switch_inline_query="")
        ],

        [InlineKeyboardButton("✍🏻 كيفيه كتابه الهمسه ?", callback_data="help")],
        [InlineKeyboardButton("قناة البوت", url="https://t.me/ADWSL")],
    ]

    # Help Message
    HELP = """
» **عليك كتابه يوزر البوت ومن ثم الرساله وبعدها يوزر الشخص **.

» **مثال : **

» @azkarkbot **رسالتك** `يوزر الشخص`
    """

    # About Message
    ABOUT = """
**حول هذا البوت** 

تم التطوير بواسطه @K_8_U


البوت : azkarkbot

شكرا لـ : [Pyrogram](docs.pyrogram.org)

لغه البرمجه : [Python](www.python.org)

قناة البوت : @ADWSL
    """
