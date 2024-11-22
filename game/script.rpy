# Вы можете расположить сценарий своей игры в этом файле.
init:
    # Эффект закрывания и открывания глаз
    $ circleirisout = ImageDissolve("eye.png", 1.0, 8)
    $ circleirisin = ImageDissolve("eye.png", 1.0, 8, reverse=True)
    $ renpy.music.register_channel('bg_sound', loop=False)

    # Трансофрмация для текста титров
    transform txt_up:
        yalign 1.9
        linear 15.0 yalign 0.05

    transform image_up(deff, x):
        xalign x
        yalign 3.9
        linear (30.0-deff) yalign -1.6 

    # Вотсановление отката
    define config.rollback_enabled = True
    $ renpy.fix_rollback()

    # Отключенияе автосохранений
    $ config.has_autosave = False
    $ config.autosave_frequency = None

    python:
        def naomi_voice(event, interact=True, **kwargs):
            if not interact:
                return

            if event == "show_done":
                renpy.sound.play("voice.mp3", loop=True)
            elif event == "slow_done":
                renpy.sound.stop()

        def autosave():
            if not renpy.game.after_rollback: 
                save_arr = renpy.list_slots()
                if len(save_arr) != 0:
                    last_slot = save_arr[-1]
                    if last_slot[-1] == '6':
                        next_slot = str(int(last_slot[0])+1)+'-1'
                    else:
                        next_slot = last_slot[0]+'-'+str(int(last_slot[-1])+1)
                else:
                    next_slot = '1-1'
                renpy.take_screenshot()
                renpy.save(next_slot, extra_info='saved_from_the_code')
        
# Определение персонажей игры.
define n = Character ('Наоми', who_color='#551010', what_color='#a0a0a0', image='naomi', callback=naomi_voice)

# Определяем переход с долгой тряской
define vpunch3 = Move ((0, 10), (0, -10),.10, bounce=True, repeat=True, delay=.275*5) 

#Перменная для запоминания выбрал ли игрок умереть в первом меню выбора
define no_choice_death = True

# Игра начинается здесь:
label start:
    show text '{color=#f60104}{size=96}Внимание!{/size}{/color}{p}{p}{color=#cfcfcf}Эта игра содержит сцены с кровью, самоувечьями и суицидом. В связи с этим настоятельно не рекомендуем к прохождению данную визуальную новеллу: детям, беременным женщинам, людям с тонкой душевной организацией или с проблемами сердечно-сосудестой системы, а также тем кому воспрещается подобный контент из-за их религиозной, политичесокй или философской позиции. Мы не несём цели кого-либо оскорбить, наш материал носит сугубо развлекательный характер.{p}{p}Приятного прохождения!{/color}'
    $ renpy.pause(20.0, hard=True)
    jump credits
    return

# Акт 1
label act1:
    scene black with fade
    pause 1.0
    scene bg room with fade
    show naomi normal

    n '''
    {cps=15}Cегодня был довольно тяжёлый день…{/cps}{w}
    {cps=15}первый день в новой школе, {/cps}{w=0.5}
    {cps=15}я даже смог познакомиться с кем-то,{/cps}

    {cps=15}они позвали меня на прогулку, но я не думаю,{/cps}{w}
    {cps=15} что моё самочувствие позволяет выйти сегодня куда-то{/cps}
    '''

    play sound knock
    pause 1.0

    n excited '{cps=15}А? Кто это может быть...{/cps}'

    scene bg door with dissolve

    narrator 'Парень медленно направился к двери, надеясь, что стучавший человек просто ошибся дверью.' 

    scene bg hallway with fade

    narrator 'На пороге никого не было, лишь одинокая записка лежала на полу.'
    
    scene bg note with dissolve
    
    n '''
    {cps=15}Записка....{w}может это у них тут почта такая?{w} Хотя кто может писать мне{/cps}

    {cps=15}"Привет, ты не знаешь меня, но я знаю тебя...{w}Наоми…{w}ну как тебе новая школа? Новое место? Оправился после случившегося? Или всё не можешь забыть своих ошибок?{/cps}"
    '''
    n @annoyed '{cps=15}Это…{w=1}это шутка?{w=0.5} Может, одноклассники так прикалываются...{/cps}'

    menu:
        'Мне стоит сдохнуть':
            n '{cps=15}мне стоит сдо...{w=1.5}....{p=3.5}…я{w=2}...я ведь не это хотел сказать...{/cps}'
            $ no_choice_death = False
            jump act2
        'Mне стоит пойти спать':
            n '{cps=15}Лучше я пойду посплю...{/cps}'
            jump act2

    return

