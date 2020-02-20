import random

def ClosestToZero(numTable):
    plus_proche = 0

    if len(numTable) > 0:
        plus_proche = numTable[0]
        for num in numTable:
            diff = 0-num
            abs_diff = abs(diff)
            if abs(plus_proche) > abs_diff:
                plus_proche = num
                # print("ABS = " + str(abs(num)))
                # print(str(num) + " (diff = " + str(diff) + ")")



    print("plus proche = " + str(plus_proche))


ts = [7,-10,13,8,4,-7,-12,-3,3,-9,6,-1,-6,7]
ts = [random.randint(-10,10) for i in range(8)]
print(ts)
ClosestToZero(ts)