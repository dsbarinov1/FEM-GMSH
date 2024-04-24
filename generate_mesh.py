import pygmsh
import numpy as np
import sys
import json

def generate_circle_mesh(num_nodes, radius):
    geom = pygmsh.geo.Geometry()
    with geom as geom:
        circle = geom.add_circle([0.0, 0.0, 0.0], radius, mesh_size=0.1)
        geom.add_physical(circle.surface, label="circle_surface")
    mesh = pygmsh.generate_mesh(geom)
    nodes = mesh.points[:, :2]
    elements = mesh.cells_dict["triangle"]
    return nodes.tolist(), elements.tolist()

def generate_polygon_mesh(num_nodes, num_sides):
    geom = pygmsh.geo.Geometry()
    with geom as geom:
        poly_points = []
        for i in range(num_sides):
            angle = 2 * np.pi * i / num_sides
            x = np.cos(angle)
            y = np.sin(angle)
            poly_points.append([x, y, 0.0])
        poly = geom.add_polygon(poly_points, mesh_size=0.1)
        geom.add_physical(poly.surface, label="polygon_surface")
    mesh = pygmsh.generate_mesh(geom)
    nodes = mesh.points[:, :2]
    elements = mesh.cells_dict["triangle"]
    return nodes.tolist(), elements.tolist()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python mesh_generator.py shape num_nodes_or_sides radius_or_none")
        sys.exit(1)
    
    shape = sys.argv[1]
    num_nodes_or_sides = int(sys.argv[2])
    radius_or_none = float(sys.argv[3]) if sys.argv[3] != "None" else None
    
    if shape == "circle":
        nodes, elements = generate_circle_mesh(num_nodes_or_sides, radius_or_none)
    elif shape == "polygon":
        nodes, elements = generate_polygon_mesh(num_nodes_or_sides, radius_or_none)
    else:
        print("Invalid shape")
        sys.exit(1)
    
    result = {
        "nodes": nodes,
        "elements": elements
    }
    print(json.dumps(result))
