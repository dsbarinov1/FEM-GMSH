import sys
import pygmsh

# Получение аргументов из командной строки
box_x, box_y, box_z, box_size_x, box_size_y, box_size_z, sphere1_x, sphere1_y, sphere1_z, cil1_siz_x, cil1_siz_y, cil1_siz_z, sphere1_radius, sphere2_x, sphere2_y, sphere2_z, cil2_siz_x, cil2_siz_y, cil2_siz_z, sphere2_radius = map(float, sys.argv[1:])
with pygmsh.occ.Geometry() as geom:
    geom.characteristic_length_max = 0.1
    ellipsoid = geom.add_ellipsoid([box_x, box_y, box_z], [box_size_x, box_size_y, box_size_z])

    cylinders = [
        geom.add_cylinder([sphere1_x, sphere1_y, sphere1_z], [2.0, 0.0, 0.0], sphere1_radius),
        geom.add_cylinder([sphere2_x, sphere2_y, sphere2_z], [0.0, 2.0, 0.0], sphere2_radius)
    ]
    geom.boolean_difference(ellipsoid, geom.boolean_union(cylinders))

    mesh = geom.generate_mesh()
    mesh = geom.generate_mesh()
    mesh.write("output.stl")

'''
with pygmsh.occ.Geometry() as geom:
    geom.characteristic_length_max = 0.1
    ellipsoid = geom.add_ellipsoid([0.0, 0.0, 0.0], [1.0, 0.7, 0.5])

    cylinders = [
        geom.add_cylinder([-1.0, 0.0, 0.0], [2.0, 0.0, 0.0], 0.3),
        geom.add_cylinder([0.0, -1.0, 0.0], [0.0, 2.0, 0.0], 0.3),
        geom.add_cylinder([0.0, 0.0, -1.0], [0.0, 0.0, 2.0], 0.3),
    ]
    geom.boolean_difference(ellipsoid, geom.boolean_union(cylinders))

    mesh = geom.generate_mesh()
with pygmsh.occ.Geometry() as geom:

    # Создание куба с параметрами из командной строки
    box = geom.add_box([box_x, box_y, box_z], [box_size_x, box_size_y, box_size_z])

    # Создание шаров с параметрами из командной строки
    sphere1 = geom.add_ball([sphere1_x, sphere1_y, sphere1_z], sphere1_radius)
    #sphere2 = geom.add_ball([sphere2_x, sphere2_y, sphere2_z], sphere2_radius)

    # Объединение куба и шаров
#    union = geom.boolean_union([box, sphere1, sphere2])
    union = geom.boolean_union([box, sphere1])#, sphere2])
    #union = geom.boolean_difference([union, sphere2])#, sphere2])

    # Генерация сетки и экспорт в STL
    mesh = geom.generate_mesh()
    mesh.write("output.stl")
'''
