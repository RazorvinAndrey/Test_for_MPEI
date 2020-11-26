# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, TemplateView
from array import *

from .models import Voice
from django import forms


def index(request):
    return render(request, "index.html")


def topic(request):
    LeftMen = array('i', [4, 3, 4, 5, 5, 6, 4, 6, 3, 4, 3, 4, 1, 2, 4, 2, 2, 3, 4, 6, 4, 4, 4, 5])
    RightMen = array('i', [8, 7, 7, 8, 9, 9, 8, 9, 7, 8, 6, 8, 5, 6, 8, 6, 6, 7, 8, 8, 8, 8, 7, 8])
    LeftWomen = array('i', [4, 3, 2, 2, 6, 5, 3, 5, 3, 5, 4, 6, 1, 1, 3, 6, 3, 2, 6, 6, 6, 5, 6, 4])
    RightWomen = array('i', [8, 7, 6, 7, 9, 8, 7, 8, 6, 9, 8, 9, 6, 6, 7, 9, 6, 5, 9, 9, 9, 8, 9, 8])
    Sum = array('f', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    F = array('f', [0, 0, 0, 0, 0, 0, 0])
    sam = 1
    if request.method == "POST":
        if request.POST.get('sex'):
            request.session['sex'] = request.POST.get('sex')
        if request.POST.get('q'):
            value = int(request.POST['value'])
            if 'cart' not in request.session:
                request.session['cart'] = []
            request.session['cart'].append(int(value))
            request.session.modified = True
            if int(request.POST.get('q')) > 23:
                cart = request.session.get('cart')
                for i in range(0,23):
                    if request.session['sex'] == 'Мужчина':
                        if cart[i] < LeftMen[i]:
                            sam -= 1
                        else:
                            if cart[i] > RightMen[i]:
                                sam += 1
                    else:
                        if cart[i] < LeftWomen[i]:
                            sam -= 1
                        else:
                            if cart[i] > RightWomen[i]:
                                sam += 1
                if sam < -5:
                    K = 1.3
                else:
                    if sam > 6:
                        K = 0.7
                    else:
                        K = 1
                for p in cart:
                    print(p)
                Sum[0] = (cart[2] * 3 + cart[3] * 4 + cart[13] * 1 + cart[21] * 1 + cart[22] * 1) * K
                print("Дизайнер -- ", Sum[0])

                Sum[1] = (cart[0] * 1 + cart[2] * 3 + cart[5] * 1 + cart[10] * 1 + cart[13] * 1 + cart[18] * 3) * K
                print("Инженер на промышленном производстве -- ", Sum[1])

                Sum[2] = (cart[2] * 2 + cart[3] * 2 + cart[5] * 1 + cart[6] * 1 + cart[9] * 1 + cart[10] * 1 + cart[21] * 2) * K
                print("Конструктор -- ", Sum[2])

                Sum[3] = (cart[1] * 1 + cart[4] * 2 + cart[8] * 1 + cart[10] * 1 + cart[13] * 2 + cart[15] * 3) * K
                print("Переводчик -- ", Sum[3])

                Sum[4] = (cart[0] * 2 + cart[2] * 4 + cart[13] * 2 + cart[18] * 1 + cart[21] * 1) * K
                print("Программист -- ", Sum[4])

                Sum[5] = (cart[5] * 1 + cart[6] * 3 + cart[10] * 1 + cart[11] * 2 + cart[12] * 2 + cart[14] * 1) * K
                print("Слесарь ремонтник -- ", Sum[5])

                Sum[6] = (cart[2] * 1 + cart[5] * 5 + cart[6] * 1 + cart[10] * 2 + cart[23] * 1) * K
                print("Станочник высокого профиля -- ", Sum[6])

                Sum[7] = (cart[6] * 2 + cart[7] * 1 + cart[11] * 1 + cart[12] * 2 + cart[14] * 3 + cart[17] * 1) * K
                print("Строитель-монтажник -- ", Sum[7])

                Sum[8] = (cart[1] * 2 + cart[4] * 2 + cart[15] * 1 + cart[17] * 1 + cart[19] * 1 + cart[20] * 1 + cart[21] * 1) * K
                print("Учёный теоретик -- ", Sum[8])

                Sum[9] = (cart[1] * 2 + cart[2] * 1 + cart[4] * 1 + cart[7] * 1 + cart[10] * 1 + cart[16] * 1 + cart[19] * 1 + cart[21] * 1) * K
                print("Учёный экспериментатор -- ", Sum[9])

                Sum[10] = (cart[2] * 3 + cart[8] * 1 + cart[13] * 3 + cart[18] * 2 + cart[23] * 1) * K
                print("Экономист -- ", Sum[10])

                # ЭнМИ 1
                F[0] = Sum[1] * 4 + Sum[2] * 4 + Sum[4] * 1 + Sum[6] * 1 + Sum[9] * 2
                # ИЭЭ или ИТАЭ или ИЭВТ или ИЭТЭ 2
                F[1] = Sum[4] * 1 + Sum[2] * 3 + Sum[1] * 3 + Sum[8] * 4 + Sum[9] * 3
                 # ИВТИ(АВТИ) 3
                F[2] = Sum[1] * 1 + Sum[2] * 3 + Sum[4] * 4 + Sum[8] * 3
                 # ИРЭ 4
                F[3] = Sum[1] * 1 + Sum[2] * 3 + Sum[3] * 1 + Sum[8] * 1 + Sum[9] * 1
                 # ИГВИЭ 5
                F[4] = Sum[1] * 2 + Sum[2] * 4 + Sum[5] * 3 + Sum[7] * 4
                 # ИнИЭ 6
                F[5] = Sum[10] * 4 + Sum[3] * 2 + Sum[4] * 4
                 #ГПИ 7
                F[6] = Sum[0] * 4 + Sum[3] * 4 + Sum[4] * 1 + Sum[10] * 3
                max = 0
                for i in range(0,6):
                    if F[i] > max:
                        S = i
                        max = F[i]
                print(S)
                if S == 0:# Вопросы для ЭнМИ
                    nom = 3
                    if 'nom' not in request.session:
                        request.session['nom'] = []
                    request.session['nom'].append(nom)
                    request.session.modified = True
                    if 'text' not in request.session:
                        request.session['text'] = []
                    request.session['text'].append("Хотели бы вы в будующем участвовать в создании новых технологических процессов и методов обработки?")
                    request.session['text'].append("Разработка научных основ исследования общих свойств, создания и принципов функционирования энергетических систем и комплексов?")
                    request.session['text'].append("Хотели бы вы проектировать новые поколений машин, приборов, аппаратуры?")
                    request.session['text'].append("Хотели бы вы заниматься исследованием автоматизированных технологических процессов, создаваемых на базе робототехнических и мехатронных систем?")
                    request.session.modified = True
                    if 'nap' not in request.session:
                        request.session['nap'] = []
                    request.session['nap'].append("Машиностроение")
                    request.session['nap'].append("Энергетическое машиностроение")
                    request.session['nap'].append("Прикладная механика")
                    request.session['nap'].append("Робототехника и мехатроника")
                    request.session.modified = True

                else:
                    if S == 1:  # Вопросы для ИЭЭ или ИТАЭ или ИЭВТ или ИЭТЭ
                        nom = 5
                        if 'nom' not in request.session:
                            request.session['nom'] = []
                        request.session['nom'].append(nom)
                        request.session.modified = True
                        if 'text' not in request.session:
                            request.session['text'] = []
                        request.session['text'].append("Разработка методов исследования и расчета радиационного теплообмена в прозрачных и поглощающих средах?")
                        request.session['text'].append("Конструирование и создание новых экспериментальных установок и аппаратуры для исследований по ядерной физике и физике космических лучей?")
                        request.session['text'].append("Создание электротехнических комплексов и систем промышленного, транспортного, бытового и специального назначения?")
                        request.session['text'].append("Проектирования электротехнологических комплексов и эффективного управления их оборудованием?")
                        request.session['text'].append("Исследование и разработка рекомендаций по повышению качества и улучшению теплофизических свойств веществ?")
                        request.session['text'].append("Создание новых и совершенствованием существующих твердотельных электронных приборов, радиоэлектронных компонентов?")
                        request.session.modified = True
                        if 'nap' not in request.session:
                            request.session['nap'] = []
                        request.session['nap'].append("Теплоэнергетика и теплотехника ИТАЭ")
                        request.session['nap'].append("ядерная энергетика")
                        request.session['nap'].append("Электроэнергетика ИЭЭ")
                        request.session['nap'].append("электоэнергетика ИЭТ")
                        request.session['nap'].append("Теплоэнергетика ИЭВТ")
                        request.session['nap'].append("Электроника")
                        request.session.modified = True

                    else:
                        if S == 2:  # Вопросы для АВТИ (ИВТИ)
                            nom = 3
                            if 'nom' not in request.session:
                                request.session['nom'] = []
                            request.session['nom'].append(nom)
                            request.session.modified = True
                            if 'text' not in request.session:
                                request.session['text'] = []
                            request.session['text'].append("Обеспечивать взаимодействие человека-оператора с управляемыми им машинами?")
                            request.session['text'].append("Разработать новые математических методы моделирования объектов и явлений?")
                            request.session['text'].append("Заниматься в область научных, технических и нормативно-технических основ, необходимых для обеспечения современных требований к единству и точности измерений?")
                            request.session['text'].append("Работать в разработке технических средств и организационных комплексов, обеспечивающих рациональное управление сложным?")
                            request.session.modified = True
                            if 'nap' not in request.session:
                                request.session['nap'] = []
                            request.session['nap'].append("Прикладная матемитика и информатика")
                            request.session['nap'].append("Информатика и вычеслительная техника")
                            request.session['nap'].append("Приборостроение")
                            request.session['nap'].append("Управление в тех системах")
                            request.session.modified = True

                        else:
                            if S == 3:  # Вопросы для ИРЭ
                                nom = 3
                                if 'nom' not in request.session:
                                    request.session['nom'] = []
                                request.session['nom'].append(nom)
                                request.session.modified = True
                                if 'text' not in request.session:
                                    request.session['text'] = []
                                request.session['text'].append("Участвовать в создании новых и совершенствованием существующих твердотельных электронных приборов, радиоэлектронных компонентов?")
                                request.session['text'].append("Работать в сфере исследований, разработки, проектирования и эксплуатации устройств телевидения и радиосвязи различного назначения")
                                request.session['text'].append("Исследование новых явлений и процессов в радиоэлектронике, позволяющих повысить эффективность систем и устройств радиолокации и радионавигации?")
                                request.session['text'].append("Обеспечивает подготовку востребованных специалистов, способных разрабатывать и проектировать приборы и системы медицинского назначения?")
                                request.session.modified = True
                                if 'nap' not in request.session:
                                    request.session['nap'] = []
                                request.session['nap'].append("Электроника")
                                request.session['nap'].append("Радиотехника")
                                request.session['nap'].append("Радиоэлектронные системы")
                                request.session['nap'].append("Биотехнические системы")
                                request.session.modified = True

                            else:
                                if S == 4:  # Вопросы для ИГВИЭ
                                    nom = 2
                                    if 'nom' not in request.session:
                                        request.session['nom'] = []
                                    request.session['nom'].append(nom)
                                    request.session.modified = True
                                    if 'text' not in request.session:
                                        request.session['text'] = []
                                    request.session['text'].append("Разработки в области рационального проектирования конструктивных и объемно-планировочных решений зданий и сооружений?")
                                    request.session['text'].append("создание электротехнических комплексов и систем промышленного, транспортного, бытового и специального назначения?")
                                    request.session['text'].append("Хотели бы вы в будующем участвовать в создании новых технологических процессов и сборки изделий машиностроения?")
                                    request.session.modified = True
                                    if 'nap' not in request.session:
                                        request.session['nap'] = []
                                    request.session['nap'].append("Строительство")
                                    request.session['nap'].append("Электроэнергетика")
                                    request.session['nap'].append("Машиностроение")
                                    request.session.modified = True

                                else:
                                    if S == 5:  # Вопросы для ИнИЭ
                                        nom = 5
                                        if 'nom' not in request.session:
                                            request.session['nom'] = []
                                        request.session['nom'].append(nom)
                                        request.session.modified = True
                                        if 'text' not in request.session:
                                            request.session['text'] = []
                                        request.session['text'].append("Исследование процессов создания, накопления и обработки информации.")
                                        request.session['text'].append("Проводит работу с пользователями системы, чтобы объяснить важность и виды защитных мер ?")
                                        request.session['text'].append("Синтез математических, естественно-научных и профессиональных дисциплин")
                                        request.session['text'].append("Изучение экономических, управленческих, социальных и гуманитарных дисциплин?")
                                        request.session['text'].append("Бизнес-управление, информационных технологий и информационных систем?")
                                        request.session['text'].append("Разработка новых и адаптация существующих методов, механизмов и инструментов функционирования экономики, организации и управления хозяйственными образованиями в промышленности.")
                                        request.session.modified = True
                                        if 'nap' not in request.session:
                                            request.session['nap'] = []
                                        request.session['nap'].append("Прикладная информатика")
                                        request.session['nap'].append("Информационная безопасность")
                                        request.session['nap'].append("Управление качеством")
                                        request.session['nap'].append("Менеджмент")
                                        request.session['nap'].append("Бизнес информатика")
                                        request.session['nap'].append("Экономика")
                                        request.session.modified = True

                                    else:
                                        if S == 6:  # Вопросы для ГПИ
                                            nom = 2
                                            if 'nom' not in request.session:
                                                request.session['nom'] = []
                                            request.session['nom'].append(nom)
                                            request.session.modified = True
                                            if 'text' not in request.session:
                                                request.session['text'] = []
                                            request.session['text'].append("Изучение основы теории коммуникации, социология массовых коммуникаций, теория и практика массовой информации, основы интегрированных коммуникаций, основы менеджмента?")
                                            request.session['text'].append("Оптимизация творческих процессов проектирования изделии текстильной, легкой, машиностроительной, приборостроительной, автомобилестроительной и других отраслей?")
                                            request.session['text'].append("Работать в областях современного языкознания, владеющий несколькими иностранными языками, в отличии от профилей, фокусирующихся на конкретном языке")
                                            request.session.modified = True
                                            if 'nap' not in request.session:
                                                request.session['nap'] = []
                                            request.session['nap'].append("Реклама и связь с общественностью")
                                            request.session['nap'].append("Дизайн")
                                            request.session['nap'].append("Лингвистика")
                                            request.session.modified = True

                nom = request.session['nom']
                print(nom[0])
                del request.session['cart']
                return redirect('/dop/')
            else:
                q = int(request.POST.get('q')) + 1
        else:
            q = 1
        ques = Voice.objects.get(num__exact=q)
        quest = {
            'q': ques,
        }
        return render(request, "test.html", quest)
    else:
        return render(request, "index.html")

def dop(request):
        if request.method == "POST":
            if request.POST.get('q'):
                value = int(request.POST['value'])
                if 'dop' not in request.session:
                    request.session['dop'] = []
                request.session['dop'].append(value)
                request.session.modified = True
                nom = request.session['nom']
                if int(request.POST.get('q')) >= int(nom[0]):
                    A = request.session['dop']
                    for i in A:
                        print(i)
                    MaxIndex = 0
                    max = -1
                    print("Вам подойдут направления: ")
                    nap = request.session['nap']
                    if int(nom[0]) == 3:
                        for z in range(0, 3):
                            for j in range(0, 3):
                                if A[j] > max:
                                    MaxIndex = j
                                    max = A[j]
                            print(MaxIndex)
                            if MaxIndex == 0:
                                if 'dir' not in request.session:
                                    request.session['dir'] = []
                                request.session['dir'].append(nap[0])
                                request.session.modified = True
                            else:
                                if MaxIndex == 1:
                                    if 'dir' not in request.session:
                                        request.session['dir'] = []
                                    request.session['dir'].append(nap[1])
                                    request.session.modified = True
                                else:
                                    if MaxIndex == 2:
                                        if 'dir' not in request.session:
                                            request.session['dir'] = []
                                        request.session['dir'].append(nap[2])
                                        request.session.modified = True
                                    else:
                                        if MaxIndex == 3:
                                            if 'dir' not in request.session:
                                                request.session['dir'] = []
                                            request.session['dir'].append(nap[3])
                                            request.session.modified = True

                            A[MaxIndex] = -69
                            max = -1

                    if int(nom[0]) == 2:
                        for z in range(0, 3):
                            for j in range(0, 3):
                                if A[j] > max:
                                    MaxIndex = j
                                    max = A[j]
                            print(MaxIndex)
                            if MaxIndex == 0:
                                if 'dir' not in request.session:
                                    request.session['dir'] = []
                                request.session['dir'].append(nap[0])
                                request.session.modified = True
                            else:
                                if MaxIndex == 1:
                                    if 'dir' not in request.session:
                                        request.session['dir'] = []
                                    request.session['dir'].append(nap[1])
                                    request.session.modified = True
                                else:
                                    if MaxIndex == 2:
                                        if 'dir' not in request.session:
                                            request.session['dir'] = []
                                        request.session['dir'].append(nap[2])
                                        request.session.modified = True

                            A[MaxIndex] = -69
                            max = -1
                    if int(nom[0]) == 5:
                        for z in range(0, 3):
                            for j in range(0, 3):
                                if A[j] > max:
                                    MaxIndex = j
                                    max = A[j]
                            print(MaxIndex)
                            if MaxIndex == 0:
                                if 'dir' not in request.session:
                                    request.session['dir'] = []
                                request.session['dir'].append(nap[0])
                                request.session.modified = True
                            else:
                                if MaxIndex == 1:
                                    if 'dir' not in request.session:
                                        request.session['dir'] = []
                                    request.session['dir'].append(nap[1])
                                    request.session.modified = True
                                else:
                                    if MaxIndex == 2:
                                        if 'dir' not in request.session:
                                            request.session['dir'] = []
                                        request.session['dir'].append(nap[2])
                                        request.session.modified = True
                                    else:
                                        if MaxIndex == 3:
                                            if 'dir' not in request.session:
                                                request.session['dir'] = []
                                            request.session['dir'].append(nap[3])
                                            request.session.modified = True
                                        else:
                                            if MaxIndex == 4:
                                                if 'dir' not in request.session:
                                                    request.session['dir'] = []
                                                request.session['dir'].append(nap[4])
                                                request.session.modified = True
                                            else:
                                                if MaxIndex == 5:
                                                    if 'dir' not in request.session:
                                                        request.session['dir'] = []
                                                    request.session['dir'].append(nap[5])
                                                    request.session.modified = True

                            A[MaxIndex] = -69
                            max = -1
                    dir = request.session['dir']
                    print("----------------------------")
                    for i in dir:
                        print(i)
                    one = dir[0]
                    two = dir[1]
                    tre = dir[2]
                    que = {
                        'one': one,
                        'two': two,
                        'tre': tre,
                    }
                    del request.session['dop']
                    del request.session['dir']
                    del request.session['text']
                    del request.session['nom']
                    del request.session['nap']
                    return render(request, "end.html", que)
                else:
                    q = int(request.POST.get('q')) + 1
            else:
                q = 0
            text = request.session['text']
            nom = request.session['nom']
            for i in text:
                print(i)
            print(q)
            print(nom[0])
            H = text[q]
            quest = {
            'q': H,
            'num': q,
            }
            return render(request, "test_dop.html", quest)
        else:
            nom = request.session['nom']
            que = {
                'v': nom[0] + 1,
            }
            return render(request, "dop1.html", que)