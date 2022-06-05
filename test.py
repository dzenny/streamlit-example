import streamlit as st
import datetime

st.markdown("""#### 1. Выбор даты из ограниченного календарного интервала и отображением в измененном формате""")
date = st.date_input(
    'Выберите дату в промежутке от 01.01.2020 до 31.12.2022',
    min_value= datetime.date(2020,1,1), 
    max_value= datetime.date(2022,12,31),
)
st.write("Выбрана дата:", date.strftime('%d.%m.%Y'))

st.markdown("""---""")


st.markdown("""#### 2. selectbox можно использовать со списками
   Думаю проблема была с незаполненным полем label
""")

options = ['Район 1', 'Район 2', 'Район 3']
i = st.selectbox('Выберите территорию', options)
st.write(f'Выбрано: {i}')

st.markdown("""---""")


st.markdown("""#### 3. Повтор ввода данных для нескольких сельхоз. культур""")

n = st.number_input(
    'Введите количество сельхоз культур',
    value=1,
    help="Если при пожаре пострадало несколько культур, данные по каждой из них надо вводить последовательно")
n = int(n)

for i in range(1,n+1,1):
    st.write(f'{i}-я культура')
    a = st.number_input(f'Площадь {i}-ой культуры:', key=str(i)+'1')
    b = st.number_input(f'Стоимость {i}-ой культуры:', key=str(i)+'2')
    st.write('И так далее...')
    st.write(f'Введено: площадь={a}, стоимость={b}')
    st.markdown("""---""")

st.markdown('... или как вариант, через "гармошки"')

for i in range(1,n+1,1):
    ex = st.expander(f"{i}-я культура")
    a = ex.number_input(f'Площадь {i}-ой культуры:', key=str(i)+'1e')
    b = ex.number_input(f'Стоимость {i}-ой культуры:', key=str(i)+'2e')
    ex.write('И так далее...')
    ex.write(f'Введено: площадь={a}, стоимость={b}')








