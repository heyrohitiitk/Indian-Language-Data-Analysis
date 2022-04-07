import pandas as pd
import numpy as np

population=pd.read_excel("data/C14-Population-By-Age_Group.xls",skiprows=[0,1,2,3,4,5,6],header=None,usecols=[1,3,4,5],names=["state-code","area","age-group","total-pop"])

lang=pd.read_excel("data/C18-Population By Bilingualism, Trilingualism, Age And Sex.xlsx",skiprows=[0,1,2,3,4,5],usecols=[0,2,3,4,8],header=None,names=["state-code","area","Total/Urban/Rural","age-group","3rd-lang-persons"])

lang=lang[(lang["Total/Urban/Rural"]=="Total") & (lang["age-group"]!="Total")]

lang.drop(columns=["Total/Urban/Rural"],inplace=True)
lang=lang.reset_index(drop=True)
lang["area"]=lang["area"].str.title()

code_mapping=dict(lang[["state-code","area"]].drop_duplicates().values)

population["area"]=population["state-code"]
population["area"]=population["area"].replace(code_mapping)

population=population[population["age-group"]!="All ages"]

age_group={"0-4":"NA","5-9":"5-9","10-14":"10-14","15-19":"15-19","20-24":"20-24","25-29":"25-29","30-34":"30-49","35-39":"30-49","40-44":"30-49","45-49":"30-49","50-54":"50-69","55-59":"50-69","60-64":"50-69","65-69":"50-69","70-74":"70+","75-79":"70+","80+":"70+"}

population["age-group"].replace(age_group,inplace=True)

population=population[population["age-group"]!="NA"]

pop_age=population.groupby(by=["state-code","area","age-group"]).sum().reset_index()

tot_pop_age={}
for x in pop_age["state-code"].unique():
    tot_pop_age[x]=dict(pop_age[pop_age["state-code"]==x][["age-group","total-pop"]].values)
    
percent_groups=[]

for x,y,z in zip(lang["state-code"].values,lang["age-group"].values,lang["3rd-lang-persons"].values):
    percent_groups.append((z/tot_pop_age[x][y])*100)
    
lang["age-percent"]=percent_groups

age_india=lang[["state-code","age-group","age-percent"]]

max_ages=[]
max_percents=[]

for x in age_india["state-code"].unique():
    age_dict=dict(age_india[age_india["state-code"]==x][["age-group","age-percent"]].values)
    tdict=dict(sorted(age_dict.items(), key=lambda item: item[1]))
    max_age,max_percent=list(tdict.items())[-1]
    max_ages.append(max_age)
    max_percents.append(max_percent)
    
age_india2=pd.DataFrame(columns=["state/ut","age-group","percentage"])

age_india2["state/ut"]=age_india["state-code"]
age_india2.drop_duplicates(inplace=True)

age_india2["age-group"]=max_ages
age_india2["percentage"]=max_percents

age_india2.reset_index(drop=True,inplace=True)

age_india2.to_csv("Question-5/age-india.csv",index=False)



