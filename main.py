import streamlit as st
from st_pages import Page, show_pages



st.set_page_config(layout="wide")
st.sidebar.title("Gmsh")

show_pages(
    [
        Page("main.py", "Начало", "🏠"),
        Page("1.py", "Общая характеристика ПО"),
        Page("elements.py", "Геометрические элементы"),
        Page("3.py", "Файл геометрии"),
        Page("4.py", "Создание области"),
        Page("5.py", "Интерактивные возможности создания области"),
        Page("6.py", "Составные области"),
        Page("7.py", "Маркирование подобластей и частей границ"),
        Page("8.py", "Генерация сетки"),
        Page("9.py", "Сгущение сетки"),
        Page("10.py", "Подготовка сетки для FEniCS"),
        Page("11.py", "CSG технологии в Gmsh"),
        Page("12.py", "Библиотеки Python pygmsh и meshio"),

    ]
)

st.title("Проект: Gmsh")
st.subheader(" генератор конечно-элементных сеток")


col1, col2, col3 = st.columns(3)

with col2:
    st.image("gmsh.png", width=250)

st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")



c1, c2 = st.columns((1, 1))

with c1:
    st.subheader("**Работу выполнили студенты МГУ Саров из группы ВМ-123    :**")

with c2:
    st.subheader("Бабенко Михаил, Баринов Даниил, Гайсин Роберт, Кислер Роман")