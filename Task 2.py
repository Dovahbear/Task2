'''
For the purpose of Task 2, we were supposed to utilize laundromat to remove something, then it was subsequently altered to not include Laundromat
Due to that, the code that was underneath the >Removed laundromat because of run issues! was not handled.
Instead, I left the initial code in, and will explain it as we go down.
Now, there are parts of the code here that may individually be confusing or misleading, but that is due to it being from task 1, and thusly
not included here.

'''

textArray = []
#Creates the empty array within which we will store our strings.

for index, row in df.head(10).iterrows():
    #row=df.iloc[i] removed, as it was not needed, when row was declared and updated in the start of the loop.
    name = row[0]
    adress = row[1]
    ssn = row[2]
    cc = row[3]
    textArray.append(f'Hi, my name is {name}. I wonder if you deliver to {adress}.')
#Iterates over the first 10 entities in the dataframe from Task 1, and assigns every value to a variable

#Inserts the name and adress from the row into the array in a sentence, then starts all over again on the next entity.
#Do note that both ssn and cc are not included here, as one would expect, when the original intention was to use laundromat to remove them.

#The below line is commented out, as it was initially provided by the code
#textArray.append(f'Hi, my name is {name}. I wonder if you deliver to {adress}. My credit card# is {cc} and my ssn is {ssn}')
'''
The code snippet above is commented out, but I wanted to keep it to better explain the purpose of the parts of the task taht would've bene done
by Laundromat, but which was ommited.
The purpose was to have the whole statement be stored in the array, but to later run laundromat to replace parts of it with :^), 
those parts are initially not specified, but are clarified to first be name and addresses, and the later part of the code will alter the parts 
of the string that matches the given 'pattern' (lookup=True will go over and find exact matches) with either an additon of information, or removal.
'''