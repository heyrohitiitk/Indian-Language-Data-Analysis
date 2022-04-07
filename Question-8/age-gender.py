import pandas as pd

population=pd.read_excel("data/C14-Population-By-Age_Group.xls",skiprows=[0,1,2,3,4,5,6],header=None,usecols=[1,3,4,6,7],names=["state-code","area","age-group","male-pop","female-pop"])

lang=pd.read_excel("data/C18-Population By Bilingualism, Trilingualism, Age And Sex.xlsx",skiprows=[0,1,2,3,4,5],header=None,usecols=[0,2,3,4,6,7,9,10],
names=["state-code","area","Total/Urban/Rural","age-group","2nd-lang-males","2nd-lang-females","3rd-lang-males","3rd-lang-females"])

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

tot_male_age={}
tot_female_age={}

for x in pop_age["state-code"].unique():
    tot_male_age[x]=dict(pop_age[pop_age["state-code"]==x][["age-group","male-pop"]].values)

for x in pop_age["state-code"].unique():
    tot_female_age[x]=dict(pop_age[pop_age["state-code"]==x][["age-group","female-pop"]].values)

first_lang_males=[]
first_lang_females=[]

for code,age,male,female in zip(lang["state-code"].values,lang["age-group"].values,lang["2nd-lang-males"].values,lang["2nd-lang-females"]):
    first_lang_males.append(tot_male_age[code][age]-male)
    first_lang_females.append(tot_female_age[code][age]-female)

lang["1st-lang-males"]=first_lang_males
lang["1st-lang-females"]=first_lang_females

lang["2nd-lang-males"]=lang["2nd-lang-males"]-lang["3rd-lang-males"]
lang["2nd-lang-females"]=lang["2nd-lang-females"]-lang["3rd-lang-females"]

ratio_groups_male_1st=[]
ratio_groups_male_2nd=[]
ratio_groups_male_3rd=[]
ratio_groups_female_1st=[]
ratio_groups_female_2nd=[]
ratio_groups_female_3rd=[]

for code,age,male in zip(lang["state-code"].values,lang["age-group"].values,lang["1st-lang-males"].values):
    ratio_groups_male_1st.append((male/tot_male_age[code][age]))

for code,age,male in zip(lang["state-code"].values,lang["age-group"].values,lang["2nd-lang-males"].values):
    ratio_groups_male_2nd.append((male/tot_male_age[code][age]))

for code,age,male in zip(lang["state-code"].values,lang["age-group"].values,lang["3rd-lang-males"].values):
    ratio_groups_male_3rd.append((male/tot_male_age[code][age]))

for code,age,female in zip(lang["state-code"].values,lang["age-group"].values,lang["1st-lang-females"].values):
    ratio_groups_female_1st.append((female/tot_female_age[code][age]))

for code,age,female in zip(lang["state-code"].values,lang["age-group"].values,lang["2nd-lang-females"].values):
    ratio_groups_female_2nd.append((female/tot_female_age[code][age]))

for code,age,female in zip(lang["state-code"].values,lang["age-group"].values,lang["3rd-lang-females"].values):
    ratio_groups_female_3rd.append((female/tot_female_age[code][age]))    

lang["1st-lang-male-ratio"]=ratio_groups_male_1st
lang["2nd-lang-male-ratio"]=ratio_groups_male_2nd
lang["3rd-lang-male-ratio"]=ratio_groups_male_3rd

lang["1st-lang-female-ratio"]=ratio_groups_female_1st
lang["2nd-lang-female-ratio"]=ratio_groups_female_2nd
lang["3rd-lang-female-ratio"]=ratio_groups_female_3rd


age_india=lang[["state-code","age-group","1st-lang-male-ratio","2nd-lang-male-ratio","3rd-lang-male-ratio","1st-lang-female-ratio","2nd-lang-female-ratio","3rd-lang-female-ratio"]]

max_male_3rd_age=[]
max_male_3rd_ratios=[]

max_female_3rd_age=[]
max_female_3rd_ratios=[]

for x in age_india["state-code"].unique():
    age_dict=dict(age_india[age_india["state-code"]==x][["age-group","3rd-lang-male-ratio"]].values)
    tdict=dict(sorted(age_dict.items(), key=lambda item: item[1]))
    max_age,max_ratio=list(tdict.items())[-1]
    max_male_3rd_age.append(max_age)
    max_male_3rd_ratios.append(max_ratio)

