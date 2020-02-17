def exercise_5(X,i):
    for i in range (i,len(X)):
        del X[i:len(X)]
    return X
print (exercise_5([10, 3, 4, 5, 9], 1))
print (exercise_5([9, 0, 12, 3, 4, 56, 9, 16], 7))