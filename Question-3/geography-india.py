import pandas as pd
from scipy import stats

population=pd.read_excel("data/DDW_PCA0000_2011_Indiastatedist.xlsx",usecols=["Level","Name","TRU","TOT_P"])
to_drop=list(population[population["TRU"]=="Total"].index)
population2=population.drop(to_drop)
population2.reset_index(drop=True,inplace=True)
india_pop=(population2[(population2["Level"]=="India") | (population2["Level"]=="STATE")]).drop(columns=["Level"])
india_pop2=india_pop.reset_index(drop=True)

rural_pop=india_pop2[india_pop2["TRU"]=="Rural"]["TOT_P"].values
urban_pop=india_pop2[india_pop2["TRU"]=="Urban"]["TOT_P"].values

to_drop=list(india_pop2[india_pop2["TRU"]=="Rural"].index)
india_pop3=india_pop2.drop(to_drop)
india_pop3.drop(columns=["TOT_P","TRU"],inplace=True)
india_pop3.reset_index(drop=True,inplace=True)

india_pop3["Rural Pop"]=rural_pop
india_pop3["Urban Pop"]=urban_pop

india_pop3.columns=["Area","Rural Pop","Urban Pop"]
india_pop3["Area"]=india_pop3["Area"].str.title()

lang=pd.read_excel("data/C18-Population By Bilingualism, Trilingualism, Age And Sex.xlsx",skiprows=[0,1,2,3,4,5],header=None)
lang.drop(columns=[1],inplace=True)

lang.columns=["State Code","Area","Total/Rural/Urban","Age Group","2nd_lang_persons","2nd_lang_males","2nd_lang_females",
              "3rd_lang_persons","3rd_lang_males","3rd_lang_females"]

lang.drop(columns=["2nd_lang_males","2nd_lang_females","3rd_lang_males","3rd_lang_females"],inplace=True)

lang=lang[(lang["Total/Rural/Urban"]=="Rural") & (lang["Age Group"]=="Total") | (lang["Total/Rural/Urban"]=="Urban") & (lang["Age Group"]=="Total")]

urban_speak_2nd_lang=lang[lang["Total/Rural/Urban"]=="Urban"]["2nd_lang_persons"].values
rural_speak_2nd_lang=lang[lang["Total/Rural/Urban"]=="Rural"]["2nd_lang_persons"].values

urban_speak_3rd_lang=lang[lang["Total/Rural/Urban"]=="Urban"]["3rd_lang_persons"].values
rural_speak_3rd_lang=lang[lang["Total/Rural/Urban"]=="Rural"]["3rd_lang_persons"].values

lang.drop(columns=["Total/Rural/Urban","Age Group","2nd_lang_persons","3rd_lang_persons"],inplace=True)
lang=lang.reset_index(drop=True)
lang["Area"]=lang["Area"].str.title()

lang.drop_duplicates(inplace=True)
lang.reset_index(drop=True,inplace=True)

lang["2nd_lang_persons_rural"]=rural_speak_2nd_lang
lang["2nd_lang_persons_urban"]=urban_speak_2nd_lang

lang["3rd_lang_persons_rural"]=rural_speak_3rd_lang
lang["3rd_lang_persons_urban"]=urban_speak_3rd_lang

code_mapping=dict(lang[["Area","State Code"]].values)

india_pop3["State Code"]=india_pop3["Area"]
india_pop3["State Code"]=india_pop3["State Code"].replace(code_mapping)


pop_mapping1=dict(india_pop3[["State Code","Rural Pop"]].values)
pop_mapping2=dict(india_pop3[["State Code","Urban Pop"]].values)

lang["Rural Pop"]=lang["State Code"]
lang["Urban Pop"]=lang["State Code"]

lang["Rural Pop"]=lang["Rural Pop"].replace(pop_mapping1)
lang["Urban Pop"]=lang["Urban Pop"].replace(pop_mapping2)

lang["1st_lang_persons_rural"]=lang["Rural Pop"]-lang["2nd_lang_persons_rural"]
lang["1st_lang_persons_urban"]=lang["Urban Pop"]-lang["2nd_lang_persons_urban"]

lang["2nd_lang_persons_rural"]=lang["2nd_lang_persons_rural"]-lang["3rd_lang_persons_rural"]
lang["2nd_lang_persons_urban"]=lang["2nd_lang_persons_urban"]-lang["3rd_lang_persons_urban"]

geography_india_a=pd.DataFrame(columns=["state-code","urban-percentage","rural-percentage","p-value"])

geography_india_a["state-code"]=lang["State Code"]
geography_india_a["urban-percentage"]=round((lang["1st_lang_persons_urban"]/lang["Urban Pop"])*100,2)
geography_india_a["rural-percentage"]=round((lang["1st_lang_persons_rural"]/lang["Rural Pop"])*100,2)

geography_india_b=pd.DataFrame(columns=["state-code","urban-percentage","rural-percentage","p-value"])

geography_india_b["state-code"]=lang["State Code"]
geography_india_b["urban-percentage"]=round((lang["2nd_lang_persons_urban"]/lang["Urban Pop"])*100,2)
geography_india_b["rural-percentage"]=round((lang["2nd_lang_persons_rural"]/lang["Rural Pop"])*100,2)

geography_india_c=pd.DataFrame(columns=["state-code","urban-percentage","rural-percentage","p-value"])

geography_india_c["state-code"]=lang["State Code"]
geography_india_c["urban-percentage"]=round((lang["3rd_lang_persons_urban"]/lang["Urban Pop"])*100,2)
geography_india_c["rural-percentage"]=round((lang["3rd_lang_persons_rural"]/lang["Rural Pop"])*100,2)

ratios=[]
overall_ratio=[]

for x in lang.iloc[:,[9,8,3,2,5,4,7,6]].values:
    temp=[x[0]/x[1],x[2]/x[3],x[4]/x[5]]
    ratios.append(temp)
    
    overall=[x[6]/x[7],x[6]/x[7],x[6]/x[7]]
    overall_ratio.append(overall)

pvalue=[]

for x,y in zip(ratios,overall_ratio):
    pvalue.append(stats.ttest_ind(x,y,equal_var=False).pvalue)
    
geography_india_a["p-value"]=pvalue
geography_india_b["p-value"]=pvalue
geography_india_c["p-value"]=pvalue

geography_india_a.to_csv("Question-3/geography-india-a.csv",index=False)
geography_india_b.to_csv("Question-3/geography-india-b.csv",index=False)
geography_india_c.to_csv("Question-3/geography-india-c.csv",index=False)










