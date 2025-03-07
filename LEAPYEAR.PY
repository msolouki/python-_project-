year = int(input('PLEASE ENTER NUMER OF THE YEAR:'))         #دریافت ورودی از کاربر(سال)
if year % 400 == 0 and year % 100 != 0 or year % 4 == 0:       #دستور شرط برای تشخیص سال عدی یا سال کبیسه
    print('THE'+' '+str(year)+' '+'IS THE LEAP YEAR')             # نمایش سال در صورت کیسه بودن
else:
    print('THE'+' '+str(year)+' '+'IS NOT THE LEAP YEAR')        # نمایش سال در صورت کبیسه نبودن
