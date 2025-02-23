import os
from ase.io import read, write
import numpy as np
# 指定文件夹路径
def convert_vasp_to_cif(input_folder, output_folder):
    # 创建输出文件夹（如果不存在）
    os.makedirs(output_folder, exist_ok=True)

    # 遍历文件夹中的所有文件
    for filename in os.listdir(input_folder):
        if filename.endswith(".vasp"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename.replace(".vasp", ".cif"))

            try:
                # 使用 ASE 读取 .vasp 文件并写入为 .cif 文件
                structure = read(input_path, format="vasp")
                write(output_path, structure, format="cif")
                print(f"Converted: {filename} -> {output_path}")
            except Exception as e:
                print(f"Error converting {filename}: {e}")

# 示例调用
input_folder = "topo_data/structure"  # 替换为包含 .vasp 文件的文件夹路径
output_folder = "topo_data"  # 替换为输出 .cif 文件的文件夹路径
convert_vasp_to_cif(input_folder, output_folder)
