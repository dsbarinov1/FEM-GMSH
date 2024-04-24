import streamlit as st
import subprocess
import meshio
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import stpyvista
import pyvista as pv
import gmsh
import math

import streamlit as st
import subprocess
import meshio
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def plot_mesh(mesh_file):
    mesh = meshio.read(mesh_file)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(mesh.points[:, 0], mesh.points[:, 1], mesh.points[:, 2], triangles=mesh.cells_dict["triangle"])
    st.pyplot(fig)

st.title('Создание областей в Gmsh')


st.subheader('1. Инициализация Gmsh')
r'''Импортируем библиотеку и инициализируем объект.'''
st.code('''
import gmsh
gmsh.initialize()
''')

st.subheader('2. Создание новой модели')
r'''Создадим новую модель".'''
st.code('''
gmsh.model.add("Название модели")
''')

st.subheader('3. Определение геометрических элементов')
r'''Добавим геометрические элементы (точки, линии, кривые и т.д.), которые будут использоваться для создания области.'''
st.code('''
p1 = gmsh.model.geo.addPoint(x1, y1, z1, meshSize)
p2 = gmsh.model.geo.addPoint(x2, y2, z2, meshSize)
l1 = gmsh.model.geo.addLine(p1, p2)
''')

st.subheader('4. Формирование области')
r'''С помощью созданных геометрических элементов сформируем области, определив контуры и поверхности.'''
st.code('''
loop = gmsh.model.geo.addCurveLoop([l1, l2, l3, l4])
surface = gmsh.model.geo.addPlaneSurface([loop])
''')

st.subheader('5. Синхронизация геометрии')
r'''Синхронизируем геометрию с внутренней структурой Gmsh'''
st.code('''
gmsh.model.geo.synchronize()
''')

st.subheader('6. Генерация сетки')
r'''Сгенерируем сетку области'''
st.code('''
gmsh.model.mesh.generate(2)  # Для 2D сетки
''')

st.subheader('7. Экспорт сетки')
r'''Экспортируем сгенерированную сетку в файл'''
st.code('''
gmsh.write("output.msh")
''')

st.subheader('8. Завершение работы с Gmsh')
st.code('''
gmsh.finalize()
''')

st.subheader('Построение прямоугольной области')

code = """
gmsh.initialize()
gmsh.model.add("Rectangle")
x_min = 0
x_max = 10
y_min = 0
y_max = 5
z = 0
dx = 1
dy = 1
# Создание точек
p1 = gmsh.model.geo.addPoint(x_min, y_min, z, dx)
p2 = gmsh.model.geo.addPoint(x_max, y_min, z, dx)
p3 = gmsh.model.geo.addPoint(x_max, y_max, z, dx)
p4 = gmsh.model.geo.addPoint(x_min, y_max, z, dx)
# Создание линий
l1 = gmsh.model.geo.addLine(p1, p2)
l2 = gmsh.model.geo.addLine(p2, p3)
l3 = gmsh.model.geo.addLine(p3, p4)
l4 = gmsh.model.geo.addLine(p4, p1)
# Создание поверхности
ll = [l1, l2, l3, l4]
gmsh.model.geo.addCurveLoop(ll)
rectangle = gmsh.model.geo.addPlaneSurface([1])
# Задание физической области
gmsh.model.addPhysicalGroup(2, [rectangle], 1)
# Задание размера сетки
gmsh.model.mesh.setSize(gmsh.model.getEntities(0), 0.5)
# Генерация сетки
gmsh.model.geo.synchronize()
gmsh.model.mesh.generate(2)
# Сохранение модели в файл
gmsh.write("rectangle.msh")
# Выход из Gmsh
gmsh.finalize()
"""
st.code(code, language='python')

if st.button("Сгенерировать" ,key='button1'):
    mesh_file = "rectangle.msh"
    subprocess.run(["python3", "generate_mesh4.py", mesh_file])
    plot_mesh(mesh_file)

st.subheader('Построение круглой области')

code = """
gmsh.initialize()
gmsh.model.add("Circle")
# Задание параметров круга
center = (0, 0, 0)
radius = 1
num_segments = 20
# Создание точек на окружности
points = [gmsh.model.geo.addPoint(center[0] + radius * math.cos(2 * math.pi * i / num_segments),
                                   center[1] + radius * math.sin(2 * math.pi * i / num_segments),
                                   center[2], 0.05) for i in range(num_segments)]
lines = [gmsh.model.geo.addLine(points[i], points[(i + 1) % num_segments]) for i in range(num_segments)]
loop = gmsh.model.geo.addCurveLoop(lines)
circle = gmsh.model.geo.addPlaneSurface([loop])
gmsh.model.addPhysicalGroup(2, [circle], 1)
gmsh.model.mesh.setSize(gmsh.model.getEntities(0), 0.1)
gmsh.model.geo.synchronize()
gmsh.model.mesh.generate(2)
gmsh.write("circle.msh")
gmsh.finalize()
"""
st.code(code, language='python')

if st.button("Сгенерировать" ,key='button2'):
    mesh_file = "circle.msh"
    subprocess.run(["python3", "generate_mesh4.py", mesh_file])
    plot_mesh(mesh_file)
