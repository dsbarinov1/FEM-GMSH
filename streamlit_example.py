import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import time
import math
from datetime import time
import plotly.express as px
import datetime


st.title('Our first app')


page = st.sidebar.selectbox("Выбрать страницу",
                            ["страница 0",
                             "страница 1",
                             "страница 2",
                             "страница 3",
                             "страница 4",
                             "страница 5",
                             "страница 6",
                             "страница 7",
                             "страница 8",
                             ])

if page == "страница 0":
    st.header("Добро пожаловать в Streamlit") #TODO оформить начальный текст в виде небольшого абзаца текста
    st.write("Streamlit это открытая библиотека для Python, "
             "которая позволяет быстро и легко создавать интерактивные веб-приложения для визуализации данных и машинного обучения."
             "В данном документе будут описаны самые основные функции это библиотеки "
             "Более подробная информация содержится в [документации](https://docs.streamlit.io). ")
    st.write("[Инструкция](https://docs.streamlit.io/library/get-started/installation) по установке")

elif page == "страница 1":
    st.header("Заголовок 1 уровня")
    st.subheader("Заголовок 2 уровня")
    st.text("Обычный скучный текст\n"
            "Скучный потому что без форматирования")
    st.title(":green[Мир Синий]")
    st.markdown(":rainbow[Сделаем текст классным]")
    st.markdown("Хорошего дня! :balloon: (╯ ° □ °) ╯ (┻━┻)")
    st.caption('Тут очень маленький текст.')
    st.divider()
    st.code('''
    st.header("Заголовок 1 уровня") # Заголовок
    st.subheader("Заголовок 2 уровня") # Заголовок поменьше
    st.text("Обычный скучный текст"  
            "Скучный потому что без форматирования") # Текст без форматирования
    st.title(":green[Мир Синий]")  #Заголовок с форматированием
    st.markdown(":rainbow[Сделаем текст классным]")
    st.markdown("Хорошего дня! :balloon:") #Текст с форматированием
    st.caption('Тут очень маленький текст.') #Маленький текст
    st.divider() #разделительная полоса (как <br> в HTML) 
    ''')
    st.write(
        "LaTeX формулы. Список элементов и формул [тут](https://katex.org/docs/supported.html)")
    st.latex(r'''
        a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
        \sum_{k=0}^{n-1} ar^k =
        a \left(\frac{1-r^{n}}{1-r}\right)
        ''')
    st.code('''st.latex(r
        a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
        \sum_{k=0}^{n-1} ar^k =
        a \left(\frac{1-r^{n}}{1-r}\right)
    ''')


