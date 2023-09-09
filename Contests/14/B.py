q = int(input())

debts = {}
credits = {}

for _ in range(q):
    command = input().split()

    if command[0] == '1':
        s1, s2, x = command[1], command[2], float(command[3])

        if s1 in debts:
            debts[s1][s2] = debts[s1].get(s2, 0) + x
        else:
            debts[s1] = {s2: x}

        if s2 in credits:
            credits[s2][s1] = credits[s2].get(s1, 0) + x
        else:
            credits[s2] = {s1: x}

    elif command[0] == '2':
        max_gain_person = ''
        max_gain = 0

        for person in credits:
            capital_gain = sum(credits[person].values()) - sum(debts.get(person, {}).values())

            if capital_gain > max_gain or (capital_gain == max_gain and person < max_gain_person):
                max_gain_person = person
                max_gain = capital_gain

        print(max_gain_person if max_gain > 0 else -1)

    elif command[0] == '3':
        min_gain_person = ''
        min_gain = 0

        for person in debts:
            capital_gain = sum(credits.get(person, {}).values()) - sum(debts[person].values())

            if capital_gain < min_gain or (capital_gain == min_gain and person < min_gain_person):
                min_gain_person = person
                min_gain = capital_gain

        print(min_gain_person if min_gain < 0 else -1)

    elif command[0] == '4':
        s = command[1]

        if s in credits:
            count = 0
            for person in credits[s]:
                if person in credits:
                    amount = credits[s][person] - credits[person].get(s, 0)
                    if amount > 0:
                        count += 1
            # print(len(credits[s]))
            print(count)
        else:
            print(0)

    elif command[0] == '5':
        s = command[1]

        if s in debts:
            count = 0
            for person in debts[s]:
                if person in debts:
                    amount = debts[s][person] - debts[person].get(s, 0)
                    if amount > 0:
                        count += 1
            print(count)
            # print(len(debts[s]))
        else:
            print(0)

    elif command[0] == '6':
        s1, s2 = command[1], command[2]

        amount = debts.get(s2, {}).get(s1, 0) - debts.get(s1, {}).get(s2, 0)
        if amount == -0: amount = 0
        print(f'{amount:.2f}')
