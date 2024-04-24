import streamlit as st
import subprocess
import meshio
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_mesh(mesh_file):
    mesh = meshio.read(mesh_file)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(mesh.points[:, 0], mesh.points[:, 1], mesh.points[:, 2], triangles=mesh.cells_dict["triangle"])
    st.pyplot(fig)

st.title("Gmsh Mesh Visualization in Streamlit")

width = st.sidebar.slider("Width", 0.01, 5.0, 2.0)
height = st.sidebar.slider("Height", 0.01, 5.0, 2.0)
mesh_size = st.sidebar.slider("Mesh Size", 0.01, 0.5, 0.01)

if st.button("Generate and Show Mesh"):
    mesh_file = "gmsh_test4.msh"
    subprocess.run(["python3", "generate_mesh4.py", mesh_file, str(width), str(height), str(mesh_size), ])
    plot_mesh(mesh_file)
