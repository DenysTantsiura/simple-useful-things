class Singleton:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

    def __init__(self, value):
        self.value = value


instance_1 = Singleton(10)
instance_2 = Singleton(20)
instance_3 = Singleton(50)


print(instance_1.value, instance_2.value)
print(instance_1, instance_2)
