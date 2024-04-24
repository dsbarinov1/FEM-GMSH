# gmsh_generate_mesh.py
import gmsh
import sys
import matplotlib.pyplot as plt
import meshio

def mark_subdomains_and_boundaries():
    gmsh.initialize()
    gmsh.model.add("marking_example")

    # Создаем геометрию, например, прямоугольник
    lc = 0.1
    p1 = gmsh.model.occ.addPoint(0, 0, 0, lc)
    p2 = gmsh.model.occ.addPoint(1, 0, 0, lc)
    p3 = gmsh.model.occ.addPoint(1, 1, 0, lc)
    p4 = gmsh.model.occ.addPoint(0, 1, 0, lc)
    l1 = gmsh.model.occ.addLine(p1, p2)
    l2 = gmsh.model.occ.addLine(p2, p3)
    l3 = gmsh.model.occ.addLine(p3, p4)
    l4 = gmsh.model.occ.addLine(p4, p1)
    ll = gmsh.model.occ.addCurveLoop([l1, l2, l3, l4])
    plane = gmsh.model.occ.addPlaneSurface([ll])

    # Маркирование подобластей
    # Указываем идентификатор элемента (в данном случае 1) и метку подобласти (в данном случае 1)
    gmsh.model.addPhysicalGroup(2, [plane], 1)
    gmsh.model.setPhysicalName(2, 1, "MARKER_1")

    # Маркирование граничных частей
    # Указываем идентификатор элемента (в данном случае 1) и метку граничной части (в данном случае 2)
    gmsh.model.addPhysicalGroup(1, [l1], 2)
    gmsh.model.setPhysicalName(1, 2, "BOUNDARY_1")

    # Генерация сетки
    gmsh.model.mesh.generate(2)
    # Отображаем графический интерфейс
    gmsh.fltk.run()
    gmsh.finalize()

def mark_subdomains_and_boundaries():
    gmsh.initialize()
    gmsh.option.setNumber("General.Terminal", 1)  # Включаем вывод в терминал

    # Создаем треугольник
    n1 = gmsh.model.geo.addPoint(0, 0, 0, 0.1)
    n2 = gmsh.model.geo.addPoint(1, 0, 0, 0.1)
    n3 = gmsh.model.geo.addPoint(0, 1, 0, 0.1)
    n4 = gmsh.model.geo.addPoint(0.5, 0.5, 1, 0.1)

    l1 = gmsh.model.geo.addLine(n1, n2)
    l2 = gmsh.model.geo.addLine(n2, n3)
    l3 = gmsh.model.geo.addLine(n3, n1)


    ll1 = gmsh.model.geo.addCurveLoop([l1, l2, l3])
    tria1 = gmsh.model.geo.addPlaneSurface([ll1])

    # Маркирование подобластей
    gmsh.model.addPhysicalGroup(2, [tria1], 1)
    gmsh.model.setPhysicalName(2, 1, "Interior")

    # Маркирование граничных частей
    gmsh.model.addPhysicalGroup(1, [l1], 2)
    gmsh.model.setPhysicalName(1, 2, "Edge")

    gmsh.model.addPhysicalGroup(1, [l2], 3)
    gmsh.model.setPhysicalName(1, 3, "Edge")

    gmsh.model.addPhysicalGroup(1, [l3], 4)
    gmsh.model.setPhysicalName(1, 4, "Edge")

    # Создание сетки
    gmsh.model.geo.synchronize()
    gmsh.model.mesh.generate(2)

    # Отображение окна с геометрией и сеткой
    gmsh.fltk.run()

    gmsh.finalize()

# Пример использования

if __name__ == "__main__":
    # output_file = sys.argv[1]
    # mark_subdomains_and_boundaries()
    mark_subdomains_and_boundaries()