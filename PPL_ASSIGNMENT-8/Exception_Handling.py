# Program to handle Assertion failed Exception
# import cv2
#
# while True:
#     try:
#         img_name = input("Enter name of image to be displayed : ")
#         img_path = "image/" + img_name
#         img = cv2.imread(img_path)
#         cv2.imshow("image", img)
#         cv2.waitKey(0)
#         break
#     except Exception as E:
#         print("No such image exists")
#         print(E)
#         print("Try again")
#
# print("Successfully Handled Assertion Failed error")


# Program to handle zero division error

# while True:
#     try:
#         dividend = int(input("Enter dividend : "))
#         divisor = int(input("Enter divisor : "))
#         print("Division result : ", dividend/divisor)
#         break
#     except ZeroDivisionError as e:
#         print("Divisor cannot be 0")
#         print(e, "error")
#         print("Try again")
#
# print("Handled ZeroDivisionError")

# Program to handle Value error

# while True:
#     try:
#         integer=int(input("Enter integer : "))
#         print(f"Square of {integer} is {integer*integer}")
#         break
#     except Exception as e:
#         print("Integer value Expected ")
#         print(e)
#         print("Try again")
#
# print("Successfully Handled ValueError")