# Акт 2
label act2:
    scene black with fade
    pause 1.0
    play bg_sound alarm_clock volume 0.5
    scene electronic_clock with fade

    pause 3
    stop bg_sound fadeout 0.6

    scene bg room with dissolve
    show naomi ill

    n '{cps=15}Сегодня мне хуже, чем вчера лучше я останусь дома...{/cps}'

    play sound knock
    pause 1.0

    n excited '{cps=15}Что? Кому есть дело до меня в такую рань…{cps=15}'

    # Автосохранение
    $ autosave()

    scene bg door with fade

    narrator 'Его нахлынуло беспокойство, и, шурша ногами по полу, он вновь подошёл к двери. Перед тем как её открыть, Наоми сильно зажмурился, боясь увидеть то, что находится за дверью.'

    scene black with circleirisin

    pause 0.5

    scene bg hallway with circleirisout

    narrator '.{w=0.3}.{w=0.3}.{w=0.3}тишина{w} .{w=0.3}.{w=0.3}.{w=0.3}никого нет кроме{w}.{w=0.3}.{w=0.3}.{w=0.3} записки.'

    scene bg note with fade

    n '{cps=10}Опять?.......{w}это уже не смешно......{cps=10}'
    n '{cps=25}Ты всё ещё общаешься с родителями? Или они до сих пор ненавидят тебя за твой поступок.{/cps}{w=1}{nw}' 

    scene bg room 

    show naomi ill with vpunch3

    narrator 'Наоми выкинул бумажку и резко отошёл от двери. Голова стала страшно болеть, схватившись за неё, парень стал ходить из стороны в сторону.'

    n ill '{cps=15}Что-то меня тошнит...{w}пойду я лучше прогуляюсь…{w=1.5}или нет…{w=1.5}а вдруг тот, кто пишет это, хочет, чтобы я вышел?{/cps}'

    n '{cps=15}А вдруг из психушки сбежал маньяк… {w}но откуда он знает обо мне, что...{w}...{w}{/cps}{nw}' 
    extend normal'{cps=15}Нужно успокоиться и решить что делать.....{/cps}'

    menu:
        'Идти на улицу':
            jump outdoors
        'Просто покончи с этим':
            jump end_it
    
    return

# Наоми решает пойти на улицу
label outdoors:
    scene bg outdoors with dissolve
    show naomi annoyed at center with moveinright 

    narrator '''
    Наоми, взяв с собой сумку, направился в сторону парка.
    Гуляя по безлюдным местам,{w=2} окутанный серыми мыслями и ощущением безысходности,{w=1.5} парень размышлял о странных записках.{w}
    Кому-то интересна его личная жизнь?
    '''

    show naomi sad 

    narrator 'Тот вопрос о родителях…{w}это была их семейная тайна,{w=1} о которой никто не мог знать... {w}Парень чувствовал, как учащается его пульс и что-то сильное давит в груди. Кажется, он вот-вот расплачется.{w} ...{w}...что?'

    narrator 'Маленькая холодная капля коснулась его головы, стекая по затылку.{w} Мурашки пробежали по коже. {w}Ещё капля...{w}и ещё...'

    n excited '{cps=25}Это что....{w=0.25}дождь!?{/cps}'

    $ flash = Fade(0.1, 0.0, 0.5, color="#fff")
    scene bg rain 
    show naomi scared
    with flash
    play bg_sound rain loop volume 0.25

    narrator '''
    Сердце Наоми забилось так сильно и быстро, что казалось, оно сейчас вырвется из груди. 

    Дыхание стало тяжёлым, коротким и прерывистым. В голове всё поплыло, а перед глазами замелькали тёмные пятна. 

    Паника охватила его, как ледяной водоворот, в который он погружался всё глубже и глубже
    '''

    n '{cps=15}Э..{w=2}этого не может быть....{w=1.5}не может быть дождя....{w=1.5}я смотрел.....{w=1.5}прогноз погоды показывал солнце.....{w=1.5}мне надо...{w=2}надо....{/cps}'

    menu:
        'Умереть':
            jump bad_enging1
        'Умереть':
            jump bad_enging1
        'Умереть':
            jump bad_enging1


    return

