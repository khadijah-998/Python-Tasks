li1=[15,20,30,40,50,300,820,450,1,33,80,1150]
larg=0
count=1
while count<len(li1):
    if(li1[count]>=li1[count-1]):
        larg=li1[count]
    count+=1
    


print("the largest number in this list")
print(li1)
print("is %d"%larg)


#other code for the user enter the list then chick for largest number.


li2=[]
num=int(input("please enter length of the list: "))
count=0
while count<num:
    item=int(input("list item : "))
    li2.append(item)
    item=0
    count+=1

larg=0
count2=1
while count2<(num):
    if(li2[count2]>=li2[count2-1]):
        larg=li2[count2]
    count2+=1
    
print("the largest number in this list")
print(li2)
print("is %d"%larg)
