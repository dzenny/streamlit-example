import streamlit as st
import openpyxl  as op
import math

st.image('SPSA.png')

def Y1():
    st.title('ущерб нанесённый пожаром объектам строительства, руб.')
    Number = int(st.number_input("Введите число объектов строительства на которых пожаром была поврежденна или уничтоженна их площадь "))
    Y34 = []
    def Y_34_price(klfg):       
        def pril_b():
            book = op.open('Б.xlsx', read_only=True)
            staff = book.active
            vc = dict()
            for i, row in enumerate(range(2,staff.max_row +1)):
                sub_rf = staff[row][0].value
                vc[sub_rf] = i

            sub_russia = st.selectbox(
                'Субъекты рф',
                vc, key=str(klfg)+'55'
            )
            vc2 = dict()

            for k,h in enumerate(range(1,staff.max_column)):
                institutions = staff[1][h].value
                vc2[institutions] = k

            institution = st.selectbox(
                'Тип объекта',
                vc2, key=str(klfg)+'55'
            )


            for d,q in enumerate(range(2,staff.max_row +1)):
                if sub_russia == staff[q][0].value:
                    liine = q

            for k1,h2 in enumerate(range(1,staff.max_column)):
                if institution == staff[1][h2].value:
                    klf = h2 

            damage = staff[liine][klf].value
            return damage
        def pril_g():
            file_XL = op.open('Г.xlsx', read_only=True)
            status_file = file_XL.active
            dict_pril_L1 = dict()
            for z, w in enumerate(range(1,status_file.max_row +1)):
                vid_avto = status_file[w][0].value
                dict_pril_L1[vid_avto] = z

            vids_avto = st.selectbox(
                'наименование территории субъекта рф',
                dict_pril_L1, key=str(klfg)+'55'
            )
            for x,m in enumerate(range(1,status_file.max_row +1)):
                if vids_avto == status_file[m][0].value:
                    straka = m
            b = status_file[straka][1].value
            return b 
        def pril_d():
            file_XL = op.open('Д.xlsx', read_only=True)
            status_file = file_XL.active
            dict_pril_L1 = dict()
            for z, w in enumerate(range(1,status_file.max_row +1)):
                vid_avto = status_file[w][0].value
                dict_pril_L1[vid_avto] = z

            vids_avto = st.selectbox(
                'вид постройки',
                dict_pril_L1, key=str(klfg)+'55'
            )
            for x,m in enumerate(range(1,status_file.max_row +1)):
                if vids_avto == status_file[m][0].value:
                    straka = m
            d = status_file[straka][1].value
            return d 
        def var_2_price():
            def first_a():
                tabl_pril_a = {
                    'ОБЪЕКТЫ ЗДРАВООХРАНЕНИЯ':1,
                    'ОБЪЕКТЫ СПОРТИВНОГО НАЗНАЧЕНИЯ': 2,
                    'ОБЪЕКТЫ ОБРАЗОВАНИЯ': 3,
                    'ОБЪЕКТЫ КУЛЬТУРЫ': 4,
                    'ОБЪЕКТЫ ТОРГОВЛИ': 5,
                    'ОБЪЕКТЫ ОБЩЕСТВЕННОГО ПИТАНИЯ' : 6,
                    'ОБЪЕКТЫ БЫТОВОГО И КОММУНАЛЬНОГО НАЗНАЧЕНИЯ': 7, 
                    'ЖИЛЫЕ ДОМА И ОБЪЕКТЫ ПРИУСАДЕБНОГО ХОЗЯЙСТВА': 8,
                    'ОБЪЕКТЫ ДЛЯ ВРЕМЕННОГО ПРЕБЫВАНИЯ ЛЮДЕЙ': 9,
                    'ПРОИЗВОДСТВЕННЫЕ ЗДАНИЯ': 10,
                    'ОБЪЕКТЫ ЛЕСНОЙ, ДЕРЕВООБРАБАТЫВАЮЩЕЙ ЦЕЛЛЮЛОЗНО-БУМАЖНОЙ ПРОМЫШЛЕННОСТИ': 11,
                    'ОБЪЕКТЫ ЛЕГКОЙ ПРОМЫШЛЕННОСТИ': 12,
                    'ОБЪЕКТЫ ГАЗОВОЙ ПРОМЫШЛЕННОСТИ': 13,
                    'ОБЪЕКТЫ ПРОМЫШЛЕННОСТИ СТРОИТЕЛЬНЫХ МАТЕРИАЛОВ, ДЕТАЛЕЙ И КОНСТРУКЦИЙ': 14,
                    'ОБЪЕКТЫ ЧЕРНОЙ МЕТАЛЛУРГИИ': 15,
                    'ОБЪЕКТЫ ХИМИЧЕСКОЙ ПРОМЫШЛЕННОСТИ': 16,
                    'ОБЪЕКТЫ НЕФТЯНОЙ ПРОМЫШЛЕННОСТИ': 17,
                    'ОБЪЕКТЫ МЕДИЦИНСКОЙ И МИКРОБИОЛОГИЧЕСКОЙ ПРОМЫШЛЕННОСТИ' : 18,
                    'ОБЪЕКТЫ МАШИНОСТРОИТЕЛЬНОЙ ПРОМЫШЛЕННОСТИ': 19,
                    'ОБЪЕКТЫ УГОЛЬНОЙ, СЛАНЦЕВОЙ, ТОРФЯНОЙ, ГОРНОРУДНОЙ И ГОРНОДОБЫВАЮЩЕЙ ПРОМЫШЛЕННОСТИ': 20,
                    'Объекты полиграфической и кинематографической промышленности': 21,
                    'ОБЪЕКТЫ ПИЩЕВОЙ, МУКОМОЛЬНОЙ И КОМБИКОРМОВОЙ ПРОМЫШЛЕННОСТИ': 22,
                    'ОБЪЕКТЫ ЖИВОТНОВОДСТВА': 23,
                    'ОБЪЕКТЫ РАСТЕНИЕВОДСТВА': 24,
                    'объекты строительства складского назначения':25,
                }
                txt_a = st.selectbox(
                'Выберите тип объекта, значение эксплуатационного параметра которого вы ввели',
                tabl_pril_a.keys(), key=str(klfg)+'55'
                )
                vibor_a = tabl_pril_a.get(txt_a)

                book_a = op.open(f'А{vibor_a}.xlsx', read_only=True)
                staf = book_a.active
                vc_c1 = dict()
                for ax,bx in enumerate(range(1,staf.max_row +1)):
                    price_a = staf[bx][0].value
                    vc_c1[price_a] = ax
                        
                price_in_pril = st.selectbox(
                    'Здания и учреждения',
                    vc_c1, key=str(klfg)+'55'
                )
                for r,n in enumerate(range(1,staf.max_row +1)):
                    if price_in_pril == staf[n][0].value:
                        strk = n
                sa = staf[strk][1].value      
                return sa

            def first_c():
                tabl_pril_c = {
                    'ОБЪЕКТЫ ЗДРАВООХРАНЕНИЯ':1,
                    'ОБЪЕКТЫ СПОРТИВНОГО НАЗНАЧЕНИЯ': 2,
                    'ОБЪЕКТЫ ОБРАЗОВАНИЯ': 3,
                    'ОБЪЕКТЫ КУЛЬТУРЫ': 4,
                    'ОБЪЕКТЫ ТОРГОВЛИ': 5,
                    'ОБЪЕКТЫ ОБЩЕСТВЕННОГО ПИТАНИЯ' : 6,
                    'ОБЪЕКТЫ БЫТОВОГО И КОММУНАЛЬНОГО НАЗНАЧЕНИЯ': 7, 
                    'ЖИЛЫЕ ДОМА И ОБЪЕКТЫ ПРИУСАДЕБНОГО ХОЗЯЙСТВА': 8,
                    'ОБЪЕКТЫ ДЛЯ ВРЕМЕННОГО ПРЕБЫВАНИЯ ЛЮДЕЙ': 9,
                    'ПРОИЗВОДСТВЕННЫЕ ЗДАНИЯ': 10,
                    'ОБЪЕКТЫ ЛЕСНОЙ, ДЕРЕВООБРАБАТЫВАЮЩЕЙ ЦЕЛЛЮЛОЗНО-БУМАЖНОЙ ПРОМЫШЛЕННОСТИ': 11,
                    'ОБЪЕКТЫ ЛЕГКОЙ ПРОМЫШЛЕННОСТИ': 12,
                    'ОБЪЕКТЫ ГАЗОВОЙ ПРОМЫШЛЕННОСТИ': 13,
                    'ОБЪЕКТЫ ПРОМЫШЛЕННОСТИ СТРОИТЕЛЬНЫХ МАТЕРИАЛОВ, ДЕТАЛЕЙ И КОНСТРУКЦИЙ': 14,
                    'ОБЪЕКТЫ ЧЕРНОЙ МЕТАЛЛУРГИИ': 15,
                    'ОБЪЕКТЫ ХИМИЧЕСКОЙ ПРОМЫШЛЕННОСТИ': 16,
                    'ОБЪЕКТЫ НЕФТЯНОЙ ПРОМЫШЛЕННОСТИ': 17,
                    'ОБЪЕКТЫ МЕДИЦИНСКОЙ И МИКРОБИОЛОГИЧЕСКОЙ ПРОМЫШЛЕННОСТИ' : 18,
                    'ОБЪЕКТЫ МАШИНОСТРОИТЕЛЬНОЙ ПРОМЫШЛЕННОСТИ': 19,
                    'ОБЪЕКТЫ УГОЛЬНОЙ, СЛАНЦЕВОЙ, ТОРФЯНОЙ, ГОРНОРУДНОЙ И ГОРНОДОБЫВАЮЩЕЙ ПРОМЫШЛЕННОСТИ': 20,
                    'Объекты полиграфической и кинематографической промышленности': 21,
                    'ОБЪЕКТЫ ПИЩЕВОЙ, МУКОМОЛЬНОЙ И КОМБИКОРМОВОЙ ПРОМЫШЛЕННОСТИ': 22,
                    'ОБЪЕКТЫ ЖИВОТНОВОДСТВА': 23,
                    'ОБЪЕКТЫ РАСТЕНИЕВОДСТВА': 24,
                    'объекты строительства складского назначения':25,
                }
                txt_c = st.selectbox(
                'Выберите тип объекта, значение эксплуатационного параметра которого вы ввели',
                tabl_pril_c.keys(), key=str(klfg)+'55'
                )
                vibor_c = tabl_pril_c.get(txt_c)
                book_c = op.open(f'А{vibor_c}.xlsx', read_only=True)
                stafc = book_c.active
                vc_c2 = dict()
                for j,l in enumerate(range(1,stafc.max_row +1)):
                    price_c = stafc[l][0].value
                    vc_c2[price_c] = j
                price_in_pril_c = st.selectbox(
                    'Объекты',
                    vc_c2, key=str(klfg)+'55'
                )
                for o,p in enumerate(range(1,stafc.max_row +1)):
                    if price_in_pril_c == stafc[p][0].value:
                        s = p
                df = stafc[s][1].value
                return df

            st.write('Выберите значение эксплуатационного параметра, того же функционального назначения,')
            st.write('но, наиболее приближенный к вашему, меньше данного значения.')
            st.write('Если ваше значение меньше, чем данные в списке,')
            st.write('то выберите наименьший параметр из предложенных и запишите его значение.')
            a = st.number_input('значение эксплуатационного параметра (меньший)', key=str(klfg)+'55')
            C_a = first_a()
            st.write('Выберите значения эксплуатационного параметра, того же функционального назначения,')
            st.write('но ,наиболее приближенный к вашему,большего данного значения')
            st.write('Если ваше значение больше, чем данные в списке,')
            st.write('то выберите наибольший параметр из предложенных.')
            c = st.number_input('значение эксплуатационного параметра (больший)', key=str(klfg)+'55')
            C_c = first_c()
            st.write('Теперь введите фактическое значение эксплуатационного параметра')
            b = st.number_input('Теперь введите фактическое значение эксплуатационного параметра', key=str(klfg)+'55')




            if (a < b < c):
                bkb = C_c - ((c-b)*((C_c - C_a)/(c - a)))
            elif a > b:
                bkb = C_a
            elif c < b:
                bkb = C_c

            return bkb
        def c1_pril():
            def c1_A():
                tabl_pril_A = {
                    'ОБЪЕКТЫ ЗДРАВООХРАНЕНИЯ':1,
                    'ОБЪЕКТЫ СПОРТИВНОГО НАЗНАЧЕНИЯ': 2,
                    'ОБЪЕКТЫ ОБРАЗОВАНИЯ': 3,
                    'ОБЪЕКТЫ КУЛЬТУРЫ': 4,
                    'ОБЪЕКТЫ ТОРГОВЛИ': 5,
                    'ОБЪЕКТЫ ОБЩЕСТВЕННОГО ПИТАНИЯ' : 6,
                    'ОБЪЕКТЫ БЫТОВОГО И КОММУНАЛЬНОГО НАЗНАЧЕНИЯ': 7, 
                    'ЖИЛЫЕ ДОМА И ОБЪЕКТЫ ПРИУСАДЕБНОГО ХОЗЯЙСТВА': 8,
                    'ОБЪЕКТЫ ДЛЯ ВРЕМЕННОГО ПРЕБЫВАНИЯ ЛЮДЕЙ': 9,
                    'ПРОИЗВОДСТВЕННЫЕ ЗДАНИЯ': 10,
                    'ОБЪЕКТЫ ЛЕСНОЙ, ДЕРЕВООБРАБАТЫВАЮЩЕЙ ЦЕЛЛЮЛОЗНО-БУМАЖНОЙ ПРОМЫШЛЕННОСТИ': 11,
                    'ОБЪЕКТЫ ЛЕГКОЙ ПРОМЫШЛЕННОСТИ': 12,
                    'ОБЪЕКТЫ ГАЗОВОЙ ПРОМЫШЛЕННОСТИ': 13,
                    'ОБЪЕКТЫ ПРОМЫШЛЕННОСТИ СТРОИТЕЛЬНЫХ МАТЕРИАЛОВ, ДЕТАЛЕЙ И КОНСТРУКЦИЙ': 14,
                    'ОБЪЕКТЫ ЧЕРНОЙ МЕТАЛЛУРГИИ': 15,
                    'ОБЪЕКТЫ ХИМИЧЕСКОЙ ПРОМЫШЛЕННОСТИ': 16,
                    'ОБЪЕКТЫ НЕФТЯНОЙ ПРОМЫШЛЕННОСТИ': 17,
                    'ОБЪЕКТЫ МЕДИЦИНСКОЙ И МИКРОБИОЛОГИЧЕСКОЙ ПРОМЫШЛЕННОСТИ' : 18,
                    'ОБЪЕКТЫ МАШИНОСТРОИТЕЛЬНОЙ ПРОМЫШЛЕННОСТИ': 19,
                    'ОБЪЕКТЫ УГОЛЬНОЙ, СЛАНЦЕВОЙ, ТОРФЯНОЙ, ГОРНОРУДНОЙ И ГОРНОДОБЫВАЮЩЕЙ ПРОМЫШЛЕННОСТИ': 20,
                    'Объекты полиграфической и кинематографической промышленности': 21,
                    'ОБЪЕКТЫ ПИЩЕВОЙ, МУКОМОЛЬНОЙ И КОМБИКОРМОВОЙ ПРОМЫШЛЕННОСТИ': 22,
                    'ОБЪЕКТЫ ЖИВОТНОВОДСТВА': 23,
                    'ОБЪЕКТЫ РАСТЕНИЕВОДСТВА': 24,
                    'объекты строительства складского назначения':25,
                    'Другое': 0,
                }

                
                
                txt_A = st.selectbox(
                    'Выберите тип объекта, цену которого следует определить',
                    tabl_pril_A.keys(), key=str(klfg)+'55' 
                )
                st.write('Если присутствуют сведения о виде i-го объекта строительства,')
                st.write('но имеющего другие значения эксплуатационного параметра, выберите пункт "другое"')
                vibor_A = tabl_pril_A.get(txt_A)

                if vibor_A == 0:
                    A = var_2_price()
                else:
                    book = op.open(f'А{vibor_A}.xlsx', read_only=True)
                    staff = book.active
                    vc = dict()
                    for i, row in enumerate(range(1,staff.max_row +1)):
                        sub_rf = staff[row][0].value
                        vc[sub_rf] = i

                    sub_russia = st.selectbox(
                        'Объекты',
                        vc, key=str(klfg)+'55'
                    )
                    for d,q in enumerate(range(1,staff.max_row +1)):
                        if sub_russia == staff[q][0].value:
                            liine = q

                    A = staff[liine][1].value

                return A

            
            vibor_price = {
                'дана': 0,
                "не дана": 1,
            }
            viborka_price =  st.selectbox(
                'восстановительная стоимость 1 кв.м i-го объекта строительства, руб./кв.м.',
                vibor_price.keys(), key=str(klfg)+'55'
            )
            vibor_ = vibor_price.get(viborka_price)
            if vibor_ == 0:
                price = st.number_input('введите восстановительную стоимость 1 кв.м i-го объекта строительства, руб./кв.м.', key=str(klfg)+'55')
            else:
                price = c1_A()
            return price
        def Fact_kap():
            st.write('Если вам известна фактическая группа капитальности объекта из проектно-сметной документации или паспорта объекта строительства, то выберите "фактическая группа капитальности объекта дана"')
            vibor_fact_group = {
                'фактическая группа капитальности объекта дана': 0,
                'выбрать фактическую группу капитальности': 1,
            }
            viborka = st.selectbox(
                        'фактичсекая капитальность объекта',
                        vibor_fact_group.keys(), key=str(klfg)+'55'
                    )
            vibor = vibor_fact_group.get(viborka)

            def danna_kap():
                vbrn_kap= int(st.number_input('введите фактическую капитальность объекта', key=str(klfg)+'55'))
                vibor_dann = {
                        'Объекты общественного и жилого назначения и элементов приусадебного хозяйства': 0,
                        'объекты строительства производственного назначения': 1,
                    }

                vibor_dannogo = st.selectbox(
                    'Выберите тип объекта из списка ниже',
                    vibor_dann.keys(), key=str(klfg)+'55'
                )

                viberi_dannoe = vibor_dann.get(vibor_dannogo)

                if viberi_dannoe == 0:
                    book = op.open('В2.xlsx', read_only=True)
                    staff = book.active
                    vc = dict()
                    for i, row in enumerate(range(1,staff.max_row +1)):
                        sub_rf = staff[row][0].value
                        vc[sub_rf] = i

                    sub_russia = st.selectbox(
                        'Объект строительства',
                        vc, key=str(klfg)+'55'
                    )
                                
                    for d,q in enumerate(range(1,staff.max_row +1)):
                        if sub_russia == staff[q][0].value:
                            liine = q

                    damage = staff[liine][vbrn_kap].value
                else:
                    book = op.open('В4.xlsx', read_only=True)
                    staff = book.active
                    vc = dict()
                    for i, row in enumerate(range(1,staff.max_row +1)):
                        sub_rf = staff[row][0].value
                        vc[sub_rf] = i

                    sub_russia = st.selectbox(
                        'Объект строительства',
                        vc, key=str(klfg)+'55'
                    )
                                
                    for d,q in enumerate(range(1,staff.max_row +1)):
                        if sub_russia == staff[q][0].value:
                            liine = q

                    damage = staff[liine][vbrn_kap].value
                return damage 
            def kap():
                vibor_kap_v = {
                    'Объекты общественного и жилого назначения и элементов приусадебного хозяйства': 0,
                    'объекты строительства производственного назначения': 1,
                }

                vibor_tipa = st.selectbox(
                    'Определяемая фактичсекая капитальность объекта',
                    vibor_kap_v.keys(), key=str(klfg)+'55'
                )

                viberi_group = vibor_kap_v.get(vibor_tipa)
                        
                def pril_v2():
                    vibor_kap_v1 = {
                        'Перекрытия:Железобетонные': 0,
                        'Перекрытия:Смешанные (металлические и деревянные заполнения)': 1,
                        'Стены: Каменные облегченные из всех видов кирпича и легких камней;бетонный фундамент': 2,
                        'Стены: Деревянные, рубленные и брусчатые смешанные; Бутобетонный фундамент': 3,
                        'Стены: Щитовые и каркасно-засыпные, сырцовые, саманные и глинобитные;Фундаменты:Деревянные стулья или каменные столбы': 4,
                        'Стены: Каркасно-камышитовые и другие облегченные;Фундаменты: Глинобитные, грунтовые ': 5, 
                    }
                    viborka_kap_v1 = st.selectbox(
                        'Фактические группы капитальности объектов строительства, определяемые по конструктивным элементам ',
                        vibor_kap_v1.keys(), key=str(klfg)+'55'
                    )

                    vibor_v_1 = vibor_kap_v1.get(viborka_kap_v1)

                    book = op.open('В2.xlsx', read_only=True)
                    staff = book.active
                    vc = dict()
                    for i, row in enumerate(range(1,staff.max_row +1)):
                        sub_rf = staff[row][0].value
                        vc[sub_rf] = i

                    sub_russia = st.selectbox(
                        'Объект строительства',
                        vc, key=str(klfg)+'55'
                    )
                        
                    for d,q in enumerate(range(1,staff.max_row +1)):
                        if sub_russia == staff[q][0].value:
                            liine = q

                    damage = staff[liine][vibor_v_1+1].value
                    return damage

                def pril_v4():
                    vibor_kap_v2 = {
                        'Стены: Сплошная кладка из кирпича, из крупных блоков или из ж/б панелей;Междуэтажные и чердачные перекрытия:Железобетонные': 0,
                        'Колонны и столбы:Железобетонные или кирпичные;Бесчердачные перекрытия:Железобетонные': 1,
                        'Стены: Облегченная кладка из всех видов кирпича или легких камней; Колонны и столбы:Кирпичные или деревянные': 2,
                        'Стены: Деревянные, брусчатые, рубленные': 3,
                        'Стены: Деревянные, каркасные, щитовые, саманные и глинобитные; Колонны и столбы:Деревянные': 4,                    
                    }
                    viborka_kap_v2 = st.selectbox(
                        'Фактические группы капитальности объектов строительства, определяемые по конструктивным элементам ',
                        vibor_kap_v2.keys(), key=str(klfg)+'55'
                    )

                    vibor_v_2 = vibor_kap_v2.get(viborka_kap_v2)

                    book = op.open('В4.xlsx', read_only=True)
                    staff = book.active
                    vc = dict()
                    for i, row in enumerate(range(1,staff.max_row +1)):
                        sub_rf = staff[row][0].value
                        vc[sub_rf] = i

                    sub_russia = st.selectbox(
                        'Объект строительства',
                        vc, key=str(klfg)+'55'
                    )
                        
                    for d,q in enumerate(range(1,staff.max_row +1)):
                        if sub_russia == staff[q][0].value:
                            liine = q

                    damage = staff[liine][vibor_v_2+1].value
                    return damage

                

                if viberi_group == 0:
                    crt =  pril_v2()
                else:
                    crt = pril_v4()
                return crt

            if vibor == 0:
                Fact_group_kap = danna_kap()
            else:
                Fact_group_kap = kap()

            return Fact_group_kap
        def Group_kap():
            tabl_pril_A = {
                'ОБЪЕКТЫ ЗДРАВООХРАНЕНИЯ':1,
                'ОБЪЕКТЫ СПОРТИВНОГО НАЗНАЧЕНИЯ': 2,
                'ОБЪЕКТЫ ОБРАЗОВАНИЯ': 3,
                'ОБЪЕКТЫ КУЛЬТУРЫ': 4,
                'ОБЪЕКТЫ ТОРГОВЛИ': 5,
                'ОБЪЕКТЫ ОБЩЕСТВЕННОГО ПИТАНИЯ' : 6,
                'ОБЪЕКТЫ БЫТОВОГО И КОММУНАЛЬНОГО НАЗНАЧЕНИЯ': 7, 
                'ЖИЛЫЕ ДОМА И ОБЪЕКТЫ ПРИУСАДЕБНОГО ХОЗЯЙСТВА': 8,
                'ОБЪЕКТЫ ДЛЯ ВРЕМЕННОГО ПРЕБЫВАНИЯ ЛЮДЕЙ': 9,
                'ПРОИЗВОДСТВЕННЫЕ ЗДАНИЯ': 10,
                'ОБЪЕКТЫ ЛЕСНОЙ, ДЕРЕВООБРАБАТЫВАЮЩЕЙ ЦЕЛЛЮЛОЗНО-БУМАЖНОЙ ПРОМЫШЛЕННОСТИ': 11,
                'ОБЪЕКТЫ ЛЕГКОЙ ПРОМЫШЛЕННОСТИ': 12,
                'ОБЪЕКТЫ ГАЗОВОЙ ПРОМЫШЛЕННОСТИ': 13,
                'ОБЪЕКТЫ ПРОМЫШЛЕННОСТИ СТРОИТЕЛЬНЫХ МАТЕРИАЛОВ, ДЕТАЛЕЙ И КОНСТРУКЦИЙ': 14,
                'ОБЪЕКТЫ ЧЕРНОЙ МЕТАЛЛУРГИИ': 15,
                'ОБЪЕКТЫ ХИМИЧЕСКОЙ ПРОМЫШЛЕННОСТИ': 16,
                'ОБЪЕКТЫ НЕФТЯНОЙ ПРОМЫШЛЕННОСТИ': 17,
                'ОБЪЕКТЫ МЕДИЦИНСКОЙ И МИКРОБИОЛОГИЧЕСКОЙ ПРОМЫШЛЕННОСТИ' : 18,
                'ОБЪЕКТЫ МАШИНОСТРОИТЕЛЬНОЙ ПРОМЫШЛЕННОСТИ': 19,
                'ОБЪЕКТЫ УГОЛЬНОЙ, СЛАНЦЕВОЙ, ТОРФЯНОЙ, ГОРНОРУДНОЙ И ГОРНОДОБЫВАЮЩЕЙ ПРОМЫШЛЕННОСТИ': 20,
                'Объекты полиграфической и кинематографической промышленности': 21,
                'ОБЪЕКТЫ ПИЩЕВОЙ, МУКОМОЛЬНОЙ И КОМБИКОРМОВОЙ ПРОМЫШЛЕННОСТИ': 22,
                'ОБЪЕКТЫ ЖИВОТНОВОДСТВА': 23,
                'ОБЪЕКТЫ РАСТЕНИЕВОДСТВА': 24,
                'объекты строительства складского назначения':25,
                'Отсутствуют сведения об объектах того же функционального назначения': 0,
                
            }
            st.subheader('Выберите объект, который вам дан, чтобы определить нормативную капитальность объекта')
            st.write('Если в предложенном списке отсутствуют сведения об объектах того же функционального назначения, то выберите "Отсутствуют сведения об объектах того же функционального назначения" ')
            txt_A = st.selectbox(
                'Выберите тип объекта, для определения нормативной капитальности',
                tabl_pril_A.keys(), key=str(klfg)+'55' 
            )

            vibor_A = tabl_pril_A.get(txt_A)
            if vibor_A == 0:
                A = 10
            else:
                book = op.open(f'А{vibor_A}.xlsx', read_only=True)
                staff = book.active
                vc = dict()
                for i, row in enumerate(range(1,staff.max_row +1)):
                    sub_rf = staff[row][0].value
                    vc[sub_rf] = i

                sub_russia = st.selectbox(
                    'Тип объекта данного субъекта',
                    vc, key=str(klfg)+'55'
                )
                for d,q in enumerate(range(1,staff.max_row +1)):
                    if sub_russia == staff[q][0].value:
                        liine = q

                A = staff[liine][2].value

            return A
        def for_y5():
            N2 = int(st.number_input('Введите последний год из числа лет, предшествующих году, в который произошел пожар', key=str(klfg)+'55'))
            C3 = st.number_input('Введите кадастровую стоимость объекта строительства', key=str(klfg)+'55')
            N1 = int(st.number_input('Введите год, в котором была произведенна оценка стоимости объекта строительства', key=str(klfg)+'55'))
            j_pril = op.open('Ж.xlsx', read_only=True)
            activate = j_pril.active

            def j(p):
                for rik in range(1, activate.max_row +1):
                    if p == activate[rik][0].value:
                        j = activate[rik][1].value
                        c22 = 1 + (j/100)
                return c22

            dict_pril_j  = []
            if (N2 - N1) > 1:
                for a in range(N1 +1,N2 +1):
                    c = j(a)
                    dict_pril_j.append(c)
                list = dict_pril_j
                list_C2 = math.prod(list)
                C2_1 = C3*list_C2
            else:
                C2_1 = C3

            return C2_1
        pril_i = {
            'одноквартирный жилой дом': 0.67,
            'многоквартирный жилой дом': 0.35,
            'Объекты общественного назначения': 0.37,
            'Административные здания': 0.24,
            'Объекты складского, производственного назначения': 0.66,
            'Другие объекты строительства': 0.64,
        }
        asas = klfg + 1
        st.subheader(f'Рассчёт ущерба на {asas} объекте')
        st.subheader('Введите Фактический срок службы i-го объекта в годах')
        T_Fi = st.number_input('Фактический срок службы i-го объекта в годах', key=str(klfg)+'55')
        st.write('Примечание.Если на объекте строительства была проведена реконструкция (модернизация),')
        st.write('то фактический срок службы исчисляется, начиная с даты завершения реконструкции (модернизации).')

        st.subheader('Выберите вид постройки для определения минимальный нормативный срок эксплуатации объекта')
        T_j = pril_d()
        Fi_isn = (T_Fi/T_j)*100

        def pril_E():
            file_XL = op.open('Е.xlsx', read_only=True)
            status_file = file_XL.active
            Fi_isn_1 = round(Fi_isn)
            for x,m in enumerate(range(1,status_file.max_row +1)):
                if Fi_isn_1 == status_file[m][0].value:
                    straka = m
            E = status_file[straka][1].value
            return E
            
        if Fi_isn <= 100:
            k1 = pril_E()
        elif Fi_isn > 200:
            k1 = 96.08 + (T_Fi - T_j)*0.01
        else:
            k1 = 91.08 + (T_Fi - T_j)*0.05
        st.subheader('Выберите субъект и тип объекта, для опеределения коэффициент пересчета восстановительной стоимости от базового субъекта РФ')
        k2 = pril_b()
        GK = Group_kap()
        vibor_pov_im = {
            'Объект строительства повреждён': 1,
            'Объект строительства уничтожен':2,
        }
        tabl_viborki_3_4 = st.selectbox(
            ' ',
            vibor_pov_im.keys(), key=str(klfg)+'55'
        )
        vibral = vibor_pov_im.get(tabl_viborki_3_4)

        if vibral == 2:
            if GK == 10:
                S2 = st.number_input('Общая площадь объекта строительства', key=str(klfg)+'55')
                C2 = for_y5()
                y5 = C2/S2     
            else:
                FK = Fact_kap()

                if GK == FK:
                    k3 = 1
                elif GK == 0:
                    k3 = 1
                else:
                    k3 = FK
                st.subheader('Выберите тип Субъекта РФ для определения,поправочно климатического коэффициента')
                k4 = pril_g()

                C1 = c1_pril()

                y5 = C1*(1-(k1/100))*k2*k3*k4
            S1 =st.number_input('Введите уничтоженную пожаром площадь i-го объекта строительства кв. м.', key=str(klfg)+'55')
            y3 = y5*S1
        else:
            tabl_i = st.selectbox(
                'Выберите тип объекта из предложенного списка',
                pril_i.keys(),
            )
            K6 = pril_i.get(tabl_i)
            if GK == 10:
                S2 = st.number_input('Общая площадь объекта строительства', key=str(klfg)+'55')
                C2 = for_y5()
                y5 = (C2/S2)*K6     
            else:
                FK = Fact_kap()

                if GK == FK:
                    k3 = 1
                elif GK == 0:
                    k3 = 1
                else:
                    k3 = FK
                st.subheader('Выберите тип Субъекта РФ для определения,поправочно климатического коэффициента')
                k4 = pril_g()

                C1 = c1_pril()

                y5 = C1*k2*k3*k4*K6
            S3 =st.number_input('Введите повреждённую пожаром площадь i-го объекта строительства кв. м.', key=str(klfg)+'55')
            y3 = y5*S3
        return y3

    for klfg in range(0,Number):
        Y32_1 = Y_34_price(klfg)
        Y34.append(Y32_1)

    dfghj = sum(Y34)
    return dfghj