elif page == "страница 2":
    st.title("Таблицы")  # TODO описание работы с таблицами используя функции библиотеки pandas
    st.markdown(
        "Настройка столбцов c помощью строк st_dataframe или st.data_editor Этот тип столбца по умолчанию для логических значений. Эту команду необходимо использовать в параметре columns_config, st.data_editor или st_dataframe .")
    st.markdown("**Статические таблицы** один из самых простых способ отображения табличных данных")
    st.caption("код")
    with st.expander("Посмотреть подробнее"):

        code1 = '''
                df = pd.DataFrame(np.random.randn(10, 5), columns=("col %d" % i for i in range(5)))

            st.table(df)'''
        st.code(code1, language='python')
    st.caption("пример")
    with st.expander("Посмотреть подробнее"):
        df = pd.DataFrame(np.random.randn(10, 5), columns=("col %d" % i for i in range(5)))

        st.table(df)

    st.markdown("Редактирование и отображение данных в таблице с помощью st.data_editor ")
    st.markdown(
        "**Виджета редактора данных**  позволяет редактировать данных и многие другие структуры данных в табличном пользовательском интерфейсе")
    st.caption("код")
    with st.expander("Посмотреть подробнее"):
        code2 = '''
                   df = pd.DataFrame(
                [
                    {"Название": "Проект1", "задание": "Streamlit", "Выполнено": True},
                    {"Название": "Проект2", "задание": "Nupay", "Выполнено": False},
                    {"Название": "Проект3", "задание": "Matplotlib", "Выполнено": False},
                    {"Название": "Проект4", "задание": "SciPy", "Выполнено": False},
                ]
            )

            edited_df = st.data_editor(df)'''
        st.code(code2, language='python')
    st.caption("пример")
    with st.expander("Посмотреть подробнее"):
        df = pd.DataFrame(
            [
                {"Название": "Проект1", "задание": "Streamlit", "Выполнено": True},
                {"Название": "Проект2", "задание": "Nupay", "Выполнено": False},
                {"Название": "Проект3", "задание": "Matplotlib", "Выполнено": False},
                {"Название": "Проект4", "задание": "SciPy", "Выполнено": False},
            ]
        )

        edited_df = st.data_editor(df)

    st.markdown("**Настройте столбец ссылки** припомощи  строк st.column_config.LinkColumn")
    st.caption("код")
    with st.expander("Посмотреть подробнее"):
        code2 = ''' data_df = pd.DataFrame(
            {
                "apps": [
                    " http://multiscalemr.ru/ru/%D1%81%D0%BE%D1%82%D1%80%D1%83%D0%B4%D0%BD%D0%B8%D0%BA%D0%B8/%D0%B2%D0%BF%D0%BD/ ",
                    " https://rcc.msu.ru/user/20  ",
                ],
            }
        )

        st.data_editor(
            data_df,
            column_config={
                "apps": st.column_config.LinkColumn(
                    "Преподователи",
                    help="The top trending Streamlit apps",
                    validate="^https://[a-z]+\.streamlit\.app$",
                    max_chars=100,
                )
            },
            hide_index=True,
        )'''
        st.code(code2, language='python')

    st.caption("пример")
    with st.expander("Посмотреть подробнее"):
        data_df = pd.DataFrame(
            {
                "apps": [
                    " http://multiscalemr.ru/ru/%D1%81%D0%BE%D1%82%D1%80%D1%83%D0%B4%D0%BD%D0%B8%D0%BA%D0%B8/%D0%B2%D0%BF%D0%BD/ ",
                    " https://rcc.msu.ru/user/20  ",
                ],
            }
        )

        st.data_editor(
            data_df,
            column_config={
                "apps": st.column_config.LinkColumn(
                    "Преподователи",
                    help="The top trending Streamlit apps",
                    validate="^https://[a-z]+\.streamlit\.app$",
                    max_chars=100,
                )
            },
            hide_index=True,
        )

    st.markdown(
        "**Статистическая метрика** отображения метрики крупным жирным шрифтом с дополнительным индикатором изменения метрики используется st.metric")
    st.caption("код")
    with st.expander("Посмотреть подробнее"):
        code3 = '''
                    col1, col2, col3 = st.columns(3)
            col1.metric("Температура", "+5 °С", "6 °С")
            col2.metric("Порывы ветра", "10 м/с", "3%")
            col3.metric("Осадки в жидком эквиволенте", "3,1мм", "1мм")'''
        st.code(code3, language='python')

    st.caption("пример")

    with st.expander("Температура на 21.10.2023"):
        col1, col2, col3 = st.columns(3)
        col1.metric("Температура", "+5 °С", "6 °С")
        col2.metric("Порывы ветра", "10 м/с", "3%")
        col3.metric("Осадки в жидком эквиволенте", "4,4мм", "-1мм")



