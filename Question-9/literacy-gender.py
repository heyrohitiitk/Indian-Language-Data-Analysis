import pandas as pd
import numpy as np

lang=pd.read_excel("data/C19-Population By Bilingualism, Trilingualism, Education Level And Sex.xlsx",skiprows=[0,1,2,3,4,5],header=None,usecols=[0,2,3,4,6,7,9,10],names=["state-code","area","total/rural/urban","education-level","2nd-lang-males","2nd-lang-females","3rd-lang-males","3rd-lang-females"])

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

population=pd.read_excel("data/C08-Population By Literacy Rate.xlsx",skiprows=[0,1,2,3,4,5,6],header=None,usecols=[1,3,4,5,10,11,13,14,16,17,19,20,22,23,25,26,28,29,31,32,34,35,37,38,40,41,43,44])

population.columns=["state-code","area","total/rural/urban","age-group","illiterate-male","illiterate-female","literate-male","literate-female","literate-without-education-level-male","literate-without-education-level-female","below-primary-male","below-primary-female","primary-male","primary-female","middle-male","middle-female","matric/secondary-male","matric/secondary-female","higher-secondary-male","higher-secondary-female","non-technical-diploma-male","non-technical-diploma-female","technical-diploma-male","technical-diploma-female","graduate&above-male","graduate&above-female","unclassified-male","unclassified-female"]

to_retain=list(population[(population["total/rural/urban"]=="Total") & (population["age-group"]=="All ages")].index)
population=population.loc[to_retain].reset_index(drop=True)

population.drop(columns=["area","total/rural/urban","age-group"],inplace=True)

population["matric/secondary-male"]=population["matric/secondary-male"]+population["non-technical-diploma-male"]+population["technical-diploma-male"]+population["higher-secondary-male"]
population["matric/secondary-female"]=population["matric/secondary-female"]+population["non-technical-diploma-female"]+population["technical-diploma-female"]+population["higher-secondary-female"]

population.drop(columns=['literate-without-education-level-male',
       'literate-without-education-level-female','unclassified-male',
       'unclassified-female',"higher-secondary-male","higher-secondary-female","non-technical-diploma-male",
                         "non-technical-diploma-female","technical-diploma-male","technical-diploma-female"],inplace=True)

population.columns=["state-code","Illiterate-Male","Illiterate-Female","Literate-Male","Literate-Female","Literate but below primary-Male","Literate but below primary-Female","Primary but below middle-Male","Primary but below middle-Female","Middle but below matric/secondary-Male","Middle but below matric/secondary-Female","Matric/Secondary but below graduate-Male","Matric/Secondary but below graduate-Female","Graduate and above-Male","Graduate and above-Female"]

population.index=population["state-code"]

tot_education={}

for x in population["state-code"]:
    a=np.array(population.columns[1:]).reshape((-1,1))
    b=population.loc[x].values[1:].reshape((-1,1))
    z=np.concatenate((a,b),axis=1)
    tot_education[x]=dict( z )

first_males=[]
first_females=[]

for code,education,male,female in zip(lang["state-code"].values,lang["education-level"].values,lang["2nd-lang-males"].values,lang["2nd-lang-females"]):
    val1=tot_education[code][f"{education}-Male"]-lang[(lang["state-code"]==code) & (lang["education-level"]==education)]["2nd-lang-males"].values[0]
    first_males.append(val1)
    val2=tot_education[code][f"{education}-Female"]-lang[(lang["state-code"]==code) & (lang["education-level"]==education)]["2nd-lang-females"].values[0]
    first_females.append(val2)
    
    
lang["1st-lang-males"]=first_males
lang["1st-lang-females"]=first_females

lang["2nd-lang-males"]=lang["2nd-lang-males"]-lang["3rd-lang-males"]
lang["2nd-lang-females"]=lang["2nd-lang-females"]-lang["3rd-lang-females"]

percent_groups_male_3rd=[]
percent_groups_female_3rd=[]

percent_groups_male_2nd=[]
percent_groups_female_2nd=[]

percent_groups_male_1st=[]
percent_groups_female_1st=[]

for code,education,males,females in zip(lang["state-code"].values,lang["education-level"].values,lang["3rd-lang-males"].values,lang["3rd-lang-females"].values):
    percent_groups_male_3rd.append((males/tot_education[code][f"{education}-Male"]))
    percent_groups_female_3rd.append((females/tot_education[code][f"{education}-Female"]))
    
for code,education,males,females in zip(lang["state-code"].values,lang["education-level"].values,lang["2nd-lang-males"].values,lang["2nd-lang-females"].values):
    percent_groups_male_2nd.append((males/tot_education[code][f"{education}-Male"]))
    percent_groups_female_2nd.append((females/tot_education[code][f"{education}-Female"]))
    
for code,education,males,females in zip(lang["state-code"].values,lang["education-level"].values,lang["1st-lang-males"].values,lang["1st-lang-females"].values):
    percent_groups_male_1st.append((males/tot_education[code][f"{education}-Male"]))
    percent_groups_female_1st.append((females/tot_education[code][f"{education}-Female"]))

lang["education-ratio-males-3rd"]=percent_groups_male_3rd
lang["education-ratio-females-3rd"]=percent_groups_female_3rd

