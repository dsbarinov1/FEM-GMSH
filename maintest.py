import streamlit as st
import subprocess
import meshio
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def plot_mesh_from_file(mesh_file):
    # Чтение сетки
    mesh = meshio.read(mesh_file)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(mesh.points[:, 0], mesh.points[:, 1], mesh.points[:, 2], triangles=mesh.cells_dict["triangle"])
    st.pyplot(fig)

    # Получение координат узлов и элементов
    points = mesh.points[:, :2]  # Используем только X и Y координаты
    cells = mesh.cells_dict["triangle"]  # Для треугольной сетки

    # Создание графика
    plt.figure(figsize=(8, 8))
    plt.gca().set_aspect('equal')

    # Отрисовка каждого треугольника
    for tri in cells:
        t_coords = np.append(tri, tri[0])  # Замыкание треугольника
        plt.plot(points[t_coords, 0], points[t_coords, 1], 'b-')

    # Отрисовка узлов
    plt.plot(points[:, 0], points[:, 1], 'ro')

    plt.title(f"Mesh Visualization: {mesh_file}")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()
    
# Пример использования для визуализации круглой и треугольной сеток
figure_type = st.selectbox("Выбирите тип фигуры:", ["Окружность", "Многоугольник"])
if figure_type == "Окружность":
        mesh_file = "circle_mesh.msh"
else: mesh_file = "triangle_mesh.msh"
if figure_type == 'Многоугольник': sides = st.slider("Количество углов" , 1, 30, 0)
else: sides = 0
radius = st.slider("Радиус" , 1.00, 10.0, 5.0)
mesh_size = st.slider("Размер сетки", 0.1, 1.00, 0.5)
if st.button("Сгенерировать"):
    
    subprocess.run(["python3", "generate_circle4.py", str(sides),str(radius), str(mesh_size), mesh_file ])
    plot_mesh_from_file(mesh_file)

def plot_mesh_from_file(mesh_file):
    # Чтение сетки
    mesh = meshio.read(mesh_file)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(mesh.points[:, 0], mesh.points[:, 1], mesh.points[:, 2], triangles=mesh.cells_dict["triangle"])
    st.pyplot(fig)

    # Получение координат узлов и элементов
    points = mesh.points[:, :2]  # Используем только X и Y координаты
    cells = mesh.cells_dict["triangle"]  # Для треугольной сетки

    # Создание графика
    plt.figure(figsize=(8, 8))
    plt.gca().set_aspect('equal')

    # Отрисовка каждого треугольника
    for tri in cells:
        t_coords = np.append(tri, tri[0])  # Замыкание треугольника
        plt.plot(points[t_coords, 0], points[t_coords, 1], 'b-')

    # Отрисовка узлов
    plt.plot(points[:, 0], points[:, 1], 'ro')

    plt.title(f"Mesh Visualization: {mesh_file}")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()
    
# Пример использования для визуализации круглой и треугольной сеток
figure_type = st.selectbox("Выбирите тип фигуры:", ["Окружность", "Многоугольник"])
if figure_type == "Окружность":
        mesh_file = "circle_mesh.msh"
else: mesh_file = "triangle_mesh.msh"
if figure_type == 'Многоугольник': sides = st.slider("Количество углов" , 1, 30, 0)
else: sides = 0
radius = st.slider("Радиус" , 1.00, 10.0, 5.0)
mesh_size = st.slider("Размер сетки", 0.1, 1.00, 0.5)
if st.button("Сгенерировать"):
    
    subprocess.run(["python3", "generate_circle4.py", str(sides),str(radius), str(mesh_size), mesh_file ])
    plot_mesh_from_file(mesh_file)
