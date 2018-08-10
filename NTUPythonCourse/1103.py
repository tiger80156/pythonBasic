import ipdb; ipdb.set_trace()
money = input("請輸入金額 : ")

num = {"1": "壹","2": "貳", "3":"參", "4":"肆",
        "5": "伍", "6":"陸","7":"柒","8":"扒","9":"玖","0":"零"}

units = {2:"拾", 3:"佰", 4:"仟", 5:"萬"}

x = ""

unit = len(money)

if eval(money) >=1 & eval(money) <= 99999:
    for number in money:
        x += num[number]
        if unit > 1:
            x += units[unit]
            unit -= 1

    print(x+"元整")

else:
    print("out of range")