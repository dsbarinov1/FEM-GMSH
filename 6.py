import streamlit as st
import pyvista as pv
from st_pages import Page, show_pages, add_page_title
from stpyvista import stpyvista
import subprocess


def plot_mesh(mesh_file):
    # Визуализация с помощью pyvista
    mesh = pv.read(mesh_file)
    plotter = pv.Plotter()
    plotter.add_mesh(mesh, show_edges=True, color=True)
    # Вывод графика pyvista в streamlit
    plotter.view_isometric()
    stpyvista(plotter)

def union():
    b1 = st.button("Показать", key='bt1')
    if b1:
        st.image("6_1.png")


def diff():
    b2 = st.button("Показать", key = 'bt2')
    if b2:
        st.image("6_2.png")


def inter():

    b3 = st.button("Показать", key='bt3')
    if b3:
        st.image("6_3.png")

def main():
    st.title("Составные области")

    st.title('')
    r'''В GMSH можно создавать составные области, объединяя более простые геометрические фигуры. '''

    
    st.subheader('1. Объединение:')
    code = """
    union = gmsh.model.occ.fragment([(2, rectangle)], [(2, circle)], removeTool=False)
    """
    st.code(code, language="python")
    st.subheader('2. Разность:')
    code = """
    diff = gmsh.model.occ.cut([(2, rectangle)], [(2, circle)], removeTool=True)
    """
    st.code(code, language="python")
    st.subheader('3. Пересечение')
    code = """
    inter = gmsh.model.occ.intersect([(2, rectangle)], [(2, circle)], removeTool=True)
    """
    st.code(code, language="python")

    st.markdown('Пример объединения прямоугольной и круглой области:')
    union()
    st.markdown('Пример разности прямоугольной и круглой области:')
    diff()
    st.markdown('Пример пересечения прямоугольной и круглой области:')
    inter()



if __name__ == '__main__':
    main()

