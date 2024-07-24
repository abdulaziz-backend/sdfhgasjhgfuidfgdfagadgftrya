from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

START = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Tap🖐 and Blaze🔥",
                web_app=WebAppInfo(url="https://inomjonqurbonov.pythonanywhere.com/")  #<=======SHU YERGA URL NI YOZASIZ ===================>
            )
        ],
        [
            InlineKeyboardButton(
                text="Invite Friends",
                callback_data="invite"
            )
        ],
        [
            InlineKeyboardButton(
                text="Join Community",
                url="https://t.me/BLAZECOMUNITY"  #<=======SHU YERGA URL NI YOZASIZ ===================>
            )
        ]
    ]
)

profile = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🔥TAP🔥",
                web_app=WebAppInfo(url="https://inomjonqurbonov.pythonanywhere.com/") #<=======SHU YERGA URL NI YOZASIZ ===================>
            )
        ],
        [
            InlineKeyboardButton(
                text="Invite Friends",
                callback_data="invite"
            )
        ]
    ]
)
