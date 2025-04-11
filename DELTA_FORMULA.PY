#-----------دریافت بخش های معادله درجه دوم---------------
a = int(input('PLEASE INTER THE FIRST ELEMENT:'))
b = int(input('PLEASE INTER THE SECOND ELEMENT:'))
c = int(input('PLEASE INTER THE THIRD ELEMENT:'))
#-----------------------فرمول دلتا-----------------------
delta_formula = (b**2) - (4*a*c)
print('delta_formula='+str(delta_formula))
#---دستور شرط برای تشخیص حقیقی یا موهومی بودن جواب فرمول دلتا---
y = 0
if delta_formula > y:
    print('THE ROOTS OF THE'+' '+str(b)+'**2-4*'+str(a)+'*'+str(c)+' '+'IS REAL')
else:
    print('THE ROOTS OF THE'+' '+str(b)+'**2-4*'+str(a)+'*'+str(c)+' '+'IS NOT REAL')
#--------------------------------------------------------------------------------------