import numpy as np
# Practice challenge 6

# 1. Generate 20 random integers between 1 and 100.
# print(np.random.randint(1,100,20))

# 2. Generate a 5×5 random integer matrix.
# print(np.random.randint(1,100,size=(5,5)))

# 3. Generate 10 random floats.
# print(np.random.rand(10))

# 4. Shuffle
arr = np.arange(1,11)
# print(arr)
np.random.shuffle(arr)
# print(arr)

# 5. Pick 3 random students without replacement.
students = np.array([
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Eva"
])
stu = np.random.choice(students,size=3,replace=False)
# print(stu)

# 6. Generate marks for 50 students using:
marks = np.random.randint(35,101,size=50)
# print(marks)
# print("Average:",marks.mean())
# print("Maximim:",marks.max())
# print("Minimum:",marks.min())

# 7. Generate 100 salaries between:
salaries = np.random.randint(30000,100000,size=100)
# print(salaries[salaries>60000])

# 8. Seed
seed = np.random.seed(42)
# print(np.random.randint(1,100,10))

# 9. Generate mean max min
arr = np.random.uniform(
    35,42,size=20
)
# print(arr.mean())
# print(arr.max())
# print(arr.min())

# 10. Generate Average, standard deviation, highest, lowest
arr = np.random.normal(
    loc=70,
    scale=8,
    size=50
)
# print(arr.mean())
# print(arr.std())
# print(arr.max())
# print(arr.min()
#---------------------------------------------------------------
# Hard Challenge
marks = np.random.normal(
    loc=70,
    scale=10,
    size=1000
)
marks = np.clip(marks,0,100)
print(marks)
# print("Average:", marks.mean())
# print("Highest:", marks.max())
# print("Lowest:", marks.min())

passed = marks > 40
pass_percentage = passed.mean() * 100
# print("Pass Percentage:",pass_percentage)

top = np.percentile(marks, 90)
top_students = marks[marks > top]
# print("Top 10% Cutoff:",top)
# print("Number of Top Students:",top_students.size)

bottom = np.percentile(marks,5)
low_students = marks[marks < bottom]
# print("Lowest 5% Cutoff:",bottom)
# print("Number of Lowest Students:",low_students.size)
#-------------------------------------------------------------

# Mini Project — Student Marks Simulator
# Generate Data
np.random.seed(42)
marks = np.random.normal(
    loc=70,
    scale=10,
    size=(100,5)
)
# print(marks.size)
marks = np.clip(marks,0,100)
# print(np.mean(marks,axis=1))
# print(np.mean(marks,axis=0))
Total_Marks = np.sum(marks,axis=1)
# print("Total_Marks:",Total_Marks)
Highest_Scorer = np.argmax(Total_Marks)
# print("Highest_Scorer:",Highest_Scorer)
# print("Highest_Total:",np.max(Total_Marks))
Lowest_Scorer = np.argmin(Total_Marks)
# print("Lowest_Scorer:",np.argmin(Total_Marks))
# print("Lowest_Total:",np.min(Total_Marks))





