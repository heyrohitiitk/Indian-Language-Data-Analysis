import pandas as pd
import numpy as np

population=pd.read_excel("data/DDW_PCA0000_2011_Indiastatedist.xlsx",usecols=["Level","Name","TRU","TOT_P"])

to_drop=list(population[(population["TRU"]=="Rural") | (population["TRU"]=="Urban")].index)
population2=population.drop(to_drop)
population2.reset_index(drop=True,inplace=True)
population2.drop(columns=["TRU"],inplace=True)

india_pop=(population2[population2["Level"]=="STATE"]).drop(columns=["Level"])

india_pop.reset_index(drop=True,inplace=True)
india_pop["Name"]=india_pop["Name"].str.title()
india_pop.columns=["Area","Total"]

lang=pd.read_excel("data/C18-Population By Bilingualism, Trilingualism, Age And Sex.xlsx",skiprows=[0,1,2,3,4,5],header=None)
lang.drop(columns=[1],inplace=True)

lang.columns=["State Code","Area","Total/Rural/Urban","Age Group","2nd_lang_persons","2nd_lang_males","2nd_lang_females",
              "3rd_lang_persons","3rd_lang_males","3rd_lang_females"]

lang.drop(columns=["2nd_lang_males","2nd_lang_females","3rd_lang_males","3rd_lang_females"],inplace=True)

lang=lang[(lang["Total/Rural/Urban"]=="Total") & (lang["Age Group"]=="Total")]

lang.drop([0],inplace=True)

lang.drop(columns=["Total/Rural/Urban","Age Group"],inplace=True)
lang=lang.reset_index(drop=True)
lang["Area"]=lang["Area"].str.title()

code_mapping=dict(lang[["Area","State Code"]].values)

india_pop["State Code"]=india_pop["Area"]
india_pop["State Code"]=india_pop["State Code"].replace(code_mapping)

pop_mapping=dict(india_pop[["State Code","Total"]].values)

lang["Total Pop"]=lang["State Code"]
lang["Total Pop"]=lang["Total Pop"].replace(pop_mapping)

lang["2nd_lang_persons"]=(lang["2nd_lang_persons"]-lang["3rd_lang_persons"])
lang["1st_lang_persons"]=lang["Total Pop"]-(lang["2nd_lang_persons"]+lang["3rd_lang_persons"])

ratio_india=pd.DataFrame(columns=["state-code","3-to-2-ratio","2-to-1-ratio"])

ratio_india["state-code"]=lang["State Code"]
ratio_india["3-to-2-ratio"]=lang["3rd_lang_persons"]/lang["2nd_lang_persons"]
ratio_india["2-to-1-ratio"]=lang["2nd_lang_persons"]/lang["1st_lang_persons"]

top2to1=np.argsort(ratio_india["2-to-1-ratio"].values)[::-1][:3]
low2to1=np.argsort(ratio_india["2-to-1-ratio"].values)[:3]

df3=ratio_india.iloc[top2to1,[0,2]]
df4=ratio_india.iloc[low2to1,[0,2]]

two_to_one_ratio=pd.concat((df3,df4))
two_to_one_ratio.reset_index(drop=True,inplace=True)

two_to_one_ratio.to_csv("Question-4/2-to-1-ratio.csv",index=False)

