
import numpy as np
import cv2


class free_fall:
    def __init__(self):
        f = 0
    def step( self,x,y ,ground,t):
        IM = np.zeros( (1024, 1024,3), dtype='uint8' )
        cv2.line( IM, (0, ground+40), (1024, ground+40), (255,255,255), 6 )
        cv2.circle( IM, (x ,y), 40, (255,0,255), -1 )
        cv2.putText(IM, "y="+str(np.round(y,4)), (15, 15), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (200,200,250), 1)
        cv2.putText(IM, "t="+str(np.round(t,4)), (15, 35), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (200,200,250), 1)
        return IM



if __name__=="__main__":
   print("File one executed when ran directly")
else:
   print("File one executed when imported")
