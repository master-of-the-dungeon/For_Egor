#################################################################################
### Telegram Messenger
#################################################################################
init python:


    ### Цветовая схема
    style_button_back = "#282E33"
    style_button_hovr = "#5F6C77"
    style_button_inst = "#14171A"

    # Стиль кнопок
    style.btn = Style(style.default)
    style.btn.background = style_button_back
    style.btn.hover_background = style_button_hovr
    style.btn.insensitive_background = style_button_inst



    # Стиль ползунка
    style.bar_vert = Style(style.default)
    style.bar_vert.right_bar = style_button_inst
    style.bar_vert.left_bar = style_button_inst
    style.bar_vert.thumb = style_button_hovr
    style.bar_vert.bar_vertical = True
    style.bar_vert.bar_invert = True
    #style.bar_vert.xalign = 1.0
    #style.bar_vert.yalign = 0.6
    #style.bar_vert.xalign = 0.9
    style.bar_vert.xpos = 344
    style.bar_vert.ypos = 100
    style.bar_vert.xsize = 8
    style.bar_vert.ysize = 428


    # Стиль текста
    style.txt_base = Style(style.default)
    style.txt_base.font = "gui/tahoma.ttf"
    style.txt_base.xalign = 0.5
    style.txt_base.yalign = 0.5
    style.txt_base.size = 18
    style.txt_base.color = "#fff"


    style.tooltipping = Style(style.default)
    style.tooltipping.xalign = 0.5 #Где по оси x будет появляться подсказка
    style.tooltipping.yalign = 0.02 #По y
    style.tooltipping.color= "#111111"#цвет шрифта

    yadj = ui.adjustment()
    # Добавление нового сообщения
    def msg(txt, who=False, sound=False):
        store.m_msg.append((who, txt, sound))
        store.yadj.value = store.yadj.range+300
        renpy.restart_interaction()
        if who:
            renpy.play("new_message.mp3", "sound")
        renpy.pause()
    # Удаление последнего сообщения
    def del_last_msg():
        if len(store.m_msg) > 0:
            del store.m_msg[-1]
    # Удаление всех сообщений
    def del_all_msg():
        store.m_msg = []


#================================================================================
# Функции работы с статистикой
    # Добавление нового перонажа
    def add_pers(_p_):
        fl = False
        if _p_ < 12:
            if EnablePers[_p_-1]:
                # Персонаж уже существует
                fl = True
            else:
                # Иначе добавить
                _pers_.append(_p_)
                EnablePers[_p_-1] = True

        return fl

