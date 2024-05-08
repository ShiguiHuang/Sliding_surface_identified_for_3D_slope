# -*- coding: utf-8 -*-
# @Time        : 2024/4/23 20:23
# @Author      : husky
# @FileName    : draw_slope_and_sliding_surface.py
# @Software    : PyCharm
# @ProjectName : pythonProject
# @Email       : shiguihuang1874@qq.com

# 1 导入需要的库和定义画图需要的变量 / Import the required library and define the variables needed for drawing
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.tri as mtri
from matplotlib import cm

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

z_str_of_current_in = np.array(
    ["02.50", "05.00", "10.00", "15.00", "20.00", "25.00", "30.00", "35.00", "40.00", "45.00", "47.50"])
z_float_of_current_in = np.array([float(str_i) for str_i in z_str_of_current_in])
image_path = "../program_process_files"

p_A = [63, 635, 0]
p_B = [1470, 635, 0]
p_C = [1470, 196, 0]
p_D = [1106, 196, 0]
p_E = [570, 465, 0]
p_F = [63, 465, 0]

k = 21.93548

z_ = 50 * k

p_A_z = [63, 635, z_]
p_B_z = [1470, 635, z_]
p_C_z = [1470, 196, z_]
p_D_z = [1106, 196, z_]
p_E_z = [570, 465, z_]
p_F_z = [63, 465, z_]

x_array_array = [0 for i in range(len(z_str_of_current_in))]
y_array_array = [0 for i in range(len(z_str_of_current_in))]
z_array_array = [0 for i in range(len(z_str_of_current_in))]

for i in range(len(z_str_of_current_in)):
    x_array_array[i] = np.loadtxt(image_path + "\\x_array_" + z_str_of_current_in[i] + ".txt", dtype=float)
    y_array_array[i] = np.loadtxt(image_path + "\\y_array_" + z_str_of_current_in[i] + ".txt", dtype=float)
    z_array_array[i] = np.loadtxt(image_path + "\\z_array_" + z_str_of_current_in[i] + ".txt", dtype=float)
# 2 开始绘图 / Start draw
# 定义坐标轴 / Define the coordinate axis
# fig = plt.figure()
# ax1 = plt.add_subplot(111, projection='3d')

# 设置坐标轴标签 / Set the axis label
ax1.set_xlabel("x_axes")
ax1.set_ylabel("y_axes")
ax1.set_zlabel("z_axes")

# 先画边坡 / draw slope
slope_zero_x_array = np.array([p_A[0], p_B[0], p_C[0], p_D[0], p_E[0], p_F[0], p_A[0]])
slope_zero_y_array = np.array([p_A[1], p_B[1], p_C[1], p_D[1], p_E[1], p_F[1], p_A[1]])
slope_zero_z_array = np.array([p_A[2], p_B[2], p_C[2], p_D[2], p_E[2], p_F[2], p_A[2]])

slope_50_x_array = np.array([p_A_z[0], p_B_z[0], p_C_z[0], p_D_z[0], p_E_z[0], p_F_z[0], p_A_z[0]])
slope_50_y_array = np.array([p_A_z[1], p_B_z[1], p_C_z[1], p_D_z[1], p_E_z[1], p_F_z[1], p_A_z[1]])
slope_50_z_array = np.array([p_A_z[2], p_B_z[2], p_C_z[2], p_D_z[2], p_E_z[2], p_F_z[2], p_A_z[2]])

# 按论文的视图设置坐标 / Set the coordinates according to the view of the paper
max_y_ = max(slope_zero_y_array)
slope_zero_y_array = max_y_ - slope_zero_y_array
slope_50_y_array = max_y_ - slope_50_y_array
slope_zero_y_array, slope_zero_z_array = slope_zero_z_array, slope_zero_y_array
slope_50_y_array, slope_50_z_array = slope_50_z_array, slope_50_y_array

ax1.plot(slope_zero_x_array, slope_zero_y_array, slope_zero_z_array, linewidth=1.5, color="#621661", zorder=2)
ax1.plot(slope_50_x_array, slope_50_y_array, slope_50_z_array, linewidth=1.5, color="#621661", zorder=2)

for i in range(len(slope_50_x_array)):
    x_array_ = np.array([slope_zero_x_array[i], slope_50_x_array[i]])
    y_array_ = np.array([slope_zero_y_array[i], slope_50_y_array[i]])
    z_array_ = np.array([slope_zero_z_array[i], slope_50_z_array[i]])

    ax1.plot(x_array_, y_array_, z_array_, linewidth=1.5, color="#621661", zorder=2)

# 绘制滑动面 / Draw the sliding surface
for i in range(len(x_array_array)):
    # 绘制滑面
    temp_y = y_array_array[i]
    temp_z = z_array_array[i]

    temp_y = max_y_ - temp_y
    temp_y, temp_z = temp_z, temp_y

    ax1.plot(x_array_array[i], temp_y, temp_z, linewidth=1, color="#ff0000", zorder=1)

    # # 尝试拟合两条滑面之间的曲面
    # if i < len(x_array_array) - 1:
    #     temp_y_add_1 = y_array_array[i + 1]
    #     temp_z_add_1 = z_array_array[i + 1]
    #     temp_y_add_1 = max_y_ - temp_y_add_1
    #     temp_y_add_1, temp_z_add_1 = temp_z_add_1, temp_y_add_1
    #     x_ = np.append(x_array_array[i], x_array_array[i + 1])
    #     y_ = np.append(temp_y, temp_y_add_1)
    #     z_ = np.append(temp_z, temp_z_add_1)
    #     tri = mtri.Triangulation(x_, y_)
    #     ax1.plot_trisurf(tri, z_, cmap=cm.coolwarm, linewidth=0, antialiased=True)

# ax1.plot([0, 0, 0, 0, 0, 100], [0, 0, 0, 100, 0, 0], [0, 100, 0, 0, 0, 0])

# 绘制y=15.00处的边坡面 / Draw the slope surface at y = 15.00
z_15 = 15 * k
z_array_15 = np.array([z_15 for i in range(7)])
ax1.plot(slope_50_x_array, z_array_15, slope_zero_z_array, linewidth=1, color="#0000ff", zorder=2)

ax1.set_xlim([0, 1500])
ax1.set_ylim([0, 1500])
ax1.set_zlim([0, 1500])

plt.show()
