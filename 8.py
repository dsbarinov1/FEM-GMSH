import streamlit as st

def rectangle_mesh():
    st.header("Пример 1: Создание структурированной квадратичной сетки для прямоугольника")

    st.subheader("1. Создание геометрии")
    st.code("""
    // Создание геометрии
    Point(1) = {-5, -5, 0, 1.0};
    Point(2) = {-5, 5, 0, 1.0};
    Point(3) = {15, -5, 0, 1.0};
    Point(4) = {15, 5, 0, 1.0};
    """)

    st.subheader("2. Определение линий")
    st.code("""
    // Определение линий
    Line(1) = {1, 2};
    Line(2) = {2, 4};
    Line(3) = {4, 3};
    Line(4) = {3, 1};
    """)

    st.subheader("3. Задание структурированной сетки")
    st.code("""
    // Задание структурированной сетки
    Transfinite Line {1, 3} = 10 Using Progression 1;
    Transfinite Line {2, 4} = 20 Using Progression 1;
    """)

    st.subheader("4. Определение контура и поверхности")
    st.code("""
    // Определение контура и поверхности
    Line Loop(1) = {1, 2, 3, 4};
    Plane Surface(1) = {1};
    """)
    st.image("8_7.png")

    st.subheader("5. Определение структурированной поверхности и объединение ее")
    st.code("""
    // Определение структурированной поверхности и объединение ее
    Transfinite Surface {1};
    Recombine Surface {1};
    """)

    st.subheader("6. Генерация сетки")
    st.code("""
    // Генерация сетки
    Mesh 2;
    """)

    st.image("8_8.png")

def circle_mesh():
    st.header("Пример 2: Создание неструктурированной квадратичной сетки для круга")

    st.subheader("1. Создание геометрии")
    st.code("""
    // Создание геометрии (круг)
    Point(1) = {0, 0, 0, 1.0};
    Point(2) = {-1, 0, 0, 1.0};
    Point(3) = {1, 0, 0, 1.0};

    Circle(1) = {2, 1, 3};
    Circle(2) = {3, 1, 2};
    """)

    st.subheader("2. Задание сетки для окружности")
    st.code("""
    // Задание сетки для окружности
    Transfinite Line{1, 2} = 20 Using Progression 1;
    """)

    st.subheader("3. Определение контура и поверхности")
    st.code("""
    // Определение контура и поверхности
    Line Loop(4) = {1,2};
    Plane Surface(1) = {4};
    """)

    st.subheader("4. Треугольники -> прямоугольники")
    st.code("""
    Recombine Surface {1};
    """)

    st.subheader("5. Генерация сетки")
    st.code("""
    // Генерация сетки
    Mesh 2;
    """)
    st.image("8_9.png")

st.title("Генерация сетки")

st.markdown("""
### Построение простой сетки

В качестве примера построим следующую простую геометрию:
""")

st.image('geo2.png', caption='Плоская геометрия')


st.markdown("""
- Определим точки прямоугольника в пространстве:
```cpp
// Point(<id>) = {<X>, <Y>, <Z>, <Заданная сетка в точке>}
Point(1) = {-5, -5, 0, 1.0};
Point(2) = {-5, 5, 0, 1.0};
Point(3) = {15, -5, 0, 1.0};
Point(4) = {15, 5, 0, 1.0};
```
""")
st.image('8_1.png')

st.markdown("""
- Для окружности нам нужно 3 точки, чтобы отследить дугу окружности:
```cpp
Point(5) = {0, 0, 0, 1.0};
Point(6) = {-1, 0, 0, 1.0};
Point(7) = {1, 0, 0, 1.0};
```
""")
st.image('8_2.png')

st.markdown("""
**Закрываем форму линиями:**
- Для прямоугольника (прямые линии):
```cpp
// Line(<id>) = {<id начальной точки>, <id конечной точки>}
Line(1) = {1, 2};
Line(2) = {2, 4};
Line(3) = {4, 3};
Line(4) = {3, 1};
```
""")
st.image('8_3.png')
            
st.markdown("""
- Для дуг окружности:
```cpp
// Circle(<id>) = {<id начальной точки>, <id точки посередине>, <id конечной точки>}
Circle(5) = {6, 5, 7};
Circle(6) = {7, 5, 6};
```
""")
st.image('8_4.png')

st.markdown("""
**Замечание:** Окружности также считаются линиями, поэтому `<id>` должен отличаться от идентификаторов линий.

**Закройте линии с помощью Curve Loop, а затем создайте поверхность из них с помощью Plane Surface.** Окончательная плоская поверхность будет ограничена кривыми петлями как прямоугольника, так и окружности.
```cpp
// Curve Loop(<id>) = {<id линии>, ...}
Curve Loop(1) = {1, 2, 3, 4};
Curve Loop(2) = {5, 6};
// Plane Surface(<id>) = {<id кривой петли>, ...}
Plane Surface(1) = {1, 2};
```
После этого уже возможно построить сетку с помощью интерфейса gmsh, перейдя по вкладкам: Modules -> Mesh -> 2D.
""")
st.image('8_5.png')

st.markdown("""
### Физические группы

Добавим физическую поверхность для 2D-геометрии (или Физический объем, если работает с 3D-геометрией).
```cpp
// Physical Curve(<id>) = {<id элемента кривой>, ...}
Physical Curve(1) = {7};
Physical Curve(2) = {6, 9};
Physical Curve(3) = {5};
Physical Curve(4) = {8};
            
// Physical Surface(id) = {<id элемента поверхности>, ...}
Physical Surface(1) = {1};
```
""")

st.markdown("""
### Сетка

**Неструктурированная сетка**

Attractor - указывает к какому физическому объекту необходимо сгущать сетку (с целью повышения точности вблизи данного объекта). 

Инициализируем attractor:

```cpp
Field[1] = Attractor;
```

Загущаем сетку ближе к окружности в данном случае:

```cpp
Field[1].EdgesList = {5};
```

Введем необходимые параметры сгущения сетки (минимальная/максимальная характеристическая длина и минимальное/максимальное расстояние "уточнения" сетки):

```cpp
Field[2].IField = 1;
Field[2].LcMin = 0.25;
Field[2].LcMax = 1;
Field[2].DistMin = 1;
Field[2].DistMax = 2;
```

Применим наш "загуститель" сетки к Field[2]:

```cpp
Background Field = 2;
```

Получившаяся сетка, как видно из графика ниже, начинает сгущаться к границам окружности:
""")
st.image('8_6.png')

option = st.selectbox(
    "Выберите пример:",
    ("Прямоугольник", "Круг")
)

if option == "Прямоугольник":
    rectangle_mesh()
elif option == "Круг":
    circle_mesh()