def y13():
    dict_y13 = []
    st.title('ущерб, нанесенный имуществу на объектах строительства, руб.')
    number_damage_im = int(st.number_input("введите кол-во Объектов, которым нанесён ущерб вследствие пожара"))
    def y13_11(w):
        fg = w+1
        st.write(f'Ущерб, нанесенный имуществу на объекте  {fg} типа')
        k_un = {"Здание производственного назначения":11704,
        "Складское здание, сооружение (в т.ч. сельскохозяйственное здание, сооружение для хранения)":22683,
        "Одноквартирный жилой дом":13273,
        "Многоквартирный жилой дом":11944,
        "Другое здание, сооружение, строение жилого сектора (кроме забора)":5608,
        "Здание, сооружение сельскохозяйственного назначения (кроме зданий, сооружений для хранения)":29707,
        "Здание, сооружение общественного назначения":27161,
        "Другое здание, сооружение, строение (кроме сооружений, установок промышленного назначения, неэксплуатируемых, строящихся зданий, сооружений)":15693,
        "иное":0,
        }

        k_pov = {"Здание производственного назначения":8947,
        "Складское здание, сооружение (в т.ч. сельскохозяйственное здание, сооружение для хранения)":9078,
        "Одноквартирный жилой дом":3630,
        "Многоквартирный жилой дом":8554,
        "Другое здание, сооружение, строение жилого сектора (кроме забора)":4891,
        "Здание, сооружение сельскохозяйственного назначения (кроме зданий, сооружений для хранения)":7402,
        "Здание, сооружение общественного назначения":25591,
        "Другое здание, сооружение, строение (кроме сооружений, установок промышленного назначения, неэксплуатируемых, строящихся зданий, сооружений)":11775,
        "иное":0,
        }

        un_im = st.selectbox(
            'Тип уничтоженного имущества на объекте строительства',
            k_un.keys(), key=str(w)+'87'
        )

        s1 = st.number_input('введите уничтоженную пожаром площадь i-го объекта строительства, кв.м. определяемую в соответствие с порядком заполнения и представления КУП', key=str(w)+'87')
        st.write('В случае, если отсутствует уничтоженная пожаром площадь i-го объекта строительства, то приравнивается к площади пожара.')
        pov_im = st.selectbox(
            'Тип повреждённого имущества на объекте строительства',
            k_pov.keys(), key=str(w)+'87'
        )

        s3 = st.number_input('введите поврежденную пожаром площадь i-го объекта строительства, кв.м. определяемую в соответствии с Порядком заполнения и представления КУП', key=str(w)+'87')   
        st.write('В случае если отсутствует поврежденная пожаром площадь /-го объекта строительства, то приравнивается к площади пожара.')
        y16 = k_un.get(un_im)
        y25 = k_pov.get(pov_im)

        if y16 == 0:
            c13 = st.number_input('введите общую стоимость имущества, находившегося на момент пожара на i-м объекте строительства, руб.', key=str(w)+'87')
            s2 = st.number_input('введите общую площадь i-го объекта строительства, кв.м. определяемую в соответствии с Порядком заполнения и представления КУП', key=str(w)+'87')       
            y14 = (c13/s2)*s1
            
        else:
            y14 = y16*s1
        if y25 == 0:
            c131 = st.number_input('введите общую стоимость имущества, находившегося на момент пожара на i-м объекте строительства, руб.', key=str(w)+'877')
            s2232 = st.number_input('введите общую площадь i-го объекта строительства, кв.м. определяемую в соответствии с Порядком заполнения и представления КУП', key=str(w)+'877')
            y15 = (0.75*(c131/s2232))*s1
            
        else:
            y15 = y25*s3
        
        y1311 = y14 + y15
        return y1311 
    for w in range(0,number_damage_im):
        y133 = y13_11(w)
        dict_y13.append(y133)
    summa_y13 = sum(dict_y13)

    return summa_y13
