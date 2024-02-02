class Person:
  Age = '23'
  Sex = 'male'
  name = 'Jack'
  print('If you want to change your data, let is go:')
  Person.Age = int(input())
  Person.Sex = str(input())
  Person.name = str(input())
