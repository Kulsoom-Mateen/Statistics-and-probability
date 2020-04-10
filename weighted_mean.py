def weighted_mean(a,arr1,arr2):
    sum1=0
    sum2=0
    for i in range(len(arr1)):
        sum1=sum1+(arr1[i]*arr2[i])
    for j in arr2:
        sum2=sum2+j

    return round(float(sum1/sum2),1)


n = 10
number1 = [32,64,23,65,3,67,34,99,12,34]
number2 = [1,4,2,4,75,8,5,3,34,8]

print("Weighted mean : ",weighted_mean(n,number1,number2))
