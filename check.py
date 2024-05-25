import cv2

# 读取图像
image = cv2.imread(r"C:\Users\grizi\Desktop\TUD\quarter_4\computer_vision\YOLOP\inference\images\0ace96c3-48481887.jpg")
image2 = cv2.imread(r"C:\Users\grizi\Desktop\TUD\quarter_4\computer_vision\view_of_delft_PUBLIC\view_of_delft_PUBLIC\lidar\training\image_2\00020.jpg")

# 获取图像的形状
image_shape = image.shape

resized_image = cv2.resize(image2,(1280,720))
cv2.imwrite('output_image.jpg', resized_image)
print("Image shape:", resized_image.shape)
print(image2.shape)