#################################################################################
# Экран сообщения
screen telegram():



    $ Inf = ("{size=15}{b}Бомж{/b}\n{size=13}Осведомитель",
             "{size=15}{b}Мяско{/b}\n{size=13}Маньяк потрошитель",
             "{size=15}{b}Нуканука{/b}\n{size=13}Сутёнер",
             "{size=15}{b}Манька Облигация{/b}\n{size=13}Дворовая шлюха",
             "{size=15}{b}Мадам Мандавошь{/b}\n{size=13}Золотая проститутка\n{size=10}(берёт золотом)",
             "{size=15}{b}Стерва{/b}\n{size=13}Стерва и в Африке стерва",)

    #frame background "messenger/back.png" xysize (600,975) align (0.9,.5):
    #frame background "messenger/fone1.png" xysize (400,720) align (0.5,0.5):



    frame background None xysize (400,720) align (x_al_fone, y_al_fone):
        xpadding 0
        ypadding 0
        #frame background None xysize (560, 810) align (0.5,0.58):
        #frame background None xysize (356, 548) pos (24,82):
        frame background None xysize (356, 528) pos (25,90):
            xpadding 0
            ypadding 0


            if nmr == 0:

                imagemap:
                    ##Кнопки в исходном состоянии
                    ground None
                    idle "1_2.png"
                    ##Кнопки в активном состоянии
                    hover "1_1.png"
                    alpha True
                    hotspot (13, 13, 52, 54) action Return(101)
                    hotspot (13, 73, 52, 54) action Return(102)
                    hotspot (13, 133, 52, 54) action Return(101)
                    hotspot (13, 193, 52, 54) action Return(101)



            elif nmr == 1:
                viewport id "vp_msg" mousewheel True   yadjustment yadj:
                    ypos 104
                    xsize 352
                    ysize 428


                    #vbox spacing 15 xsize 550 xalign 0.4 box_reverse True:
                    #vbox spacing 15 xsize 356 xpos 18 box_reverse True:
                    vbox spacing 15 xsize 356 xpos 0 box_reverse True:
                        for message in m_msg[::-1]:
                            $ who, txt, sound = message
                            $ xgn = 0.15 if who else 0.79
                            if sound:
                                imagebutton auto "messenger/sound_%s.png" xalign xgn action Play("sound", sound)
                            else:
                                #button xalign xgn xmaximum 580 xpadding 20 ypadding 10 background Frame("messenger/box.png", 25, 25):
                                button xalign xgn xmaximum 390 xpadding 20 ypadding 10 background Frame("messenger/box.png", 25, 25):
                                    text "%s"%(txt) style "txt_base"


                # Имя собеседника
                text "%s"%(msg_name) style "txt_base" size 35 xalign 0.31 xanchor 0.0 yalign 0.04
                # Аватарка собеседника
                add "messenger/av/"+msg_name.lower().replace(' ', '_')+".png" pos (5,5)
                # Стрелка
                #imagebutton auto "messenger/arr_%s.png" pos (10, 33) action NullAction()
                # Стереть сообщения
                #button background style_button_inst hover_background style_button_hovr xalign 0.99 yalign 0.03 action Function(del_all_msg) xysize (60,60):
                #    text "  x  " style "txt_base" size 40 pos (36, -2)
                # Ползунок прокрутки
                vbar value YScrollValue("vp_msg") style "bar_vert"

                imagebutton:
                    idle "images/Stat/i_exit2.png"
                    hover "images/Stat/h_exit2.png"
                    xsize 30  # Ширина кнопки
                    ysize 30  # Высота кнопки
                    xalign 0.980
                    yalign 0.002


                    action NullAction()
                    #action [SetVariable("nmr", 0), Return()]



            # Вывод статитистической информации
            elif nmr == 2:


#================================================================================
# Подсчет отображаемых слотов
#================================================================================

                $ step_ = len(_pers_)
                if step_ > 12:
                    $ step_ = 12
#================================================================================
# Демонстрационный блок, отображает только 6 слотов
# В рабочем состоянии эту строку задокуметировать или стереть
#================================================================================
                #$ step_ = 6
#================================================================================

                #Количество слотов по ширине и высоте
                $ x_len = 3
                $ y_len = 4

                $ slot_cnt =  x_len * y_len  # Количество слотов на странице


                $ wp = 100 # Ширина картинки
                $ hp = 120 # Высота картинки

                $ l_os = 0 # левое смещение
                $ x_os = 10 # Отступ картинки по x
                $ y_os = 6 # Отступ картинки по y

                # Смещения блока кнопок
                $ os_x = 18
                $ os_y = 38

                for i in range(step_ ):

                    #if i < slot_cnt:
                    #Текущий слот
                    $ x_slot = i % x_len
                    $ y_slot = int(i / x_len)

                    $ x_pos_slot = x_slot * (wp + x_os) + os_x
                    $ y_pos_slot = y_slot * (hp + y_os) + os_y


#================================================================================
# Пассивный слот
#================================================================================

#================================================================================
#                   NB! Здесь получаем пoследовательный номер персонажа

                    $ cor = i % 6
                    # Это тестовая строка для предотвращения отображения более 6 персонажей.
                    # Заменить на следующую строку
                    # $ cor = i

                    $ n_pers = _pers_[cor] - 1 # Нумерация начинается с нуля!

                    #$ pos_pict = i + (pg * slot_cnt) # Номер текущего слота
                    $ www = "images/Stat/i" + str(n_pers + 1) + ".jpg"
                    imagebutton:
                        idle www
                        xsize wp + 2  # Ширина кнопки
                        ysize hp + 2   # Высота кнопки
                        xpos  x_pos_slot + 2
                        ypos  y_pos_slot + 2

                        action NullAction()

