import datetime as dt
current_data=dt.date.today()
print(current_data)

new = dt.date(2022,5,5)
print(new)
print("year :",new.year)
print("Month :",new.month)
print("date :",new.day)

#Time
a=dt.time(10,55,3,444)
print(a)
print("hour:",a.hour)
print("minute:",a.minute)
print("second:",a.second)
print("microsecond:",a.microsecond)

#current time
m=dt.datetime.now()
print(m)

#diffrent find out
current=dt.datetime.now()
new_year=dt.datetime(2024,1,27,)
diffrent=new_year-current
print(diffrent)

s=current.strftime("%A: " "%B:" "%d:" "%Y:")
print(s)