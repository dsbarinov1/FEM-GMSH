import streamlit as st
import subprocess
import meshio
import matplotlib.pyplot as plt
import numpy as np

st.title("Сгущение сетки")

menu = st.sidebar.radio("*",
                        (
                         "Теория",
                         "Практика",
                         )
                        )
if menu == "Теория":
    st.write(
        "Сгущение сетки - это процесс увеличения количества элементов сетки в областях, где требуется более высокая точность вычислений. В GMSH сгущение сетки можно выполнить, используя инструменты рефининга сетки.")

    

    st.write("#### Шаг 1: Задание параметров рефининга сетки")
    st.write(
        "После генерации базовой сетки необходимо задать параметры рефининга сетки, которые определяют, где и как должно происходить сгущение сетки. В GMSH для этого можно использовать различные инструменты, включая команды `Refine`, `Coherence`, `Threshold` и другие.")

    st.write("#### Шаг 2: Выполнение рефининга сетки")
    st.write(
        "После того, как параметры рефининга сетки определены, можно выполнить сгущение сетки в GMSH, используя команду `Refine`. Это приведет к увеличению количества элементов сетки в областях, где это требуется для достижения более высокой точности вычислений.")

    st.write("#### Пример")
    st.write(
        "Ниже приведен пример кода на языке GMSH, который определяет квадратную область и генерирует сетку на основе треугольных элементов,а затем выполняет сгущение сетки:")

    st.code("""
        // Определение квадратной области
        Point(1) = {0, 0, 0, 1.0};
        Point(2) = {1, 0, 0, 1.0};
        Point(3) = {1, 1, 0, 1.0};
        Point(4) = {0, 1, 0, 1.0};
        Line(1) = {1, 2};
        Line(2) = {2, 3};
        Line(3) = {3, 4};
        Line(4) = {4, 1};
        Curve Loop(1) = {4, 1, 2, 3};
        Plane Surface(1) = {1};
    
        // Генерация базовой сетки
        Mesh.CharacteristicLengthMax = 0.2;
        Mesh 2;
    
        // Задание параметров рефининга сетки
        
    
        Field[1].NodesList = {1,2,3,4};
        Field[1].EdgesList = {1,2,3,4};
        Field[1].FacesList = {1};
        Field[1].XMin = 0.2;
    
    
        // Создание рефинированной сетки
        RefineMesh;
    
        // Сохранение сетки в файл
        Mesh.Save("square_mesh.msh");
        """)
    

    """При необходимости построенную сетку можно сгустить, используя кнопку Refine by splitting в модуле Mesh, либо запустив
в командной строке:"""
code = """$ gmsh mesh.geo -2 -refine"""
st.code(code)



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

    mesh_file = "circle_mesh.msh"

    distance = st.number_input('Distance', value=1.0, format="%.1f")
    threshold = st.number_input('Threshold', value=0.5, format="%.1f")
    min_size = st.number_input('Min', value=0.1, format="%.1f")
    max_size = st.number_input('Max', value=1.0, format="%.1f")



    if st.button("Сгенерировать"):
        subprocess.run(["python3", "generate_circle4.py", mesh_file, str(distance), str(threshold), str(min_size), str(max_size)])
        plot_mesh_from_file(mesh_file)