#================================================================================
# Активная накладка
#================================================================================

                    imagebutton:
                        idle "images/Stat/ram_i.png"
                        hover "images/Stat/ram.png"
                        xsize wp  # Ширина кнопки
                        ysize hp   # Высота кнопки
                        xpos  x_pos_slot + 2
                        ypos  y_pos_slot + 2
#================================================================================

#================================================================================
# Если hint не нужен, задокументировать или стереь этот блок
#================================================================================
                        if hint_enable:
                            hovered [SetVariable("hint_", True), SetVariable("_y_", y_pos_slot), SetVariable("_x_", x_pos_slot), SetVariable("g_x", x_slot), SetVariable("g_y", y_slot), SetVariable("nmm_", n_pers)]
                            unhovered SetVariable("hint_", False)
#================================================================================

                        action Return(201+ n_pers)


#================================================================================
# Для возможности отображения всех слотов этот блок стереть
#================================================================================
                if step_ < 7:
                    button:
                        xsize 300  # Ширина кнопки
                        ysize 100   # Высота кнопки

                        xalign 0.5
                        ypos  400
                        yalign 1
                        text  "Далее следует\nспецконтент.\nВозрастной ценз 1000+"  size 28 outlines [(2,"#999",0,0)] text_align 0.5

                        action NullAction()

#================================================================================


#================================================================================
# Если hint не нужен, достаточно отключть этот блок в кнопке
#================================================================================
                # Отображение hint
                if hint_:
                    $ ttttt = Inf[nmm_]
                    button:
                        background "images/Stat/ar1_.png"
                        xsize 120 # Ширина кнопки
                        ysize 120   # Высота кнопки

                        xpos _x_ + (wp/2) - (120/2)

                        #========================================================
                        # Это последняя строка. Hint уходит за пределы экрана
                        # Поэтому в последней строке он отображается сверху.
                        #========================================================
                        if g_y == 3:
                            background "images/Stat/ar2_.png"
                            ypadding 0
                            ypos  _y_ - hp + 2
                        else:
                            background "images/Stat/ar1_.png"
                            ypadding 50
                            ypos  _y_ +  hp + 2

                        # Отладка. Блочные координаты хинтов
                        #text  "[g_x] [g_y]"  size 14 outlines [(2,"#999",0,0)] text_align 0.5

                        #text  "[ttttt]"  size 16 outlines [(1,"#100",0,0)] xalign 0.5  text_align 0.5
                        text  "[ttttt]" color "#000000"  xalign 0.5 yalign 0.5  text_align 0.5

                        action NullAction()
#================================================================================
# Это кнопка выхода. Из-за всяких глюков сделана с подложкой
#================================================================================
                button:
                    xsize 32  # Ширина кнопки
                    ysize 32  # Высота кнопки
                    xalign 0.99
                    yalign 0.0
                    action NullAction()
                    imagebutton:
                        idle "images/Stat/i_exit2.png"
                        hover "images/Stat/h_exit2.png"
                        xsize 30  # Ширина кнопки
                        ysize 30  # Высота кнопки
                        xalign 0.5
                        yalign 0.5
                        action [SetVariable("nmr", 0), Return()]




#================================================================================
            elif nmr == 3:

                $ www = "images/Stat/p" + str(pic_) + ".jpg"
                button:
                    background www
                    xsize 350  # Ширина кнопки
                    ysize 520   # Высота кнопки

                    xalign 0.5
                    yalign 0.5

                    action NullAction()

                imagebutton:
                    idle "images/Stat/i_exit2.png"
                    hover "images/Stat/h_exit2.png"
                    xsize 30  # Ширина кнопки
                    ysize 30  # Высота кнопки
                    xalign 0.99
                    yalign 0.0
                    action [SetVariable("nmr", 2), Return()]
