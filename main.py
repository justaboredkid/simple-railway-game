from __future__ import print_function
from math import sin, cos, sqrt, atan2, radians
from fractions import Fraction
from datetime import datetime
from blessings import Terminal
from sys import exit
import json
import random
import secrets

term = Terminal()

with open("cities.json", "r") as cjson:
    cities = json.load(cjson)

with open("regions.json", "r") as rjson:
    regions = json.load(rjson)


def buildtrack(
        station, destination, player, devtag
):  # Distance and cost calculation. Set devtag to 1 for distance only.
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
                    return 'toolong'
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
                        return 'cancelled'

                    cost = []
                    workers[player] = people
                    people = people + (Fraction(-3, 10) * int(rnd[player]))
                    pay = list(wages.get(player)[:-1])
                    for item in pay:
                        if item == 0:
                            ethicality[player] = ethicality[player] - 33
                        else:
                            if pay.count(item) != 3:
                                ethicality[player] = ethicality[player] - 10
                            calc = int(length * (people * item))
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
                                    project[player] = str(destination)
                                    return
                                else:
                                    print("Building cancelled")
                                    return 'cancelled'
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
                                    project[player] = str(destination)
                                    return
                                else:
                                    break
    else:
        print("no building 4 u")
        return 'project'


def build(player, choicetag):  # Build menu
    while True:
        print("\nPlayer " + player.upper() + ": ")
        distance = []
        if choicetag == 1:
            starting = ''
        else:
            if len(list(stations[player])) == 1:
                starting = stations.get(player)[0]
                print(starting)
            else:
                print(stations.get(player))
                while True:
                    starting = input("Where to start? > ").title()
                    if starting not in list(cities.keys()):
                        print("Err... try again.")
                    elif starting in list(project.values()):
                        print("Someone else is taking that")
                    elif starting not in list(stations.get(player)):
                        print("You don't own that station")
                    else:
                        break
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
                    elif l == 'project':
                        print(
                            "You are still building tracks, you cannot build another station."
                        )
                        return
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
                    stations[player].append(pick)
                    return

            else:
                print(stations[player])
                build = input("Where to go? (enter 'exit' to cancel)> ").title()
                if build == 'Exit':
                    if len(list(stations[player])) == 1:
                        print("Are you TRYING to break the game?")
                    else:
                        print(len(list(stations[player])))
                        print("Exiting...")
                        return
                elif build not in list(cities.keys()):
                    print("Umm... Wrong city.")
                elif build in list(project.values()):
                    print("Someone else is taking that")
                elif build in [
                        elem for test in list(stations.values())
                        for elem in test
                ]:
                    print("Someone already got that station")
                else:
                    track = buildtrack(starting, build, player, 0)
                    if track is not None:
                        pass
                    else:
                        return


def point(player):  # Calculates points
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
        print("player " + player.upper() + " has $" + str(
            money[player]))  # Game messages


def moneychange(amount, player):  # Deals with money
    amount = int(amount)
    money[player] = int(money[player]) + amount
    if amount <= 0:
        message("spentmoney", amount, player)
    if amount >= 0:
        message("getmoney", amount, player)


def setup(faction, player):  # Game starting setup
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
            time[key] = random.randint(25, 50)
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
                    interest[investor] / 10, time[investor], inipay[investor]
                ]
                break

    if faction == "c":  #Chain funding (Chain of train stations (NO RAILRD))
        print("this feature is not complete. you are not supposed to be here")


def nextweek():  # More like next month. Need to change that.
    for key in wages:
        if project[key] != '':
            if due[key] <= weekinc:
                print("Station " + str(project[key]) + " has completed!")
                stations[key].append(project[key])
                project[key] = ''
                due[key] = 0
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
                    due[key] -= weekinc
                else:
                    print("Player " + key.upper() + " has " + str(due[key]) +
                          " weeks left on " + project[key] + " station.")
                    due[key] -= weekinc
        else:
            pass

    for key in monthpay:
        if monthpay.get(key)[-1] == 0:
            print("Player " + key.upper() + " does not need to repay anything")
        else:
            #work here
            if week < monthpay.get(key)[1]:
                print("It is not the time for Player " + key.upper() +
                      " to PAY")
            else:
                numweek = week / weekinc
                monthpay.get(key)[-1] = monthpay.get(key)[-1] + (
                    monthpay.get(key)[-1] * monthpay.get(key)[0] * int(numweek))
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
        for item in list(stations[key]):
            moneychange(10000, key)
            print("from " + item + " station")


def randomcity(player):  # Select random city
    while True:
        rcity = secrets.choice(list(cities.keys()))
        if rcity in [elem for test in list(stations.values()) for elem in test]:
            pass
        elif project[player] is '':
            stations[player].append(rcity)
            print("Your starting city is " + rcity)
            return
        else:
            if regions[cities[rcity][0]][-1] not in project[player]:
                pass
            else:
                stations[player].append(rcity)
                project[player] = []
                print("Your starting city is " + rcity)
                return