elif page == "страница 3":
    st.title("Научная графика")

    data = {"a": [23, 12, 78, 4, 54], "b": [0, 13, 88, 1, 3],
            "c": [45, 2, 546, 67, 56]}

    # df = pd.DataFrame(data)

    t1 = ''' У Streamlit есть несколько типов диаграмм, которые являются "родными", то есть которые можно использовать без сторонних библиотек'''

    code1 = '''data = {"a":[23, 12, 78, 4, 54], "b":[0, 13 ,88, 1, 3], 
    "c":[45, 2, 546, 67, 56]}
    st.line_chart(data)
    '''
    st.write(t1)

    st.markdown("**Линейная диаграмма**")
    st.code(code1, language='python')
    st.line_chart(data)
    # st.line_chart(data=df)

    code2 = '''data = {"a":[23, 12, 78, 4, 54], "b":[0, 13 ,88, 1, 3], 
    "c":[45, 2, 546, 67, 56]}
    st.bar_chart(data)
    '''
    code3 = '''data = {"a":[23, 12, 78, 4, 54], "b":[0, 13 ,88, 1, 3], 
    "c":[45, 2, 546, 67, 56]}
    st.area_chart(data)
    '''
    st.markdown("**Столбчатая диаграмма**")
    st.code(code2, language='python')
    st.bar_chart(data)

    st.markdown("**Диаграмма с областями**")
    st.code(code3, language='python')
    st.area_chart(data)

    code4 = '''
    import numpy as np
    import matplotlib.pyplot as plt

    arr = np.random.normal(1, 1, size=100)
    fig, ax = plt.subplots()
    ax.hist(arr, bins=20)'''

    arr = np.random.normal(1, 1, size=500)
    fig, ax = plt.subplots()
    ax.hist(arr, bins=20)

    t7 = '''Но так же Streamlit поддерживает подключение и использование множества библиотек, что значительно расширяет возможнсти для работы с данными. Часто используются такие библиотеки, как matplotlib.pyplot - для создания компонентов диаграммы, pandas - для работы с данными, numpy - для поддержки многомерных массивов и т.д.

    '''
    st.write(t7)
    st.markdown("**Отображение рисунка matplotlib.pyplot**")
    st.code(code4, language='python')
    st.pyplot(fig)

    code5 = '''
    import pandas as pd

    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.scatter_chart(chart_data)'''

    code6 = '''
    import matplotlib.pyplot as plt
    import numpy as np

    x = np. linspace(0, 10, 100)
    fig = plt.figure()
    plt.plot(x, np.sin(x))
    plt.plot(x,np.cos(x), '--')
    st.write(fig)'''

    st.markdown("**Отображение диаграммы рассеяния**")
    st.code(code5, language='python')
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.scatter_chart(chart_data)

    st.markdown("**Графики синуса и косинуса**")
    x = np.linspace(0, 10, 100)
    fig = plt.figure()
    plt.plot(x, np.sin(x))
    plt.plot(x, np.cos(x), '--')
    st.code(code6, language='python')
    st.write(fig)


