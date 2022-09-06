if uInput[pos] != "=":  
    print('VALOR:: CLASSE: `SINAL` (TOKEN: %d)' % counter  )
    counter +=1 
    loc["counter"]=counter
    loc["pos"]=pos
else: 
    pos,loc=generic_rule.goTo('E5',uInput,pos,loc)  