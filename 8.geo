Point(1) = {-5, -5, 0, 1.0};
Point(2) = {-5, 5, 0, 1.0};
Point(3) = {15, -5, 0, 1.0};
Point(4) = {15, 5, 0, 1.0};

Point(5) = {0, 0, 0, 1.0};
Point(6) = {-1, 0, 0, 1.0};
Point(7) = {1, 0, 0, 1.0};

Line(1) = {1, 2};
Line(2) = {2, 4};
Line(3) = {4, 3};
Line(4) = {3, 1};

Circle(5) = {6, 5, 7};
Circle(6) = {7, 5, 6};

Curve Loop(1) = {1, 2, 3, 4};
Curve Loop(2) = {5, 6};
// Plane Surface(<id>) = {<id of curve loop>, ...}
Plane Surface(1) = {1, 2};

Physical Curve(1) = {7};
Physical Curve(2) = {6, 9};
Physical Curve(3) = {5};
Physical Curve(4) = {8};

// Physical Surface(id) = {<id of surface element>, ...}
Physical Surface(1) = {1};

Field[1] = Attractor;

Field[1].EdgesList = {5};

Field[2] = Threshold;
Field[2].IField = 1;
Field[2].LcMin = 0.25;
Field[2].LcMax = 1;
Field[2].DistMin = 1;
Field[2].DistMax = 2;

Background Field = 2;