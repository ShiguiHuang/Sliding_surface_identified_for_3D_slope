# Sliding_surface_identified_for_3D_slope

> 英文为机翻，可能不太对。
>
> English for machine translation, may not be right.

## 1 背景 / Background

本项目为论文《**Identifying and analyzing the distribution of sliding surfaces in rock slopes using total displacement contour maps**》中的 “***Availability on 3D slopes and computational efficiency***” 章节的具体实现代码。

This project is the specific implementation code of the Section "***4.4 Availability on 3D slopes and computational efficiency***" in the paper "***Identifying and analyzing the distribution of sliding surfaces in slopes using total displacement contour maps***"

其他部分实现代码也可参照该项目修改后实现。

Other parts of the implementation code can also be modified with reference to the project.

## 2 文件和使用说明 / Files and instructions

### 2.1 项目结构 / Project structure

│  **list.txt** # 不重要文件 / Not important files
│  **README.md** # 帮助文件 / help file
│  **Slice_boundary.png** # 用于提取边界点的图片文件 / Image file for extracting boundary points
│  **Sliding_identification_program.ipynb** # 主要的文件，逻辑代码基本在这个文件中 / The main file, the logic code is basically in this file
│  **坐标.svg** # 不重要文件 / Not important files
│  **坐标.vsdx** # 不重要文件 / Not important files
│  **获取文件名.bat** # 不重要文件 / Not important files
│  
├─**markdown_img_of_README** # 不重要文件 / Not important files
│      **坐标.svg** # 不重要文件 / Not important files
│      
├─**program_process_files** # 程序主要资源文件夹 / Program main resource folder
│      **Slice_slide_02.50.png** # 待识别滑面的切片，下同，数字表示z轴，代码的坐标系和论文有所不同! / The slice of the sliding surface to be identified, the same below, the number represents the z-axis, the coordinate system of the code and the paper are different!
│      **Slice_slide_05.00.png**
│      **Slice_slide_10.00.png**
│      **Slice_slide_15.00.png**
│      **Slice_slide_20.00.png**
│      **Slice_slide_25.00.png**
│      **Slice_slide_30.00.png**
│      **Slice_slide_35.00.png**
│      **Slice_slide_40.00.png**
│      **Slice_slide_45.00.png**
│      **Slice_slide_47.50.png**
│      
└─**pythonProject** # PyCharm 项目文件夹，用于绘制3D边坡滑面 / PyCharm project folder for drawing 3D slope sliding surfaces
    │  **draw_slope_and_sliding_surface.py** # 绘制3D边坡滑面代码文件 / Drawing 3D slope sliding surface code file
    │  
    └─**.idea** # PyCharm 默认配置文件，下同 / PyCharm default configuration file, same below
        │  **.gitignore**
        │  **misc.xml**
        │  **modules.xml**
        │  **pythonProject.iml**
        │  **workspace.xml**
        │  
        └─**inspectionProfiles**
                **profiles_settings.xml**
                **Project_Default.xml**

### 2.2 使用说明 / Instructions

1. 使用 *Jupyter notebook* 打开主文件夹；

   Open the main folder using *Jupyter notebook*;

2. 按照 `Sliding_identification_program.ipynb`运行，得到其他文件；

   Run according to `Sliding _ identification _ program.ipynb` to get other files;

3. 使用 PyCharm 打开 `pythonProject` 项目，运行之后即可。

   Open the`pythonProject` project with PyCharm and run it.

## 3 项目依赖环境 /Projects depend on the environment

