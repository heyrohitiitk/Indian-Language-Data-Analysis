import pandas as pd
import warnings
warnings.filterwarnings("ignore")

MP=pd.read_excel("data/DDW-C17-Madhya Pradesh.XLSX",skiprows=[0,1,2,3,4,5],header=None,usecols=[3,4,8,9,13,14],names=["language1","mother_tongue","language2","2nd","language3","3rd"])
UP=pd.read_excel("data/DDW-C17-Uttar Pradesh.XLSX",skiprows=[0,1,2,3,4,5],header=None,usecols=[3,4,8,9,13,14],names=["language1","mother_tongue","language2","2nd","language3","3rd"])
CG=pd.read_excel("data/DDW-C17-chattisgarh.XLSX",skiprows=[0,1,2,3,4,5],header=None,usecols=[3,4,8,9,13,14],names=["language1","mother_tongue","language2","2nd","language3","3rd"])

central=pd.concat((MP,UP,CG),ignore_index=True)

one=central[["language1","mother_tongue"]]
two=central[["language2","2nd"]]
three=central[["language3","3rd"]]

one.dropna(inplace=True)
one.reset_index(drop=True,inplace=True)

one=one.groupby(by=["language1"]).sum().reset_index()

central_top_a=one.sort_values(by="mother_tongue",ascending=False).iloc[[0,1,2],0].values

two.dropna(inplace=True)
two.reset_index(drop=True,inplace=True)

two=two.groupby(by=["language2"]).sum().reset_index()

three.dropna(inplace=True)
three.reset_index(drop=True,inplace=True)

three=three.groupby(by=["language3"]).sum().reset_index()

all_three_language=pd.concat((one,two.rename(columns={"language2":"language1","2nd":"mother_tongue"}),three.rename(columns={"language3":"language1","3rd":"mother_tongue"})),ignore_index=True)

all_three_language=all_three_language.groupby(by=["language1"]).sum().reset_index()

central_top_b=all_three_language.sort_values(by="mother_tongue",ascending=False).iloc[[0,1,2],0].values

BH=pd.read_excel("data/DDW-C17-Bihar.XLSX",skiprows=[0,1,2,3,4,5],header=None,usecols=[3,4,8,9,13,14],names=["language1","mother_tongue","language2","2nd","language3","3rd"])
JH=pd.read_excel("data/DDW-C17-Jharkhand.XLSX",skiprows=[0,1,2,3,4,5],header=None,usecols=[3,4,8,9,13,14],names=["language1","mother_tongue","language2","2nd","language3","3rd"])
OR=pd.read_excel("data/DDW-C17-Odisha.XLSX",skiprows=[0,1,2,3,4,5],header=None,usecols=[3,4,8,9,13,14],names=["language1","mother_tongue","language2","2nd","language3","3rd"])
WB=pd.read_excel("data/DDW-C17-West Bengal.XLSX",skiprows=[0,1,2,3,4,5],header=None,usecols=[3,4,8,9,13,14],names=["language1","mother_tongue","language2","2nd","language3","3rd"])

east=pd.concat((BH,JH,OR,WB),ignore_index=True)

one=east[["language1","mother_tongue"]]
two=east[["language2","2nd"]]
three=east[["language3","3rd"]]

one.dropna(inplace=True)
one.reset_index(drop=True,inplace=True)

one=one.groupby(by=["language1"]).sum().reset_index()

east_top_a=one.sort_values(by="mother_tongue",ascending=False).iloc[[0,1,2],0].values

two.dropna(inplace=True)
two.reset_index(drop=True,inplace=True)

two=two.groupby(by=["language2"]).sum().reset_index()

three.dropna(inplace=True)
three.reset_index(drop=True,inplace=True)

three=three.groupby(by=["language3"]).sum().reset_index()

all_three_language=pd.concat((one,two.rename(columns={"language2":"language1","2nd":"mother_tongue"}),three.rename(columns={"language3":"language1","3rd":"mother_tongue"})),ignore_index=True)

all_three_language=all_three_language.groupby(by=["language1"]).sum().reset_index()

east_top_b=all_three_language.sort_values(by="mother_tongue",ascending=False).iloc[[0,1,2],0].values

