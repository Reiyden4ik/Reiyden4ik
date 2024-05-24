#include <iostream>
#include <cstdlib> // Для функции rand()
#include <ctime>   // Для функции time()
#include <vector>  // Для использования вектора
#include <algorithm> // Для использования функции find()
#include <string> // Для перевода из string в int
#include <stdlib.h> //Для очистки консоли
#include <windows.h>//Для задания размера консоли

using namespace std;
//функция для перевода char в int
int chartoint(char card1)
{
    // Преобразование строковых рангов в числовые значения
    char rank1 = card1;
    int rankValue1 = 0;
    if (rank1 == 'J') {
        rankValue1 = 11;
    } else if (rank1 == 'Q') {
        rankValue1 = 12;
    } else if (rank1 == 'K') {
        rankValue1 = 13;
    } else if (rank1 == 'T') {
        rankValue1 = 14;
    } else if (rank1 == '0') {
        rankValue1 = 0;
    } else if (rank1 == '1') {
        rankValue1 = 10;
    } else {
        rankValue1 = rank1 - '0';
    }
    return rankValue1;
}
//Функция для перевода string в int
int toint(string card1)
{
    // Преобразование строковых рангов в числовые значения
    string rank1 = card1;
    int rankValue1 = 0;
    if (rank1 == "J") {
        rankValue1 = 11;
    } else if (rank1 == "Q") {
        rankValue1 = 12;
    } else if (rank1 == "K") {
        rankValue1 = 13;
    } else if (rank1 == "T") {
        rankValue1 = 14;
    } else if (rank1 == "0") {
        rankValue1 = 0;
    } else if (rank1 == "1") {
        rankValue1 = 10;
    } else {
        rankValue1 = atoi(rank1.c_str());
    }
    return rankValue1;
}
// Функция для сравнения карт
bool compareCards(const string& card1, const string& card2)
{
    // Разделение строки на масть и значение
    string rank1 = card1.substr(card1.find(" ") + 1);
    string rank2 = card2.substr(card2.find(" ") + 1);

    // Преобразование строковых рангов в числовые значения
    int rankValue1 = 0;
    int rankValue2 = 0;
    if (rank1 == "J") {
        rankValue1 = 11;
    } else if (rank1 == "Q") {
        rankValue1 = 12;
    } else if (rank1 == "K") {
        rankValue1 = 13;
    } else if (rank1 == "T") {
        rankValue1 = 14;
    }
    else {
        rankValue1 = stoi(rank1);
    }

    if (rank2 == "J") {
        rankValue2 = 11;
    } else if (rank2 == "Q") {
        rankValue2 = 12;
    } else if (rank2 == "K") {
        rankValue2 = 13;
    } else if (rank2 == "T") {
        rankValue2 = 14;
    }
    else {
        rankValue2 = stoi(rank2);
    }

    return rankValue1 < rankValue2; // Сравнение числовых значений рангов
}
// Функция для обновления карт стола
auto updatetable(vector<string>& table, vector<string>& all1, vector<string>& all2)
{
    string suits[] = {"c", "d", "s", "h"};//где: с - club(крести), d - diamond(буби), s - spades(пики), h - heart(черви)
    string ranks[] = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "T"};
    vector<string> selectedCards; // Вектор для отслеживания уже выбранных карт
    // Функция для проверки, была ли уже выбрана данная карта
    auto isCardSelected = [&](const string& card) {
        return find(selectedCards.begin(), selectedCards.end(), card) != selectedCards.end();
    };

    // Функция для добавления выбранной карты в вектор выбранных карт
    auto addSelectedCard = [&](const string& card) {
        selectedCards.push_back(card);
    };
    int suitIndex, rankIndex;
    string card;
    do {
        suitIndex = rand() % 4;
        rankIndex = rand() % 13;
        card = suits[suitIndex] + " " + ranks[rankIndex];
    } while (isCardSelected(card)); // Проверка, была ли уже выбрана такая карта
    table.push_back(card);
    sort(table.begin(), table.end(), compareCards);
    all1.push_back(card);
    all2.push_back(card);
    sort(all1.begin(), all1.end(), compareCards);
    sort(all2.begin(), all2.end(), compareCards);
    addSelectedCard(card);

}
// Функция для первоначального размещения карт
auto addcard(vector<string>& place, int times)
{
    string suits[] = {"c", "d", "s", "h"};//где: с - club(крести), d - diamond(буби), s - spades(пики), h - heart(черви)
    string ranks[] = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "T"};
    vector<string> selectedCards; // Вектор для отслеживания уже выбранных карт
    // Функция для проверки, была ли уже выбрана данная карта
    auto isCardSelected = [&](const string& card) {
        return find(selectedCards.begin(), selectedCards.end(), card) != selectedCards.end();
    };

    // Функция для добавления выбранной карты в вектор выбранных карт
    auto addSelectedCard = [&](const string& card) {
        selectedCards.push_back(card);
    };
    for (int i = 0; i < times; ++i) {
        int suitIndex, rankIndex;
        string card;
        do {
            suitIndex = rand() % 4;
            rankIndex = rand() % 13;
            card = suits[suitIndex] + " " + ranks[rankIndex];
        } while (isCardSelected(card)); // Проверка, была ли уже выбрана такая карта

        place.push_back(card);
        addSelectedCard(card);
    }

    sort(place.begin(), place.end(), compareCards);
}
// Функция для нахождения комбинаций
auto checkCombo(vector<string>& all1, vector<string>& who, string& high, string& minim, int flag, string& message1, string& message2)
{
    vector<string> combo;
    char key = '0';
    int result = 0;
    int row = 1;
    int combination = 0;
    int counter = 0;
    int suits = 0;
    string street1;
    string street2;
    string flash1;

    int pair1 = 0;
    int pair2 = 0;
    int three = 0;
    int street = 0;
    int flash = 0;
    int fullhouse = 0;
    int four = 0;
    int streetflash = 0;
    int flashroyale = 0;

    string whois(1, who[1][2]);

    for (int i = 0; i < all1.size(); i++){
        string str(1, all1[i][2]);
        counter = 0;
        for (int j = i + 1; j < all1.size(); j++){
            if (all1[i][2] == all1[j][2])
            {
                if (toint(high) < toint(str))
                {
                    if (all1[i][2] == '1'){
                        high = "10";
                    }
                    else
                    {
                        high = all1[i][2];
                    }

                }
                if (toint(minim) > toint(str))
                {
                    if (all1[i][2] == '1'){
                        minim = "10";
                    }
                    else
                    {
                        minim = all1[i][2];
                    }
                }
                counter+=1;
            }
            if (counter == 2){
                key = all1[i][2];
            }
            if (counter == 1 && (all1[i][2] == key)){
                counter = 0;
            }
        }

        if (counter == 1){
            pair1+=1;
        }
        if (counter == 2){
            three += 1;
        }
        if (counter == 3){
            four+=1;
            if (four == 1){
                result = 7;
            }
        }


    }
    combo.push_back(high);
    combo.push_back(minim);



    for (int i = 0; i < all1.size() - 1; i++)
    {
        string str1(1, all1[i][2]);
        string str2(1, all1[i + 1][2]);
        if (toint(str1) + 1 == toint(str2))
        {
            row +=1;
            if (row >= 5)
            {
                street1 = all1[i - 3][2];
                street2 = all1[i + 1][2];
                street = 1;
            }
            if (all1[i+1][2] == 'T')
            {
                key = 'T';
            }
        }
        else if (toint(str1) == toint(str2))
        {
            continue;
        }
        else
        {
            row = 1;
            continue;
        }
    }
    for (int i = 0; i < all1.size(); i++)
    {
        for (int j = i + 1; j < all1.size(); j++){
            if (all1[i][0] == all1[j][0]){
                suits+=1;
                if (suits >= 10)
                {
                    combo[0] = all1[j][2];
                }
            }
        }
    }
    if (street == 1)
    {
        if (suits >= 10){
            if (key == 'T'){
                result = 9;
                combo[0] = street2;
                combo[1] = "10";
            }
            else{
                result = 8;
                combo[0] = street2;
                combo[1] = street1;
            }
        }
        else{
                combo[0] = street2;
                combo[1] = street1;
                result = 4;
        }
    }
    else if ((pair1 == 1 && three == 1)||(three == 2)||(pair1 == 2 && three == 1)){
        fullhouse+=1;
        result = 6;
    }
    else if (suits >= 10 && street == 0){
            result = 5;
    }
    else if (three == 1 && fullhouse != 1){
        result = 3;
    }



    else if (pair1 == 2 || pair1 == 3){
            pair2 +=1;
            if (pair2 == 1){
                result = 2;
            }
    }
    else if (pair1 == 1 && fullhouse != 1 && four != 1){
        result = 1;
    }
    if (flag == 1)
    {
        if (result == 9)
        {
            message1 += "Flash-Royale!\n";
        }
        else if (result == 8)
        {
            message1 += "Street-Flash!\n";
        }
        else if (result == 7)
        {
            message1 += "Four Of Kind!";
        }
        else if (result == 6)
        {
            message1 += "FullHouse!";
        }
        else if (result == 5)
        {
            message1 += "Flash!";
        }
        else if (result == 4)
        {
            message1 += "Street!";
        }
        else if (result == 3)
        {
            message1 += "Set!";
        }
        else if (result == 2)
        {
            message1 += "Two Of Pairs!";
        }
        else if (result == 1)
        {
            message1 += "Pair!";
        }
        else if (result == 0)
        {
            message1 += "High Card: ";
            if (all1[all1.size() - 1][2] == '1')
            {
                combo[0] = "10";
                message1 += string(1, all1[all1.size() - 1][2]);
                message1 += "0";
            }
            else
            {
                combo[0] = who[1][2];
                message1 += string(1, all1[all1.size() - 1][2]);
            }
        }

    }
    if (flag == 0)
    {
        if (result == 9)
        {
            message2 += "Flash-Royale!\n";
        }
        else if (result == 8)
        {
            message2 += "Street-Flash!\n";
        }
        else if (result == 7)
        {
            message2 += "Four Of Kind!";
        }
        else if (result == 6)
        {
            message2 += "FullHouse!";
        }
        else if (result == 5)
        {
            message2 += "Flash!";
        }
        else if (result == 4)
        {
            message2 += "Street!";
        }
        else if (result == 3)
        {
            message2 += "Set!";
        }
        else if (result == 2)
        {
            message2 += "Two Of Pairs!";
        }
        else if (result == 1)
        {
            message2 += "Pair!";
        }
        else if (result == 0)
        {
            message2 += "High Card: ";
            if (all1[all1.size() - 1][2] == '1')
            {
                combo[0] = "10";
                message2 += string(1, all1[all1.size() - 1][2]);
                message2 += "0";
            }
            else
            {
                combo[0] = who[1][2];
                message2 += string(1, all1[all1.size() - 1][2]);
            }
        }

    }

    combo.push_back(std::to_string(result));
    return combo;
}
// Функция для вывода
auto show(vector<string>& table, vector<string>& hands, vector<string>& op, int& croupier, int& times, int& moneyPlayer, int& moneyOp, string& message1, string& message2)
{
    if (times == 0)
    {
        cout << " Balance: " << moneyPlayer << endl;
    }
    else if (times == 1)
    {
        cout << "Balance: " << moneyPlayer << "(Notice: balance updates after the end of a round!)" << endl;
        cout << "==============================================================================================\n" << endl;
        cout << "Hands\t\t\t\t\t      Table\t\t\t\t      Opponent" << endl;

        cout << "_____\t\t\t\t\t _____ _____ _____ \t\t\t\t_____" << endl;
        cout << "|" << hands[0][2] << "  | \t\t\t\t\t |" << table[0][2] << "  | |" << table[1][2] << "  | |" << table[2][2] << "  |\t\t\t\t|   |" << endl;
        cout << "| " << hands[0][0] << " | \t\t\t\t\t | " << table[0][0] << " | | " << table[1][0] << " | | " << table[2][0] << " |\t\t\t\t| ? |" << endl;
        cout << "|__" << hands[0][2] << "| \t\t\t\t\t |__" << table[0][2] << "| |__" << table[1][2] << "| |__" << table[2][2] << "|\t\t\t\t|___|" << endl;

        cout << "_____\t\t\t\t\t\t\t    \t\t\t\t_____" << endl;
        cout << "|" << hands[1][2] << "  |\t\t\t\t\t\t\t\t\t\t\t|   |" << endl;
        cout << "| " << hands[1][0] << " |\t\t\t\t\t\t\t\t\t\t\t| ? |" << endl;
        cout << "|__" << hands[1][2] << "|\t\t\t\t\t\t\t\t\t\t\t|___|" << endl;

        cout << "==============================================================================================" << endl;
        cout << "Combination: " << message1 << "\t\t     ||\t\t\t\t      by Nikitin Artem" << endl;
        cout << "==============================================================================================\n" << endl;
        message1 = "";
        message2 = "";
    }
    else if (times == 2)
    {
        cout << "Balance: " << moneyPlayer << "(Notice: balance updates after the end of a round!)" << endl;
        cout << "==============================================================================================\n" << endl;
        cout << "Hands\t\t\t\t\t      Table\t\t\t\t      Opponent" << endl;

        cout << "_____\t\t\t\t     _____ _____ _____ _____    \t\t\t_____" << endl;
        cout << "|" << hands[0][2] << "  | \t\t\t\t     |" << table[0][2] << "  | |" << table[1][2] << "  | |" << table[2][2] << "  | |" << table[3][2] << "  |\t\t\t\t|   |" << endl;
        cout << "| " << hands[0][0] << " | \t\t\t\t     | " << table[0][0] << " | | " << table[1][0] << " | | " << table[2][0] << " | | " << table[3][0] << " |\t\t\t\t| ? |" << endl;
        cout << "|__" << hands[0][2] << "| \t\t\t\t     |__" << table[0][2] << "| |__" << table[1][2] << "| |__" << table[2][2] << "| |__" << table[3][2] << "|\t\t\t\t|___|" << endl;

        cout << "_____\t\t\t\t\t\t\t    \t\t\t\t_____" << endl;
        cout << "|" << hands[1][2] << "  |\t\t\t\t\t\t\t\t\t\t\t|   |" << endl;
        cout << "| " << hands[1][0] << " |\t\t\t\t\t\t\t\t\t\t\t| ? |" << endl;
        cout << "|__" << hands[1][2] << "|\t\t\t\t\t\t\t\t\t\t\t|___|" << endl;

        cout << "==============================================================================================" << endl;
        cout << "Combination: " << message1 << "\t\t     ||\t\t\t\t     by Nikitin Artem" << endl;
        cout << "==============================================================================================\n" << endl;
        message1 = "";
        message2 = "";
    }
    else if (times == 3)
    {

        cout << "Balance: " << moneyPlayer << "(Notice: balance updates after the end of a round!)" << endl;
        cout << "==============================================================================================\n" << endl;
        cout << "Hands\t\t\t\t\t      Table\t\t\t\t      Opponent" << endl;

        cout << "_____\t\t\t\t  _____ _____ _____ _____ _____   \t\t\t_____" << endl;
        cout << "|" << hands[0][2] << "  |\t\t\t\t  |" << table[0][2] << "  | |" << table[1][2] << "  | |" << table[2][2] << "  | |" << table[3][2] << "  | |" << table[4][2] << "  |\t\t\t\t|" << op[0][2] << "  |" << endl;
        cout << "| " << hands[0][0] << " |\t\t\t\t  | " << table[0][0] << " | | " << table[1][0] << " | | " << table[2][0] << " | | " << table[3][0] << " | | " << table[4][0] << " |\t\t\t\t| " << op[0][0] << " |" << endl;
        cout << "|__" << hands[0][2] << "|\t\t\t\t  |__" << table[0][2] << "| |__" << table[1][2] << "| |__" << table[2][2] << "| |__" << table[3][2] << "| |__" << table[3][2] << "|\t\t\t\t|__" << op[0][2] << "|" << endl;

        cout << "_____\t\t\t\t\t\t\t    \t\t\t\t_____" << endl;
        cout << "|" << hands[1][2] << "  |\t\t\t\t\t\t\t\t\t\t\t|" << op[1][2] << "  |" << endl;
        cout << "| " << hands[1][0] << " |\t\t\t\t\t\t\t\t\t\t\t| " << op[1][0] << " |" << endl;
        cout << "|__" << hands[1][2] << "|\t\t\t\t\t\t\t\t\t\t\t|__" << op[1][2] << "|" << endl;;

        cout << "==============================================================================================" << endl;
        cout << "Combination: " << message1 << "     ||" << "opponent combo: " << message2 << " ||\t      by Nikitin Artem" << endl;
        cout << "==============================================================================================\n";
        message1 = "";
        message2 = "";
    }
}
//Функция, показывающая победившего игрока
int round(vector<string>& comboPlayer, vector<string>& comboOp, vector<string>& hands, vector<string>& op, int& croupier, int& moneyPlayer, int& moneyOp)
{
    if (croupier != 0)
    {
        if (atoi(comboPlayer[2].c_str()) > atoi(comboOp[2].c_str()))
        {
            cout << "You win! +" << croupier/2 << "$\n";
            cout << "Next?\n1. Yes\n2. No\n";
            int next;
            cin >> next;
            system("cls");
            if (next == 1)
            {
                moneyPlayer += croupier;
                croupier = 0;
                next = 1;
                return next;
            }
            else
            {
                moneyPlayer += croupier;
                croupier = 0;
                next = 2;
                return next;
            }
        }
        else if (atoi(comboPlayer[2].c_str()) < atoi(comboOp[2].c_str()))
        {

            cout << "You lose! -" << croupier/2 << "$\n";
            cout << "Next?\n1. Yes\n2. No\n";;
            int next;
            cin >> next;
            system("cls");
            if (next == 1)
            {
                moneyOp += croupier;
                croupier = 0;
                next = 1;
                return next;
            }
            else
            {
                croupier = 0;
                next = 2;
                return next;
            }
        }
        else if (toint(comboPlayer[0]) > toint(comboOp[0]))
        {

            cout << "You win! +" << croupier/2 << "$\n";
            cout << "Next?\n1. Yes\n2. No\n";;
            int next;
            cin >> next;
            system("cls");
            if (next == 1)
            {
                moneyPlayer += croupier;
                croupier = 0;
                next = 1;
                return next;
            }
            else
            {
                croupier = 0;
                next = 2;
                return next;
            }
        }
        else if (toint(comboPlayer[0]) < toint(comboOp[0]))
        {

            cout << "You lose! -" << croupier/2 << "$\n";
            cout << "Next?\n1. Yes\n2. No\n";
            int next;
            cin >> next;
            system("cls");
            if (next == 1)
            {
                moneyOp += croupier;
                croupier = 0;
                next = 1;
                return next;
            }
            else
            {
                croupier = 0;
                next = 2;
                return next;
            }
        }
        else if (toint(comboPlayer[1]) > toint(comboOp[1]))
        {

            cout << "You win! +" << croupier/2 << "$\n";
            cout << "Next?\n1. Yes\n2. No\n";;
            int next;
            cin >> next;
            system("cls");
            if (next == 1)
            {
                moneyPlayer += croupier;
                croupier = 0;
                next = 1;
                return next;
            }
            else
            {
                croupier = 0;
                next = 2;
                return next;
            }
        }
        else if (toint(comboPlayer[1]) < toint(comboOp[1]))
        {

            cout << "You lose! -" << croupier/2 << "$\n";
            cout << "Next?\n1. Yes\n2. No\n";
            int next;
            cin >> next;
            system("cls");
            if (next == 1)
            {
                moneyOp += croupier;
                croupier = 0;
                next = 1;
                return next;
            }
            else
            {
                croupier = 0;
                next = 2;
                return next;
            }
        }
        else if (chartoint(hands[1][2]) > chartoint(op[1][2]))
        {

            cout << "You win! +" << croupier/2 << "$\n";
            cout << "Next?\n1. Yes\n2. No\n";
            int next;
            cin >> next;
            system("cls");
            if (next == 1)
            {
                moneyPlayer += croupier;
                croupier = 0;
                next = 1;
                return next;
            }
            else
            {
                croupier = 0;
                next = 2;
                return next;
            }
        }
        else if (chartoint(hands[1][2]) < chartoint(op[1][2]))
        {

            cout << "You lose! -" << croupier/2 << "$\n";
            cout << "Next?\n1. Yes\n2. No\n";
            int next;
            cin >> next;
            system("cls");
            if (next == 1)
            {
                moneyOp += croupier;
                croupier = 0;
                next = 1;
                return next;
            }
            else
            {
                croupier = 0;
                next = 2;
                return next;
            }
        }
        else if (chartoint(hands[0][2]) > chartoint(op[0][2]))
        {

            cout << "You win! +" << croupier/2 << "$\n";
            cout << "Next?\n1. Yes\n2. No\n";
            int next;
            cin >> next;
            system("cls");
            if (next == 1)
            {
                moneyPlayer += croupier;
                croupier = 0;
                next = 1;
                return next;
            }
            else
            {
                croupier = 0;
                next = 2;
                return next;
            }
        }
        else if (chartoint(hands[0][2]) < chartoint(op[0][2]))
        {

            cout << "You lose! -" << croupier/2 << "$\n";
            cout << "Next?\n1. Yes\n2. No\n";
            int next;
            cin >> next;
            system("cls");
            if (next == 1)
            {
                moneyOp += croupier;
                croupier = 0;
                next = 1;
                return next;
            }
            else
            {
                croupier = 0;
                next = 2;
                return next;
            }
        }
    }
    else
    {
        if (atoi(comboPlayer[2].c_str()) > atoi(comboOp[2].c_str()))
        {
            cout << "You could win!\n";
            cout << "Next?\n1. Yes\n2. No\n";
            int next;
            cin >> next;
            system("cls");
            if (next == 1)
            {
                next = 1;
                return next;
            }
            else
            {
                next = 2;
                return next;
            }
        }
        else if (atoi(comboPlayer[2].c_str()) < atoi(comboOp[2].c_str()))
        {
            cout << "Lucky! You could lose!\n";
            cout << "Next?\n1. Yes\n2. No\n";;
            int next;
            cin >> next;
            system("cls");
            if (next == 1)
            {
                next = 1;
                return next;
            }
            else
            {
                next = 2;
                return next;
            }
        }
        else if (toint(comboPlayer[0]) > toint(comboOp[0]))
        {
            cout << "You could win!\n";
            cout << "Next?\n1. Yes\n2. No\n";;
            int next;
            cin >> next;
            system("cls");
            if (next == 1)
            {
                next = 1;
                return next;
            }
            else
            {
                next = 2;
                return next;
            }
        }
        else if (toint(comboPlayer[0]) < toint(comboOp[0]))
        {
            cout << "Lucky! You could lose!\n";
            cout << "Next?\n1. Yes\n2. No\n";
            int next;
            cin >> next;
            system("cls");
            if (next == 1)
            {
                next = 1;
                return next;
            }
            else
            {
                next = 2;
                return next;
            }
        }
        else if (toint(comboPlayer[1]) > toint(comboOp[1]))
        {
            cout << "You could win!\n";
            cout << "Next?\n1. Yes\n2. No\n";;
            int next;
            cin >> next;
            system("cls");
            if (next == 1)
            {
                next = 1;
                return next;
            }
            else
            {
                next = 2;
                return next;
            }
        }
        else if (toint(comboPlayer[1]) < toint(comboOp[1]))
        {
            cout << "Lucky! You could lose!\n";
            cout << "Next?\n1. Yes\n2. No\n";
            int next;
            cin >> next;
            system("cls");
            if (next == 1)
            {
                next = 1;
                return next;
            }
            else
            {
                next = 2;
                return next;
            }
        }
        else if (chartoint(hands[1][2]) > chartoint(op[1][2]))
        {
            cout << "You could win!\n";
            cout << "Next?\n1. Yes\n2. No\n";
            int next;
            cin >> next;
            system("cls");
            if (next == 1)
            {
                next = 1;
                return next;
            }
            else
            {
                next = 2;
                return next;
            }
        }
        else if (chartoint(hands[1][2]) < chartoint(op[1][2]))
        {
            cout << "Lucky! You could lose!\n";
            cout << "Next?\n1. Yes\n2. No\n";
            int next;
            cin >> next;
            system("cls");
            if (next == 1)
            {
                next = 1;
                return next;
            }
            else
            {
                next = 2;
                return next;
            }
        }
        else if (chartoint(hands[0][2]) > chartoint(op[0][2]))
        {
            cout << "You could win!\n";
            cout << "Next?\n1. Yes\n2. No\n";
            int next;
            cin >> next;
            system("cls");
            if (next == 1)
            {
                next = 1;
                return next;
            }
            else
            {
                next = 2;
                return next;
            }
        }
        else if (chartoint(hands[0][2]) < chartoint(op[0][2]))
        {
            cout << "Lucky! You could lose!\n";
            cout << "Next?\n1. Yes\n2. No\n";
            int next;
            cin >> next;
            system("cls");
            if (next == 1)
            {
                next = 1;
                return next;
            }
            else
            {
                next = 2;
                return next;
            }
        }
    }
}
//Функция для прохождения одного курса
int thegame(vector<string>& table, vector<string>& hands, vector<string>& op, vector<string>& all1, vector<string>& all2, vector<string>& comboPlayer, vector<string>& comboOp, int& times, int& step, int& moneyPlayer, int& moneyOp, int& croupier, string& highPlayer, string& minPlayer, string& highOp, string& minOp)
{

    string message1 = "";
    string message2 = "";
    if (times < 3) {
        if (times == 0)
        {
            times+=1;
            comboPlayer = checkCombo(all1, hands, highPlayer, minPlayer, 1, message1, message2);
            comboOp = checkCombo(all2, op, highOp, minOp, 0, message1, message2);
            show(table, hands, op, croupier, times, moneyPlayer, moneyOp, message1, message2);
        }
        cout << "1. Check\n2. Raise\n3. Hand in " << endl;
        cin >> step;
        system("cls");
        if (step == 1) {
            times+=1;
            updatetable(table, all1, all2);

            comboPlayer = checkCombo(all1, hands, highPlayer, minPlayer, 1, message1, message2);
            comboOp = checkCombo(all2, op, highOp, minOp, 0, message1, message2);
            show(table, hands, op, croupier, times, moneyPlayer, moneyOp, message1, message2);

        } else if (step == 2) {
            times +=1;
            int bet;
            cout << "Your bet: ";
            cin >> bet;
            while (bet > moneyPlayer) {
                cout << "You Don't have enough money\n1. Decrease\n2. Cancel Bet";
                cin >> step;
                if (step == 1) {
                    cout << "Your bet: \n";
                    cin >> bet;
                }
                if (step == 2) {
                    bet = 0;
                }
            }
            moneyPlayer -= bet;
            moneyOp -= bet;
            croupier = croupier + bet + bet;

            system("cls");
            updatetable(table, all1, all2);
            comboPlayer = checkCombo(all1, hands, highPlayer, minPlayer, 1, message1, message2);
            comboOp = checkCombo(all2, op, highOp, minOp, 0, message1, message2);
            show(table, hands, op, croupier, times, moneyPlayer, moneyOp, message1, message2);

        } else if (step == 3) {
            cout << "Surround?\n1. Yes\n2. No\n";
            cin >> step;
            system("cls");
            if (step == 1) {
                if (times == 1)
                {
                    updatetable(table, all1, all2);
                    updatetable(table, all1, all2);
                }
                else if (times == 2)
                {
                    updatetable(table, all1, all2);
                }
                times = 3;
                comboPlayer = checkCombo(all1, hands, highPlayer, minPlayer, 1, message1, message2);
                comboOp = checkCombo(all2, op, highOp, minOp, 0, message1, message2);
                show(table, hands, op, croupier, times, moneyPlayer, moneyOp, message1, message2);

            } else {
                comboPlayer = checkCombo(all1, hands, highPlayer, minPlayer, 1, message1, message2);
                comboOp = checkCombo(all2, op, highOp, minOp, 0, message1, message2);
                show(table, hands, op, croupier, times, moneyPlayer, moneyOp, message1, message2);
            }
        }
    return 1;
    }
    else if (times == 3)
    {
        times = 0;
        return round(comboPlayer, comboOp, hands, op, croupier, moneyPlayer, moneyOp);
        croupier = 0;
    }
    else if (times == 4)
    {
        comboPlayer = checkCombo(all1, hands, highPlayer, minPlayer, 1, message1, message2);
        comboOp = checkCombo(all2, op, highOp, minOp, 0, message1, message2);
        times = 3;
        show(table, hands, op, croupier, times, moneyPlayer, moneyOp, message1, message2);
        return 0;
    }
}
int main()
{
    char Title[1024];
    GetConsoleTitle(Title, 1024); // Узнаем имя окна
    HWND hwnd=FindWindow(NULL, Title); // Узнаем hwnd окна

    //MoveWindow(hwnd,x,y,width,height,repaint);
    MoveWindow(hwnd,100,50,725,400,true);

    int choose;

    cout << "\t\t\t\t ____	__  __   __    ____" << endl;
    cout << "\t\t\t\t//  \\\\  ||  ||  //\\\\  ||  \\\\" << endl;
    cout << "\t\t\t\t||  ||  ||  || ||  || ||__//" << endl;
    cout << "\t\t\t\t|| ___  ||  || ||==|| ||" << endl;
    cout << "\t\t\t\t||  ||  ||  || ||  || ||" << endl;
    cout << "\t\t\t\t\\\\__//  \\\\__// ||  || ||" << endl;
    cout << "\t\t\t\t      POKER. THE GAME" << endl;
    cout << "\n\n\n\t\t\t\t\t 1.Start\n\t\t\t\t\t 2.Quit" << endl;
    cout << "\n\t\t\t\t     ====>  ";
    cin >> choose;

    int times = 0;

    while (choose == 1)
    {
        system("cls");
        int moneyPlayer;
        cout << "\n\n\n\n\n\n\n\n\t\t\t\tYour playing value: ";
        cin >> moneyPlayer;
        int moneyOp;
        moneyOp = moneyPlayer;
        int croupier = 0;
        system("cls");

        string highPlayer = "0";
        string minPlayer = "50";
        string highOp = "0";
        string minOp = "50";
        vector<string> comboPlayer;
        vector<string> comboOp;


        srand(time(0)); // Инициализация генератора случайных чисел

        vector<string> table; // Вектор для хранения карт на столе
        vector<string> hands; // Вектор для хранения карт в руке игрока
        vector<string> op;    // Вектор для хранения карт в руке оппонента
        vector<string> all1;
        vector<string> all2;

        int step;
        int go = 1;
        while (go != 2)
        {
            if (times == 0)
            {
                table.clear();
                hands.clear();
                op.clear();
                all1.clear();
                all2.clear();
                addcard(table, 3);
                addcard(hands, 2);
                addcard(op, 2);

                for (const string& card: table){
                    all1.push_back(card);
                }
                for (const string& card: hands){
                    all1.push_back(card);
                }
                sort(all1.begin(), all1.end(), compareCards);

                for (const string& card: table){
                    all2.push_back(card);
                }
                for (const string& card: op){
                    all2.push_back(card);
                }
                sort(all2.begin(), all2.end(), compareCards);

            }

            go = thegame(table, hands, op, all1, all2, comboPlayer, comboOp, times, step, moneyPlayer, moneyOp, croupier, highPlayer, minPlayer, highOp, minOp);

            if (go == 2)
            {
                choose = 2;
            }
            if (times == 3 && (moneyOp < 1 || moneyPlayer < 1))
            {
                choose = thegame(table, hands, op, all1, all2, comboPlayer, comboOp, times, step, moneyPlayer, moneyOp, croupier, highPlayer, minPlayer, highOp, minOp);
                times = 4;
                if (choose == 1)
                {
                    if (moneyOp < 1)
                    {
                        thegame(table, hands, op, all1, all2, comboPlayer, comboOp, times, step, moneyPlayer, moneyOp, croupier, highPlayer, minPlayer, highOp, minOp);;
                        cout << "Congratulations! You win! Opponent ran out of money.\n" << endl;
                        times = 0;
                    }
                    else if (moneyPlayer < 1)
                    {
                        thegame(table, hands, op, all1, all2, comboPlayer, comboOp, times, step, moneyPlayer, moneyOp, croupier, highPlayer, minPlayer, highOp, minOp);
                        cout << "You loose. You ran out of balance. Good luck mext time!\n" << endl;
                        times = 0;
                    }
                    cout << "1.Start new game\n2.Exit" << endl;
                    cin >> choose;
                    go = 2;
                }
                else if (choose == 2)
                {
                    go = 2;
                }
            }

        }
    }
    system("cls");
    cout << "\t\t\t\t ____	__  __   __    ____" << endl;
    cout << "\t\t\t\t//  \\\\  ||  ||  //\\\\  ||  \\\\" << endl;
    cout << "\t\t\t\t||  ||  ||  || ||  || ||__//" << endl;
    cout << "\t\t\t\t|| ___  ||  || ||==|| ||" << endl;
    cout << "\t\t\t\t||  ||  ||  || ||  || ||" << endl;
    cout << "\t\t\t\t\\\\__//  \\\\__// ||  || ||" << endl;
    cout << "\t\t\t\t      POKER. THE GAME" << endl;
    cout << "\n\n\t\t\t\t       See You soon!\n\t\t\t    Press any key to shutdown the game...\n\n\n\n\n\n\n\n";

    return 0;
}