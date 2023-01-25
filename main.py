import pandas as pd
import numpy  as np

df = pd.read_csv('Artjoms Kasperovičs - adult.data (1).csv')



df_complete = df.dropna() 
adult = np.array(df_complete)

print("------------------------------------------------------------")
race = df["marital-status"].value_counts()
print(race)
print("------------------------------------------------------------")
videja = round(df['age'].mean())
print(videja,"videja gadi")
print("------------------------------------------------------------")

bob = df['workclass'].isin(["Local-gov", "State-gov","Federal-gov"]).value_counts()
ed = df["workclass"].value_counts()
procent2= bob / ed.sum() * 100
print(procent2)
print("------------------------------------------------------------")
yuy = df['workclass'].isin(["Local-gov", "State-gov","Federal-gov"])
zarplata=df["salary"] == ">50K"
rich = round(df.loc[yuy & zarplata].shape[0] / df.loc[yuy].shape[0]*100)
print(rich, "% ", "cilvēku, kas strādā valsts pārvaldē (`Local-gov`, `State-gov`, or `Federal-gov`) pelna vairāk nekā 50 tūkstošus")
print("------------------------------------------------------------")

private = df['workclass'].isin(["Private"])
money=df["salary"] == ">50K"
proc = round(df.loc[private & money].shape[0] / df.loc[private].shape[0]*100 , 1)
print(proc,"%","cilvēku, kas strādā privātajā sektorā un saņem vairāk nekā 50 tūkstošus")
print("------------------------------------------------------------")
print("Maksimala:",np.amax(adult[:,10]),"capital-gain")
print("------------------------------------------------------------")
print("average:",np.average(adult[:,10]),"capital-gain")
print("------------------------------------------------------------")

#joy = df['workclass'].isin(["Local-gov", "State-gov","Federal-gov"])
#man = round(np.sum(df.loc[df['sex'] == "Male"].value_counts()).mean())
#women = round(np.sum(df.loc[df['sex'] == "Female"].value_counts()))
#print(women)
dept_gender_salary = df(df.groupby['sex','workclass']== "Male","Local-gov").mean()
print(dept_gender_salary)
                                