CH=pd.read_excel("data/DDW-C17-Chandigarh.XLSX",skiprows=[0,1,2,3,4,5],header=None,usecols=[3,4,8,9,13,14],names=["language1","mother_tongue","language2","2nd","language3","3rd"])
DL=pd.read_excel("data/DDW-C17-Delhi.XLSX",skiprows=[0,1,2,3,4,5],header=None,usecols=[3,4,8,9,13,14],names=["language1","mother_tongue","language2","2nd","language3","3rd"])
HR=pd.read_excel("data/DDW-C17-Haryana.XLSX",skiprows=[0,1,2,3,4,5],header=None,usecols=[3,4,8,9,13,14],names=["language1","mother_tongue","language2","2nd","language3","3rd"])
HP=pd.read_excel("data/DDW-C17-Himachal Pradesh.XLSX",skiprows=[0,1,2,3,4,5],header=None,usecols=[3,4,8,9,13,14],names=["language1","mother_tongue","language2","2nd","language3","3rd"])
JK=pd.read_excel("data/DDW-C17-Jammu and Kashmir.XLSX",skiprows=[0,1,2,3,4,5],header=None,usecols=[3,4,8,9,13,14],names=["language1","mother_tongue","language2","2nd","language3","3rd"])
PB=pd.read_excel("data/DDW-C17-Punjab.XLSX",skiprows=[0,1,2,3,4,5],header=None,usecols=[3,4,8,9,13,14],names=["language1","mother_tongue","language2","2nd","language3","3rd"])
UT=pd.read_excel("data/DDW-C17-Uttarkhand.XLSX",skiprows=[0,1,2,3,4,5],header=None,usecols=[3,4,8,9,13,14],names=["language1","mother_tongue","language2","2nd","language3","3rd"])

north=pd.concat((CH,DL,HR,HP,JK,PB,UT),ignore_index=True)

one=north[["language1","mother_tongue"]]
two=north[["language2","2nd"]]
three=north[["language3","3rd"]]

one.dropna(inplace=True)
one.reset_index(drop=True,inplace=True)

one=one.groupby(by=["language1"]).sum().reset_index()

north_top_a=one.sort_values(by="mother_tongue",ascending=False).iloc[[0,1,2],0].values

two.dropna(inplace=True)
two.reset_index(drop=True,inplace=True)

two=two.groupby(by=["language2"]).sum().reset_index()

three.dropna(inplace=True)
three.reset_index(drop=True,inplace=True)

three=three.groupby(by=["language3"]).sum().reset_index()

all_three_language=pd.concat((one,two.rename(columns={"language2":"language1","2nd":"mother_tongue"}),three.rename(columns={"language3":"language1","3rd":"mother_tongue"})),ignore_index=True)

all_three_language=all_three_language.groupby(by=["language1"]).sum().reset_index()

north_top_b=all_three_language.sort_values(by="mother_tongue",ascending=False).iloc[[0,1,2],0].values


AN=pd.read_excel("data/DDW-C17-Andaman Nicobar.XLSX",skiprows=[0,1,2,3,4,5],header=None,usecols=[3,4,8,9,13,14],names=["language1","mother_tongue","language2","2nd","language3","3rd"])
AP=pd.read_excel("data/DDW-C17-Arunachal Pradesh.XLSX",skiprows=[0,1,2,3,4,5],header=None,usecols=[3,4,8,9,13,14],names=["language1","mother_tongue","language2","2nd","language3","3rd"])
AS=pd.read_excel("data/DDW-C17-Assam.XLSX",skiprows=[0,1,2,3,4,5],header=None,usecols=[3,4,8,9,13,14],names=["language1","mother_tongue","language2","2nd","language3","3rd"])
MN=pd.read_excel("data/DDW-C17-Manipur.XLSX",skiprows=[0,1,2,3,4,5],header=None,usecols=[3,4,8,9,13,14],names=["language1","mother_tongue","language2","2nd","language3","3rd"])
ME=pd.read_excel("data/DDW-C17-Meghalaya.XLSX",skiprows=[0,1,2,3,4,5],header=None,usecols=[3,4,8,9,13,14],names=["language1","mother_tongue","language2","2nd","language3","3rd"])
MZ=pd.read_excel("data/DDW-C17-Mizoram.XLSX",skiprows=[0,1,2,3,4,5],header=None,usecols=[3,4,8,9,13,14],names=["language1","mother_tongue","language2","2nd","language3","3rd"])
NG=pd.read_excel("data/DDW-C17-Nagaland.XLSX",skiprows=[0,1,2,3,4,5],header=None,usecols=[3,4,8,9,13,14],names=["language1","mother_tongue","language2","2nd","language3","3rd"])
SK=pd.read_excel("data/DDW-C17-Sikkim.XLSX",skiprows=[0,1,2,3,4,5],header=None,usecols=[3,4,8,9,13,14],names=["language1","mother_tongue","language2","2nd","language3","3rd"])
TR=pd.read_excel("data/DDW-C17-Tripura.XLSX",skiprows=[0,1,2,3,4,5],header=None,usecols=[3,4,8,9,13,14],names=["language1","mother_tongue","language2","2nd","language3","3rd"])

