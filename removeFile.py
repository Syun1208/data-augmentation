import cv2
import os

width = 28
height = 28
dim = (width, height)
i = 0
j = 0
k = 0
index = input('Input the index of file: ')
img_src = 'E:\\mnist\\train\\' + index
nameFolder = "E:\\mnist\\train\\" + index + "_s"
nameFile = 'number' + index + '_'
for f in os.listdir(img_src):
    img_path = os.path.join(img_src, f)
    img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    i = i + 1
    if f.split('.')[len(f.split('.')) - 1] != 'jpg' or isinstance(img, type(None)):
        # time.sleep(5)
        print('Invalid file')
        os.remove(img_path)
        j += 1
        continue
    print('Original Dimensions : ', img.shape)
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    print('Resized Dimensions : ', resized.shape)
    if not os.path.exists(nameFolder):
        os.mkdir(nameFolder)
    if not os.path.exists(nameFolder + "\\" + nameFile + str(i) + '.jpg'):
        cv2.imwrite(nameFolder + "\\" + nameFile + str(i) + '.jpg', resized)
    cv2.imshow("Resized image", resized)
    k = k + 1
print('Check on directory: ', img_src)
print('Total: ', i)
print('Invalid file: ', j)
print('Valid file: ', k)
cv2.waitKey(0)
cv2.destroyAllWindows()