def y26():
    y29 =[]
    st.title('Ущерб нанесённый пожаром транспортным средствам, руб.')
    number_un_ts = int(st.number_input("введите кол-во Т/С, которму нанесён ущерб "))
    def y231(kraft):
        kraft_1 = kraft +1
        st.write(f'Рассчёт ущерба {kraft_1} транспортного средства')
        M1 = {
        "легковых авто, малых грузовых авто и мототехники срок эксплуатации 0-5 лет": 0.8,
        "легковых авто, малых грузовых авто и мототехники срок эксплуатации 6-10 лет": 0.65,
        "легковых авто, малых грузовых авто и мототехники срок эксплуатации 11-15 лет":0.55,
        "легковых авто, малых грузовых авто и мототехники срок эксплуатации 16-20 лет": 0.4,
        "легковых авто, малых грузовых авто и мототехники срок эксплуатации более 21 года": 0.35,
        "грузовых авто, автобусов, специальной техники срок эксплуатации 0-5 лет":0.8,
        "грузовых авто, автобусов, специальной техники срок эксплуатации 6-10 лет": 0.6,
        "грузовых авто, автобусов, специальной техники срок эксплуатации 11-15 лет": 0.5,
        "грузовых авто, автобусов, специальной техники срок эксплуатации 16-20 лет":0.35,
        "грузовых авто, автобусов, специальной техники срок эксплуатации более 21 года":0.3,
        "Иное транспортное средство":1,
        }
        N1 = {
            'автотранспортное средство':1,
            "другой тип автотранспортного средства":0,
        }
        P_raschet = {
            'легковые автомобили отечественных марок': 1,
            'легковые автомобили иностранных марок': 2,
            'грузовые автомобилей': 3,
            'сельскохозяйственная техника': 4,
            'специальная техника': 5,
            'автоприцепов (полуприцепов)': 6,
            'автобус,троллейбус,маломерные суда и легкие воздушные суда, железнодорожный подвижный состав': 7,
            'мототранспортные средства': 8,
        }
        def for_k9():
            if first_step_kf == 1:
                kk = 2 
                gg = 4 
                wp = 3  
            elif first_step_kf == 2:   
                kk = 5 
                gg = 9 
                wp = 5 
            elif first_step_kf == 3:   
                kk = 10
                gg = 16
                wp = 7
            elif first_step_kf == 4:   
                kk = 17
                gg = 22
                wp = 6
            elif first_step_kf == 5:   
                kk = 23
                gg = 27
                wp = 5
            elif first_step_kf == 6:   
                kk = 28
                gg = 31
                wp = 4
            elif first_step_kf == 7:   
                kk = 32
                gg = 35
                wp = 4
            elif first_step_kf == 8:   
                kk = 36
                gg = 39
                wp = 4
            file_p = op.open('П1.xlsx', read_only=True)
            opendd = file_p.active
            dict_pril_p = dict()

            for sf, tss in enumerate(range(kk,gg)):
                sqq = opendd[tss][0].value
                dict_pril_p[sqq] = sf

            sqq_ts = st.selectbox(
                'Уничтоженная площадь от горения транспортного средства, кв.м',
                dict_pril_p, key=str(kraft)+'44'
            )

            for fss, krek in enumerate(range(kk,gg)):
                if sqq_ts == opendd[krek][0].value:
                    ssstrochka = krek 

            dict_pril_p_2 = dict()

            for ssff, ttss in enumerate(range(1,wp)):
                qqqsss = opendd[kk-1][ttss].value
                dict_pril_p_2[qqqsss] = ssff

            sqq_ts_2 = st.selectbox(
                'Площадь транспортного средства, кв.м',
                dict_pril_p_2, key=str(kraft)+'44'
            )
            for qwe, rty in enumerate(range(1,wp)):
                if sqq_ts_2 == opendd[kk-1][rty].value:
                    ccolumn = rty 
            end_app = opendd[ssstrochka][ccolumn].value
            return end_app
        def for_k10():
            if first_step_kf == 1:
                kk = 2 
                gg = 6 
                wp = 3  
            elif first_step_kf == 2:   
                kk = 7 
                gg = 10
                wp = 5 
            elif first_step_kf == 3:   
                kk = 11
                gg = 18
                wp = 7
            elif first_step_kf == 4:   
                kk = 19
                gg = 26
                wp = 6
            elif first_step_kf == 5:   
                kk = 27
                gg = 31
                wp = 5
            elif first_step_kf == 6:   
                kk = 32
                gg = 36
                wp = 4
            elif first_step_kf == 7:   
                kk = 37
                gg = 41
                wp = 4
            elif first_step_kf == 8:   
                kk = 42
                gg = 44
                wp = 4
            file_p = op.open('П2.xlsx', read_only=True)
            opendd = file_p.active
            dict_pril_p = dict()

            for sf, tss in enumerate(range(kk,gg)):
                sqq = opendd[tss][0].value
                dict_pril_p[sqq] = sf

            sqq_ts = st.selectbox(
                'Повреждённая площадь от горения транспортного средства, кв.м',
                dict_pril_p, key=str(kraft)+'44'
            )

            for fss, krek in enumerate(range(kk,gg)):
                if sqq_ts == opendd[krek][0].value:
                    ssstrochka = krek 

            dict_prilp = dict()

            for ssff, ttss in enumerate(range(1,wp)):
                qqqsss = opendd[kk-1][ttss].value
                dict_prilp[qqqsss] = ssff

            sqq_ts2 = st.selectbox(
                'Площадь транспортного средства, кв.м',
                dict_prilp, key=str(kraft)+'44'
            )
            for qwe, rty in enumerate(range(1,wp)):
                if sqq_ts2 == opendd[kk-1][rty].value:
                    ccolumn = rty 
            end_app = opendd[ssstrochka][ccolumn].value
            return end_app
        book = op.open('Н.xlsx', read_only=True)
        staff = book.active
        vc = dict()
        for i, row in enumerate(range(1,staff.max_row +1)):
            sub_rf = staff[row][0].value
            vc[sub_rf] = i
        file_XL = op.open('Л1.xlsx', read_only=True)
        status_file = file_XL.active
        dict_pril_L1 = dict()
        for z, w in enumerate(range(2,status_file.max_row +1)):
            vid_avto = status_file[w][0].value
            dict_pril_L1[vid_avto] = z
        vids_avto = st.selectbox(
            'вид т/с ',
            dict_pril_L1, key=str(kraft)+'44'
        )
        dict_pril_L2 = dict()
        for hj,fg in enumerate(range(1,status_file.max_column)):
            otech_imp = status_file[1][fg].value
            dict_pril_L2[otech_imp] = hj
        vids_avto_2 = st.selectbox(
            'разновидности моделей т/с ',
            dict_pril_L2, key=str(kraft)+'44'
        )
        for x,m in enumerate(range(2,status_file.max_row +1)):
            if vids_avto == status_file[m][0].value:
                straka = m
        for h,y in enumerate(range(1,status_file.max_column)):
            if vids_avto_2 == status_file[1][y].value:
                hex = y
        M_kf = st.selectbox(
            'срок эксплуатациитранспортного средства на момент пожара',
            M1.keys(), key=str(kraft)+'44'
        )
        sub_russia = st.selectbox(
            'Субъекты рф',
            vc, key=str(kraft)+'44'
        )
        for d,q in enumerate(range(1,staff.max_row +1)):
            if sub_russia == staff[q][0].value:
                liine = q
        N_kf = st.selectbox(
            'вид транспортного средства',
            N1.keys(), key=str(kraft)+'44'
        )
        spisok_vida = st.selectbox(
            'вид т/с для расчёта',
            P_raschet.keys(), key=str(kraft)+'44'
        )
        first_step_kf = P_raschet.get(spisok_vida)
        s14 = st.number_input('введите общую площадь i-го транспортного средства в кв. м.', key=str(kraft)+'44')
        s4 = st.number_input('введите уничтоженную в результате горения площадь i-го т/с. в кв. м.', key=str(kraft)+'44')
        s5 = st.number_input('введите повреждённую в результате горения площадь i-го т/с. в кв. м.', key=str(kraft)+'44')

        N_vibor = N1.get(N_kf)
        if N_vibor == 0:
            k7 =1
            k8 =1
        else:
            k7 = M1.get(M_kf)
            k8 = staff[liine][1].value
        if s4 == 0:
            k9 = 0
        else:
            k9 = for_k9()
        if s5 == 0:
            k10 = 0
        else:
            k10 = for_k10()

        c4 = status_file[straka][hex].value


        def y28():
            c5 = c4/s14
            y28 = c5*(s4+0.94*s5)
            return y28

        def y281():
            if (k9 + k10) <= 1:
                y28 = c4*(1 + (k7 - 1)*k8)*(k9 + k10)
            else:
                y28 = c4*(1 + (k7 - 1)*k8)*(k9 + k10*(1 - k9))
            return y28

        def y27():
            y27 = c4*(1 + (k7 - 1)*k8)
            return y27

        if s4 == 0:
            damage = y281()
        elif c4==0 :
            damage = y28()
        else:
            damage = y27()

        return damage 
    for kraft in range(0, number_un_ts):
        y2_31 = y231(kraft)
        y29.append(y2_31)
    zcvzb = sum(y29)
    return zcvzb
