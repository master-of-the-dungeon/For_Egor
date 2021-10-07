

init:
#  Декорации

    image bg forest_1 = "L1.png"
    #image _fn_ = Image("messenger/fone1.png",  xalign = 0.5, yalign = 0.5)

    image _fn_ = Image("messenger/fone1.png")


define sdx = Character("sDextra")




label start:

# Здесь задается положение телефона
    $ x_al_fone = 0.5
    $ y_al_fone = 0.5

# Тестовый массив
    #$ _pers_ = [1,2,3,4,5,6]

# Рабочий массив. Персонажи добавляются по мере поступления в произвольном порядке по сюжету.
    $ _pers_ = []

    # Это флаговый список. Используется функцией добавления персонажей для предотвращения добавления дублей.
    $ EnablePers = [False, False, False, False, False, False,
                    False, False, False, False, False, False,]


# Пример заполнения списка
    $ add_pers(3)
    $ add_pers(4)
    $ add_pers(1)
    $ add_pers(4)   # <= Не может быть добавлен. Дубль
    $ add_pers(14)  # <= Не может быть добавлен. Превышен номер

    scene bg forest_1 with dissolve

    $ gg_name = "Username" # Имя пользователя телефона
    $ m_msg = [] # Список сообщений чата

    $ msg_name = "Матроскин" # Имя собеседника в чате.
    window hide

    $ nmr = 0
    $ hint_ = False # Это блокировка хинта при запуске статистики. Управляется автоматически скриптом. Не трогать!
    $ hint_enable = True # <= Это возможность отображаить хинты. Устаналивается программистом.

    "Включил телефон"
    # Вызов телефона
    call fone_

return


label fone_:



#    NB! Это рисунок телефона.
#   Отображается как накладка на фон
#   И не зависит от экрана
#   Для закрытия телефона необходимо стереть и эту накладку тоже.
#    hide screen telegram
#    hide _fn_
#    with dissolve
    show _fn_:
        xalign x_al_fone
        yalign y_al_fone
    #with dissolve
#=================================================


label fon:



    call screen telegram with dissolve
    with None

    $ result = _return

    if result == 101:
        jump dlg_

    if result == 102:
        $ nmr = 2

    if (result > 200) and (result < 300) :

        $ pic_ = result - 200
        $ nmr = 3


    jump fon
#return

label dlg_:
    $ nmr = 1
    show screen telegram
    #call screen telegram with dissolve
    pause

    python:
        msg("Здравствуй, [gg_name] \nКак у тебя дела?", who=True)
        msg("Привет, всё хорошо, а как у тебя?")



    "Тест телефона"
    pause

    python:
        msg("Пока.")
        msg("Пока.",who=True)


    $ nmr = 0
    show screen telegram
    stop sound fadeout 1
    "Я покинул чат."

# NB! Закрытие телефона. Стираем и экран и накладку с рисунком телефона
    hide screen telegram
    hide _fn_
    with dissolve
#=========================================================================
    "И выключил телефон"



#    return
