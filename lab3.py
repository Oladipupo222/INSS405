temperature=input('enter temperature:')
if(float(temperature)>50) :
    print('hot')

elif (float(temperature)>=30 and float(temperature)<50):
    print('warm')
elif (float(temperature)>=0 and float(temperature)<30):

    print('cold')
elif (float(temperature)<-20):
    print('extreme chill cold,shelter in place')
