import cv2

path = r"C:Users\grizi\Desktop\TUD\quarter_4\computer_vision\YOLOP\dataset_root\images\train\0000f77c-6257be58.jpg"
img = cv2.imread(path, cv2.IMREAD_COLOR | cv2.IMREAD_IGNORE_ORIENTATION)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow(img)
cv2.waitKey(0)