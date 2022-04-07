import pandas as pd
from scipy import stats

population=pd.read_excel("data/DDW_PCA0000_2011_Indiastatedist.xlsx",usecols=["Level","Name","TRU","TOT_P","TOT_M","TOT_F"])
to_drop=list(population[(population["TRU"]=="Rural") | (population["TRU"]=="Urban")].index)
population2=population.drop(to_drop)
population2.reset_index(drop=True,inplace=True)
population2.drop(columns=["TRU"],inplace=True)

india_pop=(population2[(population2["Level"]=="India") | (population2["Level"]=="STATE")]).drop(columns=["Level"])

india_pop.reset_index(drop=True,inplace=True)
india_pop["Name"]=india_pop["Name"].str.title()
india_pop.columns=["Area","Total","Male","Female"]

lang=pd.read_excel("data/C18-Population By Bilingualism, Trilingualism, Age And Sex.xlsx",skiprows=[0,1,2,3,4,5],header=None)

lang.drop(columns=[1],inplace=True)

lang.columns=["State Code","Area","Total/Rural/Urban","Age Group","2nd_lang_persons","2nd_lang_males","2nd_lang_females",
              "3rd_lang_persons","3rd_lang_males","3rd_lang_females"]

lang=lang[(lang["Total/Rural/Urban"]=="Total") & (lang["Age Group"]=="Total")]

lang.drop(columns=["Total/Rural/Urban","Age Group","2nd_lang_persons","3rd_lang_persons"],inplace=True)
lang=lang.reset_index(drop=True)
lang["Area"]=lang["Area"].str.title()

code_mapping=dict(lang[["Area","State Code"]].values)

india_pop["State Code"]=india_pop["Area"]
india_pop["State Code"]=india_pop["State Code"].replace(code_mapping)

pop_mapping1=dict(india_pop[["State Code","Male"]].values)
pop_mapping2=dict(india_pop[["State Code","Female"]].values)

lang["Male Pop"]=lang["State Code"]
lang["Female Pop"]=lang["State Code"]

lang["Male Pop"]=lang["Male Pop"].replace(pop_mapping1)
lang["Female Pop"]=lang["Female Pop"].replace(pop_mapping2)

lang["1st_lang_males"]=lang["Male Pop"]-lang["2nd_lang_males"]
lang["1st_lang_females"]=lang["Female Pop"]-lang["2nd_lang_females"]
lang["2nd_lang_males"]=lang["2nd_lang_males"]-lang["3rd_lang_males"]
lang["2nd_lang_females"]=lang["2nd_lang_females"]-lang["3rd_lang_females"]

gender_india_a=pd.DataFrame(columns=["state-code","male-percentage","female-percentage","p-value"])
gender_india_a["state-code"]=lang["State Code"]
gender_india_a["male-percentage"]=round((lang["1st_lang_males"]/lang["Male Pop"])*100,2)
gender_india_a["female-percentage"]=round((lang["1st_lang_females"]/lang["Female Pop"])*100,2)

gender_india_b=pd.DataFrame(columns=["state-code","male-percentage","female-percentage","p-value"])
gender_india_b["state-code"]=lang["State Code"]
gender_india_b["male-percentage"]=round((lang["2nd_lang_males"]/lang["Male Pop"])*100,2)
gender_india_b["female-percentage"]=round((lang["2nd_lang_females"]/lang["Female Pop"])*100,2)

gender_india_c=pd.DataFrame(columns=["state-code","male-percentage","female-percentage","p-value"])
gender_india_c["state-code"]=lang["State Code"]
gender_india_c["male-percentage"]=round((lang["3rd_lang_males"]/lang["Male Pop"])*100,2)
gender_india_c["female-percentage"]=round((lang["3rd_lang_females"]/lang["Female Pop"])*100,2)

ratios=[]
overall_ratio=[]

for x in lang.iloc[:,[8,9,2,3,4,5,6,7]].values:
    temp=[x[0]/x[1],x[2]/x[3],x[4]/x[5]]
    ratios.append(temp)
    
    overall=[x[6]/x[7],x[6]/x[7],x[6]/x[7]]
    overall_ratio.append(overall)
    

pvalue=[]

for x,y in zip(ratios,overall_ratio):
    pvalue.append(stats.ttest_ind(x,y,equal_var=False).pvalue)

gender_india_a["p-value"]=pvalue
gender_india_b["p-value"]=pvalue
gender_india_c["p-value"]=pvalue

gender_india_a.to_csv("Question-2/gender-india-a.csv",index=False)
gender_india_b.to_csv("Question-2/gender-india-b.csv",index=False)
gender_india_c.to_csv("Question-2/gender-india-c.csv",index=False)

