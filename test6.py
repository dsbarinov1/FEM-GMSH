import gmsh
import meshio
import matplotlib.pyplot as plt
import pyvista as pv

def create_mesh(shape_type):
    gmsh.initialize()
    gmsh.model.add("mesh")

    if shape_type == "1":
        lc = 0.1
        gmsh.model.occ.addPoint(0, 0, 0, lc, 1)
        gmsh.model.occ.addDisk(0, 0, 0, 2, 1)
        gmsh.model.occ.synchronize()
        gmsh.model.mesh.generate(2)
    elif shape_type == "2":
        lc = 0.1
        x, y, z = 0, 0, 0
        dx, dy, dz = 2, 3, 0
        gmsh.model.occ.addRectangle(x, y, z, dx, dy)
        gmsh.model.occ.synchronize()
        gmsh.model.mesh.generate(2)
    elif shape_type == "3":
        lc = 0.1
        # Создаем вершины треугольника
        p1 = gmsh.model.geo.addPoint(0, 0, 0, 0.1)
        p2 = gmsh.model.geo.addPoint(1, 0, 0, 0.1)
        p3 = gmsh.model.geo.addPoint(0.5, 0.866, 0, 0.1)

        # Создаем линии треугольника
        l1 = gmsh.model.geo.addLine(p1, p2)
        l2 = gmsh.model.geo.addLine(p2, p3)
        l3 = gmsh.model.geo.addLine(p3, p1)

        # Создаем петлю из линий
        loop = gmsh.model.geo.addCurveLoop([l1, l2, l3])

        # Создаем геометрическую поверхность
        triangle = gmsh.model.geo.addPlaneSurface([loop])

        # Создаем сетку для геометрии
        gmsh.model.geo.synchronize()
        gmsh.model.mesh.generate(2)
    else:
        print("Неподдерживаемый тип формы")

    gmsh.model.geo.synchronize()
    gmsh.option.setNumber("Mesh.CharacteristicLengthMin", lc)
    gmsh.option.setNumber("Mesh.CharacteristicLengthMax", lc)
    gmsh.option.setNumber("Mesh.CharacteristicLengthFromPoints", 0)
    gmsh.option.setNumber("Mesh.CharacteristicLengthFromCurvature", 0)
    gmsh.model.mesh.generate(2)

    gmsh.fltk.run()
    gmsh.finalize()




def create_compound_area(mesh_type = 'triangular'):
    # пример использования
    gmsh.initialize()

    gmsh.model.add("Compound Area")
    rect_width = 200
    rect_height = 100
    circle_radius = 50
    circle_center = (100, 50, 0)

    # Создаем прямоугольник с помощью OpenCASCADE API
    rect = gmsh.model.occ.addRectangle(0, 0, 0, rect_width, rect_height)
    
    # Создаем круг с помощью OpenCASCADE API, уточняя радиусы по X и Y
    circle = gmsh.model.occ.addDisk(circle_center[0], circle_center[1], 0, circle_radius, circle_radius)  # Теперь указываем ry

    # Выолняем операцию вырезания
    cut, _ = gmsh.model.occ.cut([(2, rect)], [(2, circle)], removeObject=True, removeTool=True)

    gmsh.model.occ.synchronize()

    gmsh.model.mesh.generate(2)

    # gmsh.fltk.run()
    gmsh.write("gmsh_test6.msh")
    # Загрузка файла .msh в pyvista
    mesh = pv.read('gmsh_test6.msh')

    # Визуализация с помощью pyvista
    plotter = pv.Plotter()
    plotter.add_mesh(mesh)  # Отображение сетки в белом цвете
    plotter.show()
    gmsh.finalize()


    mesh = meshio.read('gmsh_test6.msh')

    # Отображение данных с помощью matplotlib
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(mesh.points[:, 0], mesh.points[:, 1], mesh.points[:, 2], triangles=mesh.cells[1].data)
    plt.show()
    # Загрузка файла .msh в pyvista
    mesh = pv.read('gmsh_test6.msh')



import gmsh

def create_compound_geometry():
    # Инициализация библиотеки GMSH
    gmsh.initialize()
    gmsh.model.add("compound_geometry")

    # Создаем простые геометрические формы
    r = gmsh.model.occ.addDisk(0, 0, 0, 1, 1)
    c = gmsh.model.occ.addCircle(0, 0, 0, 0.5)
    b = gmsh.model.occ.addBox(-1, -1, -1, 2, 2, 2)

    # Создаем объединенную область
    compound = gmsh.model.occ.fragment([(2, r)], [(2, c)], True)
    compound = gmsh.model.occ.fragment(compound[0], [(3, b)], True)

    # Строим сетку для объединенной геометрии
    gmsh.model.mesh.setCharacteristicLengthMin(0.2, -1)
    gmsh.model.mesh.setCharacteristicLengthMax(0.2, -1)
    gmsh.model.occ.synchronize()
    gmsh.model.mesh.generate(3)

    # Отображаем графический интерфейс
    gmsh.finalize()


def main():
    create_compound_geometry()
    # create_compound_area()
    create_mesh("3")
    create_mesh("1")
    create_mesh("2")

if __name__ == "__main__":
    main()