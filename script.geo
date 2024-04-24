
    SetFactory("OpenCASCADE");

    // Создаем прямоугольник
    lc = 1.0; // Размер элемента сетки
    Point(1) = {0, 0, 0, lc};
    Point(2) = {10, 0, 0, lc};
    Point(3) = {10, 10, 0, lc};
    Point(4) = {0, 10, 0, lc};
    Line(1) = {1, 2};
    Line(2) = {2, 3};
    Line(3) = {3, 4};
    Line(4) = {4, 1};
    Curve Loop(1) = {1, 2, 3, 4};
    Plane Surface(1) = {1};
    
    // Создаем объем
    Extrude {0, 0, 10}
    
    {
        Surface{1};
    }

    // Генерируем сетку
    Mesh 3;
    