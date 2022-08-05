import cv2
import os
import shutil

width = 28
height = 28
dim = (width, height)
i = 0
j = 0
k = 0
index = input('Input the index of file: ')
img_src = 'E:\\train\\' + index + '_s'
img_des = 'E:\\mnist\\train\\' + index
nameFile = 'new_' + index
for f in os.listdir(img_src):
    img_path = os.path.join(img_src, f)
    img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    i = i + 1
    if f.split('.')[len(f.split('.')) - 1] != 'jpg' or isinstance(img, type(None)):
        print('False')
        os.remove(img_path)
        j += 1
        continue
    print('Original Dimensions : ', img.shape)
    if img.shape == (28, 28) or img.shape == (28, 28, 3):
        print("True")
        if not os.path.exists(os.path.join(img_src, nameFile + str(k) + '.jpg')):
            os.rename(img_path, os.path.join(img_src, nameFile + str(k) + '.jpg'))
        if os.path.isfile(os.path.join(img_src, nameFile + str(k) + '.jpg')):
            shutil.copy(os.path.join(img_src, nameFile + str(k) + '.jpg'),
                        os.path.join(img_des, nameFile + str(k) + '.jpg'))
        k = k + 1
print('Check on directory: ', img_src)
print('Total: ', i)
print('Invalid file: ', j)
print('Valid file: ', k)
cv2.waitKey(0)
cv2.destroyAllWindows()
