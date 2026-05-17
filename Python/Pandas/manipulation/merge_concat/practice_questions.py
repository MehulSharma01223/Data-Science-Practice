import pandas as pd
df1 = pd.DataFrame({
    "ID" : [1,2,3] , 
    "Name" : [ "A" , "B" , "C"]
})
df2 = pd.DataFrame({
    "ID" : [1,2,3] , 
    "Course" : [ "Python" , "SQL" , "Pandas"]
})

print(pd.merge(df1 , df2 , on= "ID" ))



students = pd.DataFrame({
    "ID" : [1,2,3 , 4] , 
    "Name" : [ "A" , "B" , "C" , "D"]
})
marks = pd.DataFrame({
    "ID" : [1,2,3] , 
    "Marks" : [ 80 , 90 , 100]
})

result = pd.merge(students , marks ,   how = "left")
print(result)

students = pd.DataFrame({
    "Student_ID" : [1,2,3] , 
    "Name" : ["A" , "B" ,"C"]
})

marks = pd.DataFrame({
    "ID": [1,2,3] ,
    "Marks" : [80 ,90 , 100]
})

result = pd.merge(
    students,
    marks, 
    left_on= "Student_ID",
    right_on= "ID"
)

print(result)