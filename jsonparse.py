# import xml.etree.ElementTree as etree
# import json


class A(object):
    pass

if __name__ == "__main__":
    a = A()
    b = A()

    print (id(a)==id(b))
    print (a, b)
