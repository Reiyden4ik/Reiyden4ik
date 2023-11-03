import re

string = str(input())
pattern = r'\d{2}'
if re.fullmatch(pattern, string):
    print('yes')