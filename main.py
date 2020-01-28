import cv2
import os

# Input directory
path_dir_in = "Depth"
path_dir_out = "Color"
# global path
PATH_IN = os.path.join(os.getcwd(), path_dir_in)
PATH_OUT = os.path.join(os.getcwd(), path_dir_out)

for i, file in enumerate(sorted(os.listdir(PATH_IN))):
    # Read image as grayscale
    path = os.path.join(PATH_IN, file)
    im_gray = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    # Conver imag to JET
    im_color = cv2.applyColorMap(im_gray, cv2.COLORMAP_MAGMA)
    cv2.imwrite(os.path.join(PATH_OUT, '{0:05d}.png'.format(i)), im_color)
    print(file,"DONE")
    # break

# print(os.listdir(PATH_IN))

# im_gray = cv2.imread("Depth\\0001.png", cv2.IMREAD_GRAYSCALE)
# im_color = cv2.applyColorMap(im_gray, cv2.COLORMAP_JET)