def loan(player):  # Pays off loan
    print("You need to pay " + str(list(monthpay.get(player))[-1]) + " dollars")
    if monthpay.get(player)[-1] >= money[player]:
        print("Difference: " +
              str(list(monthpay.get(player))[-1] - money[player]))
        print("You don't have enough money for paying back.")
        return
    else:
        while True:
            repay = input("Confirm? (y/n) > ").lower()
            if repay not in ['y', 'n']:
                print("The investor does not like jokes.")
            else:
                moneychange(-(int(monthpay.get(player)[-1])), player)
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


def research(player):
    #Needs development, skill tree?
    pass


if __name__ == "__main__":
    try:
        with term.fullscreen():
            while True:
                print(
                    term.move(0, 0) +
                    "Disclaimer: This game is based on 1860s money, not " +
                    str(datetime.now().year) + ". Inflation applies.")
                print(
                    "Hello There! Please select the amount of players. (2-26)")
                try:
                    amount = int(input("> "))
                    if amount == 1:
                        print(
                            term.move_down +
                            "loooonnnnely... I am mr loooonnnnely... I have nobody..... fooooor my owwwnnn!!!"
                        )
                        input("[Press enter to continue]")
                        print(term.clear())
                    elif amount < 0:
                        print(term.move_down +
                              "Sorry, no downers allowed here.")
                        input("[Press enter to continue]")
                        print(term.clear())
                    elif amount == 0:
                        print(term.move_down +
                              "Really, then why do you bother to play.")
                        input("[Press enter to continue]")
                        print(term.clear())
                    elif amount > 26:
                        print(term.move_down + "Too crowded.")
                        input("[Press enter to continue]")
                        print(term.clear())
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
                        stations = {p: [] for p in players}
                        project = {p: '' for p in players}
                        factions = dict(project)
                        ratio = dict(monthpay)  #The values are the same
                        print(term.clear())
                        break
                except ValueError:
                    print(term.move_down +
                          "Invalid number. You know what a number is, right?")
                    input("[Press enter to continue]")
                    print(term.clear())

            while True:
                try:
                    weekinc = int(input("How many weeks per move? > "))
                    if weekinc == 0:
                        print("You cannot stop TIME.")
                    elif weekinc < 0:
                        print("You cannot reverse TIME")
                    else:
                        print(str(weekinc) + " weeks per move")
                        break
                except ValueError:
                    print(
                        "What the heck? This is not a number. Do you think this program is dumb?"
                    )

            for key in factions:
                while True:
                    choice = input(
                        "\nPlayer " + key.upper() +
                        ": Select how you are going to start your railway: (Government/Private) >"
                    ).lower()
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
                    try:
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
                    except ValueError:
                        print("Not an option.")

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
                                    pay = [
                                        int(amount),
                                        int(amount),
                                        int(amount), 0
                                    ]
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
                        if pay[-1] not in ['1', '2', 'n']:
                            print("Hey! How are you going to pay them?")
                        else:
                            print("\n" * 20)
                            break
                    else:
                        pay[-1] = per

            for key in factions:
                build(key, 0)

            week = week + weekinc
            nextweek()

            while True:
                for item in list(factions.keys()):
                    while True:
                        print("Week " + str(week) + " : ")
                        print("Player " + item.upper() + ": ")
                        print('Options:')
                        print('1. Build More Railways')
                        print('2. Research')
                        print('3. Pay loan')
                        print('4. Stop game')
                        print('\nN: Next Player')
                        message("moneystat", 0, item)
                        menu = input('> ').lower()

                        if menu not in ['1', '2', '3', '4', 'n']:
                            print('\nInvalid option.')
                        else:
                            if menu == '1':
                                build(item, 0)
                            if menu == '2':
                                print("This feature is still unavailable")
                                # research(item)
                            if menu == '3':
                                if factions[item] != 'p':
                                    print(
                                        "Sorry, that option is not available for you."
                                    )
                                else:
                                    loan(item)
                            if menu == '4':
                                for key in wages:
                                    a = point(key)
                                    print("Player " + key.upper() + " has " +
                                          str(a) + " points")
                                exit()
                            if menu == 'n':
                                break
                week = week + weekinc
                nextweek()
    except KeyboardInterrupt:
        print("\n\nQuitting forcefully...")
        exit()

else:
    week = 4
    weekinc = 4
    money = {'A': 2500000}
    workers = {'A': 0}
    due = {'A': 0}
    rnd = {'A': 0}
    ethicality = {'A': 75}
    wages = {'A': [0, 0, 0, 0]}
    monthpay = {'A': [0, 0, 0]}
    stations = {'A': ["Toronto", "Brooklyn", "Concord"]}
    project = {'A': ''}
    factions = {'A': ''}
    ratio = {'A': [0, 0, 0]}