for x in age_india["state-code"].unique():
    age_dict=dict(age_india[age_india["state-code"]==x][["age-group","3rd-lang-female-ratio"]].values)
    tdict=dict(sorted(age_dict.items(), key=lambda item: item[1]))
    max_age,max_ratio=list(tdict.items())[-1]
    max_female_3rd_age.append(max_age)
    max_female_3rd_ratios.append(max_ratio)

age_gender_a=pd.DataFrame(columns=["state/ut","age-group-males","ratio-males","age-group-females","ratio-females"])

age_gender_a["state/ut"]=age_india["state-code"]
age_gender_a.drop_duplicates(inplace=True)

age_gender_a["age-group-males"]=max_male_3rd_age
age_gender_a["ratio-males"]=max_male_3rd_ratios

age_gender_a["age-group-females"]=max_female_3rd_age
age_gender_a["ratio-females"]=max_female_3rd_ratios

age_gender_a.reset_index(drop=True,inplace=True)

age_gender_a.to_csv("Question-8/age-gender-a.csv",index=False)

max_male_2nd_age=[]
max_male_2nd_ratios=[]

max_female_2nd_age=[]
max_female_2nd_ratios=[]

for x in age_india["state-code"].unique():
    age_dict=dict(age_india[age_india["state-code"]==x][["age-group","2nd-lang-male-ratio"]].values)
    tdict=dict(sorted(age_dict.items(), key=lambda item: item[1]))
    max_age,max_ratio=list(tdict.items())[-1]
    max_male_2nd_age.append(max_age)
    max_male_2nd_ratios.append(max_ratio)

for x in age_india["state-code"].unique():
    age_dict=dict(age_india[age_india["state-code"]==x][["age-group","2nd-lang-female-ratio"]].values)
    tdict=dict(sorted(age_dict.items(), key=lambda item: item[1]))
    max_age,max_ratio=list(tdict.items())[-1]
    max_female_2nd_age.append(max_age)
    max_female_2nd_ratios.append(max_ratio)

age_gender_b=pd.DataFrame(columns=["state/ut","age-group-males","ratio-males","age-group-females","ratio-females"])

age_gender_b["state/ut"]=age_india["state-code"]
age_gender_b.drop_duplicates(inplace=True)

age_gender_b["age-group-males"]=max_male_2nd_age
age_gender_b["ratio-males"]=max_male_2nd_ratios

age_gender_b["age-group-females"]=max_female_2nd_age
age_gender_b["ratio-females"]=max_female_2nd_ratios

age_gender_b.reset_index(drop=True,inplace=True)

age_gender_b.to_csv("Question-8/age-gender-b.csv",index=False)

max_male_1st_age=[]
max_male_1st_ratios=[]

max_female_1st_age=[]
max_female_1st_ratios=[]

for x in age_india["state-code"].unique():
    age_dict=dict(age_india[age_india["state-code"]==x][["age-group","1st-lang-male-ratio"]].values)
    tdict=dict(sorted(age_dict.items(), key=lambda item: item[1]))
    max_age,max_ratio=list(tdict.items())[-1]
    max_male_1st_age.append(max_age)
    max_male_1st_ratios.append(max_ratio)

for x in age_india["state-code"].unique():
    age_dict=dict(age_india[age_india["state-code"]==x][["age-group","1st-lang-female-ratio"]].values)
    tdict=dict(sorted(age_dict.items(), key=lambda item: item[1]))
    max_age,max_ratio=list(tdict.items())[-1]
    max_female_1st_age.append(max_age)
    max_female_1st_ratios.append(max_ratio)

age_gender_c=pd.DataFrame(columns=["state/ut","age-group-males","ratio-males","age-group-females","ratio-females"])

age_gender_c["state/ut"]=age_india["state-code"]
age_gender_c.drop_duplicates(inplace=True)

age_gender_c["age-group-males"]=max_male_1st_age
age_gender_c["ratio-males"]=max_male_1st_ratios

age_gender_c["age-group-females"]=max_female_1st_age
age_gender_c["ratio-females"]=max_female_1st_ratios

age_gender_c.reset_index(drop=True,inplace=True)

age_gender_c.to_csv("Question-8/age-gender-c.csv",index=False)
