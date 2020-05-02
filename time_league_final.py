def write_new_game():
    f=open("summary.txt","a")
    while True:
        time=input("time(for example: 11:32):")
        w_l=input("win or lose(for example: w):")
        data=time.split(":")
        f.write("m:"+data[0]+",s:"+data[1]+","+w_l+"\n")

        more = input("Do you want to input more?")
        if more == "yes" or more == "Yes" or more == "y" or more == "Y":
            continue
        elif more=="no" or more=="n" or more=="No":
            break
    f.close()
def check_games():
    f = open("summary.txt", "r")
    tmp=0
    temp_time=0
    while True:
        win=True
        minutes, seconds = 0,0
        data=f.readline()
        if not data:
            average_time=temp_time/tmp
            f.close()
            # print("average time playing: ",average_time)
            break
        tmp += 1
        new=data.split(",")
        for i in new:
            if i[0]=="m":
                minutes=int(i[2:])
            elif i[0]=="s":
                seconds=int(i[2:])
            elif i[0]=="w":
                win=True
            elif i[0]=="l":
                win=False
        temp_time+=minutes*60+seconds
        if win:
            exp=(minutes*60+seconds)*0.11+6.6
        else:
            exp=(minutes*60+seconds)*0.09+5.4
        # print("experience gained: ",exp)
    return average_time

def exp_need_for_level(level,level_reach):
    # 25-29-20
    exp=0
    exp_by_level_after_50 = [2592, 2688, 2688, 2688, 2688, 2880, 2880, 2880, 3072, 3072, 3072, 3264, 3264, 3264, 3360,
                             3360, 3360, 3456, 3456, 3456, 3456, 3552, 3552, 3648, 3648]
    exp_by_level_0 = [144, 144, 192, 240, 336, 432, 528, 624, 720, 816, 912, 984, 1056, 1128, 1344, 1440, 1536, 1680,
                      1824, 1968, 2112, 2208, 2448, 2304, 2496, 2496, 2592, 2688, 2688]
    exp_by_level_after_30 = [2688, 2688, 2688, 2784, 2784, 2784, 2880, 2880, 2880, 3072, 3072, 3168, 3168, 3264, 3264,
                             3360, 3360, 3456, 3456, 3456]
    for i in range(level,level_reach):
        if i<30:
            exp+=exp_by_level_0[i-1]
        elif i<50:
            exp+=exp_by_level_after_30[i-31]
        elif i>=50:
            exp+=exp_by_level_after_50[i%25]
    return exp
def check_levels(time):

    bonus=400
    winrate=int(input("Your winrate:"))
    if winrate < 0 or winrate>100:
        raise ValueError
    if winrate==0:
        bonus=0
    games=int(input("How many games per day you play:"))
    level=int(input("Your current level:"))
    lever_reach=int(input("Level want to reach: "))
    exp_level_need=exp_need_for_level(level,lever_reach)
    print("Exprience need:",exp_level_need)
    exp=time*(0.09+(0.02*winrate/100))+5.4+(1.2*winrate/100)
    day=games*exp+bonus
    days_left=exp_level_need/day
    if days_left>365:
        years=days_left/365
        print("years left:",years,"\ndays left: ",days_left)
    else:
        print("days left: ",days_left)
    return days_left

def main():
    # write_new_game()
    check_levels(check_games())
    #check_games()
    return


if __name__ == '__main__':
    main()