elif page == "страница 4":
    st.header("Элементы графического интерфейса")  # TODO описать кнопочки селектбоксы и тд тп с примерами кода
    "Именем элемента может быть:\n"
    "- Текст Marcdown\n"
    "- Эмодзи\n"
    "- Выражение LaTex\n"
    st.subheader("Кнопка")  # Простая кнопка
    st.text("При нажатии на кнопку возваращается True, иначе False.")
    st.subheader("Пример 1")
    if st.button("Нажми меня"):  # При нажатии на кнопку возвращается True
        st.text("Кнопка была нажата")
    code_button1 = '''if st.button("Нажми меня"):
            st.text("Кнопка была нажата")'''
    st.code(code_button1, language="python")

    st.subheader("Пример 2")
    if st.button('Привет'):
        st.text("Добрый день")
        st.button("Пока", type="primary")
    code_button2 = '''if st.button('Привет'):
        st.text("Добрый день")
        st.button("Пока", type="primary")'''
    st.code(code_button2, language="python")
    st.text("Помимо обычной кпоки есть также:\n"
            "- Кнопка скачивания, при нажатии начинается скачиваться файл\n"  # При нажатии начинается скачиваться файл
            "- Кнопка ссылки, при нажатии переходит по ссылке")  # При нажатии переходит по ссылке
    st.text("Подробнее о виждетах по ссылке")
    st.link_button("Ссылка", "https://docs.streamlit.io/library/api-reference/widgets")

    st.header("Переключатели")
    st.text("Возвращает True при установке")
    st.subheader("Checkbox")
    st.text("Вы согласны со мной ")
    agree = st.checkbox('Согласен')
    if agree:
        st.write('Молодец')
    code_check = '''st.text("Вы согласны со мной ")
    agree = st.checkbox('Согласен')
    if agree:
        st.write('Молодец')'''
    st.code(code_check, language="python")

    st.subheader("Radio")
    color = st.radio(
        "Какой твой любимый цвет ?",
        ('Черный', 'Желтый', 'Красный'))

    if color == 'Черный':
        st.write('Вы выбрали Черный.')
    elif color == 'Желтый':
        st.write('Вы выбрали Желтый.')
    else:
        st.write("Вы выбрали Красный.")

    st.write("Вы выбрали:", color)
    code_radio = '''color = st.radio(
        "Какой твой любимый цвет ?",
        ('Черный', 'Желтый', 'Красный'))
    if color == 'Черный':
        st.write('Вы выбрали Черный.')
    elif color == 'Yellow':
        st.write('Вы выбрали Желтый.')
    else:
        st.write("Вы выбрали Красный.")

    st.write("Вы выбрали:", color)'''
    st.code(code_radio, language="python")
    st.header("Слайдеры")

    st.text("Результатом слайдера может быть:\n"
            "- Целое или вещественное число(int,float)\n"
            "- Дата или время(time)\n"
            "- Строка или символ(str,char)\n"
            "- Список(list())")
    st.subheader("Slider")
    age = st.slider('Сколько тебе лет', 0, 120, 22)
    st.write("Мне ", age)
    code_sl1 = '''age = st.slider('Сколько тебе лет', 0, 120, 22)
    st.write("Мне ", age)'''
    st.code(code_sl1, language="python")

    st.subheader("Range slider")
    value = st.slider(
        'В каком диапазоне загадать число ?',
        0, 100, (25, 75))
    st.write(value, '  от', min(value), 'до', max(value))
    code_sl2 = '''values = st.slider(
    'В каком диапазоне загадать число ?',
    0, 100, (25, 75))
    st.write(values,'  от', min(values), 'до', max(values))'''
    st.code(code_sl2, language="python")

    st.subheader("Time slider")
    otpr, prib = st.slider(
        "Сколько едет поезд",
        value=(time(11, 30), time(12, 45)))
    st.write("Поезд выезжает в :", otpr, 'и прибывает в', prib)
    code_sl3 = '''import streamlit as st
from datetime import time

appointment = st.slider(
    "Schedule your appointment:",
    value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)'''
    st.code(code_sl3, language="python")

    st.subheader("Multiselect")
    options = st.multiselect(
        'Выберите цвета',
        ['Green', 'Yellow', 'Red', 'Blue'],
        ['Yellow', 'Red'])
    st.write('Вы выбрали:', options)
    code_sl12 = '''options = st.multiselect(
    'Какие у вас любимые цвета ?',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])
    st.write('Вы выбрали:', options)'''
    st.code(code_sl12, language="python")
    st.subheader("Select_slider")
    start_color, end_color = st.select_slider(
        'Выберите диапазон цвета',
        options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
        value=('red', 'blue'))
    st.write('Вы выбрали цвета между', start_color, 'и', end_color)
    code_sl5 = '''start_color, end_color = st.select_slider(
        'Выберите диапазон цвета',
        options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
        value=('red', 'blue'))
    st.write('Вы выбрали цвета между', start_color, 'and', end_color)'''
    st.code(code_sl5, language="python")

    st.header("Строки ввода")
    st.subheader("Text_input")
    st.text("Результатом является str или None")
    st.subheader("Введите название предмета")
    title = st.text_input('Численные методы, Философи, Английский')
    st.write('Вы ввели :', title)
    code_inp1 = '''title = st.text_input('Movie title', 'Life of Brian')
    st.write('The current movie title is', title)'''
    st.code(code_inp1, language="python")

    st.subheader("Number_input")
    st.text("При использовании Number_input можно указать:\n"
            "- label - краткое описание, что нужно ввести\n"  # Надпись на строкой ввод
            "- value - значение при первом отображени\n"
            "- min_value, max_value - максимальная и минимальная велечина"
            "- step - шаг"
            "- format (%d %e %f %g %i %u)")  # Надпись на строкой ввод
    number = st.number_input('Insert a number')
    st.write('The current number is ', number)
    code_inp2 = '''number = st.number_input('Insert a number')
    st.write('The current number is ', number)'''
    st.code(code_inp2, language="python")

    st.subheader("Time_input")
    t = st.time_input('Установите будильник', datetime.time(8, 45))
    st.write('Будильник установлен на ', t)
    code_inp3 = '''t = st.time_input('Установите будильник', datetime.time(8, 45))
    st.write('Будильник установлен на ', t)'''
    st.code(code_inp3, language="python")


