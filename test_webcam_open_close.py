# ATTENTION ... it finds the builtin laptop camera.

from cv2 import *
import numpy as np
import math
import matplotlib.pyplot as plt
import traceback

cam=range(10)
cams=[]
imgs=[]

for ii in range(len(cam)):
  try:
    vc=VideoCapture(ii)
    if vc.isOpened():
      print ii, "FOUND camera ...", vc
      cams.append(ii)
      vc.release()
    else:
      print ii, "... can't open"
  except:
    cam[ii]=None
    print ii, "... Exception passed"

print " "
for ii in cams:
  try:
    vc=VideoCapture(ii)
    vc.set(CAP_PROP_FRAME_WIDTH, 1) ; vc.set(CAP_PROP_FRAME_HEIGHT, 1)
    for kk in range(2):
      vc.grab()
      rr,img=vc.retrieve()
      size=0
      if rr: size=len(img)
    print ii, vc, rr, size
    if rr:
      imgs.append(img)
    #vc.release()
  except:
    print traceback.print_exc()
    print ii, "... Exception passed"

print " "
if 1==1:
  # MATPLOTLIB used to show images
  fig=plt.figure()
  for ii in range(len(imgs)):
    print ii
    fig.add_subplot(int(math.ceil(len(imgs)/2.0)), 2, ii+1)
    plt.imshow(imgs[ii])
  plt.show()
else:
  # OPENCV used to show images
  axis=0  # if all have same height
  axis=1  # if all have same width
  for ii in range(len(imgs)):
    if 0==ii:
      imall=imgs[ii]
    else:
      imall=np.concatenate((imall, imgs[ii]), axis=axis)
  imshow("All images", imall)
  waitKey(0)
