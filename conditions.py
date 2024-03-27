# Conditions

# if <condition>:
#    <statement>

# Note: before the statement in if:
# must have a tab, 2 spaces or 4 spaces

if True:
    print('All true')
  
if False:
    print('All false')
    
b = True
if b:
    print("The value of b must be true")

# + - * / < > <= >= == 

if 2 < 10:
    print('True')

n1 = 2
if n1 < 10:
    print('2 is less than 10 - True')
    
# if <condition>:
#   <statement>
# else:
#   <statement>

if n1 == 7:
    print('n1 is 7')
else:
    print('n1 is NOT 7')
    
# להגדיר משתנה מסוג מחרוזת עם השם שלכם
# בדקו האם המשתנה שווה למחרוזת 'ABC'

n1 = 'Michelle'
if n1 == 'ABC':
    print('Yes')
else:
    print('No')
    
    
#print( 'admin' == 'michelle')
print(False == 0)

#a = False
#b = 0
a = True
b = 1

if a == b:
    print('Equal')
else:
    print('Not equal')