import cv2
import os

width = 28
height = 28
dim = (width, height)
i = 0
j = 0
k = 0
img_dir0 = 'E:\\mnist\\train\\1'
for f in os.listdir(img_dir0):
    img_path = os.path.join(img_dir0, f)
    img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    i = i + 1
    print('Original Dimensions : ', img.shape)
    if f.split('.')[len(f.split('.')) - 1] != 'jpg' or img is None:
        # time.sleep(5)
        print('Invalid file')
        os.remove(img_path)
        j += 1
        continue
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    print('Resized Dimensions : ', resized.shape)
    if not os.path.exists("E:\\mnist\\train\\9_s"):
        os.mkdir("E:\\mnist\\train\\9_s")
    if not os.path.exists("E:\\mnist\\train\\9_s\\" + 'number9_' + str(i) + '.jpg'):
        cv2.imwrite("E:\\mnist\\train\\9_s\\" + 'number9_' + str(i) + '.jpg', resized)
    cv2.imshow("Resized image", resized)
    k = k + 1
print('Check on directory: ', img_dir0)
print('Total: ', i)
print('Invalid file: ', j)
print('Valid file: ', k)
cv2.waitKey(0)
cv2.destroyAllWindows()
