# def disp():
#     def show():
#         print("show function")
#     print(" disp function")
#     show()
#
# disp()

# # ---------------------------------------------------------
#
# def disp():
#     def show():
#         return "show function"
#     result=show() + " disp function"
#     return result
#
# a=disp()
# print(a)
# ------------------------------------------------------------

# passing function as an argument
# def disp(function):
#     print("disp function" + function())
# def show():
#     return "  show function"
#
# disp(show)



# def disp(function):
#     return ("disp function" + function())
# def show():
#     return " show function"
#
# x=disp(show)
# print(x)



# function return another function
# def disp():
#     def show():
#         return "show function"
#     print("disp function")
#     return show
# r_sh=disp()
# print(r_sh())