def y9_summa():
    y9 = []
    st.title('ущерб, нанесенный имуществу на транспортных средствах, руб.')
    Number_ucherb_im_ts =int(st.number_input("введите кол-во имущества, которму нанесён ущерб на трансопртных средствах"))

    def input_data(i):
        g = i+1
        st.write(f'ущерб, нанесенный {g} имуществу на транспортных средствах')
        s7 = st.number_input("введите общую площадь имущества, находившегося на момент пожара на г-м транспортном средстве, кв.м.", key=str(i)+'1')
        c7 =  st.number_input("введите общую стоимость имущества, находившегося на момент пожара на г-м транспортном средстве, руб.", key=str(i)+'1')
        s6 =  st.number_input("введите площадь уничтоженного имущества на г-м транспортном средстве, кв.м.", key=str(i)+'1')
        s8 =  st.number_input("введите площадь поврежденного имущества на г-м транспортном средстве, кв.м.", key=str(i)+'1')

        def y17():
            c6 = c7/s7

            y18 = c6*s6
            y19 = 0.94*c6*s8
            y1711 = y18 + y19 
            return y1711
        damage = y17()  
        return damage
    for i in range(0,Number_ucherb_im_ts):    
        y9_1 = input_data(i)
        y9.append(y9_1)

    vbnm = sum(y9)

    return vbnm
