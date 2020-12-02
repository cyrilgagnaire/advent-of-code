import pandas as pd

input_df = pd.read_csv(
    r'C:\git\github\public\2020adventOfCode\Day 2\02-1\02-1-input.txt', delim_whitespace=True, header=None)

input_df.columns = ['criteria', 'letter', 'password']
input_df[['Pos1', 'Pos2']] = input_df['criteria'].str.split('-', expand=True)
input_df['letter'] = input_df['letter'].str[:-1]

numberOfValidPassword = 0
for row in range(len(input_df)):
    string = input_df['password'][row]
    Position1 = int(input_df['Pos1'][row])-1
    Position2 = int(input_df['Pos2'][row])-1
    letter = input_df['letter'][row]
    if string[Position1] == letter:
        if string[Position2] != letter:
            numberOfValidPassword += 1
    elif string[Position2] != letter:
        numberOfValidPassword += 1
print(numberOfValidPassword)
