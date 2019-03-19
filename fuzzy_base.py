from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import pandas as pd

path = "source_database_file.csv"
df = pd.read_csv(path,encoding = "ISO-8859-1")

database = df.to_list()
sent = pd.read_csv(r'C:\Users\names.csv',encoding = "UTF-8")
sent = sent['header'].to_list()

matches = []
s_length = len(sent)-1
d_length = len(database)-1
for i in range(0,s_length):
    for n in range(0,q_length):
        if fuzz.token_sort_ratio(sent[i],database[n]) >= 90:
            matches.append(str(sent[i])+" / "+str(database[n])+" / "+(str(fuzz.token_sort_ratio(sent[i],database[n]))))
            print(str(sent[i])+" / "+str(database[n])+" / "+(str(fuzz.token_sort_ratio(sent[i],database[n]))))
                
fuzzymatches = pd.DataFrame(matches)
fuzzymatches.to_csv('fuzzy_matches.csv')
fuzzymatches