# Плохая концовка с самодушением
label bad_enging1:
    stop music fadeout 1
    # stop bg_sound fadeout 0.5
    scene end rain with vpunch3
    play music knife fadein 0.5 loop
    pause 2

    narrator 'Наоми почувствовал, как руки, которые он больше не мог контролировать, сами стали подниматься к шее.{w=3.6} Обхватив холодными руками горло,{w=2.5} пальцы ощутили пульсирующую вену,{w=3} и он закрыл глаза,{w=2} больше не имея власти над своим телом.'

    narrator 'С каждым мгновением его хватка становилась всё сильнее.{w=1.5} Дышать стало невозможно, и Наоми почувствовал,{w=1.5} как подкашиваются его ноги.{w=2.5} Мышцы шеи напряглись до предела,{w=1.5} лёгкие отчаянно пытались захватить воздух,{w=1.5} но это только усиливало хватку.'

    narrator 'Больше он никогда не почувствует прикосновение воды на себе'

    $ renpy.quit()
    return

# Наоми решает покончит с этим
label end_it:
    n excited '{cps=15}что{w=0.1}.{w=0.1}.{w=0.1}.{/cps}'

    if no_choice_death == False:
        $ renpy.block_rollback()
        
    menu:
            'УБЕЙ СЕБЯ.' if no_choice_death:
                n scared '{cps=15}Убей...{/cps}'
                n niger '....себя?{w=0.5}{nw}'
                jump bad_ending2
            'Иногда в мою голову поступают странные мысли.' if no_choice_death:
                n '{cps=15}Иногда в мою голову поступают странные мысли..... {w=1}наверное, я просто слишком нагрузил себя в школе...{/cps}'
                jump act3
            'Остаться дома.' if no_choice_death:
                jump act3

            'Покончи с этим.' if no_choice_death == False:
                n excited '{cps=15}Я...{w=1.5} не должен об этом...{w=1.5}думать...{/cps}'
                jump act3

    return

# Плохая концовка с канцелярским ножом
label bad_ending2:
    stop music fadeout 0.5
    scene end knife
    pause 2

    $ renpy.quit()
    return
    
# Акт 3
label act3:
    scene black with fade
    play bg_sound alarm_clock volume 0.5
    scene electronic_clock with fade
    
    pause 3
    stop bg_sound fadeout 0.6
    
    scene bg room
    show naomi normal

    menu:
        'она умерла':
            n '{cps=5}я знаю{/cps}'
    menu:
        'это все из-за тебя':
            n sad '{cps=15}я знаю{/cps}'
    menu:
        'ты ничтожество':
            n annoyed'{cps=25}ХВАТИТ,{w=0.1} ХВАТИТ ДУМАТЬ ОБ ЭТОМ,{w=0.1} ПРЕКРАТИ,{w=0.1} ПРЕКРАТИ ЭТО ДЕЛАТЬ{/cps}'

    $ quickmoveoutr = MoveTransition(0.1, leave=offscreenright, enter_time_warp=_warper.easein)

    play sound knock
    narrator 'Парень пулей летит к двери и резко её открывает.{w=1}{nw}'
    hide naomi at right with quickmoveoutr
    scene bg note with hpunch
    narrator '{w=0.5}Записка.{w=1.5} Хватая её дрожащими руками, Наоми быстро её раскрывает'

    n '{cps=20}Я знаю, что ты устал от всего этого. Этот груз камнем висит на тебе несколько лет. Я помогу тебе избавиться от него...{w=0.5}...{w=0.5}...{/cps}'
    n '{cps=20}...{w=0.5}...{w=0.5}приходи ночью к морю неподалёку от своего дома, там тебя будет ждать последняя записка.{/cps}'
    stop music fadeout 1
    jump good_end

    return

