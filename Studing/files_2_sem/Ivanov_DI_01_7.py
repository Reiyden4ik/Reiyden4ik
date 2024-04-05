class Ratiofraction:
    def __init__(self, rum, den):
        if self.__check_den__(den):
            self.rum = rum
            self.den = den
    @classmethod
    def __check_den__(cls, den):
        if den > 0:
            return True
        raise ValueError("den must be natural!")
    def verify_data(cls, other):
        if not isinstance(other, (int, Ratiofraction)):
            raise TypeError("Операнд справа должен быть целым числом или объектом эксземпляра класса Clock")
        return other if isinstance(other, int) else other.rum
        return other if isinstance(other, int) else other.den

    def __eq__(self, other):
        sc = self.verify_data(other)
        return self.rum == sc
        return self.den == sc

    def __lt__(self, other):
        sc = self.verify_data(other)
        return self.rum < sc
        return self.den == sc

    def __ge__(self, other):
        sc = self.verify_data(other)
        return self.rum >= sc
        return self.den == sc

rt1 = Ratiofraction(int(input('Числитель 1 дроби ')), int(input('Знаменатель 1 дроби ')))
rt2 = Ratiofraction(int(input('Числитель 2 дроби ')), int(input('Знаменатель 2 дроби ')))
if rt1.rum == rt1.den:
    print('first ratiofraction is 1')
    if rt2.rum == rt2.den:
        print('second ratiofraction is 1')
if rt1.rum == rt1.den and rt2.rum == rt2.den:
    print('they both equal and ')


