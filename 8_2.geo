Point(1) = {0, 0, 0, 1.0};
Point(2) = {-1, 0, 0, 1.0};
Point(3) = {1, 0, 0, 1.0};
Circle(1) = {2, 1, 3};
Circle(2) = {3, 1, 2};

Transfinite Line{1, 2} = 20 Using Progression 1;

Line Loop(4) = {1,2};

Plane Surface(1) = {4};

Recombine Surface {1};

Mesh 2;