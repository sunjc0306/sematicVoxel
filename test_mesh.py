import numpy as np
import os
from cuda_voxelization.cuda_mesh_voxelize import MeshVoxelization
import utils.VoxelizerUtil as voxel_util
from utils.ObjIO import *
import torch
VOXEL_H = 192
VOXEL_W = 128
H_NORMALIZE_HALF = 0.5
VOXEL_SIZE = 2.*H_NORMALIZE_HALF/VOXEL_H
meshPathNew = "/home/sunjc0306/render/dataset_example/FRONT_mesh_normalized.obj"
meshNew = load_obj_data(meshPathNew)
voxeltool=MeshVoxelization(1.,(128,192,128), 7)
occ_volume=voxeltool(torch.from_numpy(meshNew['v']).float().cuda(),torch.from_numpy(meshNew['f']).float().cuda())
occ_volume= voxel_util.binary_fill_from_corner_3D(occ_volume.cpu().numpy().astype(np.uint8))
voxel_util.save_volume(occ_volume, "occ_volume.obj", VOXEL_H, VOXEL_W, VOXEL_SIZE)