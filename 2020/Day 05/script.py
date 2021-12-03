import pandas as pd
import numpy as np


def findSeatId(boardingPass):
    midPoint = 0
    top = 127
    bottom = 0
    for i in range(7):
        midPoint = (top - bottom + 1) / 2
        if boardingPass[i] == "F":
            top = top - midPoint
        else:
            bottom = bottom + midPoint
    row = bottom

    midPoint = 0
    bottom = 0
    top = 7
    for j in range(7, 10):
        midPoint = (top - bottom + 1) / 2
        if boardingPass[j] == "L":
            top = top - midPoint
        else:
            bottom = bottom + midPoint
    column = bottom

    seatId = (row * 8) + column
    return seatId


with open(r"C:\git\github\public\2020adventOfCode\Day 05\input.txt") as f:
    _result = 0
    for line in f:
        if findSeatId(line) > _result:
            _result = findSeatId(line)
print("Part 1: " + str(int(_result)))
f.close()

df = pd.DataFrame(index=np.arange(1024), columns=np.arange(1))
df.columns = ["Status"]
for i in range(1024):
    seat = 1
    df.at[i, "Status"] = "Not found"
    seat += 1

with open(r"C:\git\github\public\2020adventOfCode\Day 05\input.txt") as f:
    for line in f:
        seat = int(findSeatId(line))
        df.at[seat, "Status"] = "Found"
f.close()

for i in range(1, 1024):
    if df["Status"][i] == "Not found":
        if df["Status"][i - 1] == "Found":
            print("Part 2: " + str(i))
            break