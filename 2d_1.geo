// инициализация переменных
x0 = 0;
x1 = 1;
y0 = 0;
y1 = 1;
x_c = (x0 + x1) / 2;
y_c = (y0 + y1) / 2;
cl_1 = 0.05;
cl_2 = 0.025;
rad = 0.25;

If (2 * rad >= x1 - x0 || 2 * rad >= y1 - y0)
  Printf("Error! Diameter is too large!");
  //Exit;
EndIf

// точки прямоугольника
Point(1) = {x0, y0, 0, cl_1};
Point(2) = {x1, y0, 0, cl_1};
Point(3) = {x0, y1, 0, cl_1};
Point(4) = {x1, y1, 0, cl_1};

// точки окружности
Point(10) = {x_c, y_c, 0, cl_2};
Point(11) = {x_c-rad, y_c, 0, cl_2};
Point(12) = {x_c+rad, y_c, 0, cl_2};
Point(13) = {x_c, y_c-rad, 0, cl_2};
Point(14) = {x_c, y_c+rad, 0, cl_2};

// линии прямоугольника
Line(1) = {1, 2};
Line(2) = {1, 3};
Line(3) = {2, 4};
Line(4) = {3, 4};

// линии окружности
Circle(11) = {11, 10, 13};
Circle(12) = {13, 10, 12};
Circle(13) = {12, 10, 14};
Circle(14) = {14, 10, 11};

// замкнутый контур прямоугольника
Line Loop(21) = {1, 3, -4, -2};

// замкнутый контур окружности
Line Loop(22) = {11, 12, 13, 14};

// поверхности
Plane Surface(1) = {21, 22};
Plane Surface(2) = {22};