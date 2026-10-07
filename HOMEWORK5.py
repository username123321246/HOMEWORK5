import pandas as pd


#PRACTICE 1


asd = pd.read_csv("LESSONS\\titanic.csv")

#result1 = asd.loc[(asd["Age"] >= 20) & (asd["Age"] <= 40), ["Name", "Fare"]]
# print(result1)
# print()

# result2 = asd.loc[asd["Fare"] > 100, [ "Name", "Pclass"]]
# print(result2)
# print()

# result3 = asd.loc[(asd["Survived"] == 1) & (asd["Pclass"] == 3), "Name"]
# print(result3)
# print()


#PRACTICE 2


asd.iloc[0:5, 2] = "Test Passenger"
print(asd)

asd.iloc[10:16, 7] = 999
print(asd.head(15))


print(asd.iloc[0:16])
print()


#PRACTICE 3


asd["FarePerPerson"] = asd["Fare"] / (asd["Siblings/Spouses Aboard"] + 1)
print(asd[["Fare", "Siblings/Spouses Aboard", "FarePerPerson"]])
print()



def age_group(age):
    if age < 12:
        return "Child"
    elif age <= 18:
        return "Teen"
    else:
        return "Adult"

asd["AgeGroup"] = asd["Age"].apply(age_group)
print(asd[["Age", "AgeGroup"]])



