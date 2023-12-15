#Вы организуете спортивную лигу по круговой системе. Каждая команда встречается со всеми остальными командами.
#В вашей лиге победа дает команде, ничья дает обеим командам. После нескольких игр вы должны вычислить порядок команд в вашей лиге. 
#Для расстановки команд используются следующие критерии:2 points1 point

#Точки
#Разница забитых и пропущенных мячей (разница между забитыми и пропущенными мячами)
#Забитые голы
#Сначала вы сортируете команды по набранным очкам. Если две или более команд набрали одинаковое количество очков, в игру вступает второй критерий и так далее.
#Наконец, если все критерии одинаковы, команды делят между собой места.

def circle_method(teams):

    # If there is an odd amount of teams,
    # there will be 1 more 'non-existent' team, standing for no match-up
    rounds = teams - 1
    if teams % 2 == 1:
        rounds = teams
    # Matches per round
    mpr = int((rounds+1) / 2)

    # Table of teams [1, 2, ..., n]
    t = []
    for i in range(rounds+1):
        t.append(i+1)

    # Stores the rounds with the corresponding matches inside
    # e.g.: [[(1, 4), (2, 3)], [(1, 3), (4, 2)], [(1, 2), (3, 4)]]
    matches = []
    for r in range(rounds):
        matches.append([])
        for m in range(mpr):
            matches[r].append((t[m], t[-1-m]))
        t.remove(rounds-r+1)
        t.insert(1, rounds-r+1)
    print("\n")
    i = 1
    for r in matches:
        print("\nRound "+str(i))
        for m in r:
            print("Team " +str(m[0]) + " vs. Team " + str(m[1]))
        i += 1

if __name__ == "__main__":
    circle_method(int(input("Teams: ")))