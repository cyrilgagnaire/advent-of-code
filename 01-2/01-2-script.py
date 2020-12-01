import pandas as pd

input_df = pd.read_csv(
    r'C:\git\github\public\2020adventOfCode\01-2\01-2-input.txt', header=None)

for i in range(len(input_df)-2):
    for j in range(i+1, len(input_df)-1):
        for k in range(j+1, len(input_df)):
            result = input_df[0][i] + input_df[0][j] + input_df[0][k]
            if result == 2020:
                NumberA = input_df[0][i]
                NumberB = input_df[0][j]
                NumberC = input_df[0][k]
                print(str(input_df[0][i]) + " + " + str(input_df[0][j]) +
                      " + " + str(input_df[0][k]) + " = " + str(result))
                print(NumberA * NumberB * NumberC)
