import gmsh
import meshio
import matplotlib.pyplot as plt
import pyvista as pv
from mpl_toolkits.mplot3d import Axes3D
# Инициализация Gmsh


    gmsh.initialize()

    # Создание точек
    p1 = gmsh.model.geo.addPoint(0, 0, 0)
    p2 = gmsh.model.geo.addPoint(1, 0, 0)
    p3 = gmsh.model.geo.addPoint(1, 1, 0)
    p4 = gmsh.model.geo.addPoint(0, 1, 0)

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

    # Визуализация сетки (необязательно)
    #теперь выводится сразу график из matplotlib, а не открываетсяс gmsh
    #gmsh.fltk.run()

    gmsh.write("gmsh_test4.msh")
    # Creates graphical user interface
    mesh = meshio.read('gmsh_test4.msh')

    # Отображение данных с помощью matplotlib
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(mesh.points[:, 0], mesh.points[:, 1], mesh.points[:, 2], triangles=mesh.cells[1].data)
    plt.show()
    # Загрузка файла .msh в pyvista
    mesh = pv.read('gmsh_test4.msh')

# Визуализация с помощью pyvista
plotter = pv.Plotter()
plotter.add_mesh(mesh)  # Отображение сетки в белом цвете
plotter.show()

