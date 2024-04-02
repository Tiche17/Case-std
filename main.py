# Syntiche Tshimanga
#Main.py
# This program determin if a student is qualified for the Dean's  list of Honor roll


last_name = input('Enter a last name (or ZZZ to exit): ') 
while last_name != 'ZZZ' : 
    first_name = input('Enter a first name: ')
    gpa = float (input ('Enter a gpa: ') )
    if gpa >= 3.5: 
        print ('The student has made the Dean list')
    elif gpa >= 3.25:
        print ('The student has made the Honor roll') 
    else :
        print ('The student did not make the Dean list or the Honor roll')
    last_name = input('Enter a name (or ZZZ to exit): ') 
  