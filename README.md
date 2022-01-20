# Voxelization and Semantic Voxelization Codes for 3D Human Models



This repository contains a pytorch implementation of the voxelization and semantic voxelization code for 3D human models. 
In this repository , the CUDA is used to accelerate the speed of voxelization and the computation of the semantic code. 
Compared to other repositories, our code can dynamically implement computation at any resolution and is not limited to the model's coordinate space. 
The input to the code can be either an SMPL model or an arbitrary human model. 
The human model can be obtained its voxel representation, and the SMPL model can additionally be obtained its semantic voxel. 
The relevant computational principles will be given in our paper.


## Requirements
- Python 3
- PyTorch
- numpy


## Demo
Note: H_NORMALIZE and volume_res represent the height and resolution of the model, respectively. 
It is worth noting that the human model can be in any coordinate space, but its spatial symmetry must be guaranteed, e.g. [-0.5,-0.5,-0.5]* [0.5,0.5,0.5].
1. run the following script to voxelize a arbitrary human model and obtain its  its voxel representation.
```
python test_mesh.py
```

2. run the following script to voxelize a smpl model and obtain its its voxel and semantic voxel. 
```
python semanticVoxel.py
```


## Contact 
If you have some trouble using this software, please contact me[Jianchi Sun: [sunjc0306@mails.ccnu.edu.cn](mailto:sunjc0306@mails.ccnu.edu.cn) or [sunjc0306@qq.com](mailto:sunjc0306@qq.com).]



