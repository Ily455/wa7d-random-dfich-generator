import random
print("studio l7z9apointcom présente **9elet maydar**")
print("mmmmmm ana ghi talib o 7az9 achno ndir f lghda lyom ?")
list1 =["lbid",
        "btata",
        "roz",
        "ma9aronia",
        "lgr3a a wjh lgr3a",
        ]
list2 =["maticha",
        "bssla",
        "thon",
        "khizo"]
list3 =["w chi brad atay bien sur", ""]
list4 =["lefkaren","lmchoch","lklab","l3bid","l7raga(ly3awnhom)","l7bs","sra9 zit"]
random_one = random.choice(list1)
random_two = random.choice(list2)
random_three = random.choice(list3)
random_four = random.choice(list4)
if random_one == "lbid" :
    random_one_price=1
elif random_one=="btata":
    random_one_price=2
elif random_one=="roz":
    random_one_price=3
elif random_one=="ma9aronia":
    random_one_price=3.5
else :
    random_one_price=2
if random_two=="maticha":
    random_two_price=1.5
elif random_two=="bssla":
    random_two_price=1.5
elif random_two=="thon":
    random_two_price=6
else :
    random_two_price=2
if random_three==list3[0]:
    if random_one==list1[4]:
        print(f"lyom tdrb {random_one} m3a {random_two} {random_three} , makla dyal {random_four} safi, ha bchhal m9yom hadchi al3chir:")
        print(f"lgr3a: {int(random_one_price)}dhs , {random_two}:{int(random_two_price)}dhs ,hiya total : {int(random_one_price)}dhs + {int(random_two_price)}dhs={int(random_one_price + random_two_price)}dhs")
    else :
        print(f"lyom tdrb {random_one} m3a {random_two} {random_three} , makla dyal {random_four} safi, ha bchhal m9yom hadchi al3chir:")
        print(f"{random_one}: {int(random_one_price)}dhs , {random_two}:{int(random_two_price)}dhs w atay rak tma ghi j9ro 3la lcoloc wla chi l3ba, hiya total : {int(random_one_price)}dhs + {int(random_two_price)}dhs={int(random_one_price + random_two_price)}dhs")
else :
    if random_one==list1[4]:
        print(f"lyom tdrb {random_one} m3a {random_two} {random_three} , makla dyal {random_four} safi, ha bchhal m9yom hadchi al3chir:")
        print(f"lgr3a: {int(random_one_price)}dhs , {random_two}:{int(random_two_price)}dhs ,hiya total : {int(random_one_price)}dhs + {int(random_two_price)}dhs={int(random_one_price + random_two_price)}dhs")
    else :
        print(f"lyom tdrb {random_one} m3a {random_two} {random_three} , makla dyal {random_four} safi, ha bchhal m9yom hadchi al3chir:")
        print(f"{random_one}: {int(random_one_price)}dhs , {random_two}:{int(random_two_price)}dhs , hiya total : {int(random_one_price)}dhs + {int(random_two_price)}dhs={int(random_one_price + random_two_price)}dhs")
print("aya sa7a")