def y10():
    price_list_cost = []
    st.title('ущерб в результате уничтожения сельскохозяйственных посевов, лесных насаждений, руб.')
    number_get_costs = int(st.number_input("Введите кол-во видов уничтоженных сельскохозяйственных посевов, лесных насаждений  "))
    def get_cost(r):
        fd = r+1 
        st.write(f'ущерб, нанесенный уничтоженному сельскохозяйственному посеву, лесному насаждению {fd} вида')
        costs = {
            "Соя": 3.42,
            "Рапс": 3.46,
            "Рожь":  1.26,
            "Овес": 1.23,
            "Просо": 1.12,
            "Ячмень":   2.58,
            "Гречиха": 1.84,
            "Пшеница": 2.53,
            "Кукуруза": 4.36,
            "Зернобобовые": 2.37,
            "Подсолнечник": 3.09,
            "Однолетние травы": 0.73,
            "Многолетние травы": 0.87,
            "Лен - долгунец (волокно)": 2.61,
            "Прочие зерновые и зернобобовые": 2.47,
            "Прочие технические культуры (плодово-ягодные, овощно-бахчевые и др.)": 66.81,
            "Иная сельхозяйственная культура": 0,
        }
        plant = st.selectbox(
            'Пострадала сельхозяйственная культура',
            costs.keys(), key=str(r)+'77'
        )
        st.write('Введите:')
        total_area = st.number_input('Общую площадь i-х сельскохозяйственных посевов (лесного насаждения), кв.м.', key=str(r)+'77')
        destroyed_area = st.number_input('Общую уничтоженную пожаром площадь г-х сельскохозяйственных посевов (лесного насаждения), кв.м.', key=str(r)+'77')
        total_cost = st.number_input('Общую стоимость i-х сельскохозяйственных посевов (лесного насаждения), руб.', key=str(r)+'77')

        price = costs.get(plant) 


        if price == 0:
            res = (total_cost/total_area)*destroyed_area
        else:	
            res = price*destroyed_area
        return res
    for r in range(0, number_get_costs):
        get_cost_v = get_cost(r)
        price_list_cost.append(get_cost_v)
    price_one_get_cost = sum(price_list_cost)

    return price_one_get_cost
