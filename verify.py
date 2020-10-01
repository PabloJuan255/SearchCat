usefulthings = [
'cm',
'metros',
'centimetros',
'kg',
'C',
'F',
'c',
'F',
'pounds',
'ounces',
'did you know?',
'lbs'
]

def isuse(x):
 for i in usefulthings:
   print(x,i)
   y = x.split()
   if(i in y):
     break
     return True
   else:
     return None
   print(x)