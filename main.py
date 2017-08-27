
from lane import *
from moviepy.editor import VideoFileClip
import matplotlib.pylab as plt

if __name__ == "__main__":
    imagepath = 'examples/test3.jpg'
    img = plt.imread(imagepath)
    img_aug ,b,c,pts,pts_left,pts_right,color_warp= process_frame(img)
#   print(pts_left)
#   print("********************************")
#   print(pts_right)
    #plt.imshow(color_warp)
    #plt.imshow(c)
    plt.imshow(img_aug)
    plt.show()
