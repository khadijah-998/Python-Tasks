def dolist(list1):
    YorN=input("please enter y if you wont to add task to your to do list if not enter n:  ")
    if YorN=="y":
        count=int(input("enter the number of tasks :   "))
    count2=0
    while(count!=0):
        item=input("enter your task:  ")
        list1.append(item)
        print(" %s"%item)
        count-=1
    
    print(list1)
    YorN=input("please enter y if you wont to remove task from your to do list if not enter n:  ")
    while YorN=="y":
        item=int(input("enter your tasks adress:  "))
        del list1[item]
        YorN=input("please enter y if you wont to remove task from your to do list if not enter n:  ")
    
    print(list1)


li=[]
dolist(li)