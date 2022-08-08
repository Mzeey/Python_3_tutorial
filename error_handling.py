from turtle import right


try:
    raise NameError
    print(int("Hello"))
except Exception as e:
    print(str(e))
finally:
    print("closing program ... ")