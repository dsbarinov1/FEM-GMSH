import streamlit as st
import gmsh
import subprocess
import meshio
import matplotlib.pyplot as plt
import numpy as np

st.title("Сгущение сетки")

st.write(
    "Сгущение сетки - это процесс увеличения количества элементов сетки в областях, где требуется более высокая точность вычислений. В GMSH сгущение сетки можно выполнить, используя инструменты рефининга сетки.")

st.write("#### Шаг 1: Определение геометрии и генерация сетки")
st.write(
    "Прежде чем можно будет выполнить сгущение сетки, необходимо определить геометрию модели и сгенерировать базовую сетку в GMSH, используя описанные в предыдущем слайде шаги.")

st.write("#### Шаг 2: Задание параметров рефининга сетки")
st.write(
    "После генерации базовой сетки необходимо задать параметры рефининга сетки, которые определяют, где и как должно происходить сгущение сетки. В GMSH для этого можно использовать различные инструменты, включая команды `Refine`, `Coherence`, `Threshold` и другие.")

st.write("#### Шаг 3: Выполнение рефининга сетки")
st.write(
    "После того, как параметры рефининга сетки определены, можно выполнить сгущение сетки в GMSH, используя команду `Refine`. Это приведет к увеличению количества элементов сетки в областях, где это требуется для достижения более высокой точности вычислений.")

st.write("#### Пример")
st.write(
    "Ниже приведен пример кода на языке GMSH, который определяет квадратную область и генерирует сетку на основе треугольных элементов,а затем выполняет два уровня сгущения сетки в области, близкой к центру квадрата:")

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
    Plane Surface(1) = {1, 2, 3, 4};

    // Генерация базовой сетки
    Mesh.CharacteristicLengthMax = 0.2;
    Mesh 2;

    // Задание параметров рефининга сетки
    Field[1] = Distance;
    Field[2] = Threshold;
    Field[3] = Min;
    Field[4] = Max;
    Field[5] = Angle;
    Field[6]= Anisotropic;
    Field[7] = Symmetric;
    Field[8] = Transfinite;
    Field[9] = Alignment;
    Field[10] = BoundaryLayer;
    Field[11] = Cascade;
    Field[12] = Compound;
    Field[13] = Coherence;
    Field[14] = Curvature;
    Field[15] = Density;
    Field[16] = Gradient;
    Field[17] = Hex;
    Field[18] = Length;
    Field[19] = Levelling;
    Field[20] = Metric;
    Field[21] = Orientation;
    Field[22] = Periodic;
    Field[23] = Sizing;
    Field[24] = Smooth;
    Field[25] = Threshold;
    Field[26] = Transfinite;
    Field[27] = Volume;

    Field[1].NodesList = {1,2,3,4};
    Field[1].EdgesList = {1,2,3,4};
    Field[1].FacesList = {1};
    Field[1].XMin = 0.2;


    // Создание рефинированной сетки
    RefineMesh;

    // Сохранение сетки в файл
    Mesh.Save("square_mesh.msh");
    """)
