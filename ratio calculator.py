print("ratio calculator: \n")
mater_1_name=""
mater_2_name=""
mater_1_originalamount=0
mater_2_originalamount=0
mater_1_newamount=0
mater_2_newamount=0

while True:
    mater_1_name=input("the name of the first material:")
    if not mater_1_name:
        print("please do not leave blank")
    else:
        break

while True:
    mater_1_originalamount=int(input("amount(must in intenger):"))
    if not mater_1_originalamount:
        print("please do not leave blank")
    else:
        break

while True:
    mater_2_name=input("the name of the second material:")
    if not mater_2_name:
        print("please do not leave blank")
    else:
        break

while True:
    mater_2_originalamount=int(input("amount(must in intenger):"))
    if not mater_2_originalamount:
        print("please do not leave blank")
    else:
        break

while True:
    baseon=input("base on which material(you change the amount of which one):")
    if not baseon:
        print("please do not leave blank")
    else:
        break


if baseon==mater_1_name:
    while True:
        print(mater_1_name)
        mater_1_newamount=int(input("amount(must in intenger):"))
        if not mater_1_newamount:
            print("please do not leave blank")
        else:
            break
    ratio=mater_1_originalamount/mater_1_newamount
    mater_2_newamount=mater_2_originalamount/ratio
    print("so you need",mater_2_newamount,"of",mater_2_name)


elif baseon==mater_2_name:
    while True:
        print(mater_2_name)
        mater_2_originalamount=int(input("amount(must in intenger):"))
        if not mater_2_originalamount:
            print("please do not leave blank")
        else:
            break
    ratio=mater_2_originalamount/mater_2_newamount
    mater_1_newamount=mater_1_originalamount/ratio
