
data_case = input("Data case = ")

##"ThiS is String with Upper and lower case Letters"
letter_counts ={}
for letter in (data_case):
    letter_counts[letter] = letter_counts.get(letter, 0) +1
    
    print(letter_counts, "\n", end =".")
    

