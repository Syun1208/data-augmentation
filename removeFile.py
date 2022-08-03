import cv2
import os
import time
width = 28
height = 28
dim = (width, height)
i = 0
j = 0
img_dir0 = 'E:\\mnist\\train\\3'
for f in os.listdir(img_dir0):
    img_path = os.path.join(img_dir0, f)
    img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    print('Original Dimensions : ', img.shape)
    if img_path.split('.')[1] != 'jpg':
        time.sleep(5)
        print('Invalid file')
        os.remove(img_path)
        j += 1
        continue
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    print('Resized Dimensions : ', resized.shape)
    cv2.imwrite("E:\\mnist\\train\\3_s\\" + 'number3_' + str(i) + '.jpg', resized)
    cv2.imshow("Resized image", resized)
    i = i + 1
print('Total: ', i)
print('Invalid file: ', j)
# i = 0
# for f in os.listdir(img_dir1):
#     img_path = os.path.join(img_dir1, f)
#     img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
#     print('Original Dimensions : ', img.shape)
#     # if img.shape == (28, 28):
#     #     continue
#     # resize image
#     resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
#     print('Resized Dimensions : ', resized.shape)
#     cv2.imwrite("D:\\Pictures\\Data_Centric\\1\\" + 'number_1' + str(i) + '.jpg', resized)
#     cv2.imshow("Resized image", resized)
#     i = i + 1
# i = 0
# for f in os.listdir(img_dir2):
#     img_path = os.path.join(img_dir2, f)
#     img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
#     print('Original Dimensions : ', img.shape)
#     # if img.shape == (28, 28):
#     #     continue
#     # resize image
#     resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
#     print('Resized Dimensions : ', resized.shape)
#     cv2.imwrite("D:\\Pictures\\Data_Centric\\2\\" + 'number_2' + str(i) + '.jpg', resized)
#     cv2.imshow("Resized image", resized)
#     i = i + 1
# i = 0
# for f in os.listdir(img_dir3):
#     img_path = os.path.join(img_dir3, f)
#     img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
#     print('Original Dimensions : ', img.shape)
#     # if img.shape == (28, 28):
#     #     continue
#     # resize image
#     resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
#     print('Resized Dimensions : ', resized.shape)
#     cv2.imwrite("D:\\Pictures\\Data_Centric\\3\\" + 'number_3' + str(i) + '.jpg', resized)
#     cv2.imshow("Resized image", resized)
#     i = i + 1
# i = 0
# for f in os.listdir(img_dir4):
#     img_path = os.path.join(img_dir4, f)
#     img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
#     print('Original Dimensions : ', img.shape)
#     # if img.shape == (28, 28):
#     #     continue
#     # resize image
#     resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
#     print('Resized Dimensions : ', resized.shape)
#     cv2.imwrite("D:\\Pictures\\Data_Centric\\4\\" + 'number_4' + str(i) + '.jpg', resized)
#     cv2.imshow("Resized image", resized)
#     i = i + 1
# i = 0
# for f in os.listdir(img_dir5):
#     img_path = os.path.join(img_dir5, f)
#     img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
#     print('Original Dimensions : ', img.shape)
#     # if img.shape == (28, 28):
#     #     continue
#     # resize image
#     resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
#     print('Resized Dimensions : ', resized.shape)
#     cv2.imwrite("D:\\Pictures\\Data_Centric\\5\\" + 'number_5' + str(i) + '.jpg', resized)
#     cv2.imshow("Resized image", resized)
#     i = i + 1
# i = 0
# for f in os.listdir(img_dir6):
#     img_path = os.path.join(img_dir6, f)
#     img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
#     print('Original Dimensions : ', img.shape)
#     # if img.shape == (28, 28):
#     #     continue
#     # resize image
#     resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
#     print('Resized Dimensions : ', resized.shape)
#     cv2.imwrite("D:\\Pictures\\Data_Centric\\6\\" + 'number_6' + str(i) + '.jpg', resized)
#     cv2.imshow("Resized image", resized)
#     i = i + 1
# i = 0
# for f in os.listdir(img_dir7):
#     img_path = os.path.join(img_dir7, f)
#     img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
#     print('Original Dimensions : ', img.shape)
#     # if img.shape == (28, 28):
#     #     continue
#     # resize image
#     resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
#     print('Resized Dimensions : ', resized.shape)
#     cv2.imwrite("D:\\Pictures\\Data_Centric\\7\\" + 'number_7' + str(i) + '.jpg', resized)
#     cv2.imshow("Resized image", resized)
#     i = i + 1
# i = 0
# for f in os.listdir(img_dir8):
#     img_path = os.path.join(img_dir8, f)
#     img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
#     print('Original Dimensions : ', img.shape)
#     # if img.shape == (28, 28):
#     #     continue
#     # resize image
#     resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
#     print('Resized Dimensions : ', resized.shape)
#     cv2.imwrite("D:\\Pictures\\Data_Centric\\8\\" + 'number_8' + str(i) + '.jpg', resized)
#     cv2.imshow("Resized image", resized)
#     i = i + 1
# i = 0
# for f in os.listdir(img_dir9):
#     img_path = os.path.join(img_dir9, f)
#     img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
#     print('Original Dimensions : ', img.shape)
#     # if img.shape == (28, 28):
#     #     continue
#     # resize image
#     resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
#     print('Resized Dimensions : ', resized.shape)
#     cv2.imwrite("D:\\Pictures\\Data_Centric\\9\\" + 'number_9' + str(i) + '.jpg', resized)
#     cv2.imshow("Resized image", resized)
#     i = i + 1
cv2.waitKey(0)
cv2.destroyAllWindows()
