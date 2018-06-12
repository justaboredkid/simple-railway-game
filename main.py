import random
from math import sin, cos, sqrt, atan2, radians
from fractions import Fraction
from collections import Counter

cities = {
    'Toronto': ['on', 43.654805, -79.380595],
    'Montreal': ['qc', 45.501080, -73.568140],
    'Ottawa': ['on', 45.415387, -75.565701],
    'Edmonton': ['ab', 53.594894, -113.463576],
    'Winnipeg': ['ma', 49.897735, -97.134426],
    'Brampton': ['on', 43.735508, -79.767844],
    'Seattle': ['wa', 47.607286, -122.334005],
    'Moscow': ['id', 46.731839, -117.010040],
    'Philadelphia': ['pe', 39.961121, -75.160669],
    'Fargo': ['nd', 46.876391, -96.783252],
    'Brooklyn': ['ny', 40.679016, -73.936774],
    'Concord': ['nh', 43.206977, -71.527225],
    'Springfield': ['il', 39.781697, -89.651612],
    'Kamloops': ['bc', 50.687770, -120.347863],
    'Dallas': ['tx', 32.775833, -96.796667],
    'Nashville': ['tn', 36.162725, -86.781820],
    'Salt Lake City': ['ut', 40.75, -111.883333],
    'Houston': ['tx', 29.762778, -95.383056],
    'Atlanta': ['ga', 33.755, -84.39]
}

regions = {
    'bc': ['British Columbia', 'mountains', 'forest', 'snow', 'rainy', 'ca'],
    'qc': ['Quebec', 'French', 'snow', 'arctic', 'rainy', 'ca'],
    'on': ['Ontario', 'snow', 'cold', 'ca'],
    'ab': ['Alberta', 'snow', 'cold', 'mountains', 'ca'],
    'ma': ['Manitoba', 'ca'],
    'wa': ['Washington', 'rainy', 'us'],
    'wy': ['Wyoming', 'dry', 'windy', 'extreme', 'mountains', 'us'],
    'id': ['Idaho', 'humid', 'rainy', 'freshwater', 'us'],
    'pe': ['Pennsylvania', 'humid', 'cold', 'snow', 'dry', 'freshwater', 'us'],
    'ny': ['New York', 'cold', 'dry', 'snow', 'forest', 'freshwater', 'us'],
    'nd': ['North Dakota', 'hot', 'humid', 'mountains', 'us'],
    'nh':
    ['New Hampshire', 'windy', 'humid', 'snow', 'extreme', 'mountains', 'us'],
    'il': ['Illinois', 'us'],
    'tx': ['Texas', 'us'],
    'tn': ['Tennessee', 'us'],
    'ut': ['Utah', 'us'],
    'ga': ['Georgia', 'us']
}


def buildtrack(station, destination, player, devtag):
    if due[player] <= 0:
        while True:

            a = list(cities[station])
            b = list(cities[destination])
            # I plagiarized this bit
            r = 6373.0

            lat1 = radians(a[1])
            lon1 = radians(a[2])
            lat2 = radians(b[1])
            lon2 = radians(b[2])

            dlon = lon2 - lon1
            dlat = lat2 - lat1

            a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))
            length = r * c
            # Track is not straight
            bias = random.randint(250, 300)
            length = int(length) + bias
            if length >= 1000:
                if devtag == 1:
                    return
                else:
                    print(
                        "You can't build that! It's too long! What do you expect?"
                    )
                    return
            else:
                if devtag == 1:
                    return length
                while True:
                    try:
                        while True:
                            people = int(
                                input(
                                    "How many workers do you want to hire? (Type any letters to cancel)> "
                                ))
                            if Fraction(-1, 50) * (people + (Fraction(
                                    -3, 10) * int(rnd[player]))) + length <= 0:
                                print("Too many people")
                                pass
                            else:
                                while True:
                                    iratio = []
                                    groups = [
                                        "white", "immigrant/aboriginal",
                                        "black"
                                    ]
                                    for item in groups:
                                        iratio.append(
                                            int(
                                                input("ratio of workers (" +
                                                      item + ") %>")) / 100)

                                    if sum(iratio) != 1:
                                        print(
                                            "over/under 100 percent. Try again"
                                        )
                                        pass
                                    else:
                                        ratio[player] = iratio
                                        break
                                break

                    except ValueError:
                        return

                    cost = []
                    workers[player] = people
                    people = people + (Fraction(-3, 10) * int(rnd[player]))
                    pay = wages.get(player)[:-1]
                    for item in pay:
                        a = item
                        if item == 0:
                            ethicality[player] = ethicality[player] - 33
                            pass
                        elif item != pay[0]:
                            ethicality[player] = ethicality[player] - 10
                            pass
                        else:
                            calc = int(length * (people * a))
                            cost.append(calc)

                    c = 0
                    for item in cost:
                        if c == 3:
                            break
                        else:
                            cost[c] = item * ratio.get(player)[c]
                            c += 1

                    cost = sum(cost)

                    if money[player] - cost <= 0:
                        print(cost - money[player])
                        print("Too expensive")
                        break
                    while True:
                        if wages.get(player)[-1] == '2':
                            confirm = input("Total cost is $" + str(
                                cost) + ". That is around $" + format(
                                    int(cost / length), '.2f'
                                ) + " per KM. Are you sure? (Y/N)>").lower()

                            if confirm not in ['y', 'n']:
                                print("Really?")
                                pass
                            else:
                                if confirm == 'y':
                                    due[player] = Fraction(
                                        -1, 50) * people + length
                                    print("It will take " + str(due[player]) +
                                          " weeks to complete.")
                                    moneychange(-cost, player)
                                    project[player] = destination
                                    return
                                else:
                                    print("Building cancelled")
                                    return
                        else:
                            time = Fraction(-1, 50) * people + length
                            confirm = input("Total cost is $" + str(
                                cost) + ". That is around $" + str(
                                    format(cost / time, '.2f')
                                ) + " per week. Are you sure? (Y/N)>").lower()
                            if confirm == 'y':
                                due[player] = time
                                print("It will take " + str(due[player]) +
                                      " weeks to complete.")
                                moneychange(-(cost / time), player)
                                project[player] = destination
                                return

    else:
        print("no building 4 u")
        return


