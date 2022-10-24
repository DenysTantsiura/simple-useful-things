# 11-2 video 46minnext

class A:

    def __init__(self):

        self.__private_field = 10

    @property  # getter
    def private_field(self):
        return self.__private_field
        # if self.__private_field <= 0:
        #     return 0
        # elif self.__private_field > 100:
        #     return 100
        # else:
        #     return self.__private_field

    @private_field.setter
    def private_field(self, new_value):
        self.__private_field = new_value

    def __str__(self):
        return f"{self.private_field}"


class B(A):

    @A.private_field.setter
    def private_field(self, new_value):
        if new_value < 0:
            self._A__private_field = 0
        elif new_value > 100:
            self._A__private_field = 100
        else:
            self._A__private_field = new_value

    # def __str__(self):
    #     return f"{self.private_field}"


a = A()
print(B())
print(a.private_field)
a.private_field = -1
print(a.private_field)
a.private_field = 115
print(a.private_field)
a.private_field = 184
print(a.private_field)

b = B()
print(b.private_field)
b.private_field = -1
print(b.private_field)
b.private_field = 115
print(b.private_field)
b.private_field = 184
print(b.private_field)
# c = B().private_field = 98
# print(c.private_field)
print("___________")
print(b)
#===========================================================================================

class A:

    def __init__(self):

        self.__private_field = 10

    @property  # getter
    def private_field(self):
        print("getter A")
        return self.__private_field

    @private_field.setter
    def private_field(self, new_value):
        print("setter A")
        self.__private_field = new_value

    def __str__(self):
        return f"{self.private_field}"


class B(A):

    @property  # getter
    def private_field(self):
        print("getter B")
        return self.__private_field

    @private_field.setter
    def private_field(self, new_value):
        print("setter B")
        if new_value < 0:
            self.__private_field = 0
        elif new_value > 100:
            self.__private_field = 100
        else:
            self.__private_field = new_value

    # def __str__(self):
    #     return f"{self.private_field}"


a = A()
a.private_field = 155
print(a.private_field)

b = B()
b.private_field = 155
print(b.private_field)
