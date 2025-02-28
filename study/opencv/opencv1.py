import cv2
import numpy as np
from matplotlib import pyplot as plt

def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# img=cv2.imread('1.jpg')
# cv2.imshow('IMG',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# print(img.shape)

# vc=cv2.VideoCapture('video.mp4')
# if vc.isOpened():
#     open,frame=vc.read()
# else:
#     open=False
#
# while open:
#     ret,frame=vc.read()
#     if frame is None:
#         break
#     if ret==True:
#         gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#         cv2.imshow('result',gray)
#         if cv2.waitKey(20) & 0xFF==ord('q'):
#             break
# vc.release()
# cv2.destroyAllWindows()
# img=cv2.imread('1.jpg')
# b,g,r=cv2.split(img)
#
# img2=cv2.merge((b,g,r))
# cv_show('1',img2)

"""边界填充"""
img=cv2.imread('1.jpg')

# top_size,bottom_size,left_size,right_size=(50,50,50,50)
# replicate=cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_REPLICATE)
# reflect=cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,cv2.BORDER_REFLECT)
# reflect101 = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_REFLECT_101)
# wrap = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_WRAP)
# constant = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size,cv2.BORDER_CONSTANT, value=0)
# plt.subplot(231),plt.imshow(img,'gray'),plt.title('1')
# plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('2')
# plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('3')
# plt.subplot(234),plt.imshow(reflect101),plt.title('4')
# plt.subplot(235),plt.imshow(wrap),plt.title("5")
# plt.subplot(236),plt.imshow(constant),plt.title('6')
# plt.show()

'''图像融合'''
# img2=cv2.imread('2.jpg')
# print(img2.shape)
# img1=cv2.resize(img,(268,140))
# cv_show('cd',img1)
# res=cv2.addWeighted(img1,0.4,img2,0.6,0)
# res=cv2.resize(img,(0,0),fx=1,fy=3)
# cv_show('1',res)

'''图像处理'''
# hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# cv2.imshow('hsv',hsv)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# ret,thresh1=cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY)
# ret, thresh2 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)
# ret, thresh3 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TRUNC)
# ret, thresh4 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TOZERO)
# ret, thresh5 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TOZERO_INV)
# titles=['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
# images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
# for i in range(6):
#     plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()

'''图像平滑'''
# blur=cv2.blur(img,(3,3))
# box1=cv2.boxFilter(img,-1,(3,3),normalize=True)
# box2=cv2.boxFilter(img,-1,(3,3),normalize=False)
# aussian=cv2.GaussianBlur(img,(5,5),1)
# median=cv2.medianBlur(img,5)
# res=np.hstack((blur,aussian,median))
# cv_show('res',res)

'''形态学腐蚀'''
# kernel=np.ones((5,5),np.uint8)
# erosion_1=cv2.erode(img_gray,kernel,iterations=1)
# erosion_2=cv2.erode(img_gray,kernel,iterations=2)
# erosion_3=cv2.erode(img_gray,kernel,iterations=3)
# res=np.hstack((erosion_1,erosion_2,erosion_3))
# cv_show('res',erosion_2)

'''形态学膨胀'''
# kernel=np.ones((30,30),np.uint8)
# dilate_1=cv2.dilate(img_gray,kernel,iterations=1)
# dilate_2=cv2.dilate(img_gray,kernel,iterations=2)
# dilate_3=cv2.dilate(img_gray,kernel,iterations=3)
# res=np.hstack((dilate_1,dilate_2,dilate_3))
# cv_show('2',res)