north_east=pd.concat((AN,AP,AS,MN,ME,MZ,NG,SK,TR),ignore_index=True)

one=north_east[["language1","mother_tongue"]]
two=north_east[["language2","2nd"]]
three=north_east[["language3","3rd"]]

one.dropna(inplace=True)
one.reset_index(drop=True,inplace=True)

one=one.groupby(by=["language1"]).sum().reset_index()

north_east_top_a=one.sort_values(by="mother_tongue",ascending=False).iloc[[0,1,2],0].values

two.dropna(inplace=True)
two.reset_index(drop=True,inplace=True)

two=two.groupby(by=["language2"]).sum().reset_index()

three.dropna(inplace=True)
three.reset_index(drop=True,inplace=True)

three=three.groupby(by=["language3"]).sum().reset_index()

all_three_language=pd.concat((one,two.rename(columns={"language2":"language1","2nd":"mother_tongue"}),three.rename(columns={"language3":"language1","3rd":"mother_tongue"})),ignore_index=True)

all_three_language=all_three_language.groupby(by=["language1"]).sum().reset_index()

north_east_top_b=all_three_language.sort_values(by="mother_tongue",ascending=False).iloc[[0,1,2],0].values


AD=pd.read_excel("data/DDW-C17-Andhra Pradesh.XLSX",skiprows=[0,1,2,3,4,5],header=None,usecols=[3,4,8,9,13,14],names=["language1","mother_tongue","language2","2nd","language3","3rd"])
KN=pd.read_excel("data/DDW-C17-Karnataka.XLSX",skiprows=[0,1,2,3,4,5],header=None,usecols=[3,4,8,9,13,14],names=["language1","mother_tongue","language2","2nd","language3","3rd"])
KL=pd.read_excel("data/DDW-C17-Kerala.XLSX",skiprows=[0,1,2,3,4,5],header=None,usecols=[3,4,8,9,13,14],names=["language1","mother_tongue","language2","2nd","language3","3rd"])
LD=pd.read_excel("data/DDW-C17-Lakshadweep.XLSX",skiprows=[0,1,2,3,4,5],header=None,usecols=[3,4,8,9,13,14],names=["language1","mother_tongue","language2","2nd","language3","3rd"])
PY=pd.read_excel("data/DDW-C17-Puducherry.XLSX",skiprows=[0,1,2,3,4,5],header=None,usecols=[3,4,8,9,13,14],names=["language1","mother_tongue","language2","2nd","language3","3rd"])
TN=pd.read_excel("data/DDW-C17-Tamilnadu.XLSX",skiprows=[0,1,2,3,4,5],header=None,usecols=[3,4,8,9,13,14],names=["language1","mother_tongue","language2","2nd","language3","3rd"])

south=pd.concat((AD,KN,KL,LD,PY,TN),ignore_index=True)

one=south[["language1","mother_tongue"]]
two=south[["language2","2nd"]]
three=south[["language3","3rd"]]

one.dropna(inplace=True)
one.reset_index(drop=True,inplace=True)

one=one.groupby(by=["language1"]).sum().reset_index()

south_top_a=one.sort_values(by="mother_tongue",ascending=False).iloc[[0,1,2],0].values

two.dropna(inplace=True)
two.reset_index(drop=True,inplace=True)

two=two.groupby(by=["language2"]).sum().reset_index()

three.dropna(inplace=True)
three.reset_index(drop=True,inplace=True)

three=three.groupby(by=["language3"]).sum().reset_index()

