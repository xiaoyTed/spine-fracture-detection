from pathlib import Path, PurePath
from src.nii_to_image import Transformation
import cv2


if __name__ == '__main__':
    current_path = Path.cwd()
    data_path = Path(current_path, "segmentations")
    path = PurePath(data_path)
    for file_name in data_path.glob("*.nii"):
        transfor = Transformation(file_name)
        transfor.file_name = 1
        img = transfor.out_img()
