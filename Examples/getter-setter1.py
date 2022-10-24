class A:
    def __init__(self, attr):
        self._attr = None
        self.attr = attr

    @property
    def attr(self):
        try:
            return self._attr
        except AttributeError:
            return ''


class B(A):
    @A.attr.setter
    def attr(self, value):
        if value.lower() == value:
            self._attr = value
        else:
            print("No corect value")


if __name__ == '__main__':
    c = B("qwerty")
    print(' After set:', repr(c.attr))
    c = B("Qwerty")
    print(' After set:', repr(c.attr))
    # d = A("Qwerty") # AttributeError    No setter in A
    # print(' After set:', repr(d.attr))

