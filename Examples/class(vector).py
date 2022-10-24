# class A:
#     @property
#     def attr(self):
#         try:
#             return self._attr
#         except AttributeError:
#             return ''


# class B(A):
#     @A.attr.setter
#     def attr(self, value):
#         self._attr = value


# if __name__ == '__main__':
#     b = B()
#     print('Before set:', repr(b.attr))
#     b.attr = 'abc'
#     print(' After set:', repr(b.attr))


class Vector_bad:

    def __init__(self, v):

        if type(v) == list:
            self.x = v[0]
            self.y = v[1]
        elif type(v) == dict:
            self.x = v['x']
            self.y = v['y']

    def __str__(self):
        return f"({self.x}, {self.y})"


print(Vector_bad([1, 2]))
print(Vector_bad({'x': 2, 'y': 3}))


class Vector_good:

    def __init__(self, vector_type):
        self.vector_type = vector_type

    # def __call__(self): # !!! in default
    #     raise TypeError("... is not callable")

    def __call__(self, v):
        if type(v) == list:
            self.__handle_list(v)
        elif type(v) == dict:
            self.__handle_dict(v)
        return (self.x, self.y)

    def __handle_list(self, v_list):
        self.x = v_list[0]
        self.y = v_list[1]

    def __handle_dict(self, v_dict):
        self.x = v_dict['x']
        self.y = v_dict['y']

    def __str__(self):
        return f"Vector {self.vector_type}: ({self.x}, {self.y})"


vector = Vector_good("2D")
print(vector([1, 2]))
print(vector.vector_type)
print(vector)
print(vector({'x': 2, 'y': 3}))
print(str(vector([1, 2])))
print(str(vector({'x': 2, 'y': 3})))