def build(player):
    while True:
        print("Player " + player.upper() + ": ")
        distance = []
        starting = list(stations.get(player))
        print(starting)
        for key in cities:
            if key == starting[0]:
                pass
            else:
                l = buildtrack(starting[0], key, player, 1)
                if l is None:
                    pass
                else:
                    distance.append([key, regions[cities.get(key)[0]][0], l])
        print(distance, "\n")
        while True:
            build = input("Where to go first? >").title()
            if build not in list(cities.keys()):
                print("Umm... Wrong city.")
                pass
            elif build == 'exit':
                print("Exiting...")
                return
            else:
                buildtrack(starting[0], build, player, 0)
                return


def point(player):
    value = money[player]
    place = int(len(stations.get(player)))
    ethics = ethicality[player] / 100
    return (value / 10000) * place * ethics


def message(mt, amount, player):
    if mt == "getmoney":
        print("Player " + player.upper() + " has earned $" + str(amount))
    if mt == "test":
        print("this is a test message")
    if mt == "spentmoney":
        print("Player " + player.upper() + " has spent $" + str(abs(amount)))
    if mt == "rndcheat":
        rnd[player] = amount
        print("Player " + player.upper() + " has time traveled and stole " +
              str(abs(amount)) + " RND points")


def moneychange(amount, player):
    amount = int(amount)
    money[player] = int(money[player]) + amount
    if amount <= 0:
        message("spentmoney", amount, player)
    if amount >= 0:
        message("getmoney", amount, player)


def setup(faction, player):
    if faction == "g":
        moneychange(2500000, player)
        print("\nPlayer " + player.upper() +
              ", you have chosen to get funded by the Government."
              )  # add what this means, word formating
        print("Which project do you want to participate in?")
        while True:
            project[player] = input("(CA/US)> ")
            project[player] = project[player].lower()
            if project[player] not in ['ca', 'us']:
                print("\nYeah... Nope.\n")
                pass
            else:
                break

    if faction == "p":
        interest = {"a": 0, "b": 0, "c": 0}
        inipay = {"a": 0, "b": 0, "c": 0}
        time = {"a": 0, "b": 0, "c": 0}
        for key in interest:
            interest[key] = format(random.uniform(1, 4), ".2f")
        for key in inipay:
            inipay[key] = float(format(random.uniform(5, 25), ".2f")) * 1000000
        for key in time:
            time[key] = random.randint(2, 6)
        print("Player " + player.upper() + ", choose your investor:")
        for key in interest:
            print("Investor " + key.upper() + ": " + str(inipay[key]) + " " +
                  str(interest[key]) + "% per " + str(time[key]) + " weeks")
        while True:
            investor = input("> ")
            investor = investor.lower()
            if investor not in ['a', 'b', 'c']:
                print("that investor does not exist.")
                pass
            else:
                moneychange(inipay[investor], player)
                monthpay[player] = [
                    interest[investor], time[investor], inipay[investor]
                ]
                break

    if faction == "c":

        pass


def start():
    locations = list(cities.keys())
    starting = random.randint(0, len(locations) - 1)
    return locations[starting]


def nextweek():
    for key in wages:
        if due[key] == 0:
            print("Station " + project[key] + " has completed!")
            stations[key].append(project[key])
            project[key] = ''
        else:
            if wages.get(key)[-1] == 1:
                print("Player " + key.upper() + ": Wages")
                cost = ((wages.get(key)[0] *
                         (workers[key] * ratio.get(key)[0])) +
                        (wages.get(key)[1] *
                         (workers[key] * ratio.get(key)[1])) +
                        (wages.get(key)[2] *
                         (workers[key] * ratio.get(key)[2]))) * 4
                moneychange(-cost, key)
                due[key] -= 1
            else:
                due[key] -= 1

    for key in monthpay:
        if monthpay.get(key)[-1] == 0:
            print("Player " + key.upper() + " does not need to repay anything")
        else:
            numweek = week / monthpay.get(key)[1]
            monthpay.get(key)[-1] = (
                monthpay.get(key)[-1] *
                (monthpay.get(key)[0] / 100) + monthpay.get(key)[-1]
            ) * int(numweek)
            print("Player " + key.upper() + ", you now owe $" +
                  str(list(monthpay.get(key))[-1]))

    for key in due:
        if due[key] == 0:
            break
        else:
            break  # WILD CARDS!

    for key in money:
        if money[key] <= 0:
            print("GAME OVER. Player " + key.upper() + " Filed for bankruptcy")
            for key in wages:
                a = point(key)
                print("Player " + key.upper() + str(a))
            exit()
    for key in stations:
        for item in stations[key]:
            moneychange(5000, key)
            print("from " + item + " station")


