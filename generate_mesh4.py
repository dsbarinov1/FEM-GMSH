# gmsh_generate_mesh.py
import gmsh
import sys
import matplotlib.pyplot as plt
import meshio


def generate_mesh(output_file, width, height, mesh_size ):
    gmsh.initialize()
    gmsh.model.add("Plane")

    # Создание точек
    p1 = gmsh.model.geo.addPoint(0, 0, 0, mesh_size)
    p2 = gmsh.model.geo.addPoint(width, 0, 0, mesh_size)
    p3 = gmsh.model.geo.addPoint(width, height, 0, mesh_size)
    p4 = gmsh.model.geo.addPoint(0, height, 0, mesh_size)

    # Создание линий
    l1 = gmsh.model.geo.addLine(p1, p2)
    l2 = gmsh.model.geo.addLine(p2, p3)
    l3 = gmsh.model.geo.addLine(p3, p4)
    l4 = gmsh.model.geo.addLine(p4, p1)

    # Создание контурной петли из линий
    curveLoop = gmsh.model.geo.addCurveLoop([l1, l2, l3, l4])

    # Использование контурной петли для создания плоской поверхности
    planeSurface = gmsh.model.geo.addPlaneSurface([curveLoop])

    # Синхронизация геометрии
    gmsh.model.geo.synchronize()

    # Генерация сетки для домена (необязательно)
    gmsh.model.mesh.generate(2)  # 2D сетка
    gmsh.write(output_file)

    # Визуализация сетки (необязательно)
    #теперь выводится сразу график из matplotlib, а не открываетсяс gmsh
    #gmsh.fltk.run()

    gmsh.write("gmsh_test4.msh")
    # Creates graphical user interface
    mesh = meshio.read('gmsh_test4.msh')


if __name__ == "__main__":
    output_file = sys.argv[1]
    width = float(sys.argv[2])
    height = float(sys.argv[3])
    mesh_size = float(sys.argv[4])
    generate_mesh( output_file, width, height, mesh_size)