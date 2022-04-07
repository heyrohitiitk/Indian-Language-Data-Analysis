import pandas as pd

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

lang.drop(columns=["2nd_lang_males","2nd_lang_females","3rd_lang_males","3rd_lang_females"],inplace=True)

lang=lang[(lang["Total/Rural/Urban"]=="Total") & (lang["Age Group"]=="Total")]

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

percent_india=pd.DataFrame(columns=["state-code","percent-one","percent-two","percent-three"])

percent_india["state-code"]=lang["State Code"]
percent_india["percent-one"]=round((lang["1st_lang_persons"]/lang["Total Pop"])*100,2)
percent_india["percent-two"]=round((lang["2nd_lang_persons"]/lang["Total Pop"])*100,2)
percent_india["percent-three"]=round((lang["3rd_lang_persons"]/lang["Total Pop"])*100,2)

percent_india.to_csv("Question-1/percent-india.csv",index=False)
