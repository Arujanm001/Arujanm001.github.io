def exercise_2(A):
    b=[]
    for i in range(len(A)):
        if i%2==0:
            b.append(A[i])
    return b
print(exercise_2([10, 3, 4, 5, 9]))
print(exercise_2([9, 0, 12, 3, 4, 56, 9, 16]))