elif page == "страница 5":
    st.header(
        "Расчетная программа с параметрическим вводом")  # TODO пример программы которая работает от ввода параметров на странице

    st.subheader("Сложение чисел")

    num1 = st.number_input('Введите первое число', value=0.0)
    st.text(f'number1 = {num1:.2f}')
    num2 = st.number_input('Введите второе число', value=0.0)
    st.text(f'number2 = {num2:.2f}\n'
            f'Сумма чисел равна = {num1:.2f} + {num2:.2f} = {(num1 + num2):.2f}')
    code_inp4 = '''num1 = st.number_input('Insert a number1',value=0.0)
    st.text(f'number1 = {num1:.2f}')
    num2 = st.number_input('Insert a number2',value = 0.0)
    st.text(f'number2 = {num2:.2f}')
    st.text(f'sum = {num1:.2f} + {num2:.2f} = {num1 + num2}')'''
    st.code(code_inp4, language="python")

    st.subheader("Матрицы")
    size = st.number_input('Выберите размер матрицы', min_value=1, max_value=10, value=3, step=1, format='%d')
    type_arr = st.radio(
        "Выберите тип матрицы",
        ('Единичная', 'Нулевая', 'Рандомная'))
    st.write("You selected:", type_arr)
    if type_arr == 'Единичная':
        arr = np.ones((size, size))
    elif type_arr == 'Нулевая':
        arr = np.zeros((size, size))
    elif type_arr == 'Рандомная':
        values = st.slider(
            'Выберите диапазон чисел',
            0, 100, (1, 100))
        st.write('Values:', values)
        arr1 = np.random.randint(min(values), max(values), (size, size))
        arr = arr1
    st.text(arr)
    transp = st.checkbox('Транспонировать матрицу')
    if transp:
        st.text(np.transpose(arr))
    ar_oper = st.radio(
        "Арифметические операции с матрицей",
        ('Умножение на число', 'Сложение', 'Найти максимальное число'))

    if ar_oper == 'Умножение на число':
        chislo = st.number_input('Введите число на которое хотите умножить')
        st.write(chislo * arr)
        st.text(chislo * arr)
    elif ar_oper == 'Сложение':
        chislo = st.number_input('Введите число c которым хотите сложить')
        st.write(arr + chislo)
        st.text(arr + chislo)
    elif ar_oper == 'Найти максимальное число':
        st.write(np.amax(arr))
        st.text(np.amax(arr))
    code_inp5 = '''size = st.number_input('Выберите размер матрицы', min_value=1, max_value=10, value=3, step=1, format='%d')
type_arr = st.radio(
    "Выберите тип матрицы",
    ('Единичная', 'Нулевая', 'Рандомная'))
st.write("You selected:", type_arr)
if type_arr == 'Единичная':
    arr = np.ones((size, size))
elif type_arr == 'Нулевая':
    arr = np.zeros((size, size))
elif type_arr == 'Рандомная':
    values = st.slider(
        'Выберите диапазон чисел',
        0, 100, (1, 100))
    st.write('Values:', values)
    arr1 = np.random.randint(min(values), max(values), (size, size))
    arr = arr1
st.text(arr)
transp = st.checkbox('Транспонировать матрицу')
if transp:
    st.text(np.transpose(arr))
ar_oper = st.radio(
    "Арифметические операции с матрицей",
    ('Умножение на число', 'Сложение', 'Найти максимальное число'))

if ar_oper == 'Умножение на число':
    chislo = st.number_input('Введите число на которое хотите умножить')
    st.write(chislo * arr)
    st.text(chislo * arr)
elif ar_oper == 'Сложение':
    chislo = st.number_input('Введите число c которым хотите сложить')
    st.write(arr + chislo)
    st.text(arr + chislo)
elif ar_oper == 'Найти максимальное число':
    st.write(np.amax(arr))
    st.text(np.amax(arr))'''
    st.code(code_inp5, language="python")

    st.latex("Решение\ квадратного\ уравнения\ ax^2+bx+c=0")

    a = st.slider('Коэффициент a', -10.0, 10.0, 1.0, step=0.01)
    b = st.slider('Коэффициент b', -10.0, 10.0, 1.0, step=0.01)
    c = st.slider('Коэффициент c', -10.0, 10.0, 1.0, step=0.01)
    st.latex(f"{a}x^2+{b}x+{c}=0")
    discr = b ** 2 - 4 * a * c

    st.latex(f"Дискриминант D = {discr:.2f}")

    if discr > 0 and a != 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        st.latex(f'x1 = {x1:.2f}')
        st.latex(f'x2 = {x2:.2f}')
    elif a == 0 and b == 0:
        st.latex("Введите другие коэффециенты")
    elif discr > 0 and a == 0:
        x = -c / (b)
        st.latex(f"x = {x:.2f}")
    elif discr == 0:
        x = -b / (2 * a)
        st.latex=(f"x = {x:.2f}")
    else:
        st.latex("Действительных корней нет")
    code_inp6 = '''a = st.slider('Коэффициент a', -10.0, 10.0, 1.0, step=0.01)
b = st.slider('Коэффициент b', -10.0, 10.0, 1.0, step=0.01)
c = st.slider('Коэффициент c', -10.0, 10.0, 1.0, step=0.01)
st.latex(f"{a}x^2+{b}x+{c}=0")
discr = b ** 2 - 4 * a * c

st.latex(f"Дискриминант D = {discr:.2f}")

if discr > 0 and a != 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    st.latex(f'x1 = {x1:.2f}')
    st.latex(f'x2 = {x2:.2f}')
elif a == 0 and b == 0:
    st.latex("Введите другие коэффециенты")
elif discr > 0 and a == 0:
    x = -c / (b)
    st.latex(f"x = {x:.2f}")
elif discr == 0:
    x = -b / (2 * a)
    st.latex=(f"x = {x:.2f}")
else:
    st.latex("Действительных корней нет")'''
    st.code(code_inp6, language="python")

