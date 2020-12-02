import pandas as pd

input_df = pd.read_csv(
    r'C:\git\github\public\2020adventOfCode\Day 2\02-1\02-1-input.txt', delim_whitespace=True, header=None)

input_df.columns = ['criteria', 'letter', 'password']

input_df.columns = ['criteria', 'letter', 'password']

input_df['letter'] = input_df['letter'].str[:-1]

numberOfValidPassword = 0
for row in range(len(input_df)):
    string = input_df['password'][row]
    numberOfHit = 0
    for letter in string:
        if letter == input_df['letter'][row]:
            numberOfHit = numberOfHit + 1
    if numberOfHit >= int(input_df['Min'][row]) and numberOfHit <= int(input_df['Max'][row]):
        numberOfValidPassword = numberOfValidPassword + 1
print(numberOfValidPassword)
