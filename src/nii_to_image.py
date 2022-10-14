# import numpy as np
import os
from pathlib import Path, PurePath  # 遍历文件夹
import nibabel as nib  # nii格式一般都会用到这个包
import cv2

class Transformation():        
    def __init__(self, __file_name):
        self.__file_name = __file_name
        self.__nii = nib.load(self.__file_name)
        self.__img_fdate = self.__nii.get_fdata()

    def nii_to_image_z(self, z_value):
        image_z = self.__img_fdate[:, :, z_value]
        return image_z
         
    def out_img(self):
        print(self.__file_name)
        file_path_stem = PurePath(self.__file_name).stem
        file_path_parent = PurePath(self.__file_name).parent
        extra_folder = Path(file_path_parent, file_path_stem)
        if not os.path.exists(extra_folder):
            os.makedirs(extra_folder)
        for i in range(self.__img_fdate.shape[2]):
            image_z = self.nii_to_image_z(i)
            name = str(i) + ".png"
            export_img_name = PurePath(file_path_parent, file_path_stem, name)
            export_img_name = str(export_img_name)
            print(export_img_name)
            cv2.imwrite(export_img_name, image_z)
