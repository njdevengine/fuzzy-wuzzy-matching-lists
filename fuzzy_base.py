#conda install retrying
#pip install python-Levenshtein
#pip install python_Levenshtein-0.12.0-cp35-none-win_amd64.whl
#conda install -c conda-forge python-levenshtein
#pip install fuzzywuzzy

from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import pandas as pd

path = "source_database_file.csv"
df = pd.read_csv(path,encoding = "ISO-8859-1")

database = df.to_list()
sent = pd.read_csv(r'C:\Users\names.csv',encoding = "UTF-8")
sent = sent['header'].to_list()

sent_name = []
quickbase_match = []
match_score = []
s_length = len(sent)-1
q_length = len(quickbase)-1
for i in range(0,s_length):
    for n in range(0,q_length):
        if fuzz.token_sort_ratio(sent[i],quickbase[n]) >= 90:
            sent_name.append(sent[i])
            quickbase_match.append(quickbase[n])
            match_score.append(fuzz.token_sort_ratio(sent[i],quickbase[n]))
            print(str(sent[i])+" / "+str(quickbase[n])+" / "+(str(fuzz.token_sort_ratio(sent[i],quickbase[n]))))

fuzzy_dataframe = pd.DataFrame({'sent_name': sent_name, 'quickbase_match': quickbase_match, 'match_score': match_score})
fuzzy_dataframe.to_csv('fuzzy_matches.csv')
