import numpy as np
import ripser
from ase.io import read

def use_ripser_all_atom(cif_path):
    # 读取结构并提取原子坐标
    atoms = read(cif_path, format='cif')
    coordinates = atoms.get_positions()

    # 转换为NumPy数组
    data = np.array(coordinates)

    # 计算持久同调
    result = ripser.ripser(data, maxdim=2)
    dgms = result['dgms']

    # 提取 H0、H1 和 H2 的持久性条带
    H0_barcodes = dgms[0]
    H1_barcodes = dgms[1]
    H2_barcodes = dgms[2]

    # 计算持久性统计量,包括最大持久性、平均持久性、中位数持久性和标准差持久性
    def persistence_features(barcodes):
        lengths = [death - birth for birth, death in barcodes if np.isfinite(death - birth)]
        max_persistence = max(lengths) if lengths else 0
        mean_persistence = np.mean(lengths) if lengths else 0
        median_persistence = np.median(lengths) if lengths else 0
        std_persistence = np.std(lengths) if lengths else 0
        return [max_persistence, mean_persistence, median_persistence, std_persistence]

    # 提取出生和死亡时间
    def barcodes(barcodes):
        birth = [birth for birth, death in barcodes if np.isfinite(death - birth)]
        death = [death for birth, death in barcodes if np.isfinite(death - birth)]
        return birth + death

    # 根据参数返回结果

    b0 = barcodes(H0_barcodes)
    b1 = barcodes(H1_barcodes)
    b2 = barcodes(H2_barcodes)
    
    H0_features = persistence_features(H0_barcodes)
    H1_features = persistence_features(H1_barcodes)
    H2_features = persistence_features(H2_barcodes)
    # print(H2_features)
    all_features = H0_features + H1_features + H2_features
    return b0, b1, b2, all_features

