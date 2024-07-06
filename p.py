import numpy as np, cv2, shutil

for i  in range(1000):
  image = f'data/frame-{str(i).zfill(6)}.color.jpg'
  dist_image = f'frames/{str(i).zfill(6)}.jpg'

  shutil.copy(image, dist_image)