elif page == "страница 6":
    st.title("Компановка страницы")
    st.divider()
    st.subheader('st.sidebar')
    st.text("Добавление виджетов на боковую панель")
    with st.sidebar:
        add_radio = st.radio(
            "Выбор метода",
            ("Example1", "Example2")
        )
    st.code('''    with st.sidebar:
        add_radio = st.radio(
            "Выбор метода",
            ("Example1", "Example2")
        )''')
    st.image("./pics/Снимок экрана 2023-10-20 091413.png")
    st.divider()

    st.subheader('st.columns')
    st.text("Оформление в колонках")
    st.code('''col1, col2, col3 = st.columns(3)

with col1:
   st.header("A Letter")
   st.image("./pics/ALetter.png")

with col2:
   st.header("B Letter")
   st.image("./pics/BLetter.png")

with col3:
   st.header("C Letter")
   st.image("./pics/CLetter.png")''')
    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("A Letter")
        st.image("./pics/ALetter.png")

    with col2:
        st.header("B Letter")
        st.image("./pics/BLetter.png")

    with col3:
        st.header("C Letter")
        st.image("./pics/CLetter.png")

    st.divider()
    st.subheader("st.tabs")
    st.text("Добавление контейнеров разделенных на вкладки")
    st.code('''tab1, tab2, tab3 = st.tabs(["A", "B", "C"])

    with tab1:
        st.header("A Letter")
        st.image("./pics/ALetter.png", width = 300)

    with tab2:
        st.header("B Letter")
        st.image("./pics/BLetter.png", width = 300)

    with tab3:
        st.header("C Letter")
        st.image("./pics/CLetter.png", width = 300)''')
    tab1, tab2, tab3 = st.tabs(["A", "B", "C"])

    with tab1:
        st.header("A Letter")
        st.image("./pics/ALetter.png", width = 200)

    with tab2:
        st.header("B Letter")
        st.image("./pics/BLetter.png", width = 200)

    with tab3:
        st.header("C Letter")
        st.image("./pics/CLetter.png", width = 200)

    st.divider()
    st.subheader("st.expander")
    st.text("Добавляем контейнер который можно свернуть или развернуть")
    st.code('''ith st.expander("Посмотреть подробнее"):
        st.write("Вы думали тут будет что-то умное, а тут собака")
        st.image("./pics/Annoying_Dog2.gif")''')
    with st.expander("Посмотреть подробнее"):
        st.write("Вы думали тут будет что-то умное, а тут собака")
        st.image("./pics/Annoying_Dog2.gif")

    st.divider()
    st.subheader("st.container")
    st.text("Простой контейнер для элементов")
    st.code('''    with st.container():
        st.write("Это внутри контейнера")

        st.image("./pics/cat_programmer2.gif")

    st.write("А это не внутри контейнера")''')
    with st.container():
        st.write("Это внутри контейнера")

        st.image("./pics/cat_programmer2.gif")

    st.write("А это не внутри контейнера")