| Package                       | Version     |
| ----------------------------- | ----------- |
| aiofiles                      | 23.1.0      |
| aiohttp                       | 3.8.4       |
| aiosignal                     | 1.3.1       |
| alphashape                    | 1.3.1       |
| altair                        | 4.2.2       |
| anyio                         | 3.6.2       |
| astor                         | 0.8.1       |
| asttokens                     | 2.2.1       |
| async-timeout                 | 4.0.2       |
| attrdict                      | 2.0.1       |
| attrs                         | 22.2.0      |
| Babel                         | 2.12.1      |
| backcall                      | 0.2.0       |
| backports.functools-lru-cache | 1.6.4       |
| bce-python-sdk                | 0.8.83      |
| beautifulsoup4                | 4.12.2      |
| Brotli                        | 1.0.9       |
| cachetools                    | 5.3.0       |
| certifi                       | 2022.12.7   |
| cffi                          | 1.15.1      |
| charset-normalizer            | 3.1.0       |
| click                         | 8.1.3       |
| click-log                     | 0.4.0       |
| colorama                      | 0.4.6       |
| comm                          | 0.1.3       |
| comtypes                      | 1.3.1       |
| contourpy                     | 1.0.7       |
| cssselect                     | 1.2.0       |
| cssutils                      | 2.6.0       |
| cycler                        | 0.11.0      |
| Cython                        | 0.29.34     |
| debugpy                       | 1.6.7       |
| decorator                     | 5.1.1       |
| descartes                     | 1.1.0       |
| EasyProcess                   | 1.1         |
| entrypoint2                   | 1.1         |
| entrypoints                   | 0.4         |
| et-xmlfile                    | 1.1.0       |
| executing                     | 1.2.0       |
| fastapi                       | 0.95.0      |
| ffmpy                         | 0.3.0       |
| filelock                      | 3.11.0      |
| fire                          | 0.5.0       |
| Flask                         | 2.2.3       |
| flask-babel                   | 3.1.0       |
| fonttools                     | 4.39.3      |
| frozenlist                    | 1.3.3       |
| fsspec                        | 2023.4.0    |
| future                        | 0.18.3      |
| gensim                        | 4.3.1       |
| gevent                        | 22.10.2     |
| geventhttpclient              | 2.0.2       |
| gradio                        | 3.25.0      |
| gradio_client                 | 0.0.10      |
| greenlet                      | 2.0.2       |
| grpcio                        | 1.53.0      |
| h11                           | 0.14.0      |
| httpcore                      | 0.17.0      |
| httpx                         | 0.24.0      |
| huggingface-hub               | 0.13.4      |
| idna                          | 3.4         |
| imageio                       | 2.27.0      |
| imgaug                        | 0.4.0       |
| importlib-metadata            | 6.3.0       |
| importlib-resources           | 5.12.0      |
| ipykernel                     | 6.22.0      |
| ipython                       | 8.12.0      |
| itsdangerous                  | 2.1.2       |
| jedi                          | 0.18.2      |
| Jinja2                        | 3.1.2       |
| joblib                        | 1.2.0       |
| jsonschema                    | 4.17.3      |
| jupyter_client                | 8.1.0       |
| jupyter_core                  | 5.3.0       |
| kiwisolver                    | 1.4.4       |
| linkify-it-py                 | 2.0.0       |
| llvmlite                      | 0.40.0      |
| lmdb                          | 1.4.1       |
| lxml                          | 4.9.2       |
| markdown-it-py                | 2.2.0       |
| MarkupSafe                    | 2.1.2       |
| matplotlib                    | 3.7.1       |
| matplotlib-inline             | 0.1.6       |
| mdit-py-plugins               | 0.3.3       |
| mdurl                         | 0.1.2       |
| mpmath                        | 1.3.0       |
| mss                           | 8.0.2       |
| multidict                     | 6.0.4       |
| nest-asyncio                  | 1.5.6       |
| networkx                      | 3.1         |
| numba                         | 0.57.0      |
| numpy                         | 1.24.3      |
| onnx                          | 1.13.1      |
| opencv-contrib-python         | 4.6.0.66    |
| opencv-python                 | 4.1.2.30    |
| openpyxl                      | 3.1.2       |
| opt-einsum                    | 3.3.0       |
| orjson                        | 3.8.10      |
| packaging                     | 23.1        |
| paddle-bfloat                 | 0.1.7       |
| paddleocr                     | 2.6.1.3     |
| paddlepaddle                  | 2.4.2       |
| pandas                        | 2.0.0       |
| parso                         | 0.8.3       |
| pdf2docx                      | 0.5.6       |
| pickleshare                   | 0.7.5       |
| Pillow                        | 9.5.0       |
| pip                           | 23.0.1      |
| pkgutil_resolve_name          | 1.3.10      |
| platformdirs                  | 3.2.0       |
| premailer                     | 3.10.0      |
| prompt-toolkit                | 3.0.38      |
| protobuf                      | 3.20.2      |
| psutil                        | 5.9.4       |
| pure-eval                     | 0.2.2       |
| pyaes                         | 1.6.1       |
| pyclipper                     | 1.3.0.post4 |
| pycparser                     | 2.21        |
| pycryptodome                  | 3.17        |
| pydantic                      | 1.10.7      |
| pyDOE2                        | 1.3.0       |
| pydub                         | 0.25.1      |
| Pygments                      | 2.15.0      |
| pykeyboard                    | 0.1.5       |
| PyMouse                       | 1.0         |
| PyMuPDF                       | 1.20.2      |
| pynput                        | 1.7.6       |
| pyparsing                     | 3.0.9       |
| pyperclip                     | 1.8.2       |
| pypiwin32                     | 223         |
| Pyrogram                      | 2.0.103     |
| pyrsistent                    | 0.19.3      |
| pyscreenshot                  | 3.0         |
| PySocks                       | 1.7.1       |
| python-dateutil               | 2.8.2       |
| python-docx                   | 0.8.11      |
| python-multipart              | 0.0.6       |
| python-rapidjson              | 1.10        |
| pytz                          | 2023.3      |
| PyUserInput                   | 0.1.10      |
| PyWavelets                    | 1.4.1       |
| pywin32                       | 304         |
| PyYAML                        | 6.0         |
| pyzmq                         | 25.0.2      |
| rapidfuzz                     | 2.15.1      |
| rarfile                       | 4.0         |
| requests                      | 2.28.2      |
| Rtree                         | 1.0.1       |
| scikit-image                  | 0.17.2      |
| scikit-learn                  | 1.2.2       |
| scipy                         | 1.10.1      |
| semantic-version              | 2.10.0      |
| setuptools                    | 67.6.1      |
| shapely                       | 2.0.1       |
| six                           | 1.16.0      |
| smart-open                    | 6.3.0       |
| sniffio                       | 1.3.0       |
| soupsieve                     | 2.4         |
| stack-data                    | 0.6.2       |
| starlette                     | 0.26.1      |
| sympy                         | 1.11.1      |
| termcolor                     | 2.2.0       |
| TgCrypto                      | 1.2.5       |
| threadpoolctl                 | 3.1.0       |
| tifffile                      | 2023.3.21   |
| toolz                         | 0.12.0      |
| tornado                       | 6.2         |
| tqdm                          | 4.65.0      |
| traitlets                     | 5.9.0       |
| trimesh                       | 3.21.5      |
| tritonclient                  | 2.32.0      |
| typing_extensions             | 4.5.0       |
| tzdata                        | 2023.3      |
| uc-micro-py                   | 1.0.1       |
| urllib3                       | 1.26.15     |
| uvicorn                       | 0.21.1      |
| visualdl                      | 2.5.1       |
| Wand                          | 0.6.13      |
| wcwidth                       | 0.2.6       |
| websockets                    | 11.0.1      |
| Werkzeug                      | 2.2.3       |
| wheel                         | 0.40.0      |
| x2paddle                      | 1.4.1       |
| yarl                          | 1.8.2       |
| zipp                          | 3.15.0      |
| zope.event                    | 4.6         |
| zope.interface                | 6.0         |