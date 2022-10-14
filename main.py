from pathlib import Path, PurePath
from nii_to_image import Transformation
import cv2


if __name__ == '__main__':
    current_path = Path.cwd()
    data_path = Path(current_path, "segmentations")
    path = PurePath(data_path)
    for file_name in data_path.glob("*.nii"):
        transfor = Transformation(file_name)
        img = transfor.out_img()
