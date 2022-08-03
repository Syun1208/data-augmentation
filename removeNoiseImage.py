import os
import cv2

j = 0
i = 0
img_dir = 'E:\\mnist\\train\\0'
for f in os.listdir(img_dir):
    img_path = os.path.join(img_dir, f)
    j = j + 1
    if len(f.split('__')) == 2:
        if f.split('__')[1] == 'zoom-10_-20_10_10.jpg' or f.split('__')[1] == 'trans-10_0.jpg' or f.split('__')[1] \
                == 'trans20_20.jpg':
            os.remove(img_path)
            i = i + 1
            print('Noise Image')
print('Check on directory: ', img_dir)
print('Total: ', j)
print('Invalid file: ', i)
