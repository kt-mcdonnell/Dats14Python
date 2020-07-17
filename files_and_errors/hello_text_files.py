# try:
#     print("Trying to open the file")
#     file = open("order.txt")
#     print("Successfully opened file!")
# except FileNotFoundError as errmsg:
#    print("Couldn't open the file! PANIC !!!")

# try:
#     print("Trying to open the file")
#     file = open("order.txt")
#     print("Successfully opened file!")
# except FileNotFoundError as errmsg:
#     print("Couldn't open the file! PANIC !!!")
#     print(errmsg)
#     raise
# finally:
#     print("Finished handling everything")

# r - read mode (default)
# w - write mode (if no file, creates one; if file, truncate)
# x - create mode (if file, fails)
# a - append mode (if no file, creates one; if file, appends)
# t - text mode
# b - binary mode
# + - reading and writing

# def open_and_print_file(filename):
#     try:
#         opened_file = open(filename, "r")
#         file_line_list = opened_file.readlines()

#         for line in file_line_list:
#             print(line)

#         opened_file.close()
    
#     except FileNotFoundError:
#         print("File not found. Please check file name provided")

# # open_and_print_file("order.txt")

# file = open("order.txt")
# print(1, file.readline())
# print(2, file.readline())
# print(3, file.readline())
# print(4, file.readline())
# print(5, file.readline())


# def open_and_print_file(filename):
#     try:
#         with open(file_name, "r") as opened_file:
#             file_line_list = opened_file.readlines()

#             for line in file_line_list:
#                 print(line.rstrip('\n'))
#     except FileNotFoundError:
#         print("File cannot be found. Check name")
#         raise


# with open("order.txt", "a") as opened_file:
#     opened_file.write("\nCheeseburger, \nPizza, \nPasta, \nToast")

def append_to_file(filename, order):
    try:
        with open(filename, "a") as opened_file:
            opened_file.write(order + '\n')
    except TypeError:
            print("Order needs to be a string. Try again.")

append_to_file("order.txt", "Pasta")
append_to_file("order.txt", "Kebab")
append_to_file("order.txt", "Hot Dog")