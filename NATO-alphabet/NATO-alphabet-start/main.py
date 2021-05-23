# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

# Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(value)
    # Access key and value
    # pass


import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    # pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
df = pandas.DataFrame(data)
df_dict = {value.letter: value.code for (key, value) in df.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

words = input("Enter a word: ").upper()
p_list = [df_dict[letter] for letter in words]
print(p_list)

