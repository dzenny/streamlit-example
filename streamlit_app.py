import pandas as pd
import streamlit as st

st.title('Расчет ущерба от пожара')
#st.subheader('Расчет ущерба')

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
}


plant = st.selectbox(
    'Пострадала сельхозяйственная культура',
    costs.keys()
)

st.write(f'Цена за 1 кв.м (руб): {costs.get(plant, "неизвестно")}')

st.write('Введите:')
total_area      = st.number_input('Общую площадь i-х сельскохозяйственных посевов (лесного насаждения), кв.м.')
destroyed_area  = st.number_input('Общую уничтоженную пожаром площадь г-х сельскохозяйственных посевов (лесного насаждения), кв.м.')
total_cost      = st.number_input('Общую стоимость i-х сельскохозяйственных посевов (лесного насаждения), руб.')

price = costs.get(plant, 'неизвестно') 

def get_cost():
    if price == 'неизвестно':
        res = (total_cost/total_area)*destroyed_area
    else:	
        res = price*destroyed_area
    return res

if st.button('Вычислить..'):
    st.subheader('Результат:')
    
    damage = get_cost()
    if total_cost == 0:
        total_cost = price*total_area

    st.write(f'Общая площадь: {total_area} кв.м.')
    st.write(f'Уничтожено: {destroyed_area} кв.м.')
    st.write(f'Сельхоз. культура: {plant} (цена за 1 кв.м: {costs.get(plant,"неизвестно")})')
    st.write(f'Ущерб: {damage:.2f} руб.')

    df = pd.DataFrame(
        {'стоимость': [damage, total_cost-damage] },
        index = ['Ущерб','Спасено']
    )


    ax = df.plot.pie(y='стоимость', figsize=(3,5),
        autopct='%1.1f%%', shadow=True, startangle=0
    )
    st.pyplot(ax.get_figure())

