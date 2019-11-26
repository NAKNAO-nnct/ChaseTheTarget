import copy


class A:
    name = None

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name


a = A()
b = copy.deepcopy(a)

b.setName("bokenasu")
print(b.getName())

print(a.getName())
