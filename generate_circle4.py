import gmsh
import math
import sys
import matplotlib.pyplot as plt
import meshio


def create_circle_mesh(radius, mesh_size, output_file="circle_mesh.msh"):
    gmsh.initialize()
    gmsh.model.add("Circle")

    # Создание круглой границы
    center = gmsh.model.geo.addPoint(0, 0, 0, mesh_size)
    points = []
    num_points = 100  # Количество точек для аппроксимации круга
    for i in range(num_points):
        angle = 2 * math.pi * i / num_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        p = gmsh.model.geo.addPoint(x, y, 0, mesh_size)
        points.append(p)
    lines = [gmsh.model.geo.addLine(points[i], points[(i + 1) % num_points]) for i in range(num_points)]
    loop = gmsh.model.geo.addCurveLoop(lines)
    gmsh.model.geo.addPlaneSurface([loop])

    gmsh.model.geo.synchronize()
    gmsh.model.mesh.generate(2)
    gmsh.write(output_file)
    gmsh.finalize()

def create_polygon_mesh(sides, radius, mesh_size, output_file="polygon_mesh.msh"):
    gmsh.initialize()
    gmsh.model.add(f"{sides}-sided Polygon")

    # Создание вершин многоугольника
    points = []
    for i in range(sides):
        angle = 2 * math.pi * i / sides
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        p = gmsh.model.geo.addPoint(x, y, 0, mesh_size)
        points.append(p)
    lines = [gmsh.model.geo.addLine(points[i], points[(i + 1) % sides]) for i in range(sides)]
    loop = gmsh.model.geo.addCurveLoop(lines)
    gmsh.model.geo.addPlaneSurface([loop])

    gmsh.model.geo.synchronize()
    gmsh.model.mesh.generate(2)
    gmsh.write(output_file)


    gmsh.write("gmsh_test4.msh")

    mesh = meshio.read('circle_mesh.msh')
    mesh = meshio.read('triangle_mesh.msh')




    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(mesh.points[:, 0], mesh.points[:, 1], mesh.points[:, 2], triangles=mesh.cells[0].data)
    plt.show()
    gmsh.finalize()


def generate_mesh(distance, threshold, min_size, max_size):
    gmsh.initialize()
    gmsh.model.add("model")

    # Здесь добавьте вашу логику построения модели...
    # Например, построение простой фигуры или загрузка существующей модели.

    gmsh.model.geo.synchronize()

    # Создание поля для сгущения сетки
    field = gmsh.model.mesh.field.add("Threshold")
    gmsh.model.mesh.field.setNumber(field, "InField", 1)
    gmsh.model.mesh.field.setNumber(field, "DistanceMin", min_size)
    gmsh.model.mesh.field.setNumber(field, "DistanceMax", max_size)
    gmsh.model.mesh.field.setNumber(field, "Threshold", threshold)

    gmsh.model.mesh.field.setAsBackgroundMesh(field)

    gmsh.model.mesh.generate(2)

    # Экспорт сетки
    mesh_filename = "model.msh"
    gmsh.write(mesh_filename)
    gmsh.finalize()

    return mesh_filename


if (__name__ == "__main__"):
    sides = int(sys.argv[1])
    radius = float(sys.argv[2])  # Размер фигуры (например, радиус)
    mesh_size = float(sys.argv[3])  # Размер элемента сетки
    mesh_file = sys.argv[4]  # Имя файла вывода

# Пример использования
    
if  sides == 0: create_circle_mesh(radius, mesh_size, "circle_mesh.msh")
create_polygon_mesh(sides, radius, mesh_size,  "triangle_mesh.msh")  # Пример для треугольника
