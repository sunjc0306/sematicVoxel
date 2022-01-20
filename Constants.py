from __future__ import division, absolute_import, print_function
import numpy as np
import os
class Constants:
    def __init__(self,):
        self.smpl_vertex_code=self.read_smpl_constants()
    def read_smpl_constants(self):
        """Load smpl vertex code"""
        smpl_vtx_std = np.loadtxt(os.path.join('vertices.txt'))
        min_x = np.min(smpl_vtx_std[:, 0])
        max_x = np.max(smpl_vtx_std[:, 0])
        min_y = np.min(smpl_vtx_std[:, 1])
        max_y = np.max(smpl_vtx_std[:, 1])
        min_z = np.min(smpl_vtx_std[:, 2])
        max_z = np.max(smpl_vtx_std[:, 2])

        smpl_vtx_std[:, 0] = (smpl_vtx_std[:, 0] - min_x) / (max_x - min_x)
        smpl_vtx_std[:, 1] = (smpl_vtx_std[:, 1] - min_y) / (max_y - min_y)
        smpl_vtx_std[:, 2] = (smpl_vtx_std[:, 2] - min_z) / (max_z - min_z)
        smpl_vertex_code = np.float32(np.copy(smpl_vtx_std))
        return smpl_vertex_code

consts = Constants()