elif page == "страница 7":
    img3 = Image.open("pics/sc1.png")
    img1 = Image.open("pics/sc2.png")
    img2 = Image.open("pics/sc3.png")
    img4 = Image.open("pics/sc4.png")

    st.title("Многостраничный документ")

    # По мере того, как приложения становятся большими, становится полезным организовать их на несколько страниц. Это упрощает управление приложением для разработчика и навигацию для пользователя.
    t1 = ''' Streamlit обеспечивает простой способ создания многостраничных приложений.

    Для начала, создадём простую домашнюю страницу, т.е. главную страницу, которая будет отображаться первой при запуске.


    Далее, в каталоге, где находится этот файл python, создаём новую папку с именем pages. У папки должно быть именно такое название, так как Streamlit не будет понимать никаких других имен каталогов.
    '''
    t2 = '''
    В папке pages создаём файлы (страницы проекта) 2_Научная графика.py, 3_Многостраничность.py.
    Streamlit по умолчанию упорядочивает страницы в алфавитном порядке, чтобы это изменить, добавим определенные числа перед их названиями, за которыми следует подчеркивание.
    '''

    t3 = '''
    После создания и сохранения, при перезагруке проекта из браузера, увидим отображение страниц с нужным упорядочиванием на боковой панели.
    Можно заметить, цифры не отобразились в названии.
    '''

    st.write(t1)
    st.image(img1)
    st.write(t2)
    st.image(img2)
    st.write(t3)
    st.image(img3, width=500)

    st.markdown("**Создание многостраничности с помощью элементов интерфейса**")

    t4 = '''
    Можно не создавать отдельные файлы .py. А поместить весь контент в один файл, при этом сделать нафигацию с помощью радиокнопок, выпадающего списка и т.д. В данном примере используется поле выбора.
    '''
    t5 = '''
    Вид списка при запуске проекта
    '''

    code1 = '''
    import streamlit as st

    page = st.sidebar.selectbox("Выбрать страницу",
                                ["страница 0",
                                 "страница 1",
                                 "страница 2",
                                 "страница 3",
                                 "страница 4",
                                 "страница 5",
                                 "страница 6",
                                 "страница 7",
                                 "страница 8",
                                 ])

    if page == "страница 0":
        st.header("Общая характеристика")

    elif page == "страница 1":
        st.header("Научная графика")
    '''
    st.write(t4)
    st.code(code1, language='python')
    st.write(t5)
    st.image(img4, width=350)


elif page == "страница 8":
    st.title("Медиа-элементы")

    image = "pics/p1.jpg"

    st.markdown("**Вставка изображения**")

    code1 = '''
    image = "pics/p1.jpg"
    st.image(image, caption="Это кот", width=650)
    '''
    st.code(code1, language='python')
    st.image(image, caption="Это кот", width=650)

    st.markdown("**Вставка звука**")

    code2 = '''
    audio_file = open('pics/s1.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')
    '''
    st.code(code2, language='python')
    audio_file = open('pics/s1.mp3', 'rb')
    audio_bytes = audio_file.read()

    st.audio(audio_bytes, format='audio/mp3')

    st.markdown("**Вставка видео**")

    code3 = '''
    video_file = open('pics/v.mp4', 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)
    '''

    st.code(code3, language='python')
    video_file = open('pics/v.mp4', 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)


