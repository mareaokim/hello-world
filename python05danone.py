
def main():
    day = int(input("Day number 를 입력하시오 : "))
    month =int(input("month number 를 입력하시오 : ")) 
    year = int(input("year number 를 입력하시오 : ")) 



    date1 = "{0}/{1}/{2}".format(month,day,year)

    months =  ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    date2 = "{0} {1} {2}".format(months[month-1],day,year)

    print("The date is {0} or {1}.".format(date1,date2))


main()