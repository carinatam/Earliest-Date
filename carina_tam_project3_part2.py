#Project 3 Question 3
print("This program will determine the earliest date that appears on the calendar")
print("Enter 0 on all inputs to indicate that no more dates will be entered")
month=int(input("Please enter a date (month): "))
day=int(input("Please enter a date (day): "))
year=int(input("Please enter a date (year): "))
print(month,end="/")#so this will print (month)/
print(day,end="/") #and this will print (day)/
print(year) #so altogether it will print month/day/year
while(month!=0 and day!=0 and year!=0): #until the user indicates that there are no more dates
    month2=int(input("Please enter a date (month): ")) 
    day2=int(input("Please enter a date (day): "))
    year2=int(input("Please enter a date (year): "))
    if(month2==0 and day2==0 and year2==0): #if what the user enters is all 0
        print(month,end="/")
        print(day,end="/")
        print(year,"is the earliest date") #it will print the earliest date
        break #exits
    print(month2,end="/") #if what the user enters isn't 0
    print(day2,end="/")
    print(year2)
    if(year<year2): #if the year is less, then it is earlier than the other date and there is no need to check the month and day
        e_y=year
        e_m=month
        e_d=day
        month2=int(input("Please enter a date (month): ")) #if year2 is bigger, there is no need for it to be there so new line of input
        day2=int(input("Please enter a date (day): "))
        year2=int(input("Please enter a date (year): "))
        print(month2,end="/") #if digits entered are not 0
        print(day2,end="/")
        print(year2)
        if(month2==0 and day2==0 and year2==0): #if the digits entered are 0
            print(e_m,end="/")
            print(e_d,end="/")
            print(e_y,"is the earliest date") #then it will print the earliest date
            break #exit
    if(year2<year): #opposite of step completed above
        e_y=year2
        e_m=month2
        e_d=day2
        month=int(input("Please enter a date (month): "))
        day=int(input("Please enter a date (day): "))
        year=int(input("Please enter a date (year): "))
        print(month,end="/") #if digits entered are not 0
        print(day,end="/")
        print(year)
        if(month==0 and day==0 and year==0): #if digits entered is 0
            print(e_m,end="/")
            print(e_d,end="/")
            print(e_y,"is the earliest date") #it will print the earliest date
            break #exit
        
    if(year==year2): #if the two years are the same
        if(month<month2): #then we will check the month
            e_y=year
            e_m=month
            e_d=day
            month2=int(input("Please enter a date (month): "))
            day2=int(input("Please enter a date (day): "))
            year2=int(input("Please enter a date (year): "))
            if(month2==0 and day2==0 and year2==0): #if inputs is 0
                print(e_m,end="/")
                print(e_d,end="/")
                print(e_y,"is the earliest date") #will print
                break #exit
            print(month2,end="/")
            print(day2,end="/")
            print(year2)
            if(month>month2): #if the date of month is less, then it is earlier
                e_y=year2
                e_m=month2
                e_d=day2
                month=int(input("Please enter a date (month): "))
                day=int(input("Please enter a date (day): "))
                year=int(input("Please enter a date (year): "))
                if(month==0 and day==0 and year==0):
                    print(e_m,end="/")
                    print(e_d,end="/")
                    print(e_y,"is the earliest date")
                    break #exit
                print(month,end="/") #if inputs is not 0
                print(day,end="/")
                print(year)
            if(month2>month): #same concept as above
                e_y=year
                e_m=month
                e_d=day
                month2=int(input("Please enter a date (month): "))
                day2=int(input("Please enter a date (day): "))
                year2=int(input("Please enter a date (year): "))
                if(month2==0 and day2==0 and year2==0): #if the months are the same
                    print(e_m,end="/")
                    print(e_d,end="/")
                    print(e_y,"is the earliest date")
                    break
                print(month2,end="/")
                print(day2,end="/")
                print(year2)
            if(month==month2): #if the months and years are the same
                if(day<day2): #check days
                    e_y=year
                    e_m=month
                    e_d=day
                    month2=int(input("Please enter a date (month): "))
                    day2=int(input("Please enter a date (day): "))
                    year2=int(input("Please enter a date (year): "))
                    if(month2==0 and day2==0 and year2==0):
                        print(e_m,end="/")
                        print(e_d,end="/")
                        print(e_y,"is the earliest date")
                        break
                    print(month2,end="/")
                    print(day2,end="/")
                    print(year2)
                if(day2<day):
                    e_y=year2
                    e_m=month2
                    e_d=day2
                    month=int(input("Please enter a date (month): "))
                    day=int(input("Please enter a date (day): "))
                    year=int(input("Please enter a date (year): "))
                    if(month==0 and day==0 and year==0):
                        print(e_m,end="/")
                        print(e_d,end="/")
                        print(e_y,"is the earliest date")
                        break
                    print(month,end="/")
                    print(day,end="/")
                    print(year)
