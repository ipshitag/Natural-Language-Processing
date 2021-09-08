import pandas as pd
import numpy as np

Naukri = pd.read_csv('/home/shaury/Downloads/Copy of naukri.csv',index_col='Unnamed: 0')
Times = pd.read_csv('/home/shaury/Downloads/Copy of times.csv',index_col='Unnamed: 0')

Times['skills'] = Times['skills'].map(lambda x:x.replace("\n",""))
Times['skills'] = Times['skills'].map(lambda x:x.replace("  ",""))
Times['skills'] = Times['skills'].map(lambda x:x.lstrip())
Times['skills'] = Times['skills'].map(lambda x:x.rstrip())
Times['skills'] = Times['skills'].map(lambda x: x.lower())
Naukri['skills'] = Naukri['skills'].map(lambda x:x.lower())
Naukri['skills'] = Naukri['skills'].map(lambda x:x.replace(" ",","))
Naukri['skills'] = Naukri['skills'].map(lambda x:x.lstrip())
Naukri['skills'] = Naukri['skills'].map(lambda x:x.rstrip())

monster = pd.read_csv("/home/shaury/Work/monster_jobs_scrapped.csv",index_col='Unnamed: 0').drop('Unnamed: 0.1',axis=1)
glassdoor = pd.read_csv("/home/shaury/Work/glassdoor_jobs_scrapped.csv",index_col='Unnamed: 0').drop('Unnamed: 0.1',axis=1)

jobs = pd.read_excel("/home/shaury/Work/files/Semantic Titles.xlsx",sheet_name='Sheet1')
jobs.fillna("None",inplace=True)



def funct(job,x):
    naukri = Naukri[Naukri['Searched Job Title']==job]
    times = Times[Times['Searched Job Title']==job]
    appdev = np.concatenate([np.array(naukri['skills']),np.array(times['skills'])])
    uniqapp = []
    for i in range(0,len(appdev)):
        for j in appdev[i].split(','):
            uniqapp.append(j)
            uniqapp = list(np.unique(uniqapp))
    for i in range(0,len(uniqapp)):
        uniqapp[i] = uniqapp[i].lstrip()
        uniqapp[i] = uniqapp[i].rstrip()
        uniqapp[i] = uniqapp[i].replace("-"," ")
    para = []
    for j in x.split():
        if(j in uniqapp):
            para.append(j) 
    if(len(np.unique(para)) ==0):
        return 'None'
    else:
        return ",".join(list(np.unique(para)))
        
        
def skill(indeed):
	for k in range(0,len(indeed)):
	    f = True
	    for i in range(0,len(jobs)):
		if(f==False):
		    break
		job = jobs['Job Title'][i]
		for j in jobs.columns:
		    if(jobs[j][i].lstrip().rstrip()==indeed['Job Title'][k].lstrip().rstrip()):
		        print(funct(job,indeed['Full Description'][k]))
		        indeed['Skills'][k] = funct(job,indeed['Full Description'][k])
		        f = False
		        break

skill(monster)
skill(glassdoor)


