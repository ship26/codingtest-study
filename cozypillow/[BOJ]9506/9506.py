run = 1

while run == 1:
    number = int(input())
    if number == -1:
        run = 0

    else:
        yaksoos = []
        yaksoos_str = []
        yaksoo = 1
        while yaksoo < number:
            if number % yaksoo == 0:
                yaksoos.append(yaksoo)
                yaksoos_str.append(str(yaksoo))
            yaksoo += 1

        if sum(yaksoos) == number:
            result = " + ".join(yaksoos_str)
            print(f"{number} = {result}")
        else:
            print(f'{number} is NOT perfect.')