all_three_language=pd.concat((one,two.rename(columns={"language2":"language1","2nd":"mother_tongue"}),three.rename(columns={"language3":"language1","3rd":"mother_tongue"})),ignore_index=True)

all_three_language=all_three_language.groupby(by=["language1"]).sum().reset_index()

south_top_b=all_three_language.sort_values(by="mother_tongue",ascending=False).iloc[[0,1,2],0].values

DN=pd.read_excel("data/DDW-C17-Dadra and Nagar haveli.XLSX",skiprows=[0,1,2,3,4,5],header=None,usecols=[3,4,8,9,13,14],names=["language1","mother_tongue","language2","2nd","language3","3rd"])
DD=pd.read_excel("data/DDW-C17-Daman and Deu.XLSX",skiprows=[0,1,2,3,4,5],header=None,usecols=[3,4,8,9,13,14],names=["language1","mother_tongue","language2","2nd","language3","3rd"])
GA=pd.read_excel("data/DDW-C17-Goa.XLSX",skiprows=[0,1,2,3,4,5],header=None,usecols=[3,4,8,9,13,14],names=["language1","mother_tongue","language2","2nd","language3","3rd"])
GJ=pd.read_excel("data/DDW-C17-Gujarat.XLSX",skiprows=[0,1,2,3,4,5],header=None,usecols=[3,4,8,9,13,14],names=["language1","mother_tongue","language2","2nd","language3","3rd"])
MH=pd.read_excel("data/DDW-C17-Maharashtra.XLSX",skiprows=[0,1,2,3,4,5],header=None,usecols=[3,4,8,9,13,14],names=["language1","mother_tongue","language2","2nd","language3","3rd"])
RJ=pd.read_excel("data/DDW-C17-Rajasthan.XLSX",skiprows=[0,1,2,3,4,5],header=None,usecols=[3,4,8,9,13,14],names=["language1","mother_tongue","language2","2nd","language3","3rd"])

west=pd.concat((DN,DD,GA,GJ,MH,RJ),ignore_index=True)

one=west[["language1","mother_tongue"]]
two=west[["language2","2nd"]]
three=west[["language3","3rd"]]

one.dropna(inplace=True)
one.reset_index(drop=True,inplace=True)

one=one.groupby(by=["language1"]).sum().reset_index()

west_top_a=one.sort_values(by="mother_tongue",ascending=False).iloc[[0,1,2],0].values

two.dropna(inplace=True)
two.reset_index(drop=True,inplace=True)

two=two.groupby(by=["language2"]).sum().reset_index()

three.dropna(inplace=True)
three.reset_index(drop=True,inplace=True)

three=three.groupby(by=["language3"]).sum().reset_index()

all_three_language=pd.concat((one,two.rename(columns={"language2":"language1","2nd":"mother_tongue"}),three.rename(columns={"language3":"language1","3rd":"mother_tongue"})),ignore_index=True)

all_three_language=all_three_language.groupby(by=["language1"]).sum().reset_index()

west_top_b=all_three_language.sort_values(by="mother_tongue",ascending=False).iloc[[0,1,2],0].values

region_india_a=pd.DataFrame(columns=["region","language-1","language-2","language-3"])

region_india_a["region"]=["North","West","Central","East","South","North-East"]
region_india_a.iloc[0,[1,2,3]]=north_top_a
region_india_a.iloc[1,[1,2,3]]=west_top_a
region_india_a.iloc[2,[1,2,3]]=central_top_a
region_india_a.iloc[3,[1,2,3]]=east_top_a
region_india_a.iloc[4,[1,2,3]]=south_top_a
region_india_a.iloc[5,[1,2,3]]=north_east_top_a

region_india_a.to_csv("Question-7/region-india-a.csv",index=False)

region_india_b=pd.DataFrame(columns=["region","language-1","language-2","language-3"])

region_india_b["region"]=["North","West","Central","East","South","North-East"]
region_india_b.iloc[0,[1,2,3]]=north_top_b
region_india_b.iloc[1,[1,2,3]]=west_top_b
region_india_b.iloc[2,[1,2,3]]=central_top_b
region_india_b.iloc[3,[1,2,3]]=east_top_b
region_india_b.iloc[4,[1,2,3]]=south_top_b
region_india_b.iloc[5,[1,2,3]]=north_east_top_b

region_india_b.to_csv("Question-7/region-india-b.csv",index=False)