# Каноничная концовка
label good_end:
    scene black with fade
    pause 1.0
    scene end naomi_sea with dissolve
    play music it_hurts fadein 1.0 loop

    narrator '''
    Молча стоя на берегу, Наоми смотрел на бескрайние волны ночного моря. 
    
    Лунный свет отражался в его глазах, наполняя их таинственным блеском. 
    
    Он открывает бутылку и достаёт записку. 
    
    Медленно водя глазами по листку бумаги, он аккуратно складывает его и засовывает обратно в бутылку, отправляя её в плаванье по морю.
    '''

    n '''
    {cps=15}Ей было 5, а мне 7{/cps}

    {cps=15}У неё были лучшие подарки,{w=0.5} лучшая забота,{w=0.5} лучшая любовь родителей...{w=0.2}...{/cps}

    {cps=15}Я просто хотел того же.{w=1} Поездка на это море тоже была подарком для неё, на её день рождения...{w=1.5} последний день рождения.{/cps} 
    
    {cps=15}Родители отправили нас купаться, наказав мне присматривать за ней.{/cps}
    
    {cps=15}Мы отплыли довольно далеко, и только тогда я схватил её за волосы и погрузил под воду.{w=2} Чем больше она кричала, тем больше заглатывала воды.{/cps}
    
    {cps=15}Родители очнулись слишком поздно.{w=1} С тех пор они никогда не были прежними.{/cps}
    
    {cps=15}Я убил не только её, но и их любовь.{/cps}
    '''
    scene black with fade 
    pause 1.0
    scene end sea with dissolve

    narrator '''
    Парень провёл рукой по своим волосам. Кажется, за все эти прошедшие года ему наконец-то стало легко. Он медленно заходит в воду, погружаясь всё глубже. 
    
    Голова опускается в море. Наоми делает медленный вдох. Его лёгкие начинают наполняться жидкостью. 
    
    Больше ему не нужно бояться воды.
    '''

    jump credits

    return

# Титры
label credits:
    scene black with dissolve
    $ renpy.pause(2.0, hard=True)

    show text 'Спасибо за прохождение игры!{p}{p}Авторы:{p}vicfires - художник, сценарист,{p} организатор и создатель идеи{p}vezha8 - программист{p}Bush =D - композитор{p}{p}Отдельная благодарность:{p}Маше за помощь в создании игры{p}{p}Сделано с помощью Ren\'Py' at txt_up

    image fanart_1 = im.FactorScale('images/fanarts/fanart_1.jpg', 0.21)
    image fanart_2 = im.FactorScale('images/fanarts/fanart_2.jpg', 0.5)
    image fanart_3 = im.FactorScale('images/fanarts/fanart_3.jpg', 0.5)
    image fanart_4 = im.FactorScale('images/fanarts/fanart_4.jpg', 0.5)
    image fanart_5 = im.FactorScale('images/fanarts/fanart_5.jpg', 0.45)
    image fanart_6 = im.FactorScale('images/fanarts/fanart_6.jpg', 0.45)
    image fanart_7 = im.FactorScale('images/fanarts/fanart_7.jpg', 0.5)
    image fanart_8 = im.FactorScale('images/fanarts/fanart_8.jpg', 0.5)
    image fanart_9 = im.FactorScale('images/fanarts/fanart_9.jpg', 0.5)
    image fanart_10 = im.FactorScale('images/fanarts/fanart_10.png', 0.25)
    show fanart_1 at image_up(0, 0.0)
    show fanart_2 at image_up(0, 1.0)    
    $ renpy.pause(7.0, hard=True)
    show fanart_3 at image_up(5, 0.0)
    show fanart_4 at image_up(5, 1.0)
    $ renpy.pause(6.0, hard=True)
    show fanart_5 at image_up(7.2, 0.0)
    show fanart_6 at image_up(7.2, 1.0)    
    $ renpy.pause(7.0, hard=True)
    show fanart_7 at image_up(10, 0.0)
    show fanart_8 at image_up(10, 1.0)
    $ renpy.pause(6.0, hard=True)
    show fanart_9 at image_up(0, 0)    
    show fanart_10 at image_up(0, 1.0)
    pause 25

    return