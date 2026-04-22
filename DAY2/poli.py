x="Hellloooooiiiiiiiii"
y=[46,72,'hehe',100.04]
z=('96.69','ahem')
print(len(x))
print(len(y))
print(len(z))
G={'des':25,'niru':20}#only keys are counted in length of dictionary
print(len(G))


class zoo:
    def speak(self):
        print("animals speak")
class dog(zoo):
    def speak(self):
        print("dog barks")
class cat(zoo):
    def speak(self):
        print("cat meows")
z=zoo()
z.speak()
d=dog()
d.speak()


class person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
p1=person("des",20)
print(p1.name)
print(p1._person__age)#accessing the age attribute using name mangling


