class A:

    def __init__(self):
        self.public_field = None
        self._protected_field = None
        self.__private_field = None

    def __private(self):
        pass

    def _protected(self):
        pass

    def public(self):
        self._calculate_inside_obj()
        pass


class B(A):

    def my_method(self):
        self._protected()


a = A()
a.public_field
a._protected()
# a.__private()   # has no attribute! (attribute renamed:
a._A__private()
