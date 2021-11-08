import eel
import requests

@eel.expose
def sum(a):
    cities = ["Абаза",
    "Алатырь",
    "Азов",
    "Астрахань",
    "Алупка",
    "Алагир",
    "Аркадак",
    "Асино",
    "Абакан",
    "Алдан",
    "Андреаполь",
    "Аткарск",
    "Ардатов",
    "Алейск",
    "Александровск",
    "Ахтубинск",
    "Абдулино",
    "Александров",
    "Альметьевск",
    "Ачинск",
    "Абинск",
    "Алексеевка",
    "Арск",
    "Аргун",
    "Агидель",
    "Алексин",
    "Анжеро-Судженск",
    "Арзамас",
    "Адыгейск",
    "Амурск",
    "Ардон",
    "Армавир",
    "Агрыз",
    "Арамиль",
    "Апрелевка",
    "Арсеньев",
    "Азнакаево",
    "Аша",
    "Апатиты",
    "Артем",
    "Алапаевск",
    "Анапа",
    "Апшеронск",
    "Артемовский",
    "Аксай",
    "Ангарск",
    "Асбест",
    "Архангельск",
    "Алушта",
    "Армянск",
    "Алзамай",
    "Артемовск",
    "Ак-Довурак",
    "Александровск",
    "Анива",
    "Анадырь",
    "Бабаево",
    "Барабинск",
    "Балашов",
    "Батайск",
    "Балабаново",
    "Балахна",
    "Балашиха",
    "Брянск",
    "Балтийск",
    "Березники",
    "Бологое",
    "Бежецк",
    "Белая-Калитва",
    "Беслан",
    "Благовещенск",
    "Бердск",
    "Белоярский",
    "Братск",
    "Бобров",
    "Белгород",
    "Березовский",
    "Баксан",
    "Боровичи",
    "Белебей",
    "Бирск",
    "Барнаул",
    "Большой-Камень",
    "Белово",
    "Благовещенск",
    "Биробиджан",
    "Бор",
    "Белогорск",
    "Благодарный",
    "Богородицк",
    "Борзя",
    "Белорецк",
    "Богданович",
    "Борисоглебск",
    "Бийск",
    "Белореченск",
    "Бугульма",
    "Буденновск",
    "Буй",
    "Бутурлиновка",
    "Бугуруслан",
    "Бузулук",
    "Буйнакск",
    "Бавлы",
    "Белокуриха",
    "Буинск",
    "Белозерский",
    "Баймак",
    "Бикин",
    "Болотное",
    "Багратионовск",
    "Бакал",
    "Боготол",
    "Бородино",
    "Богучар",
    "Балаково",
    "Бодайбо",
    "Бронницы",
    "Беломорск",
    "Барыш",
    "Бокситогорск",
    "Боровск",
    "Бирюч",
    "Белый",
    "Белоусово",
    "Болхов",
    "Болохово",
    "Белев",
    "Белая-Холуница",
    "Богородск",
    "Болгар",
    "Белинский",
    "Бахчисарай",
    "Белогорск",
    "Балей",
    "Байкальск",
    "Бабушкин",
    "Билибино",
    "Бирюсинск",
    "Белоозерский",
    "Валуйках",
    "Великий-Новгород",
    "Видное",
    "Валдай",
    "Великие-Луки",
    "Вельск",
    "Воркута",
    "Верещагино",
    "Великий-Устюг",
    "Верхний-Уфалей",
    "Вольск",
    "Владивосток",
    "Верхняя-Салда",
    "Верхняя-Пышма",
    "Воронеж",
    "Владикавказ",
    "Волхов",
    "Вичуга",
    "Всеволожск",
    "Владимир",
    "Вязники",
    "Вилючинск",
    "Воткинск",
    "Воскресенск",
    "Вятские-Поляны",
    "Волоколамск",
    "Волгореченск",
    "Волгоград",
    "Вязьма",
    "Волжск",
    "Выборг",
    "Волгодонск",
    "Выкса",
    "Волжский",
    "Вышний",
    "Волочек",
    "Вологда",
    "Высоковск",
    "Весьегонск",
    "Вытегра",
    "Волосово",
    "Высоцк",
    "Велиж",
    "Венев",
    "Вуктыл",
    "Ветлуга",
    "Володарск",
    "Ворсма",
    "Верхний",
    "Тагил",
    "Верхотурье",
    "Волчанск",
    "Верхнеуральск",
    "Вихоревка",
    "Вяземский",
    "Верхняя-Тура",
    "Верхоянск",
    "Вилюйск",
    "Верея",
    "Гагарин",
    "Губаха",
    "Гай",
    "Голицыно",
    "Гатчина",
    "Губкинский",
    "Галич",
    "Гуково",
    "Глазов",
    "Губкин",
    "Гаврилов-Ям",
    "Горно-АлтайскГородец",
    "Гулькевичи",
    "Гороховец",
    "Грозный",
    "Горячий",
    "Гусь-Хрустальный",
    "Геленджик",
    "Гудермес",
    "Грязь",
    "Гурьевск",
    "Георгиевск",
    "Гусев",
    "Грязовец",
    "Гусиноозерск",
    "Гаджиево",
    "Гдов",
    "Гвардейск",
    "Гурьевск",
    "Гаврилов",
    "Грайворон",
    "Горбатов",
    "Горнозаводск",
    "Гремячинск",
    "Городовиковск",
    "Дальнегорск",
    "Дубна",
    "Дальнереченск",
    "Данков",
    "Дедовск",
    "Дюртюли",
    "Дагестан",
    "Огни",
    "Димитровград",
    "Дзержинский",
    "Дзержинск",
    "Дербент",
    "Дмитров",
    "Дивногорск",
    "Домодедово",
    "Десногорск",
    "Долгопрудный",
    "Добрянка",
    "Донецк",
    "Дудинка",
    "Дятьково",
    "Донской",
    "Давлеканово",
    "Дубовка",
    "Данилов",
    "Дрезна",
    "Демидов",
    "Дмитровск",
    "Дмитриев",
    "Дорогобуж",
    "Духовщина",
    "Джанкой",
    "Далматово",
    "Долинск",
    "Дигора",
    "Дегтярск",
    "Егорьевск",
    "Ершов",
    "Ефремов",
    "Ейск",
    "Елизово",
    "Ессентуки",
    "Елабуга",
    "Еманжелинск",
    "Екатеринбург",
    "Енисейск",
    "Евпатория",
    "Ельня",
    "Елец",
    "Ермолино",
    "Эмва",
    "Железногорск",
    "Железногорск-Илимский",
    "Жигулевск",
    "Железноводск",
    "Жердевка",
    "Жуковка",
    "Жирновск",
    "Жуковский",
    "Жиздра",
    "Жуков",
    "Заволжье",
    "Златоуст",
    "Заводоуковск",
    "Заполярный",
    "Заинск",
    "Знаменск",
    "Зарайск",
    "Заволжск",
    "Заречный",
    "Западная",
    "Двина",
    "Зверево",
    "Звенигород",
    "Заринск",
    "Заозерск",
    "Зеленогорск",
    "Звенигово",
    "Зеленодольск",
    "Зуевка",
    "Зерноград",
    "Зеленоградск",
    "Зеленокумск",
    "Злынка",
    "Змеиногорск",
    "Заречный",
    "Зея",
    "Задонск",
    "Зубцова",
    "Зима",
    "Заозёрный",
    "Закаменск",
    "Зеленогорск",
    "Зеленоград",
    "Завитинск",
    "Ивантеевка",
    "Ивангород",
    "Игарка",
    "Ивдель",
    "Иваново",
    "ИжевскОбильная",
    "Инза",
    "Инта",
    "Ипатово",
    "Избербаш",
    "Ирбит",
    "Исилькул",
    "Иланский",
    "Истра",
    "Искитим",
    "Иркутск",
    "Ишим",
    "Инсар",
    "Иннополис",
    "Инкерман",
    "Ишимбай",
    "Йошкар-Ола",
    "Каменка",
    "Камышлов",
    "Казань",
    "Карталы",
    "Калач-на-Дону",
    "Калачинск",
    "Кадников",
    "Киров",
    "Кандалакша",
    "Калач",
    "Калининград",
    "Карабулак",
    "Касимов",
    "Калининск",
    "Комсомольск",
    "Качканар",
    "Катайск",
    "Курлово",
    "Калтан",
    "Кашин",
    "Курган",
    "Калуга",
    "Каменск-Уральский",
    "Кириши",
    "Красный",
    "Сулин",
    "Калязин",
    "Камешково",
    "Ковров",
    "Курганинск",
    "Каменногорск",
    "Каменск-Шахтинский",
    "Когалым",
    "Курчатов",
    "Каргополь",
    "Камышин",
    "Коломна",
    "Кудымкар",
    "Кемерово",
    "Канаш",
    "Коммунар",
    "Кузнецк",
    "Кемь",
    "Костерево",
    "Кодинск",
    "Куйбышев",
    "Кимры",
    "Канск",
    "Конаково",
    "Кулебаки",
    "Короча",
    "Карабаш",
    "Козельск",
    "Кумертау",
    "Красное",
    "Карабаново",
    "Копейск",
    "Кунгур",
    "Кронштадт",
    "Карасук",
    "Козьмодемьянск",
    "Курск",
    "Кизел",
    "Карачев",
    "Коряжма",
    "Кушва",
    "Кизилюрт",
    "КарпинскКола",
    "Кувандык",
    "Кизляр",
    "Каспийск",
    "Костомукша",
    "Кропоткин",
    "Краснознаменск",
    "Касли",
    "Кострома",
    "Крымск",
    "Красавино",
    "Катав-Ивановск",
    "Колпашево",
    "Куровское",
    "Кимовск",
    "Кашира",
    "Котельники",
    "Котельниково",
    "Кириллов",
    "Кораблино",
    "Котельнич",
    "Куртамыш",
    "Колпино",
    "Котово",
    "Кондрово",
    "Кстово",
    "Кингисепп",
    "Климовск",
    "Котлас",
    "Куса",
    "Кинель",
    "Клин",
    "Котовск",
    "Кубинка",
    "Кинешма",
    "Клинцы",
    "Красногорск",
    "Краснозаводск",
    "Киреевск",
    "Ковылкино",
    "Краснодар",
    "Кяхта",
    "Киров",
    "Ковдор",
    "Краснознаменск",
    "Красноармейск",
    "Киржач",
    "Кохма",
    "Краснокаменск",
    "Красновишерск",
    "Кировск",
    "Кольчугино",
    "Краснокамск",
    "Краснослободск",
    "Кирово-Чепецк",
    "Кондопога",
    "Красноуральск",
    "Красный",
    "Кут",
    "Кировград",
    "Кореновск",
    "Краснотурьинск",
    "Купино",
    "Киселевск",
    "Коркино",
    "Красноярск",
    "Кызыл",
    "Кисловодск",
    "Королев",
    "Красноуфимск",
    "Кыштым",
    "Константиновск",
    "Корсаков",
    "Кременки",
    "Кологрив",
    "Красный",
    "Холм",
    "Кувшиново",
    "Кирс",
    "Княгинино",
    "Красноармейск",
    "Краснослободск",
    "Камбарка",
    "Козловка",
    "Камызяк",
    "Керчь",
    "Красноперекопск",
    "Киренск",
    "Каргат",
    "Кедровый",
    "Курильск",
    "Кировск",
    "Карачаевск",
    "Кирсанов",
    "Комсомольск-на-Амуре",
    "Кудрово",
    "Курчалой",
    "Кукмор",
    "Лангепас",
    "Лебедянь",
    "Лабинск",
    "Лосино-Петровский",
    "Лабытнанги",
    "Лаишево",
    "Лагань",
    "Ломоносов",
    "Лесной",
    "Ленск",
    "Лермонтов",
    "Лукоянов",
    "Лахденпохья",
    "Лениногорск",
    "Лакинск",
    "Луза",
    "Лесозаводск",
    "Ленинск-Кузнецкий",
    "Ладушкин",
    "Любим",
    "Лесосибирск",
    "Ливны",
    "Липки",
    "Лысково",
    "Луга",
    "Лихославль",
    "Ленинск",
    "Лысьва",
    "Луховицы",
    "Ликино-Дулево",
    "Лобня",
    "Лыткарино",
    "Людиново",
    "Липецк",
    "Лодейное",
    "Поле",
    "Люберцы",
    "Любань",
    "Лиски",
    "Льгов",
    "Лянтор",
    "Малоярославец",
    "Магадан",
    "Махачкала",
    "Майский",
    "Майкоп",
    "Магнитогорск",
    "Мамоново",
    "Малгобек",
    "Мариинск",
    "Мантурово",
    "Медвежьегорск",
    "Малая-Вишера",
    "Маркс",
    "Медногорск",
    "Межгорье",
    "Мамадыш",
    "Мегион",
    "Междуреченск",
    "Миасс",
    "Медынь",
    "Менделеевск",
    "Мелеуз",
    "Малмыж",
    "Меленки",
    "Мирный",
    "Миллерово",
    "Михайлов",
    "Мензелинск",
    "Могоча",
    "Микунь",
    "Морозовск",
    "МещовскМожга",
    "Макушино",
    "Моршанск",
    "Мглин",
    "Можайск",
    "Минеральные",
    "Воды",
    "Мариинский",
    "Посад",
    "Макарьев",
    "Малоархангельск",
    "Минусинск",
    "Москва",
    "Мценск",
    "Моздок",
    "Михайловск",
    "Миньяр",
    "Мураши",
    "Московский",
    "Мичуринск",
    "Муравленко",
    "Мыски",
    "Мончегорск",
    "Михайловка",
    "Мурманск",
    "Мытищи",
    "Мосальск",
    "Михайловск",
    "Муром",
    "Мышкин",
    "Макаров",
    "Мезень",
    "Мирный",
    "Магас",
    "Мурино",
    "Надым",
    "Назрань",
    "Набережные",
    "Челны",
    "Невинномысск",
    "Нарьян-Мар",
    "Находка",
    "Назарово",
    "Нариманов",
    "Нефтеюганск",
    "Невьянск",
    "Нальчик",
    "Нелидово",
    "Новоалександровск",
    "Невель",
    "Наро-Фоминск",
    "Неман",
    "Новоалтайск",
    "Нефтекумск",
    "Нарткала",
    "Нерехта",
    "Нововоронеж",
    "Нестеров",
    "Навашино",
    "Нерюнгри",
    "Новозыбков",
    "Наволоки",
    "Новоульяновск",
    "Нерчинск",
    "Новодвинск",
    "Нея",
    "Новоузенск",
    "Нефтегорск",
    "Новокубанск",
    "Нижневартовск",
    "Новая-Ляля",
    "Нефтекамск",
    "Новокузнецк",
    "Нижнеудинск",
    "Новоаннинский",
    "Называевск",
    "Новокуйбышевск",
    "Нижнекамск",
    "Новый-Оскол",
    "Николаевск",
    "Новомичуринск",
    "Никольское",
    "Новая",
    "Ладога",
    "Новошахтинск",
    "Новомосковск",
    "Нижний-Ломов",
    "Новоржев",
    "Новый-Уренгой",
    "Новгород",
    "Новосокольники",
    "Ногинск",
    "Тагил",
    "Новохопёрск",
    "Норильск",
    "Новосибирск",
    "Нижние-Серги",
    "Новосиль",
    "Ноябрьск",
    "Новотроицк",
    "Нижняя",
    "Тура",
    "Нолинск",
    "Нюрба",
    "Новоуральск",
    "Нижняя",
    "Салда",
    "Невельск",
    "Нязепетровск",
    "Новочебоксарск",
    "Никольск",
    "Нурлат",
    "Нягань",
    "Октябрьский",
    "Онега",
    "Оленегорск",
    "Обнинск",
    "Оса",
    "Оренбург",
    "Омутнинск",
    "Обь",
    "Осинники",
    "Острогожск",
    "Октябрьск",
    "Обоянь",
    "Остров",
    "Орлов",
    "Омск",
    "Одинцово",
    "Отрадный",
    "Ожерелье",
    "Опочка",
    "Озеры",
    "Отрадное",
    "Оха",
    "Орел",
    "Озерск",
    "Олёкминск",
    "Орехово-Зуево",
    "Озерск",
    "Осташков",
    "Очёр",
    "Орск",
    "Окуловка",
    "Облучье",
    "Оханск",
    "Олонец",
    "Островной",
    "Пенза",
    "Партизанск",
    "Пенза",
    "Павлово",
    "Павловск",
    "Первомайск",
    "Петрозаводск",
    "Павловский",
    "Посад",
    "Плавск",
    "Первоуральск",
    "Печора",
    "Павловск",
    "Пласт",
    "Пересвет",
    "Печоры",
    "Палласовка",
    "Плес",
    "Переславль-Залесский",
    "Пикалево",
    "Пермь",
    "Подпорожье",
    "Петровск",
    "Полысаево",
    "Пестово",
    "Поворино",
    "Пушкино",
    "Похвистнево",
    "Петропавловск-Камчатский",
    "Подольск",
    "Пугачев",
    "Приволжск",
    "Петров-Вал",
    "Покачи",
    "Пыть-Ях",
    "Приморско-Ахтарск",
    "Петровск-Забайкальский",
    "Полевской",
    "Пыталово",
    "Пролетарск",
    "Петушки",
    "Полярные",
    "Зори",
    "Перевоз",
    "Прокопьевск",
    "Пионерский",
    "Полярный",
    "Петергоф",
    "Правдинск",
    "Питкяранта",
    "Поронайск",
    "Пудож",
    "Протвино",
    "Полесск",
    "Пошехонье",
    "Пушкин",
    "Порхов",
    "Псков",
    "Почеп",
    "Пучеж",
    "Прохладный",
    "Приморск",
    "Починок",
    "Петухово",
    "Приозерск",
    "Пущино",
    "Пятигорск",
    "Покровск",
    "Приморск",
    "Пустошка",
    "Певек",
    "Покров",
    "Радужный",
    "Ревда",
    "Райчихинск",
    "Ржев",
    "Рассказово",
    "Реутов",
    "Раменское",
    "Рыльск",
    "Реж",
    "Родники",
    "Рудня",
    "Рыбное",
    "Ртищево",
    "Рославль",
    "Руза",
    "Россошь",
    "Рузаевка",
    "Ростов",
    "Рязань",
    "Ростов-на-Дону",
    "Рубцовск",
    "Рошаль",
    "Ряжск",
    "Рыбинск",
    "Радужный",
    "Салехард",
    "Суджа",
    "Свирск",
    "Сенгилей",
    "Салават",
    "Сосновка",
    "Светлогорск",
    "Саранск",
    "Сурск",
    "Светлоград",
    "Сычевка",
    "Сарапул",
    "Сальск",
    "Светогорск",
    "Славск",
    "Саратов",
    "Самара",
    "Светлый",
    "Скопин",
    "Саров",
    "Санкт-Петербург",
    "Свободный",
    "Славгород",
    "Советск",
    "Сатка",
    "Себеж",
    "Славянск-на-Кубани",
    "Сасово",
    "Советск",
    "Североморск",
    "Сланцы",
    "Сельцо",
    "Старица",
    "Солигалич",
    "Слободской",
    "Судогда",
    "Сафоново",
    "Северобайкальск",
    "Суоярви",
    "Семенов",
    "Спас-Деменск",
    "Северодвинск",
    "Смоленск",
    "Семикаракорск",
    "Суздаль",
    "Североуральск",
    "Снежинск",
    "Семилуки",
    "Саяногорск",
    "Севск",
    "Советск",
    "Сураж",
    "Саянск",
    "Северск",
    "Советский",
    "Сольвычегодск",
    "Старая-Русса",
    "Сегежа",
    "Советская",
    "Гавань",
    "Сергач",
    "Стрежевой",
    "Сердобск",
    "Спас-Клепики",
    "Сергиев",
    "Посад",
    "Сухой-Лог",
    "Серов",
    "Сясьстрой",
    "Сестрорецк",
    "Старая",
    "Купавна",
    "Сертолово",
    "Сокол",
    "Серпухов",
    "Старый",
    "Оскол",
    "Сольцы",
    "Спасск-Рязанский",
    "Сухиничи",
    "Стерлитамак",
    "Сим",
    "Соликамск",
    "Суворов",
    "Строитель",
    "Снежногорск",
    "Солнечногорск",
    "Сибай",
    "Ступино",
    "Спасск-Дальний",
    "Соль-Илецк",
    "Собинка",
    "Сургут",
    "Сосногорск",
    "Сортавала",
    "Сосенский",
    "Суровикино",
    "Сочи",
    "Сорочинск",
    "Сызрань",
    "Струнино",
    "Среднеуральск",
    "Сосновоборск",
    "Сыктывкар",
    "Стародуб",
    "Ставрополь",
    "Сосновый",
    "Бор",
    "Сысерть",
    "Серафимович",
    "Слюдянка",
    "Саки",
    "Старый",
    "Крым",
    "Симферополь",
    "Судак",
    "Севастополь",
    "Сретенск",
    "Салаир",
    "Сковородино",
    "Сорск",
    "Среднеколымск",
    "Северо-Курильск",
    "Спасск",
    "Сусуман",
    "Сунжа",
    "Тавда",
    "Тайга",
    "Таштагол",
    "Талдом",
    "Таганрог",
    "Тамбов",
    "Талица",
    "Тайшет",
    "Тара",
    "Таруса",
    "Татарск",
    "Тарко-Сале",
    "Тверь",
    "Теберда",
    "Темрюк",
    "Трехгорный",
    "Темников",
    "Томари",
    "Тобольск",
    "Трубчевск",
    "Тейково",
    "Тогучин",
    "Торжок",
    "Троицк",
    "Терек",
    "Тольятти",
    "Топки",
    "Туапсе",
    "Тетюши",
    "Томск",
    "Тосно",
    "Тулун",
    "Тимашевск",
    "Торопец",
    "Тутаев",
    "Тихвин",
    "Тотьма",
    "Троицк",
    "Туймазы",
    "Тихорецк",
    "Томмот",
    "Туран",
    "Тула",
    "Тында",
    "Тюкалинск",
    "Туринск",
    "Тюмень",
    "Тырныауз",
    "Углич",
    "Ужур",
    "Урень",
    "УярУрай",
    "Урус-Мартан",
    "Уварово",
    "Уржум",
    "Урюпинск",
    "Усть-Джегута",
    "Удачный",
    "Улан-Удэ",
    "Усинск",
    "Усть-Илимск",
    "Удомля",
    "Устюжна",
    "Усть-Кут",
    "Учалы",
    "Усмань",
    "Ульяновск",
    "Усть-Лабинск",
    "Усть-Катав",
    "Узловая",
    "Унеча",
    "Усолье-Сибирское",
    "Уфа",
    "Ухта",
    "Уссурийск",
    "Фокино",
    "Фокино",
    "Фатеж",
    "Фролово",
    "Феодосия",
    "Фрязино",
    "Фурманов",
    "Хадыженск",
    "Хасавюрт",
    "Харовск",
    "Ханты-Мансийск",
    "Хабаровск",
    "Харабали",
    "Холмск",
    "Хвалынск",
    "Холм",
    "Хотьково",
    "Химки",
    "Хилок",
    "Цивильск",
    "Циолковский",
    "Цимлянск",
    "Чебаркуль",
    "Чайковский",
    "Чаплыгин",
    "Чебоксары",
    "Чапаевск",
    "Чегем",
    "Черноголовка",
    "Челябинск",
    "Черемхово",
    "Чекалин",
    "Черногорск",
    "Чёрмоз",
    "Чернушка",
    "Череповец",
    "Черкесск",
    "Чердынь",
    "Чехов",
    "Черняховск",
    "Чита",
    "Черепаново",
    "Чудово",
    "Чусовой",
    "Чистополь",
    "Чкаловск",
    "Чухлома",
    "Чулым",
    "Чадан",
    "Шарыпово",
    "Шали",
    "Шадринск",
    "Шахтерск",
    "Шагонар",
    "Шатура",
    "Шарья",
    "Шахты",
    "Шахунья",
    "Шелехов",
    "Шебекино",
    "Шацк",
    "Шенкурск",
    "Шилка",
    "Шимановск",
    "Шумерля",
    "Шлиссельбург",
    "Шиханы",
    "Шуя",
    "Шумиха",
    "Щекино",
    "Щербинка",
    "Щелкино",
    "Щелково",
    "Щигры",
    "Щучье",
    "Электрогорск",
    "Электросталь",
    "Электроугли",
    "Энгельс",
    "Элиста",
    "Эртиль",
    "Югорск",
    "Юбилейный",
    "Южа",
    "Южно-Сахалинск",
    "Южноуральск",
    "Юрга",
    "Юрьевец",
    "Юрьев-Польский",
    "Южно-Сухокумск",
    "Юрюзань",
    "Юхнов",
    "Ялуторовск",
    "Ялта",
    "Ядрин",
    "Янаул",
    "Ярославль",
    "Яранск",
    "Якутск",
    "Яровое",
    "Ярцево",
    "Ясногорск",
    "Ясный"]

    last=[]

    if len(cities) > 0:
        city=str(a.capitalize())
        add_city=[]
        expand=[]
        if last == [] or last[-1] == city[0].upper():
            if city in cities:
                cities.remove(city)
                if city[-1] == 'ь':
                    add_city.append(city.upper())
                    expand.extend(add_city[0])
                    last.append(expand[-2])
                    add_city.clear()
                    expand.clear()
                else:
                    add_city.append(city.upper())
                    expand.extend(add_city[0])
                    last.append(expand[-1])
                    add_city.clear()
                    expand.clear()
                if len(cities) > 0:
                    for i in range(len(cities)):       
                        if cities[i].find(last[-1]) == 0:
                            return f'{cities[i]}'
                            if cities[i][-1] == 'ь':
                                add_city.append(cities[i].upper())
                                expand.extend(add_city[0])
                                last.append(expand[-2])
                                cities.remove(cities[i].lower().capitalize())
                                add_city.clear()
                                expand.clear()
                                break
                            else:
                                add_city.append(cities[i].upper())
                                expand.extend(add_city[0])
                                last.append(expand[-1])
                                cities.remove(cities[i].lower().capitalize())
                                add_city.clear()
                                expand.clear()
                                break
                else:
                    return 'Вы победили!'   
            else:
                return 'Нет такого города!'
        else:
            return f'Ваш город начинаеться на  {last[-1]}'
    else:
        return 'Вы проиграли!'

eel.init("web")
eel.start("main.html", host= "citiesgame.tk" , port=0,  size=(1080,720))