from cuda_voxelization.cuda_mesh_voxelize import MeshVoxelization,binary_fill_from_corner_3D,SematicVoxelization
from utils.VoxelizerUtil import save_volume,save_v_volume
from utils.ObjIO import  load_obj_data, save_obj_data
import torch
import numpy as np

from Constants import consts
smplMesh = load_obj_data('/home/sunjc0306/render/dataset_example/FRONT_smpl_normalized.obj')
# save_obj_data(smplNew, smplPathNew)  # notice that face's vertex idx should start from +1, not 0
voxeltool = MeshVoxelization(1., (128, 192, 128), 7)
semantictool = SematicVoxelization(consts.smpl_vertex_code, smplMesh['f'], 1., (128, 192, 128), 0.05, 7).cuda()
occ_volume = voxeltool(torch.from_numpy(smplMesh['v']).float().cuda(), torch.from_numpy(smplMesh['f']).float().cuda())
occ_volume = binary_fill_from_corner_3D(occ_volume.cpu().numpy().astype(np.uint8))
smplSemVoxels, _ = semantictool(torch.from_numpy(smplMesh['v']).float().cuda(),
                                torch.from_numpy(occ_volume).float().cuda())
save_volume(occ_volume, "occ_volume.obj", 128, 192, 1/192)
save_v_volume(smplSemVoxels.cpu().numpy(),'smplSemVoxels.obj',128, 192, 1/192)