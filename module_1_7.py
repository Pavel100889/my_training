grades=[[4,3,4,5],[3,4,2,5],[4,3,5,2],[3,3,4,2]]
students={'Max','Anna','Denis','Adam'}
students1 =sorted(students)
grades1=[sum(grades[0])/len(grades[0]),sum(grades[1])/len(grades[1]),sum(grades[2])/len(grades[2]),sum(grades[3])/len(grades[3])]
list={students1[0]:grades1[0],students1[1]:grades1[1],students1[2]:grades1[2],students1[3]:grades1[3]}
print(list)