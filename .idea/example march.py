temperature=input('Enter Temperature:')
if(int(temperature)>=50):
    print('I am here')
    print('hot')
if(int(temperature)>=30 and int(temperature)<=49):
    print('Warm')
if(int(temperature)<=29):
    print('Cold')

#90-A
#80-B
#70-C
#60-D



score=input ('enter score:')
if (int(score)==90):
     print ('A')
if (int(score)==80):
     print('B')

#50-60-F
#60-70-C
#70-80-B
#80-90-A
score= input('enter score:')
if(int(score)>=80 and int(score)<=90):
    print('A')
if(int(score)>=70 and int(score)<=80):
    print('B')
if(int(score)>=60 and int(score)<=70):
    print('C')