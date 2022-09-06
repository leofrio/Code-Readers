while pos < len(uInput):  
    """ print("current uInput:%s" % uInput[pos]) 
    print("current pos: %d" % pos)
    print("current loc :",end="") 
    print(loc)  """
    #if pos == 41: 
        #print("got here!");
    if uInput[pos] == " ": 
        pos += 1  
        loc["pos"]=pos
    elif uInput[pos] == "%" :  
        pos +=1  
        loc["pos"]=pos
        pos,loc=generic_rule.goTo("E6",uInput,pos,loc)  
        loc["pos"]=pos
    elif uInput[pos] == ":": 
        pos +=1  
        loc["pos"]=pos
        pos,loc=generic_rule.goTo("E4",uInput,pos,loc)
        loc["pos"]=pos 
    elif uInput[pos] in numbers: 
        pos,loc=generic_rule.goTo("E3",uInput,pos,loc)   
        loc["pos"]=pos
    elif uInput[pos] in letters:  
        loc["collected"].append(uInput[pos])
        pos,loc=generic_rule.goTo('E2',uInput,pos,loc)  
        loc["collected"]=[]
        loc["pos"]=pos
        
    else:   
        loc["collected"].append(uInput[pos])  
        pos,loc=generic_rule.goTo("E7",uInput,pos,loc)
        pos += 1   
        loc["pos"]=pos   