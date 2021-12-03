import pandas as pd

input_df = pd.read_csv(
    r'C:\git\github\public\2020adventOfCode\Day 03\Part 1\input.txt', header=None)

column_offset = 3
row_offset = 1
map_width = len(input_df[0][0])

column = 0
row = 0

numberOfTrees = 0
for i in range(len(input_df.index)):
    if str(input_df[0][row])[column] == "#":
        numberOfTrees += 1

    row += row_offset
    if column + column_offset >= map_width:
        column = column + column_offset - map_width
    else:
        column += column_offset

print("Number of trees hit:")
print(numberOfTrees)
