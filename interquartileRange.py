import math
def iqr(n,elements,frequency):
    s=[]
    x=0
    a=0
    q1=0
    for i in range(len(frequency)):
        s += [elements[i]] * frequency[i]
    s=sorted(s)
    x=len(s)/2
    if(x%2==0):
        aa=s[0:int(x)]
        bb=s[int(x):int(len(s))]
        a=(x+1)/2
        frac,whole=math.modf(a)
        whole=int(whole-1)
        q1=s[whole] + (frac * (s[whole+1]-s[whole]))
        b=len(bb)/2
        frac1,whole1=math.modf(b)
        whole1=int(whole1-1)
        q3=bb[whole1] + (frac1 * (bb[whole1+1]-bb[whole1]))
    else:
        aa=s[0:int(x)]
        bb=s[int(x):int(len(s))]
        a=(x+1)/2
        frac,whole=math.modf(a)
        whole=int(whole-1)
        q1=s[whole] + (frac * (s[whole+1]-s[whole]))
        b=int(len(bb)/2)
        frac1,whole1=math.modf(b)
        whole1=int(whole1-1)
        q3=bb[b]
        print("Quartile 1 : ",int(q1))
        print("Quartile 3 : ",q3)

    return q3-q1

n = 15
number = [10,40,30,50,20]
freq = [1,2,3,4,5]
print("Interquartile Range : ",iqr(n,number,freq))
