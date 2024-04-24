

import streamlit as st
import datetime
import matplotlib.animation as animation
from st_pages import Page, show_pages, add_page_title



st.title('Интерактивные возможности создания области')

def main():
    st.header('Geometry')
    st.image('gui.png', caption='')
    st.subheader('Elementary entities')
    st.write('Здесь вы создаете базовые геометрические объекты, такие как точки, линии, поверхности и т.д.')
    st.image('gui_add_rectangle.png', caption='')
    st.subheader('Physical groups')
    st.image('Physical groups.png', caption='')
    st.write('Физические группы используются для обозначения частей геометрии, которым будут присвоены определенные граничные условия или материалы при расчетах.')
    st.subheader('Reload script')
    st.write('Позволяет перезагрузить скрипты для автоматического создания геометрии.')
    st.subheader('Remove last script command')
    st.write('Удаляет последнюю команду из скрипта.')
    st.subheader('Edit script')
    st.write('Переход к редактированию скрипта геометрии.')

    st.header('Mesh')
    st.image('gui_mesh.png', caption='')
    st.subheader('Define')
    st.write('Настройка параметров сетки, таких как размер элементов.')
    st.write('1D, 2D, 3D: Генерация сеток соответствующей размерности.')
    st.write('Optimize 3D (Netgen): Оптимизация трехмерной сетки с использованием алгоритмов Netgen.')
    st.write('Set order 1, 2, 3: Установка порядка элементов сетки.')
    st.write('High-order tools: Инструменты для работы с элементами высокого порядка.')
    st.write('Refine by splitting: Уточнение сетки путем деления элементов.')
    st.write('Partition, Unpartition: Разделение и слияние разделенных сеток.')
    st.write('Smooth 2D: Сглаживание двумерной сетки.')
    st.write('Recombine 2D, Reclassify 2D: Рекомбинация и переклассификация элементов двумерной сетки.')
    st.write('Experimental: Экспериментальные функции для работы со сеткой.')
    st.write('Reverse: Реверсирование направления элементов сетки.')
    st.write('Delete, Inspect: Удаление и инспектирование элементов сетки.')

    st.header('Solver')
    st.write('GetDP: Интеграция с решателем GetDP для выполнения численных расчетов на основе сетки.')

    st.header('View')
    st.write('Здесь будут отображаться инструменты для визуализации и манипулирования геометрией и сетками, но в данном интерфейсе они не отображаются.')

    st.header('Статусная строка')
    st.write('В нижней части интерфейса обычно отображается статусная строка, которая информирует пользователя о текущих действиях или сообщениях/ошибках программы.')
    st.image('screenshot.png', caption='')
    st.image('screenshot2.png', caption='')
    


    

if __name__ == '__main__':
    main()