lang["education-ratio-males-2nd"]=percent_groups_male_2nd
lang["education-ratio-females-2nd"]=percent_groups_female_2nd

lang["education-ratio-males-1st"]=percent_groups_male_1st
lang["education-ratio-females-1st"]=percent_groups_female_1st

max_groups_male_3rd=[]
max_ratios_male_3rd=[]

max_groups_female_3rd=[]
max_ratios_female_3rd=[]

for x in lang["state-code"].unique():
    education_dict_male=dict(lang[lang["state-code"]==x][["education-level","education-ratio-males-3rd"]].values)
    tdict_male=dict(sorted(education_dict_male.items(), key=lambda item: item[1]))
    max_group,max_ratio=list(tdict_male.items())[-1]
    max_groups_male_3rd.append(max_group)
    max_ratios_male_3rd.append(max_ratio)
    
    education_dict_female=dict(lang[lang["state-code"]==x][["education-level","education-ratio-females-3rd"]].values)
    tdict_female=dict(sorted(education_dict_female.items(), key=lambda item: item[1]))
    max_group,max_ratio=list(tdict_female.items())[-1]
    max_groups_female_3rd.append(max_group)
    max_ratios_female_3rd.append(max_ratio)

literacy_gender_a=pd.DataFrame(columns=["state/ut","literacy-group-males","ratio-males","literacy-group-females","ratio-females"])

literacy_gender_a["state/ut"]=lang["state-code"]
literacy_gender_a.drop_duplicates(inplace=True)

literacy_gender_a["literacy-group-males"]=max_groups_male_3rd
literacy_gender_a["ratio-males"]=max_ratios_male_3rd

literacy_gender_a["literacy-group-females"]=max_groups_female_3rd
literacy_gender_a["ratio-females"]=max_ratios_female_3rd

literacy_gender_a.reset_index(drop=True,inplace=True)

literacy_gender_a.to_csv("Question-9/literacy-gender-a.csv",index=False)

max_groups_male_2nd=[]
max_ratios_male_2nd=[]

max_groups_female_2nd=[]
max_ratios_female_2nd=[]

for x in lang["state-code"].unique():
    education_dict_male=dict(lang[lang["state-code"]==x][["education-level","education-ratio-males-2nd"]].values)
    tdict_male=dict(sorted(education_dict_male.items(), key=lambda item: item[1]))
    max_group,max_ratio=list(tdict_male.items())[-1]
    max_groups_male_2nd.append(max_group)
    max_ratios_male_2nd.append(max_ratio)
    
    education_dict_female=dict(lang[lang["state-code"]==x][["education-level","education-ratio-females-2nd"]].values)
    tdict_female=dict(sorted(education_dict_female.items(), key=lambda item: item[1]))
    max_group,max_ratio=list(tdict_female.items())[-1]
    max_groups_female_2nd.append(max_group)
    max_ratios_female_2nd.append(max_ratio)

literacy_gender_b=pd.DataFrame(columns=["state/ut","literacy-group-males","ratio-males","literacy-group-females","ratio-females"])

literacy_gender_b["state/ut"]=lang["state-code"]
literacy_gender_b.drop_duplicates(inplace=True)

literacy_gender_b["literacy-group-males"]=max_groups_male_2nd
literacy_gender_b["ratio-males"]=max_ratios_male_2nd

literacy_gender_b["literacy-group-females"]=max_groups_female_2nd
literacy_gender_b["ratio-females"]=max_ratios_female_2nd

literacy_gender_b.reset_index(drop=True,inplace=True)

literacy_gender_b.to_csv("Question-9/literacy-gender-b.csv",index=False)

max_groups_male_1st=[]
max_ratios_male_1st=[]

max_groups_female_1st=[]
max_ratios_female_1st=[]

for x in lang["state-code"].unique():
    education_dict_male=dict(lang[lang["state-code"]==x][["education-level","education-ratio-males-1st"]].values)
    tdict_male=dict(sorted(education_dict_male.items(), key=lambda item: item[1]))
    max_group,max_ratio=list(tdict_male.items())[-1]
    max_groups_male_1st.append(max_group)
    max_ratios_male_1st.append(max_ratio)
    
    education_dict_female=dict(lang[lang["state-code"]==x][["education-level","education-ratio-females-1st"]].values)
    tdict_female=dict(sorted(education_dict_female.items(), key=lambda item: item[1]))
    max_group,max_ratio=list(tdict_female.items())[-1]
    max_groups_female_1st.append(max_group)
    max_ratios_female_1st.append(max_ratio)

literacy_gender_c=pd.DataFrame(columns=["state/ut","literacy-group-males","ratio-males","literacy-group-females","ratio-females"])

literacy_gender_c["state/ut"]=lang["state-code"]
literacy_gender_c.drop_duplicates(inplace=True)

literacy_gender_c["literacy-group-males"]=max_groups_male_1st
literacy_gender_c["ratio-males"]=max_ratios_male_1st

literacy_gender_c["literacy-group-females"]=max_groups_female_1st
literacy_gender_c["ratio-females"]=max_ratios_female_1st

literacy_gender_c.reset_index(drop=True,inplace=True)

literacy_gender_c.to_csv("Question-9/literacy-gender-c.csv",index=False)
