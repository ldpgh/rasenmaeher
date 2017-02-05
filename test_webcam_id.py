# ATTENTION ... it finds the builtin laptop camera.

from cv2 import *
import numpy as np
import math

cam=range(10)
cams=[]
imgs=[]

for ii in range(len(cam)):
  try:
    vc=VideoCapture(ii)
    if vc.isOpened():
      print ii, "FOUND camera ...", vc
      vc.set(CAP_PROP_FRAME_WIDTH, 240) #320)
      vc.set(CAP_PROP_FRAME_HEIGHT, 160) #240)
      print vc.get(CAP_PROP_FRAME_WIDTH), vc.get(CAP_PROP_FRAME_HEIGHT)
      cams.append(vc)
    else:
      print ii, "... can't open"
  except:
    cam[ii]=None
    print ii, "... Exception passed"

axis=1  # if all have same height
axis=0  # if all have same width
for ii in range(len(cams)):
  cams[ii].grab()
  retval,img=cams[ii].retrieve()
  imgs.append(img)
  if 0==ii:
    imall=imgs[ii]
  else:
    imall=np.concatenate((imall, imgs[ii]), axis=axis)

imshow("All images", imall)
waitKey(0)
