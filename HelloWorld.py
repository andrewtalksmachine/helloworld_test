#test this IDE

from datetime import datetime 

today = datetime.today()
time_now = datetime.now()


print "Hello there and welcome to this new app!"
name = raw_input("What is your name? ").lower()
age = int(raw_input("What is your age? "))
year_born = today.year - age 

#print "Today is " + str(today.month) + ' ' + str (today.day) + ' ' + str(today.year) + ' ' + name
print "Hello %s, today is %02d %02d %04d" % (name,today.month, today.day, today.year)
print "Since you are %d years old you were probably born in the year %d" % (age, year_born)


