# import numpy as np
import os
from pathlib import Path, PurePath  # 遍历文件夹
import nibabel as nib  # nii格式一般都会用到这个包
import cv2

class Transformation():        
    def __init__(self, file_name):
        self.file_name = file_name
        self.nii = nib.load(self.file_name)
        self.img_fdate = self.nii.get_fdata()

    def nii_to_image_z(self, z_value):
        image_z = self.img_fdate[:, :, z_value]
        return image_z
         
    def out_img(self):
        file_path_stem = PurePath(self.file_name).stem
        file_path_parent = PurePath(self.file_name).parent
        extra_folder = Path(file_path_parent, file_path_stem)
        if not os.path.exists(extra_folder):
            os.makedirs(extra_folder)
        for i in range(self.img_fdate.shape[2]):
            image_z = self.nii_to_image_z(i)
            name = str(i)
            export_img_name = PurePath(file_path_parent, file_path_stem, name, ".png")
            cv2.imwrite(image_z, export_img_name)