def y21():
    y21_tabl =[]
    st.title('ущерб, нанесенный имуществу на открытой территории, руб.')
    Number_price_open_ter =int(st.number_input("введите кол-во имущества, которму нанесён ущерб на открытой территории"))
    def y21_1(e):
        f = e +1 
        st.write(f'Рассчёт ущерба нанесенный {f} имуществу на открытой территории')
        s12 = st.number_input("введите общую площадь имущества i-го вида на открытой территории, кв.м", key=str(e)+'88')
        c11 = st.number_input("введите общую стоимость имущества i-го вида на открытой территории, руб.", key=str(e)+'88')
        s11 = st.number_input("введите площадь уничтоженного имущества i-го вида на открытой территории, кв.м.", key=str(e)+'88')
        s13 = st.number_input("введите площадь поврежденного имущества i-го вида на открытой территории, кв.м.", key=str(e)+'88')
        c10 = c11/s12
        y22 = (c10*s11)
        y23 = (0.75*c10*s13)

        y2111 = y22 + y23
        return y2111
    for e in range(0, Number_price_open_ter):    
        y21_11 =  y21_1(e)
        y21_tabl.append(y21_11)

    vbgh = sum(y21_tabl)

    return vbgh
def y12():
    list_death = []
    st.title("Ущерб, нанесенный животным в руб.")
    Number_death_animal = int(st.number_input("Введите кол-во видов уничтоженных животных"))
    def get_animal(q):
        mm = q+1 
        st.write(f'Ущерб, нанесенный животным {mm} типа')
        price_animals_list = {
            "Корова":59177,
            "Бык":102214,
            "Овца":5823,
            "Баран":7764,
            "Коза":3882,
            "Козел":4852,
            "Свинья":21532,
            "Кабан":32298,
            "Осел":27936,
            "Мул":37249,
            "Пони":16139,
            "Верховая (легкоупряжная) лошадь":48417,
            "Тяжеловозная лошадь":91455,
            "Северный олень (самка)":13987,
            "Северный олень (самец)":18291,
            "Курица (петух)":260,
            "Гусь":613,
            "Утка":383,
            "Индюк":1225,
            "Индюшка":689,
            "Кролик":1500,
            "Пчелосемья":3000,
        } 
        animal = st.selectbox(
            'Выберите животное',
            price_animals_list.keys(),key=str(q)+'100'
        )
        number_animals =st.number_input('количество животных данного вида',key=str(q)+'100')

        price_animal = price_animals_list.get(animal)
        res_animal = price_animal*number_animals
        return res_animal 
    for q in range(0, Number_death_animal):
        y12_1 = get_animal(q)
        list_death.append(y12_1)

    summ_price = sum(list_death)
    return summ_price

