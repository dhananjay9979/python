def dec1(func):
    def nowexe():
        print("executing now")
        func()
        print("executed")
    return nowexe()


@dec1
def who_is_harry():
    print("harry is a good boy")

#who_is_harry=dec1(who_is_harry)

who_is_harry()

