import pandas as pd

input_df = pd.read_csv(
    r'C:\git\github\public\2020adventOfCode\Day 03\Part 2\input.txt', header=None)

data = {
    'Slope number': ['Slope 1', 'Slope 2', 'Slope 3', 'Slope 4', 'Slope 5'],
    'Right': [1, 3, 5, 7, 1],
    'Down': [1, 1, 1, 1, 2]
}

slope_df = pd.DataFrame(data, columns=['Slope number', 'Right', 'Down'])

map_width = len(input_df[0][0])
result = 1
for slope in range(len(slope_df.index)):
    omMap = True
    column = 0
    row = 0
    column_offset = slope_df['Right'][slope]
    row_offset = slope_df['Down'][slope]
    numberOfTrees = 0
    for i in range(len(input_df.index)):
        if str(input_df[0][row])[column] == "#":
            numberOfTrees += 1
        # Move right
        if column + column_offset >= map_width:
            column = column + column_offset - map_width
        else:
            column += column_offset
        # Move down
        if row + row_offset <= len(input_df.index):
            row += row_offset
        else:
            break

    print("Number of trees hit, using Slope " + str(slope+1) + ", Right " +
          str(column_offset) + " & Down " + str(row_offset) + " : " + str(numberOfTrees))
    result = result * numberOfTrees
# Final result
print("\nFinal Result :" + str(result))
