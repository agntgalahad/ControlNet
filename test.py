import cv2

# Path to the image file
image_path = '../datasets/coco_train_2017/dataset/000000571678.jpg'

# Read the image
image = cv2.imread(image_path)
image2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Display the image
cv2.imshow('Image', image)
cv2.imshow('BWImage', image2)
cv2.waitKey(0)
cv2.destroyAllWindows()