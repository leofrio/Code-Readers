possibleWord="" 
originalPos=pos 
while uInput[pos] in numbers or uInput[pos] in letters: 
    possibleWord ="".join(collected) 
    if possibleWord.upper() in reservedWords:        
        print('VALOR:%s CLASSE: PALAVRA RESERVADA(TOKEN: %d)' % (possibleWord,counter))
        counter +=1    
        pos=pos +1
        break
    else: 
        if len(possibleWord) > 6:               
            print('VALOR:%s CLASSE: IDENTIFICADOR(TOKEN: %d)' % (possibleWord,counter)  )
            counter +=1    
            collected=[]
            pos=originalPos +1 
            break
        else:
            if pos+1 < len(uInput):
                hasChance=False 
                for i in reservedWords:  
                    if i.startswith(possibleWord.upper()): 
                        hasChance=True  
                        break
                if hasChance:
                    pos +=1
                    collected.append(uInput[pos]) 
                else:    
                    if uInput[pos+1] == "": 
                        print('VALOR:%s CLASSE: IDENTIFICADOR(TOKEN: %d)' % (possibleWord,counter)  )
                        counter +=1 
                        pos +=1 
                        break;  
                    else: 
                        while  (pos+1) < len(uInput) and uInput[pos+1] != " " and uInput[pos+1] not in signs: 
                            possibleWord += uInput[pos+1] 
                            pos += 1
                        print('VALOR:%s CLASSE: IDENTIFICADOR(TOKEN: %d)' % (possibleWord,counter)  )
                        pos+=1
                        counter +=1   
                        #print("E2 pos: %s" %pos)
                        break;

            else:                  
                print('VALOR:%s CLASSE: IDENTIFICADOR(TOKEN: %d)' % (possibleWord,counter)  )
                counter +=1  
                collected=[]
                pos=originalPos +1 
                break 