from __future__ import print_function
from math import sin, cos, sqrt, atan2, radians
from fractions import Fraction
import random
import secrets

cities = {
    'Toronto': ['on', 43.654805, -79.380595],
    'Montreal': ['qc', 45.501080, -73.568140],
    'Ottawa': ['on', 45.415387, -75.565701],
    'Edmonton': ['ab', 53.594894, -113.463576],
    'Winnipeg': ['ma', 49.897735, -97.134426],
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
    #'Salt Lake City': ['ut', 40.75, -111.883333],
    'Houston': ['tx', 29.762778, -95.383056],
    'Atlanta': ['ga', 33.755, -84.39],
    'Calgary': ['ab', 51.04861, -114.07084],
    'Hemingford': ['nb', 42.32162, -103.07297],
    'Alexandria': ['mi', 45.88481, -95.37766],
    'Rugby': ['nd', 48.36888, -99.99624],
    'Chicago': ['il', 41.87811, -87.62979],
    'Sioux Falls': ['sd', 43.54459, -96.7311],
    'Casper': ['wy', 42.85007, -106.32517],
    'Tillamook': ['or', 45.45621, -123.84401],
    'Cincinnati': ['oh', 39.10311, -84.51201],
    'Pittsburgh': ['pe', 40.43956, -79.98986],
    'Alameda': ['cl', 37.7652, -122.24163],
    'Anahiem': ['cl', 33.83659, -117.9143],
    'Arcata': ['cl', 40.86651, -124.08283],
    #'Santa Fe': ['nm', 35.68697, -105.93779],
    'Memphis': ['tn', 35.14953, -90.04898]
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
    'ga': ['Georgia', 'us'],
    'nb': ['Nebraska', 'us'],
    'mi': ['Minnesota', 'us'],
    'sd': ['South Dakota', 'us'],
    'or': ['Oregon', 'us'],
    'oh': ['Ohio', 'us'],
    'cl': ['California', 'us'],
    'nm': ['New Mexico', 'us']
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
                            due[player] = 0
                            people = int(
                                input(
                                    "How many workers do you want to hire? (Type any letters to cancel)> "
                                ))
                            if Fraction(-1, 50) * (people + (Fraction(
                                    -3, 10) * int(rnd[player]))) + length <= 0:
                                print("Too many people")
                            else:
                                while True:
                                    iratio = []
                                    groups = [
                                        "white", "immigrant/aboriginal", "black"
                                    ]
                                    for item in groups:
                                        iratio.append(
                                            int(
                                                input("ratio of workers (" +
                                                      item + ") %>")) / 100)

                                    if sum(iratio) != 1:
                                        print(
                                            "over/under 100 percent. Try again")
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
                        elif item != pay[0]:
                            ethicality[player] = ethicality[player] - 10
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
                            confirm = input(
                                "Total cost is $" + str(cost) +
                                ". That is around $" +
                                format(int(cost / length), '.2f') +
                                " per KM. Are you sure? (Y/N)>").lower()

                            if confirm not in ['y', 'n']:
                                print("Really?")
                            else:
                                if confirm == 'y':
                                    due[player] = Fraction(-1,
                                                           50) * people + length
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
                            confirm = input(
                                "Total cost is $" + str(cost) +
                                ". That is around $" +
                                str(round(cost / time, 2)) +
                                " per week. Are you sure? (Y/N)>").lower()
                            if confirm not in ['y', 'n']:
                                print("Oh. You are not sure.")
                            else:
                                if confirm == 'y':
                                    due[player] = time
                                    print("It will take " + str(due[player]) +
                                          " weeks to complete.")
                                    moneychange(-(cost / time), player)
                                    project[player] = destination
                                    return
                                else:
                                    break
    else:
        print("no building 4 u")
        return


def build(player, choicetag):
    while True:
        print("\nPlayer " + player.upper() + ": ")
        distance = []
        if choicetag == 1:
            starting = []
        else:
            starting = stations.get(player)
            print(starting)
        for key in cities:
            if choicetag == 1:
                if project[player] is '':
                    print(key)
                    distance = []
                else:
                    if project[player] == list(regions[list(
                            cities.get(key))[0]])[-1]:
                        print(key)
                    else:
                        pass
            else:
                if key == starting:
                    pass
                else:
                    l = buildtrack(starting, key, player, 1)
                    if l is None:
                        pass
                    else:
                        distance.append(
                            [key, regions[cities.get(key)[0]][0], l])
        print(distance, "\n")
        while True:
            if choicetag == 1:
                pick = input("Starting station: >").title()
                if pick in list(stations.values()):
                    print("Really? Nuuupe")
                elif pick not in list(cities.keys()):
                    print("Wow.")
                else:
                    stations[player] = pick
                    project[player] = ''
                    return

            else:
                build = input("Where to go? >").title()
                if build not in list(cities.keys()):
                    print("Umm... Wrong city.")
                elif build == 'exit':
                    print("Exiting...")
                    return
                elif build in list(project.values()):
                    print("Someone else is taking that")
                elif build in list(stations.values()):
                    print("Someone already got that station")
                else:
                    buildtrack(starting, build, player, 0)
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
    if mt == "moneystat":
        print("player " + player.upper() + " has $" + str(money[player]))


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
        print(
            "\nPlayer " + player.upper() +
            ", you have chosen to get funded by the Government. You get less money, but you don't have to pay back."
        )  # add what this means, word formating
        print("Which project do you want to participate in?")
        while True:
            project[player] = input("(CA/US)> ")
            project[player] = project[player].lower()
            if project[player] not in ['ca', 'us']:
                print("\nYeah... Nope.\n")
            else:
                break

    if faction == "p":
        interest = {"a": 0, "b": 0, "c": 0}
        inipay = {"a": 0, "b": 0, "c": 0}
        time = {"a": 0, "b": 0, "c": 0}
        for key in interest:
            interest[key] = round(random.uniform(1, 4), 2)
        for key in inipay:
            inipay[key] = round(random.uniform(5, 25), 2) * 1000000
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
            else:
                moneychange(inipay[investor], player)
                monthpay[player] = [
                    interest[investor], time[investor], inipay[investor]
                ]
                break

    if faction == "c":  #Chain funding (Chain of train stations (NO RAILRD))
        print("this feature is not complete. you are not supposed to be here")


def nextweek():  #per letter station count, the output of monthpay is buggy
    for key in wages:
        if due[key] == 0:
            print("Station " + project[key] + " has completed!")
            stations[key].append(project[key])
            project[key] = ''
        else:
            if wages.get(key)[-1] == 1:
                print("Player " + key.upper() + ": Wages")
                cost = (
                    (wages.get(key)[0] * (workers[key] * ratio.get(key)[0])) +
                    (wages.get(key)[1] * (workers[key] * ratio.get(key)[1])) +
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
            monthpay.get(key)[-1] = (monthpay.get(key)[-1] *
                                     (monthpay.get(key)[0] / 100) +
                                     monthpay.get(key)[-1]) * int(numweek)
            print("Player " + key.upper() + ", you now owe $" +
                  str(list(monthpay.get(key))[-1]))

    for key in due:
        if due[key] == 0:
            break
        else:
            # wildcard(attrib, diff, type)
            break

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


def randomcity(player):
    while True:
        rcity = secrets.choice(list(cities.keys()))
        if rcity in list(stations.values()):
            pass
        elif list(project[player]) is None:
            stations[player] = rcity
            print("Your starting city is " + rcity)
            return
        else:
            if regions[cities[rcity][0]][-1] not in project[player]:
                pass
            else:
                stations[player] = rcity
                project[player] = []
                print("Your starting city is " + rcity)
                return


def loan(player):
    print("You need to pay " + str(list(monthpay.get(player))[-1]) + " dollars")
    if monthpay.get(player)[-1] >= money[player]:
        print("You don't have enough money for paying back.")
        return
    else:
        while True:
            repay = input("Confirm? (y/n) > ").lower()
            if repay not in ['y', 'n']:
                print("The investor does not like jokes.")
            else:
                moneychange(list(monthpay.get(player)[-1]), player)
                monthpay[player] = [0, 0, 0]
                investquery = input(
                    "Do you want more funding? (y/n) > ").lower()
                if investquery not in ['y', 'n']:
                    print("I have no time for you sillyness, choose a option.")
                else:
                    if investquery == 'y':
                        setup('p', player)
                    else:
                        return


print(
    "\nDisclaimer: This game is based on 1860s money, not 2018. Inflation applies."
)
while True:
    print("Hello There! Please select the amount of players. (2-26)")

    try:
        amount = int(input("> "))
        if amount == 1:
            print(
                "loooonnnnely... I am mr loooonnnnely... I have nobody..... All on my owwwnnn!!!"
            )
        elif amount < 0:
            print("Sorry, no downers allowed here.")
        elif amount == 0:
            print("Really, then why do you bother to play.")
        elif amount > 26:
            print("Too crowded.")
        else:
            players = list(map(chr, range(97, 97 + amount)))
            initvalue = {p: 0 for p in players}
            money = dict(initvalue)
            workers = dict(initvalue)
            due = dict(initvalue)
            rnd = dict(initvalue)
            ethicality = {p: 100 for p in players}
            wages = {p: [0, 0, 0, 0] for p in players}
            monthpay = {p: [0, 0, 0] for p in players}
            stations = {p: [""] for p in players}
            project = {p: '' for p in players}
            factions = dict(project)
            ratio = dict(monthpay)  #The values are the same
            break
    except ValueError:
        print("Invalid number. You know what a number is, right?")

for key in factions:
    while True:
        choice = input(
            "\nPlayer " + key.upper() +
            ": Select how you are going to start your railway: (Government/Private) >"
        )
        if choice not in ['g', 'p']:
            print("try again")
        else:
            factions[key] = choice
            break

week = 0

for key in factions:
    setup(factions[key], key)

for key in project:
    while True:
        print("Player " + key.upper() + ": ")
        print("1. Select starting point")
        print("2. Random city")
        select = int(input("> "))
        if select not in [1, 2]:
            print("Ummm... Nope.")
        else:
            if select == 1:
                build(key, 1)
                break
            else:
                randomcity(key)
                break

for key in wages:
    pay = [0, 0, 0, 0]
    while True:
        message("moneystat", 0, key)
        print("\nAdjust wages between ethnic groups")
        print("1. White")
        print("2. Immigrants and Aboriginals")
        print("3. Black")
        print("4. All")
        print("\nn: Next Step")
        groups = input("> ").lower()
        if groups not in ['1', '2', '3', '4', 'n']:
            print("\nreally?\n")

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

    while True:
        print("\n\n\n\nPlayer " + key.upper() + ": ")
        print("Hourly or Per KM?")
        print("1. Hourly")
        print("2. per KM")
        print("n: Next Player")
        per = input("> ").lower()
        if per not in ['1', '2', 'n']:
            print("\nSELECT THE NUMBER!!\n")
        elif per == 'n':
            if pay[-1] == 0:
                print("Hey! How are you going to pay them?")
            else:
                print("\n" * 20)
                break
        else:
            pay[-1] = per

for key in factions:
    build(key, 0)

week += 4
nextweek()

while True:
    for key in stations:
        while True:
            print("Week " + week + " : ")
            print("Player " + key + ": ")
            print('Options:')
            print('1. Build More Railways')
            print('2. Research')
            print('3. Pay loan')
            print('4. Stop game')
            print('\nN: Next Player')
            message("moneystat", 0, key)
            menu = input('> ').lower
            try:
                if menu is not [1, 2, 3, 4]:
                    print('\nInvalid option.')
                else:
                    if menu == 1:
                        build(key, 0)
                    if menu == 2:
                        print("This feature is still unavailable")
                        # research(key)
                    if menu == 3:
                        if factions[key] is not 'p':
                            print(
                                "Sorry, that option is not available for you.")
                        else:
                            loan(key)
                    if menu == 4:
                        for key in wages:
                            a = point(key)
                            print("Player " + key.upper() + str(a))
                        exit()
            except TypeError:
                if menu is not 'n':
                    print('\nInvalid option.')
                else:
                    break
        break
    week += 4
    nextweek()
