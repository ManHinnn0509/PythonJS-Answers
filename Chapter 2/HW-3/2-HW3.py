import random

# Part 1
fruit = ["蘋果","葡萄","香蕉"]
fruit.append("草莓")

print("現在水果有", len(fruit), "個，分別拿起來吃：）")
for f in fruit:
    print("我手上拿的是", f, "，好吃！", sep = "")

print("")       # Sep

# Part 2
for _ in range (0, 3):
    r = random.random()
    status = ""

    if (r < 0.1):
        status = "中獎"
    else:
        status = "沒中獎"
    
    print("Number = ", r, ", ", status, sep = "")
