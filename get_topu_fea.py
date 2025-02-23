import os
import numpy as np
import json
from use_ripser import use_ripser_all_atom

def process_all_cifs_in_directory(directory):
    # 创建一个字典存储文件名和特征
    results = {}

    # 遍历目录中的所有文件
    for filename in os.listdir(directory):
        if filename.endswith('.cif'):
            cif_path = os.path.join(directory, filename)
            try:
                _, _, _, all_features = use_ripser_all_atom(cif_path)
                results[filename.replace('.cif', '')] = all_features
                print(f"Processed: {filename}")
                print(all_features)
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    # 保存结果为 npy 文件
    output_path = os.path.join(directory, 'topo', 'features.npy')
    np.save(output_path, results)

    # 保存字典为 JSON 文件，
    json_output_path = os.path.join(directory, 'topo', 'features.json')
    with open(json_output_path, 'w') as json_file:
        json.dump(results, json_file, indent=4)

    print(f"Feature extraction completed. Results saved to {output_path} and {json_output_path}")

process_all_cifs_in_directory('demo_dataset')
