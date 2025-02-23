# Persistent Homology Crystal Graph Convolutional Neural Network (PH-CGCNN)

## Installation

This project requires the following dependencies, which you can find in the `requirements.txt` file:
- Pytorch
- Pymatgen
- Other necessary libraries

Please install all the required dependencies by running:
```
pip install -r requirements.txt
```



# Usage

For training and testing, you need a dataset consisting of structure files (in CIF format) and related properties data (id_prop.csv) in the same directory (`data_demo`), along with a topology information dictionary stored under `directory/topo`. After organizing your dataset, you can start the training process with the following command:

```
python main.py data_demo
```

Then, you can get model_best.pth.tar which store model with best validation accuracy. You can run prediction by following command:
```
python predict.py data_demo
```



## Features

You can add your own features by editing the `atom_init.json` file. This file defines the initialization of features for atoms in the crystal structure.



## Data Format

The dataset should include the following files:

1. **`id_prop.csv`**: This file contains two columns:
   - The first column should have the filename of the structure file (without the `.cif` extension).
   - The second column should contain the property values related to the structure.
Example:
structure1, 5.2
structure2, 4.8

2. **Topology Information (`topo/features.npy`)**: You need to create the `features.npy` file under the `topo` directory. This file contains the topology features of your dataset, which can be generated by running the `get_topu_fea.py` script on your CIF dataset. The `features.npy` will store a dictionary that maps the structure filenames (without `.cif` extension) to their corresponding topological features extracted via persistent homology.

Example of what the dictionary might look like:
```
{
    'structure1': [0.1, 0.2, 0.3, ...],
    'structure2': [0.05, 0.15, 0.25, ...],
}
```



## License

CGCNN is released under the MIT License.


