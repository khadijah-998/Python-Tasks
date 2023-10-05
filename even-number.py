
try:
    count=0
    while(count<5):
        num1=int(input("enter intger number: "))
    
        if (num1 %2==0):
            print("right answer it's even number")
        else:
            print("wrong answer it's odd number")
        count+=1
except ValueError:
    print("please inter integer number")