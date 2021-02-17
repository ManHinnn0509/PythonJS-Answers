import datetime

# Easy way:

now = datetime.datetime.now()
timeNow = now.strftime("%H:%M:%S")
print("現在時間：" + timeNow)

# Or even shorter:
# print("現在時間：" + datetime.datetime.now().strftime("%H:%M:%S"))

# ----------------------------------------------------------------------------------
# Hard way:

# print("現在時間：" + str(datetime.datetime.now()).split(".")[0].split(" ")[1])

# Explain:
# datetime.datetime.now() returns "2021-02-13 02:53:38.855674"
# splitting it by character "." would end up with 2 parts:
# parts[0] = 2021-02-13 02:53:38
# parts[1] = 855674

# parts[0] is the one we want.

# and by splitting it by character " " (space bar) would end up with 2 parts again:
# parts[0] = 2021-02-13
# parts[1] = 02:53:38

# parts[1] is the time which is what we want.