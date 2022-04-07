import pandas as pd
import numpy as np

lang=pd.read_excel("data/C19-Population By Bilingualism, Trilingualism, Education Level And Sex.xlsx",skiprows=[0,1,2,3,4,5],header=None,usecols=[0,2,3,4,8],names=["state-code","area","total/rural/urban","education-level","3rd-lang-persons"])

lang.drop([864,865,866],inplace=True)

to_drop=list(lang[(lang["total/rural/urban"]!="Total") | (lang["education-level"]=="Total")].index)

lang.drop(to_drop,inplace=True)

lang.drop(columns=["total/rural/urban"],inplace=True)

lang["area"]=lang["area"].str.title()

codes=lang["state-code"].astype('int64').unique()
area_name=lang["area"].unique()
code_area=dict(np.stack((codes,area_name),axis=1))

lang["state-code"]=lang["state-code"].astype('int64')
lang.reset_index(drop=True,inplace=True)

population=pd.read_excel("data/C08-Population By Literacy Rate.xlsx",skiprows=[0,1,2,3,4,5,6],header=None,usecols=[1,3,4,5,9,12,15,18,21,24,27,30,33,36,39,42],names=["state-code","area","total/rural/urban","age-group","illiterate","literate","literate-without-education-level","below-primary","primary","middle","matric/secondary","higher-secondary","non-technical-diploma","technical-diploma","graduate&above","unclassified"])

to_retain=list(population[(population["total/rural/urban"]=="Total") & (population["age-group"]=="All ages")].index)
population=population.loc[to_retain].reset_index(drop=True)

population["area"]=population["state-code"]
population["area"].replace(code_area,inplace=True)

population.drop(columns=["total/rural/urban","age-group","literate-without-education-level","unclassified"],inplace=True)

population["matric/secondary"]=population["matric/secondary"]+population["non-technical-diploma"]+population["technical-diploma"]+population["higher-secondary"]

population.drop(columns=["higher-secondary","non-technical-diploma","technical-diploma"],inplace=True)

population.columns=["state-code","area","Illiterate","Literate","Literate but below primary","Primary but below middle","Middle but below matric/secondary","Matric/Secondary but below graduate","Graduate and above"]

population.index=population["state-code"]

percent_groups=[]

for x,y,z in zip(lang["state-code"].values,lang["education-level"].values,lang["3rd-lang-persons"].values):
    percent_groups.append((z/population.loc[x,y])*100)
    
lang["education-percent"]=percent_groups

max_groups=[]
max_percents=[]

for x in lang["state-code"].unique():
    education_dict=dict(lang[lang["state-code"]==x][["education-level","education-percent"]].values)
    tdict=dict(sorted(education_dict.items(), key=lambda item: item[1]))
    max_group,max_percent=list(tdict.items())[-1]
    max_groups.append(max_group)
    max_percents.append(max_percent)
    
literacy_india=pd.DataFrame(columns=["state/ut","literacy-group","percentage"])

literacy_india["state/ut"]=lang["state-code"]
literacy_india.drop_duplicates(inplace=True)

literacy_india["literacy-group"]=max_groups
literacy_india["percentage"]=max_percents

literacy_india.reset_index(drop=True,inplace=True)

    
literacy_india.to_csv("Question-6/literacy-india.csv",index=False)

    
    