factions = {'a': '', 'b': '', 'c': '', 'd': ''}
print(
    "\nDisclaimer: This game is based on 1860s money, not 2018. Inflation applies."
)
for key in factions:
    while True:
        choice = input("\nPlayer " + key.upper(
        ) + ": Select how you are going to start your railway: (Government/Private) >"
                       )
        if choice not in ['g', 'p', 'c']:
            print("try again")
            pass
        else:
            factions[key] = choice
            break

week = 0
money = {"a": 0, "b": 0, "c": 0, "d": 0}
workers = {"a": 0, "b": 0, "c": 0, "d": 0}
due = {"a": 0, "b": 0, "c": 0, "d": 0}
monthpay = {
    "a": [0, 0, 0],
    "b": [0, 0, 0],
    "c": [0, 0, 0],
    "d": [0, 0, 0]
}  # interest, weeks, owe
wages = {
    "a": [0, 0, 0, 0],
    "b": [0, 0, 0, 0],
    "c": [0, 0, 0, 0],
    "d": [0, 0, 0, 0]
}  # white, immigrant/aboriginal, black, km/hr
ratio = {"a": [0, 0, 0], "b": [0, 0, 0], "c": [0, 0, 0], "d": [0, 0, 0]}
rnd = {"a": 0, "b": 0, "c": 0, "d": 0}
project = {"a": "", "b": "", "c": "", "d": ""}
stations = {"a": [""], "b": [""], "c": [""], "d": [""]}
ethicality = {"a": 100, "b": 100, "c": 100, "d": 100}

for key in factions:
    setup(factions[key], key)

for key in stations:
    while True:
        bgin = start()
        print(bgin)
        chosen = list(stations.values())
        print(chosen)
        country = project[key]
        if Counter(chosen)[bgin] > 0:
            print(Counter(chosen)[bgin])
            pass
        else:
            if country == list(regions[list(cities.get(bgin))[0]])[-1]:
                stations[key] = [bgin]
                project[key] = ''
                print(stations[key])
                print(stations.values())
                print(Counter(chosen))
                break
            elif country == '':
                stations[key] = [bgin]
                break
            else:
                pass

for key in wages:
    pay = [0, 0, 0, 0]
    while True:
        print("Player " + key.upper() + ": ")
        print("\nAdjust wages between ethnic groups")
        print("1. White")
        print("2. Immigrants and Aboriginals")
        print("3. Black")
        print("4. All")
        print("\nn: Next Step")
        groups = input("> ").lower()
        if groups not in ['1', '2', '3', '4', 'n']:
            print("\nreally?\n")
            pass

        else:
            if groups == 'n':
                pay[-1] = 2
                wages[key] = pay
                break

            else:
                print("select amount")
                amount = input("$> ")
                try:
                    if groups == '4':
                        pay = [int(amount), int(amount), int(amount), 0]
                    else:
                        pay[int(groups) - 1] = int(amount)
                except ValueError:
                    print("Nope")
                    pass

    while True:
        print("\n\n\n\nPlayer " + key.upper() + ": ")
        print("Hourly or Per KM?")
        print("1. Hourly")
        print("2. per KM")
        print("n: Next Player")
        per = input("> ").lower()
        if per not in ['1', '2', 'n']:
            print("\nSELECT THE NUMBER!!\n")
            pass
        elif per == 'n':
            if pay[-1] == 0:
                print("Hey! How are you going to pay them?")
                pass
            else:
                print("\n" * 20)
                break
        else:
            pay[-1] = per
            pass

for key in stations:
    build(key)

week += 4  # edit next week
nextweek()

while True:
    for key in stations:
        while True:
            print("Week " + week + " : ")
            print('Options:')
            print('1. Build More Railways')
            print('2. Research')
            print('3. Pay loan')
            print('4. Stop game')
            print('\nN: Next Player')
            menu = input('> ').lower
            try:
                if menu is not [1, 2, 3, 4]:
                    print('\nInvalid option.')
                    pass
                else:
                    if menu == 1:
                        build(key)
                    if menu == 2:
                        print("This feature is still unavailable")
                        # research(key)
                    if menu == 3:
                        print("This feature is still unavailable")
                        # loan(key)
                    if menu == 4:
                        for key in wages:
                            a = point(key)
                            print("Player " + key.upper() + str(a))
                        exit()
            except TypeError:
                if menu is not 'n':
                    print('\nInvalid option.')
                    pass
                else:
                    break
        break
