import main
import sys


def tests():

    test1 = main.buildtrack("Toronto", "Brooklyn", 'A', 1)
    if 800 <= test1 <= 870:
        print("\n\nCHECK 1: DISTANCE ALGORITHM CHECK [✓]\n\n")
    else:
        print(test1)
        print("\n\nCHECK 1: DISTANCE ALGORITHM CHECK [FAILED]\n\n")
        return '- Distance Algorithm Failure'

    test2 = main.point('A')
    if test2 == 562.5:
        print("\n\nCHECK 2: POINT ALGORITHM CHECK [✓]\n\n")
    else:
        print("\n\nCHECK 2: POINT ALGORITHM CHECK [FAILED]\n\n")
        print("Have you changed the algorithm?")
        return '- Point Algorithm Failure'

    test3 = main.moneychange(-500, 'A')
    if main.money['A'] == 2499500:
        print("\n\nCHECK 3: MONEY EXCHANGE CHECK [✓]\n\n")
    else:
        print("\n\nCHECK 3: MONEY EXCHANGE CHECK [FAILED]\n\n")
        return '- Money Exchange Function Failure'

    for i in range(0, 5):
        main.randomcity('A')
    chklist = main.stations['A']
    for item in chklist:
        station_num = chklist.count(item)
        if station_num != 1:
            print(station_num)
            print(item)
            print(main.stations)
            print("\n\nCHECK 4: RANDOM CITY SELECTION CHECK [FAILED]\n\n")
            return '- Random City Generation Failure'
        else:
            pass

    print("\n\nCHECK 4: RANDOM CITY SELECTION CHECK [✓]\n\n")
    main.due = {'A': 1}
    main.project = {'A': 'testcityofdooomness'}

    try:
        test4 = main.nextweek()
        print("\n\nCHECK 5: NEXT WEEK FUNCTION [✓]")
        if main.due['A'] == 0:
            if main.stations['A'].count('testcityofdooomness') == 1:
                print("    CHECK 5.1: HOURLY PAY METHOD [✓]")
            else:
                print(main.stations['A'])
                print("    CHECK 5.1: HOURLY PAY METHOD [FAILED]")
                return '- Problem with appending station list'
        else:
            print(main.due['A'])
            print("    CHECK 5.1: HOURLY PAY METHOD [FAILED]")
            return '- Problem with due[player] or hourly pay wages'

        if main.monthpay['A'] == [0, 0, 0]:
            print("    CHECK 5.2: LOAN CALCULATION [✓]")
        else:
            print(main.monthpay)
            print("    CHECK 5.2: LOAN CALCULATION [FAILED]")
            return "- 'if monthpay' did not catch"

        if main.money['A'] == 2589500:
            print("    CHECK 5.3: STATION PROFIT SYSTEM [✓]")
        else:
            print(main.money['A'])
            print("    CHECK 5.3: STATION PROFIT SYSTEM [FAILED]")
            return "- Unexpected behavior from profit"

    except:
        print("\n\nCHECK 5: NEXT WEEK FUNCTION [FAILED]\n\n")
        return "- Problem with function / test script"

    main.weekinc = 20
    print(main.week)
    print(main.weekinc)

    main.week = main.week + main.weekinc
    main.nextweek()
    if main.week == 24:
        print("\n\nCHECK 6: WEEK INCREMENT [✓]\n\n")
    else:
        print(main.week)
        print("\n\nCHECK 6: WEEK INCREMENT [FAILED]\n\n")
        return '- Unexpected behavior from week increment'

    return 0


test = tests()
print(test)
if test == 0:
    sys.exit(0)
else:
    print("ERROR")
    sys.exit(1)
