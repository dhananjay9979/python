def f1():
    if __name__=='__main__':
        print("the code executed as individual program")
        print("the value of __name__:", __name__)
    else:
        print("the code executed as a module from some other program")
        print("the value of __name__:", __name__)

f1()


