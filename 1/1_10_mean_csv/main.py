import pandas as pd

data = pd.read_csv(r"D:\Python\rand\Chat GPT learning\1_10_mean_csv\grades.csv")

df = pd.DataFrame(data=data)

math_grades = []
science_grades = []
english_grades = []

for grade in (df["Math"]):
    math_grades.append(grade)

for grade in (df["Science"]):
    science_grades.append(grade)
    
for grade in (df["English"]):
    english_grades.append(grade)

math_mean = sum(math_grades) / len(math_grades)
science_mean = sum(science_grades) / len(science_grades)
english_mean = sum(english_grades) / len(english_grades)

print(f"Math mean: {math_mean}")
print(f"Science mean: {science_mean}")
print(f"English mean: {english_mean}")



