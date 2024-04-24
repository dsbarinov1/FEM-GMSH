import streamlit as st
from st_pages import Page, show_pages, add_page_title
import numpy as np

def gmsh_overview():
    st.title("Общая характеристика Gmsh")

    st.markdown("""
    ## Что такое Gmsh?
    
    Gmsh - это программное обеспечение для генерации трехмерных неструктурированных сеток с большим количеством инструментов для построения сложных геометрических моделей и проведения численных расчетов.
    
    Является одним из наиболее популярных инструментов для генерации сеток в научных и инженерных приложениях.
                
    ## Структура программного компонента
    Gmsh состоит из четырёх модулей:

    - геометрия

    - сетка

    - решатель

    - постпроцессор

    Параметры ввода в эти модули можно задавать либо интерактивно с помощью графического интерфейса пользователя, либо в текстовых файлах ASCII с помощью собственного языка сценариев Gmsh.

                
    ## Основные характеристики

    - **Мультиплатформенность**: Gmsh поддерживается на операционных системах Windows, macOS и Linux, что делает его доступным для широкого круга пользователей.
    
    - **Открытый исходный код**: Gmsh распространяется под лицензией GNU General Public License (GPL), что позволяет пользователям свободно использовать, изменять и распространять программу.

    - **Интеграция с другими пакетами**: Gmsh интегрируется с различными инструментами для численного моделирования, такими как FEniCS, OpenFOAM и другими.

    - **Гибкий интерфейс пользователя**: Gmsh предоставляет простой и интуитивно понятный пользовательский интерфейс, позволяющий пользователям легко создавать и редактировать геометрические модели.

    - **Автоматизация через скрипты**: Gmsh поддерживает автоматизацию процесса моделирования через скрипты на языке Python, что делает его удобным инструментом для автоматизации и оптимизации задач.
                
    ## Области применения

    Gmsh используется для построения конечно-элементых сеток с целью аппроксимации моделируемого тела, учитывающей все важные для расчета ньюансы геометрии тела.
    Таким образом, область применения кончается там, где кончается область использования самих конечно-элементых сеток.
    Примеры областей применения метода конечных элементов:
    - **Теплопроводность**
    - **Механика**
    - **Гидродинамика**
    - **Электродинамика**
    - **Диффузия**
    """)

    
    st.header('Установка Gmsh')

    st.write('Для установки Gmsh можно воспользоваться различными методами:')

    st.subheader('1. Установка через менеджер пакетов (Linux):')
    
    st.code('sudo apt-get install gmsh', language='bash')
    

    st.subheader('2. Установка из исходного кода:')
    st.write('Скачайте исходный код с [официального сайта](https://gmsh.info/), затем:')
    
    code = r"""
    mkdir build
    cd build
    cmake ..
    make
    sudo make install
    """
    st.code(code, language='bash')

    st.subheader('3. Установка через pip (Python):')
    
    st.code('pip install gmsh', language='bash')
    

    st.subheader('4. Установка через Conda:')
    
    st.code('conda install -c conda-forge gmsh', language='bash')
    

    st.header('Использование Gmsh в Python')

    st.write('После установки Gmsh вы можете импортировать его в свой Python-скрипт:')
    st.code('import gmsh', language='python')


if __name__ == "__main__":
    gmsh_overview()