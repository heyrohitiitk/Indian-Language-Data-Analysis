								     CS685: DATA MINING						
					                            21111053_ASSIGNMENT-2


-All the external data files used in the questions are present inside the "data/" folder

-to run the entire assignment run the "assign2.sh" file, note the alias for python is "python3" in my linux i.e. each python file is called inside the .sh 
file by the command "python3 folder_name/file_name.py".

-output file of each question generated inside the respective "Question-x/" folder

Question-1

-the script file to run this is "percent-india.sh" which calls the python file "percent-india.py" inside "Question-1/" folder.

-The data files used in this question are "DDW_PCA0000_2011_Indiastatedist.xlsx" which contains the india census data and 
 "C18-Population By Bilingualism, Trilingualism, Age And Sex.xlsx" which contain the language data

-there is one output csv file "percent-india.csv" generated inside the "Question-1/" folder.


Question-2

-the script file to run this is "gender-india.sh" which calls the python file "gender-india.py" inside "Question-2/" folder.

-The data files used in this question are "DDW_PCA0000_2011_Indiastatedist.xlsx" which contains the india census data and 
 "C18-Population By Bilingualism, Trilingualism, Age And Sex.xlsx" which contain the language data

-there are three output csv files "gender-india-a.csv" for monolinguals,"gender-india-b.csv" for bilinguals and "gender-india-c.csv" for trilinguals 
 generated inside the "Question-2/" folder

-Now this question required us to calculate the p-value and for this I have used "Welch's t-test" which is used when we have two samples and having unequal
 variance, here in this question there are two vectors, in the 1st vector there are three values ["male to female ratio speaking exactly 1 language","male to female ratio speaking exactly 2 languages","male to female ratio speaking 3 or more languages"]
 and 2nd vector ["ratio of male population to female population","ratio of male population to female population","ratio of male population to female population"]

--to report the p-value i used the "scipy.stats.ttest_ind(1st vector,2nd vector,equal_var=False)" function in the scipy library

-Now since the p-value for all the states and overall india is greater than 0.05 significance level so the ratio between males and females is not significantly different for any state

Question-3

-the script file to run this is "geography-india.sh" which calls the python file "geography-india.py" inside "Question-3/" folder.

-The data files used in this question are "DDW_PCA0000_2011_Indiastatedist.xlsx" which contains the india census data and 
 "C18-Population By Bilingualism, Trilingualism, Age And Sex.xlsx" which contain the language data

-there are three output csv files "geography-india-a.csv" for monolinguals,"geography-india-b.csv" for bilinguals and "geography-india-c.csv" for 
 trilinguals generated inside the "Question-3/" folder

-Now this question required to calculate the p-value and for this I have used "Welch's t-test" which is used when we have two samples and having unequal
 variance, here in this question there are two vectors, in the 1st vector there are three values ["Urban to Rural population ratio speaking exactly 1 language","Urban to Rural population ratio speaking exactly 2 languages","Urban to Rural population ratio speaking 3 or more languages"]
 and 2nd vector also has three values ["ratio of urban population to rural population","ratio of urban population to rural population","ratio of urban population to rural population"]

--to report the p-value i used the "scipy.stats.ttest_ind(1st vector,2nd vector,equal_var=False)" function in the scipy library

-Now since the p-value for all the states and overall india is greater than 0.05 significance level so the ratio between urban and rural is not significantly different for any state

Question-4

-there are two script files for two parts in this question, one is "2-to-1-ratio.sh" which calls the python file "2-to-1-ratio.py" inside "Question-4/" 
 folder and other file is "3-to-2-ratio.sh" which calls the python file "3-to-2-ratio.py" inside "Question-4/" folder

-The data files used in this question are "DDW_PCA0000_2011_Indiastatedist.xlsx" which contains the india census data and 
 "C18-Population By Bilingualism, Trilingualism, Age And Sex.xlsx" which contain the language data

-there are two output csv files "2-to-1-ratio.csv" and "3-to-2-ratio.csv" generated inside the "Question-4/" folder


Question-5

-the script file to run this is "age-india.sh" which calls the python file "age-india.py" inside "Question-5/" folder.

-The data files used in this question are "C14-Population-By-Age_Group.xls" which contains the india population data by age group and 
 "C18-Population By Bilingualism, Trilingualism, Age And Sex.xlsx" which contain the language data

-there is one output csv file "age-india.csv" generated inside the "Question-5/" folder

Question-6

-the script file to run this is "literacy-india.sh" which calls the python file "literacy-india.py" inside "Question-6/" folder.

-The data files used in this question are "C19-Population By Bilingualism, Trilingualism, Education Level And Sex.xlsx" which contains the india language 
 data by education level and "C08-Population By Literacy Rate.xlsx" which contain the india population data by education level

-there is one output csv file "literacy-india.csv" generated inside the "Question-6/" folder

Question-7

-the script file to run this is "region-india.sh" which calls the python file "region-india.py" inside "Question-7/" folder.

-There is seperate data file for each state like, "DDW-C17-Madhya Pradesh.XLSX" and using these data files i divided india into 6 regions

-there are two output csv files for each part one is "region-india-a.csv" and other is "region-india-b.csv" generated inside the "Question-7/" folder

QUESTION-8

-the script file to run this is "age-gender.sh" which calls the python file "age-gender.py" inside "Question-8/" folder.

-The data files used in this question are "C14-Population-By-Age_Group.xls" which contains the india population data by age group and 
 "C18-Population By Bilingualism, Trilingualism, Age And Sex.xlsx" which contain the language data

-there are three output csv files "age-gender-a.csv" for trilinguals,"age-gender-b.csv" for bilinguals and "age-gender-c.csv" for monolinguals  
 generated inside the "Question-8/" folder

QUESTION-9

-the script file to run this is "literacy-gender.sh" which calls the python file "literacy-gender.py" inside "Question-9/" folder.

-The data files used in this question are "C19-Population By Bilingualism, Trilingualism, Education Level And Sex.xlsx" which contains the india 
 language data by education level and "C08-Population By Literacy Rate.xlsx" which contain the india population data by education level

-there are three output csv files "literacy-gender-a.csv" for trilinguals,"literacy-gender-b.csv" for bilinguals and "literacy-gender-c.csv" for monolinguals  
 generated inside the "Question-9/" folder
