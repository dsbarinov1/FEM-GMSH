# gmsh_generate_mesh.py
import gmsh
import sys
import matplotlib.pyplot as plt
import meshio


def union_mesh(output_file, width1, height1, width2, height2):
    gmsh.initialize()
    gmsh.model.add("union_example")
    # if (selectbox_1 == "Прямоугольник")
    #     rectangle = gmsh.model.occ.addRectangle(0, 0, 0, width1, height1)
    # elif (selectbox_1 == "Окружность")
    #     rectangle = gmsh.model.occ.addDisk(0, 0, 0, width1, height1)
    #
    # if (selectbox_2 == "Прямоугольник")
    #     circle = gmsh.model.occ.addDisk(0.5, 0.5, 0, width2, height2)
    # elif (selectbox_2 == "Окружность")
    #     circle = gmsh.model.occ.addRectangle(0.5, 0.5, 0, width2, height2)
    rectangle = gmsh.model.occ.addRectangle(0, 0, 0, width1, height1)
    circle = gmsh.model.occ.addDisk(0.5, 0.5, 0, width2, height2)
    union = gmsh.model.occ.fragment([(2, rectangle)], [(2, circle)], removeTool=False)

    gmsh.model.occ.synchronize()
    gmsh.model.mesh.generate(2)

    # Синхронизация геометрии
    gmsh.model.geo.synchronize()

    # Генерация сетки для домена (необязательно)
    gmsh.model.mesh.generate(2)  # 2D сетка

    # Отображаем графический интерфейс
    # gmsh.fltk.run()
    gmsh.write(output_file)

    # Визуализация сетки (необязательно)
    #теперь выводится сразу график из matplotlib, а не открываетсяс gmsh
    # gmsh.fltk.run()

    # Creates graphical user interface
    gmsh.finalize()

def diff_mesh(output_file, width):
    gmsh.initialize()
    gmsh.model.add("difference_example")

    rectangle = gmsh.model.occ.addRectangle(0, 0, 0, 2, 4)
    circle = gmsh.model.occ.addDisk(0.5, 0.5, 0, 2,2)

    difference = gmsh.model.occ.cut([(2, rectangle)], [(2, circle)], removeTool=True)

    gmsh.model.occ.synchronize()
    gmsh.model.mesh.generate(2)
    gmsh.fltk.run()
    gmsh.write(output_file)
    gmsh.finalize()

def intersec_mesh(output_file, width):
    gmsh.initialize()
    gmsh.model.add("intersection_example")
    rectangle = gmsh.model.occ.addRectangle(0, 0, 0, 2, 2)
    circle = gmsh.model.occ.addDisk(0.5, 0.5, 0, 0.2, 0.5)
    intersection = gmsh.model.occ.intersect([(2, rectangle)], [(2, circle)])
    gmsh.model.occ.synchronize()
    gmsh.model.mesh.generate(2)
    gmsh.fltk.run()
    gmsh.write(" intersec_mesh.msh")
    gmsh.finalize()

if __name__ == "__main__":
    output_file = sys.argv[1]
    width_1 = float(sys.argv[2])
    height_1 = float(sys.argv[3])
    width_2 = float(sys.argv[4])
    height_2 = float(sys.argv[5])
    # selectbox_1 =sys.argv[6]
    # selectbox_2 = sys.argv[7]
    # print(selectbox_1)
    # print(selectbox_2)
    if output_file == "union_mesh6.msh":
        union_mesh(output_file, width_1, height_1, width_2, height_2)
    elif output_file == "diff_mesh6.msh":
        diff_mesh(output_file, width)
    elif output_file == "intersec_mesh6.msh":
        intersec_mesh(output_file, width)