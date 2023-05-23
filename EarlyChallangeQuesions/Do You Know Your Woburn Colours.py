c1=input()
c2=input()
if (c1== 'BLUE' and c2=='WHITE') or (c1=='WHITE' and c2== 'BLUE'):
    print('RED')
elif (c1== 'BLUE' and c2=='RED') or (c1=='RED' and c2=='BLUE'):
    print('WHITE')
elif (c1=='WHITE' and c2=='RED') or (c1=='RED' and c2=='WHITE'):
    print('BLUE')
