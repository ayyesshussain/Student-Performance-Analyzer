import numpy as np 

np.random.seed(42)
num_of_std=8

ids=np.arange(101, 101+num_of_std)

names=np.array([f"student{i}" for i in range(1, num_of_std)])

departments=np.random.choice(["SE", "CS", "AI", "CE"], size=num_of_std)

gender=np.random.choice(["M","F"], size=num_of_std)

marks=np.random.randint(30,101,(num_of_std,5))

attendance=np.random.randint(50,101,num_of_std)


print("Dataset created with shape: ", marks)

#subject wise analytics
subj_avg=np.mean(marks, axis=0)
std_topper=np.max(marks, axis=0)
std_weakest=np.min(marks, axis=0)
print("Average: ", subj_avg)
# print("Topper: ", std_topper)
# print("Weakest: ", std_weakest)

#student wise analytics
avg_marks=np.mean(marks, axis=1)
highest=ids[np.argmax(avg_marks)]
lowest=ids[np.argmin(avg_marks)]
# print(highest)
# print(lowest)
print("Average marks",avg_marks)

#department wise analytics
for dept in np.unique(departments):
    dept_mask=departments==dept
    dept_avg=np.mean(avg_marks[dept_mask])
    print(f"department{dept} Avg marks:", dept_avg)

#gender wise performance
for g in np.unique(gender):
    g_mask=gender==g
    g_avg=np.mean(avg_marks[g_mask])
    print(f"Gender:{g} Avg Marks: ", g_avg)


#advanced filtering
failing_std = ids[avg_marks < 50]
star_std = ids[(avg_marks > 85) & (attendance > 90)]
chronic_defaulters=ids[(avg_marks<50) & (attendance<50)]

gpa=(marks/100)*4
stud_gpa=np.mean(gpa,axis=1)

correlation=np.corrcoef(attendance, avg_marks)[0,1]

print("Highest scorer:", highest)
print("lowest scorer:", lowest)
print("Chronic student:", chronic_defaulters)
print("failing student:", failing_std)
print("Star student: ", star_std)
print("Attendance marks correlation", correlation)