import numpy as np, cv2





v = cv2.VideoCapture('data/0.avi')

cnt = 0
ext = 10
while True:
  _, img = v.read()
  if img is None: break

  cv2.imshow('_', img)
  if cv2.waitKey(1) == 27: exit()
  cnt += 1
  if cnt%ext == 0:
    cv2.imwrite(f'data/{cnt//ext}.png', img)





