student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

for (key, value) in student_dict.items():
    print(key)

#We can iterate through dataframes the same way we iterate through dictionaries

import pandas as pd 

student_data_frame = pd.DataFrame(student_dict)

#Loop through rows

for (index, row) in student_data_frame.iterrows():
    print(row.score)

#Each row is a pandas series object