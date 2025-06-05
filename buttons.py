from aiogram.types import ReplyKeyboardMarkup , InlineKeyboardMarkup , InlineKeyboardButton , KeyboardButton , ReplyKeyboardRemove
from aiogram.fsm.state import StatesGroup , State
from dbmedia.media import webappurls


# Главная клавиатура РУССКИЙ
mainkb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Наш сайт 🌐",web_app={"url": webappurls["aboutus"]})
        ],
        [
            InlineKeyboardButton(text="Адрес 📍",callback_data="location")
        ],
        [
            InlineKeyboardButton(text="IELTS курсы",callback_data="ieltscourses")
        ],
        [
            InlineKeyboardButton(text="SAT курсы",callback_data="satcourses")
        ],
        [
            InlineKeyboardButton(text="О нас 🚀",callback_data="aboutus")
        ],
        [
            InlineKeyboardButton(text="Челлендж 🎯",callback_data="challenge")
        ],
        [
            InlineKeyboardButton(text="Записаться на консультацию ☎️",callback_data="consult")
        ],
        [
            InlineKeyboardButton(text="Отзывы ✅",callback_data="feedback")
        ]
    ]
)
useridkb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Узнать свой UserId 🆔")
        ]
    ],
    resize_keyboard=True
)

# Нужно поменять на серваке 
# FSM state, класс для хранения данных для каждого пункта
class Sendall(StatesGroup):
    GET_PHOTO = State()
    GET_TEXT = State()
    GET_BUTTON = State()
    GET_LINK = State()
    CONFIRM = State()



participating = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Да",callback_data="yes_i_am"),
            InlineKeyboardButton(text="Нет",callback_data="no_im_not")
                                
        ]
    ],
    resize_keyboard=True
)





#Изменения своих данных в профиле!

photoyesorno = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Да",callback_data="yesphoto"),
            InlineKeyboardButton(text="Нет",callback_data="nophoto")
                                
        ]
    ],
    resize_keyboard=True
)

# с кнопкой или нет 
buttonsyesorno = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Да",callback_data="yesbutton"),
            InlineKeyboardButton(text="Нет",callback_data="nobutton")
                                
        ]
    ],
    resize_keyboard=True
)
    
# confirmation yes or no 
confirmationyesorno = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Да",callback_data="yesconfirm"),
            InlineKeyboardButton(text="Нет",callback_data="noconfirm")
                                
        ]
    ],
    resize_keyboard=True
)




back = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙",callback_data="backtomainkb")
        ]
    ]
)
# ссылка на наши инстаграммы
onstudyinstas = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="onstudy.prep",url="https://www.instagram.com/onstudy.prep/")
        ],
        [
            InlineKeyboardButton(text="onstudy.consult",url="https://www.instagram.com/onstudy.consult/")
        ],
        [
            InlineKeyboardButton(text="🔙",callback_data="backtomainkb")
        ]
    ]
)


# Вся информация про нашу команду
aboutusallinfo = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Результаты наших студентов 🎯",callback_data="results")
        ],
        [
            InlineKeyboardButton(text="Отзывы наших студентов 🗣",callback_data="feedbackfromstudents")
        ],
        [
            InlineKeyboardButton(text="Наши студенты 🤩",callback_data="ourstudents")
        ],
        [
            InlineKeyboardButton(text="Наши контакты ☎️",callback_data="contacts")
        ],
        [
            InlineKeyboardButton(text="🔙",callback_data="backtomainkb")
        ]
    ]
)
# возращение в меню где О нас !
backfromresultsetc = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙",callback_data="aboutus")
        ]
    ]
)


# IELTS курсы, вся информация 
ieltskb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Стоимость 💸",callback_data="price")
        ],
        [
            InlineKeyboardButton(text="Наши Менторы 😍",callback_data="ourmentors")
        ],
        [
            InlineKeyboardButton(text="Формат обучения 🗓",callback_data="formatofclasses")
        ],
        [
            InlineKeyboardButton(text="🔙",callback_data="backtomainkb")
        ]
    ]
)

getbackieltskb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙",callback_data="ieltscourses")
        ]
    ]
)


# IELTS курсы, вся информация 
satkb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Стоимость 💸",callback_data="pricesat")
        ],
        [
            InlineKeyboardButton(text="Наши Менторы 😍",callback_data="ourmentorssat")
        ],
        [
            InlineKeyboardButton(text="Формат обучения 🗓",callback_data="formatofclassessat")
        ],
        [
            InlineKeyboardButton(text="🔙",callback_data="backtomainkb")
        ]
    ]
)

getbacksatkb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙",callback_data="satcourses")
        ]
    ]
)


# Зарегаться 
getregistrated = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Зарегистрироваться 🚀",callback_data="registrationform")
        ]
    ]
)
# ссылка на нашу группу 
tggroup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="ТЕЛЕГРАМ ГРУППА",url="https://t.me/+oNK9c1Utr_hhMjVi")
        ],
        [
            InlineKeyboardButton(text="Я подписался(ась)✅",callback_data="checkoffollowing")
        ]
    ]
)