p = float(input('What is your percentage?:  '))

if p >= 90:
    p=p-90 
    if p >= 7:
        letter = 'A+'
    elif p <=3:
        letter = 'A-' 
    else:
        letter = 'A'    
elif p >= 80:
    letter = 'B'
elif p >= 70:
    letter = 'C'
elif p >= 60:
    letter = 'D'
else:
    letter = 'F'

print(f'you got a {letter}')         