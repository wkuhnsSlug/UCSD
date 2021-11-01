import pandas as pd
import matplotlib.pyplot as plt
import math
import json
from pandas.io.json import json_normalize

print(pd.__version__)
path = "C:\\Users\\Will\\PycharmProjects\\pandaPractice\\venv\\data\\"

#with open(path+'world_bank_projects.json') as f:
 #   d = json.load(f)

wb_data = pd.read_json(path+'world_bank_projects.json')

data = [{'state': 'Florida',
         'shortname': 'FL',
         'info': {'governor': 'Rick Scott'},
         'counties': [{'name': 'Dade', 'population': 12345},
                      {'name': 'Broward', 'population': 40000},
                      {'name': 'Palm Beach', 'population': 60000}]},
        {'state': 'Ohio',
         'shortname': 'OH',
         'info': {'governor': 'John Kasich'},
         'counties': [{'name': 'Summit', 'population': 1234},
                      {'name': 'Cuyahoga', 'population': 1337}]}]
pd.json_normalize(data,'counties')



#1
wb_data.value_counts('countryname')[:10]
#2
dat = json.load((open(path+'world_bank_projects.json')))
project = pd.json_normalize(dat, 'mjtheme_namecode', ['project_name'])
code_grouped = project.groupby(['code']).agg('count').sort_values(by=['name'],ascending=False)[['name']].rename(columns={'name': '# of project themes'})
#3
#1:economic managment, 2:public sector governace, 3:Rule of law, 4:Financial and rpivate sector development, 5:trade and integration, 6:Social protection and risk management, 7:Social dev/gender/inclusion, 8:human development, 9:Urban Development, 10:Rural development, 11: Environment and natural resource management
values_map= {'1': 'economic managment',
         '2': 'public sector governace',
         '3': 'Rule of law',
         '4': 'Financial and pivate sector development',
         '5': 'trade and integration',
         '6': 'Social protection and risk management',
         '7': 'Social dev/gender/inclusion',
         '8': 'human development',
         '9': 'Urban Development',
         '10': 'Rural development',
         '11': 'Environment and natural resource management'}

project_no_na = project
project_no_na['name']=project_no_na['code']
project_no_na['name'] = project_no_na['name'].map(values_map)


