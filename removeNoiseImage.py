import os
import cv2

j = 0
i = 0
img_dir = 'E:\\mnist\\train\\2'
for f in os.listdir(img_dir):
    img_path = os.path.join(img_dir, f)
    j = j + 1
    for n in f.split('__'):
        if n == 'zoom-10_-20_10_10.jpg' or n == 'trans-10_0.jpg' or n == 'trans20_20.jpg' or n == \
                'noise0.5.jpg':
            os.remove(img_path)
            i = i + 1
            print('Noise Image')
print('Check on directory: ', img_dir)
print('Total: ', j)
print('Invalid file: ', i)
