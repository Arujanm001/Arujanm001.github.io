def exercise_3(X,i):
    y=[]
    for i in range (i, len(X)):
        X[i]=X[i]**2
    return X
print(exercise_3([10, 3, 4, 5, 9], 2))
print(exercise_3([9, 0, 12, 3, 4, 56, 9, 16], 6))