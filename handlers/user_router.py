from aiogram import Router, F
from aiogram.types import Message, FSInputFile
from imagetovideo import imagetovideo
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.filters import CommandStart
from os import remove, mkdir
from shutil import rmtree, copy


user_data = {}
user_router = Router()
quest1 = ["Ищем домик мумитролей (подсказки: черепичная крыша, и что-то про письма), в сказке он выглядит так:"
          , "Ищем оригинальную историческую мостовую (ей точно больше 100 лет) - фотографируем, отправляем."
          , "Теперь ищем уличное искусство с карельской мифологической базой – на самой высокой точке города вас ждет «Старик», чтобы к нему добраться, надо преодолеть 183 каменные ступеньки"
          , "Устали? Присядьте рядом с Архитектором Уно Улбергом и скиньте нам селфи)"
          , "Обратимся к природе, вернее, к ее обитателям – делаем фото с арт-объектами (скульптурами, памятниками) в виде диких животных."
          , "Продолжаем тему фауны: попробуйте сфотографировать городских птиц, которые тусуются возле воды"
          , "Продолжая тему птиц, фотографируем ЖЭК-арт, если не знаете что это – погуглите (наша картинка в помощь) А наш бот ждет фото."
          , "Возвращаемся к истории города, на многих старинных зданиях указан год постройки. Находи и присылай фотку."
          , "И завершает наш квест немного футуристическое здание с ногами. Нейросеть вот такое рисует, но искать вам"
          , "Спасибо за участие в квесте! Уверены, вы получили яркие эмоции, гуляя по нашему любимому городу ❤️ А на память дарим вам небольшое видео с вашими впечатлениями!"]


text = ["Спасибо, отличное фото.", "Красота", "Ты точно не фотограф?"
         ,"С тобой интересно гулять!", "Отличный ракурс, продолжай в том же духе!"
         , "Твои ответы впечатляют!", "Сколько необычных уголков в нашем городе."
         , "Кря! Мне нравится твоя активность!", "Кря - кря!" ," Ты меня приятно удивляешь!"
         , "Вот это кадр!"]


class quest(StatesGroup):
    nquest1 = State()
    nquest2 = State()
    nquest3 = State()
    nquest4 = State()
    nquest5 = State()
    nquest6 = State()
    nquest7 = State()
    nquest8 = State()
    nquest9 = State()
    nquest10 = State()


@user_router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await message.answer('Получайте задание от нашего умненького бота и присылайте в ответ фотоответы. Можно и нужно пользоваться поиском в Интернете. Но также можно просто гулять с широко открытыми глазами, включая воображение. Наш бот очень голодный – скорее начинайте!')
    await message.answer('Начнем с архитектуры. Ищем короны на исторических зданиях города. Нашему боту хватит одной фотографии.')
    await state.set_state(quest.nquest1)
def quests(name, name1, texts, path = None, video = False):
    @user_router.message(name, F.photo)
    async def text1(message:Message, state: FSMContext):
        user_name = message.from_user.full_name
        try:
                mkdir(f"image{user_name}")
                
        except FileNotFoundError:
            None
        except FileExistsError:
            None
        if(len(str(name)) == 23):
            await message.bot.download(file=message.photo[-1].file_id, destination=fr"image{message.from_user.full_name}/{str(name)[20:21]}.jpg")
        else:
            await message.bot.download(file=message.photo[-1].file_id, destination=fr"image{message.from_user.full_name}/{str(name)[20:22]}.jpg")
        await message.answer(text[texts])
        await message.answer(quest1[texts])
        if path != None: await message.answer_photo(photo=FSInputFile(path))
        if video == True: 
            copy("0sorsa.jpg", f"image{user_name}")
            imagetovideo(user_name)
            await message.answer_video(video=FSInputFile(f"{user_name}.mp4"))
            remove(f"{user_name}.mp4")
            rmtree(f"image{user_name}")
        await state.set_state(name1)

quests(quest.nquest1, quest.nquest2, 0, "1 квест.jpg")
quests(quest.nquest2, quest.nquest3, 1)
quests(quest.nquest3, quest.nquest4, 2)
quests(quest.nquest4, quest.nquest5, 3)
quests(quest.nquest5, quest.nquest6, 4)
quests(quest.nquest6, quest.nquest7, 5)
quests(quest.nquest7, quest.nquest8, 6, "2 квест.jpg")
quests(quest.nquest8, quest.nquest9, 7)
quests(quest.nquest9, quest.nquest10, 8, "3 квест.jpg")
quests(quest.nquest10, quest.nquest10, 9, None ,True)