list_price = []
st.title('Расчет материального ущерба,нанесеного пожаром объектам строительства и имуществу')
p1 = st.checkbox('Ущерб нанесённый пожаром объектам строительства')
if p1:
    k1 =Y1()
    list_price.append(k1)
p2 = st.checkbox('ущерб, нанесенный имуществу на объектах строительства')
if p2:
    k2 =y13()
    list_price.append(k2)
p3 = st.checkbox('Ущерб нанесённый пожаром транспортным средствам')
if p3:
    k3 =y26()
    list_price.append(k3)
p4 = st.checkbox('ущерб, нанесенный имуществу на транспортных средствах')
if p4:
    k4 = y9_summa()
    list_price.append(k4)
p5 = st.checkbox('ущерб в результате уничтожения сельскохозяйственных посевов, лесных насаждений')
if p5:
    k5 =y10()
    list_price.append(k5)
p6 = st.checkbox('ущерб, нанесенный имуществу на открытой территории')
if p6:
    k6=y21()
    list_price.append(k6)
p7 = st.checkbox('Ущерб, нанесенный животным')
if p7:
    k7=y12()
    list_price.append(k7)
damage = sum(list_price)  

if st.button('Вычислить..'):
    st.subheader('Результат:')
    st.write(damage)
st.image('SPSA2.png')   
