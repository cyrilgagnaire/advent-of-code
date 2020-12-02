import pandas as pd

input_df = pd.read_csv(
    r'C:\git\github\public\2020adventOfCode\01-1\input.txt', header=None)

for i in range(len(input_df)-1):
    for j in range(i+1, len(input_df)):
        result = input_df[0][i] + input_df[0][j]
        if result == 2020:
            NumberA = input_df[0][i]
            NumberB = input_df[0][j]
            print(str(input_df[0][i]) + " + " +
                  str(input_df[0][j]) + " = " + str(result))
            print(NumberA * NumberB)
