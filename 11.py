import streamlit as st
import subprocess
import meshio
import matplotlib.pyplot as plt
import numpy as np


st.title("Constructive Solid Geometry технологии в Gmsh")

menu = st.sidebar.radio("*",
                        (
                         "Теория",
                         "Практика",
                         )
                        )
if menu == "Теория":
    st.write("Constructive Solid Geometry (CSG) - это технология, используемая в GMSH для создания сложных геометрических объектов из простых геометрических форм. Она позволяет объединять, вычитать или пересекать простые формы, создавая более сложные объекты.")

    st.write("#### Шаг 1: Создание простых форм")
    st.write("Прежде чем можно будет использовать технологию CSG, необходимо создать простые геометрические формы, такие как куб, сфера или цилиндр. Это можно сделать в GMSH, используя инструменты создания форм, такие как Box, Sphere, Cylinder и другие.")

    st.write("#### Шаг 2: Создание более сложных форм с помощью технологии CSG")
    st.write("После того, как простые формы созданы, их можно объединять, вычитать или пересекать, используя технологию CSG в GMSH. Для этого можно использовать инструменты Boolean Union, Boolean Difference и Boolean Intersection в меню Geometry -> Boolean Operations.")

    st.write("#### Пример")
    st.write("Ниже приведен пример кода на языке GMSH, который создает куб и сферу, объединяет их в один объект и экспортирует его в формат STL:")

    st.code("""
   import pygmsh

 with pygmsh.occ.Geometry() as geom:
    # Создание куба
    box = geom.add_box([0, 0.3, 0.3], [0.5, 0.5, 3])
    
    # Создание первого шара
    sphere1 = geom.add_ball([0.9, 0.9, 0.9], 0.5)
    
    # Создание второго шара, симметричного первому относительно центра параллелепипеда по оси X и Y
    sphere2 = geom.add_ball([0.1, 0.1, 0.9], 0.5)
    
    # Объединение куба и шаров
    union = geom.boolean_union([box, sphere1])
    
    # Генерация сетки и экспорт в STL
    mesh = geom.generate_mesh()
    mesh.write("output.stl")
    """)

    st.write("После выполнения этого кода будет создан объект, состоящий из куба и сферы, и экспортирован в формат STL.")


if menu == "Практика":

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


    st.subheader("Задайте параметры геометрических фигур")

    # Ввод параметров для куба
    st.write("#### Параметры куба")
    box_x = st.number_input("Координата X для куба:", value=0.0, format="%.2f")
    box_y = st.number_input("Координата Y для куба:", value=0.3, format="%.2f")
    box_z = st.number_input("Координата Z для куба:", value=0.3, format="%.2f")
    box_size_x = st.number_input("Размер по оси X для куба:", value=0.5, format="%.2f")
    box_size_y = st.number_input("Размер по оси Y для куба:", value=0.5, format="%.2f")
    box_size_z = st.number_input("Размер по оси Z для куба:", value=3.0, format="%.2f")

    # Ввод параметров для первого шара
    st.write("#### Параметры первого шара")
    sphere1_x = st.number_input("Координата X для первого шара:", value=0.7, format="%.2f")
    sphere1_y = st.number_input("Координата Y для первого шара:", value=0.1, format="%.2f")
    sphere1_z = st.number_input("Координата Z для первого шара:", value=0.9, format="%.2f")
    sphere1_radius = st.number_input("Радиус первого шара:", value=0.5, format="%.2f")

    # Ввод параметров для второго шара
    st.write("#### Параметры второго шара")
    sphere2_x = st.number_input("Координата X для второго шара:", value=0.1, format="%.2f")
    sphere2_y = st.number_input("Координата Y для второго шара:", value=0.1, format="%.2f")
    sphere2_z = st.number_input("Координата Z для второго шара:", value=0.9, format="%.2f")
    sphere2_radius = st.number_input("Радиус второго шара:", value=0.5, format="%.2f")


    mesh_file = "output.stl"


    if st.button("Сгенерировать"):

        #Сборка аргументов в список строк
        args = [box_x, box_y, box_z, box_size_x, box_size_y, box_size_z, sphere1_x, sphere1_y, sphere1_z, sphere1_radius,
                sphere2_x, sphere2_y, sphere2_z, sphere2_radius]
        args_str = list(map(str, args))
        # Запуск script.py с аргументами
        subprocess.run(["python3", "3D.py"] + args_str)

    if st.button("Показать"):
        subprocess.run(["python3", "3D.py", mesh_file,
                        str(box_x), str(box_y),
                        str(box_z), str(box_size_x),
                        str(box_size_y), str(box_size_z),
                        str(sphere1_x), str(sphere1_y),
                        str(sphere1_z), str(sphere1_radius),
                        str(sphere2_x), str(sphere2_y),
                        str(sphere2_z), str(sphere2_radius)
                        ])
        plot_mesh_from_file(mesh_file)