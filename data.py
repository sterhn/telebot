import requests
import re
from bs4 import BeautifulSoup as bp
import emoji
from random import randint
# requested libraries



# getting data
page = requests.get("https://paimon.moe/items")
# data but prettier
data = bp(page.content, 'html.parser')
# all talents and characters 
talents= data.find('table', class_='w-full block p-4 bg-item rounded-xl')
chars = data.find_all('td', class_ = 'border-gray-700 border-b py-2 svelte-xhx6q1')
# patterns for talents and names
pattern_t = '\<\w*\>(\w+\ *)\<\w*'
pattern_n = '([A-Z][a-z]*\s*\(*\w+\)*)'
# formating talents names and getting it into a list
r_talents = re.compile(pattern_t).findall(str(talents))
# days for dictionary
days = ['Monday/Thursday', 'Tuesday/Friday', 'Wednesday/Saturday']
# empty dict with future scheldule
scheldule = {}
# empty char list corresponding to talents
char_list = []
# talents ad days counter
t, day  = 0, 0
emoj_list = ['red_heart', 'yellow_heart','purple_heart', 'orange_heart', 'green_heart']
# lookinf for all lines of characters
for i in range(len(chars)):
    # formatted chars names in a list
    char = re.compile(pattern_n).findall(str(chars[i]))
    # joining it all in a pretty string
    char_str = ', '.join(char)
    # if line not empty
    if char !=[]:
        # formatting result string in 'talents:list of chars'
        emj = emoji.emojize(':' + emoj_list[randint(0,len(emoj_list)-1)] + ':')
        res = str(f'{emj} {r_talents[t]}: {char_str} \n')
        char_list.append(res)
        # moving to next talent
        t+=1
    # if line is empty moving to next day
    else:
        # adding previous char and talents 
        scheldule[days[day]]=char_list
        # clearing list
        char_list = []
        day+=1


# function for getting result
def get_day(day):
    return '\n'.join(list(scheldule.values())[day]) 

print(get_day(0))