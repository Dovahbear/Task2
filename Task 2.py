'''
Hello hello, this is my multiline comment
'''

textArray = []


for index, row in df.head(10).iterrows():
    row = df.iloc[i]
    name = row[0]
    adress = row[1]
    ssn = row[2]
    cc = row[3]

    textArray.append(f'Hi, my name is {name}. I wonder if you deliver to {adress}. My credit card# is {cc} and my ssn is {ssn}')

# Display the resulting list of text values will me deleted
for text in textArray:
    print(text)