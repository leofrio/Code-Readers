fullnum=""
while uInput[pos] in numbers: 
    #print('VALOR:%s CLASSE: NUMERO(TOKEN: %d)' % (uInput[pos],counter)  )
    #counter +=1 
    fullnum += uInput[pos] 
    pos+= 1  
    if pos +1 > len(uInput): 
        break; 
print('VALOR:%s CLASSE: NUMERO(TOKEN: %d)' % (fullnum,counter)  )
counter +=1 