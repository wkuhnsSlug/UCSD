n=100
y=[77234 ,69855 , 63178]
p=0.488
pvf=0.999
def rec(one, two, three,n):
    if n==1:
        print("One " + str(pvf*(p*one+(1-p)*two)) + " Two " + str(pvf*(p*two+(1-p)*three)))
        return 0
    print(one, two , three)
    rec(pvf*(p*one+(1-p)*two),pvf*(p*two+(1-p)*three),pvf*(p*three+(1-p)*0),n-1)