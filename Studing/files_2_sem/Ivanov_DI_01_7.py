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
    def __eq__(self, other):
        return self.rum == other.rum and self.den == other.den
    def __hash__(self):
        return hash((self.rum, self.den))
rt1 = Ratiofraction(int(input('Числитель 1 дроби')), int(input('Знаменатель 1 дроби')))
rt2 = Ratiofraction(int(input('Числитель 2 дроби')), int(input('Знаменатель 2 дроби')))
if rt1.rum == rt1.den and rt2.rum == rt2.den:
    print('1 = 1', 'they both equal')

