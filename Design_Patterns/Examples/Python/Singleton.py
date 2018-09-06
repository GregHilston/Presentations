"""
Ensure a class only has one instance, and provide a global point of
access to it.
"""


class Singleton(type):
    """
    Define an Instance operation that lets clients access its unique
    instance.
    """

    my_attr = None # class variable

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class MyClass(metaclass=Singleton):
    """
    Example class.
    """

    pass

class Scott:
    pass
    
def main():
    # m1 = MyClass()
    # m2 = MyClass()
    # assert m1 is m2
    # assert id(m1) == id(m2)
    scott1 = Scott()
    scott2 = Scott()
    assert scott1 is scott2

if __name__ == "__main__":
    main()
