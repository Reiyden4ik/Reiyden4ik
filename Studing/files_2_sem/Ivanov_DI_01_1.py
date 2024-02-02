class Person:
  Age = int(input())
  Sex = str(input())
  Name = str(input())
  def set_parameters(self, high, weight):
    self.high = high
    self.weight = weight
pr = Person()
pr.set_parameters(170, 72)
print('lol')
