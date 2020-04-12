# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
def mean(n,number):
    sum=0
    mean=0
    for i in range(n):
        sum=sum+number[i]
    mean=sum/n
    
    for i in range(len(number)):
        number[i]=number[i]-mean
        number[i]=number[i]*number[i]
    
    new_number=0
    for i in number:
        new_number=new_number+i
    return round(math.sqrt(new_number/n),1)


n = int()
number = [10,40,30,50,20] 
n=5
print("Given list is : ",number)
print("Standard deviation of given list is : ",mean(n,number))