class Syntaxer (object):
    def __init__(self, *arg):
        self.lexemes = arg
        # print('arg = ', arg)

    # statemenize method - create statement list from lexemes
    def syntaxer(self):
        lexemes = list(self.lexemes[0])
        begin = 0
        resultlist = []

        print('len(lexemes) = ', len(lexemes))


        
        while begin < len(lexemes) and begin >= 0:

            isCheck, result, newBegin = checkAllRules(lexemes, begin)

            print('Returned from CheckAllRules')

            resultlist.append(result)
            print('isCheck = ', isCheck)
            for i in result:
                print(i)
           
            begin = newBegin
            print('\n\n')


        print('Done with all Lexemes')
        return resultlist
     

# ==============================================
# End class here
# ==============================================

def checkAllRules(arg, begin):
    count = begin
    availableLen = len(arg) - begin
    print('availableLen = ', availableLen)

    #This returns the next semicolon position so that you can tell where to end
    #print("Begin value")
    print(begin)
    semicolkey,semicolval,semicolpos = getSpecificKV(arg,";",begin)
    templist = arg[begin:semicolpos+1]

    print("++++++++++++++++++++templist++++++++++++++++")
    print(templist)
    print("++++++++++++++++++++++++++++++++++++++++++++")

    #testkey,testval,testpos = getSpecificKVreverse(arg,"+",semicolpos)

    #print("isDeclarative Check in CheckAllRules")
    if len(templist) == 3:

        #print("Going into isDeclarative CheckAllRules")
        isDeclare, resultDeclare = isDeclarative (templist)
        #print("Return from isDeclarative in CheckAllRules")

        if isDeclare:
            count = begin + 3
            return isDeclare, resultDeclare, count

    eqkey,eqval,eqpos = getSpecificKV(templist,"=",0)
    
    #print("isAssign Check in CheckAllRules")
    if eqval == "=":
    
        #print("Going into isAssign in CheckAllRules")
        isAss, resultAssign, AddCount = isAssign (templist)
        #print("Return from isAssign in CheckAllRules")

        if isAss:
            count += AddCount
            return isAss, resultAssign, count

    #print("Going into isExpress in CheckAllRules")
    isExp, resultExpress, AddCount,newpos = isExpress(templist,0)
    #print("Return from isExpress in CheckAllRules")

    if isExp:
        count += AddCount
        return isExp,resultExpress,count

    #print('End of CheckAllRules')
    return False,[],-1

def getKeyValue (mydict):
    for key, value in mydict.items():
        return key, value

def getSpecificKV (arg,myvalue,beginval):
    positionval = beginval
    for x in arg[beginval:]:   
        for key,value in x.items():
            # print("Next in specific function")
            # print(key,value,positionval)
            # print("++++++++++++++++++++++++++++++++++++++")
            if value == myvalue :
                #print("Match in specific function")
                #print(key,value,positionval)
                #print("++++++++++++++++++++++++++++++++++++++")
                return key,value,positionval
        positionval = positionval + 1
    #print("Could not find the specific key/value")
    return None,None,9999999999

#<Statement> -> <Declarative>
#<Declarative> -> <Type> <id>;
def isDeclarative (arg):
    myType = ['int', 'float', 'bool']
    #print('Inside isDeclarative')

    key0, value0 = getKeyValue(arg[0])
    key1, value1 = getKeyValue(arg[1])
    key2, value2 = getKeyValue(arg[2])

    if (value0 in myType) and key1 == 'IDENTIFIER' and value2 == ';':
        result = []
        result.append( {
            'Token': key0,
            'Lexeme': value0,
            'Grammar': '<Statement> -> <Declarative>' 
                        '<Declarative> -> <Type> <id>;'
         })
        result.append({            
            'Token': key1,
            'Lexeme': value1,
            'Grammar': '<Statement> -> <Declarative>' 
                        '<Declarative> -> <Type> <id>;'
            })
        result.append({            
            'Token': key2,
            'Lexeme': value2,
            'Grammar': '<Statement> -> <Declarative>' 
                        '<Declarative> -> <Type> <id>;'
            })
        return True, result
    else:
        return False, -1, 999999999999
  

#<Statement> -> <Assign>
#<Assign> -> <ID> = <Expression>;
def isAssign(arg):
    #print("Inside Assign")

    count = 0
    key0, value0 = getKeyValue(arg[0])
    key1, value1 = getKeyValue(arg[1])
    key2, value2 = getKeyValue(arg[len(arg)-1]) 
    

    #print("Going into Assign check")
    #print(key0,value1)
    if key0 == 'IDENTIFIER' and value1 == '=':
        result = []
        result.append( {
            'Token': key0,
            'Lexeme': value0,
            'Grammar': '<Statement> -> <Assign>' 
                        '<Assign> -> <ID> = <Expression>;'

            })
        result.append({            
            'Token': key1,
            'Lexeme': value1,
            'Grammar': '<Statement> -> <Assign>' 
                        '<Assign> -> <ID> = <Expression>;'
            })
        count += 2
        #print("Going into isExpress from isAssign")
        isExp, resultExpress, AddCount,newpos = isExpress (arg,2)
        #print("Return from isExpress in isAssign")

        if isExp:
            count = count + AddCount + 1
            result.extend(resultExpress)
            result.append({            
                'Token': key2,
                'Lexeme': value2,
                'Grammar': '<Statement> -> <Assign>' 
                            '<<Assign> -> <ID> = <Expression>;'
                })
        else:
            print('Assign Error 1 at lexeme ', count)

        


        return isExp, result, count
    else:
        print('Assign Error 2 at lexeme ', count)
        return False, -1, 999999999999

#<Expression> -> <Expression> + <Term> | <Expression> - <Term> | <Term>
def isExpress(arg,posval):
    #print("Inside Expression")

    count = 0

    isresult = False
    
    result = []

    lastpos = posval

    # print("printing the current arg and posval")
    # print(arg[posval])
    # print("after printing the current arg and posval")

    #print("Going into isTerm")
    isTe, resultTerm, AddCount ,newpos= isTerm (arg,posval)
    #print("Return from isTerm in isExpress")

    # print("printing the current arg and posval")
    # print(arg[newpos])
    # print("after printing the current arg and posval")
        
    if isTe:
        lastpos = newpos
        isresult = isTe
        count += AddCount
        result.extend(resultTerm)
    else:
        print('Expression Error 1 at lexeme ', posval)


    
    # print("printing the current arg and posval")
    # print(arg[lastpos])
    # print("after printing the current arg and posval")

    #print("Going into isExpressPrime")
    isExp, resultExpress, AddCount,newpos = isExpressPrime (arg, lastpos)
    #print("Return from isExpressPrime in isExpress")

    # print("printing the current arg and posval")
    # print(arg[newpos])
    # print("after printing the current arg and posval")
        
    if isExp:
        lastpos = newpos
        isresult = isExp
        result.extend(resultExpress)
        count += AddCount
    else:
        print('Expression Error 2 at lexeme ', lastpos)

    if isresult:
        return isresult,result,count,lastpos
        
def isExpressPrime(arg,posval):
    #print("Inside isExpressPrime")
    count = 0
    result = []
    isresult = False
    lastpos = posval
    
    pkey,pvalue,pluspos = getSpecificKV(arg,'+',posval)
    mkey,mvalue, minuspos = getSpecificKV(arg,'-',posval)

    # print("printing the current arg and posval")
    # print(arg[posval])
    # print("after printing the current arg and posval")
    if pvalue == '+' and pluspos < minuspos:
        #print("Inside Express + appending to result")

        result.append( {
            'Token': pkey,
            'Lexeme': pvalue,
            'Grammar': '<Expression> -> <Expression> + <Term> | <Expression> - <Term> | <Term>'
        })
        #the +1 is to account for the append
        count += 1

        #print("Inside ExpressPrime + going into Term")
        isTe, resultTerm, AddCount,newpos = isTerm (arg,lastpos+1)
        #print("Return isTerm in isExpressPrime +")
        #print(newpos)
        if isTe:
            lastpos = newpos
            isresult = isTe
            count += AddCount
            result.extend(resultTerm)
        else:
            print('ExpressionPrime Error 1 at lexeme ', lastpos)

        #print("Inside ExpressPrime + going into ExpressPrime")
        isExp, resultExpress, AddCount,newpos = isExpressPrime (arg, lastpos)
        #print("Return from isExpressPrime in isExpressPrime +")
        
        if isExp:
            lastpos = newpos
            isresult = isExp
            result.extend(resultExpress)
            count += AddCount
        else:
            print('ExpressionPrime Error 2 at lexeme ', lastpos)
        

    mkey,mvalue, minuspos = getSpecificKV(arg,'-',lastpos)
    if mvalue == '-' and minuspos < pluspos:
        #print("Inside Express - appending to result")

        result.append( {
            'Token': mkey,
            'Lexeme': mvalue,
            'Grammar': '<Expression> -> <Expression> + <Term> | <Expression> - <Term> | <Term>'
        })
        
        #the +1 is to account for the append
        count += 1
        
        #print("Inside ExpressPrime - going into Term")
        isTe, resultTerm, AddCount,newpos = isTerm (arg,lastpos+1)
        #print("Return from isTerm in isExpressPrime -")
        
        if isTe:
            lastpos = newpos
            isresult = isTe
            count += AddCount
            result.extend(resultTerm)
        else:
            print('ExpressionPrime Error 3 at lexeme ', lastpos)

        #print("Inside ExpressPrime + going into ExpressPrime")
        isExp, resultExpress, AddCount,newpos = isExpressPrime (arg, lastpos)
        #print("Return from isExpressPrime in isExpressPrime -")
        
        if isExp:
            lastpos = newpos
            isresult = isExp
            result.extend(resultExpress)
            count += AddCount
        else:
            print('ExpressionPrime Error 4 at lexeme ', lastpos)

    #print("ExpressPrime Epsilon Check")
    #print(pvalue,mvalue)
    if pvalue == None and mvalue == None:
        #print("Inside ExpressPrime Epsilon")
        #This does nothing really it just returns whatever it found which should be nothing

        return True,result,count,lastpos
        
    #print("ExpressPrime final Check")
    if isresult:
        return isresult,result,count,lastpos

#<Term> -> <Term> * <Factor> | <Term> / <Factor> | <Factor>
def isTerm(arg,posval):
    #print('Inside isTerm')


    count = 0

    isresult = False
    
    result = []

    lastpos = posval

    # print("printing the current arg and posval")
    # print(arg[posval])
    # print("after printing the current arg and posval")

    #print("Going into isFactor inside isTerm")
    isFac, resultFac, AddCount,newpos = isFactor (arg,posval)
    #print("Return from isFactor in isTerm")

    # print("printing the current arg and posval")
    # print(arg[newpos])
    # print("after printing the current arg and posval")
        
    if isFac:
        lastpos = newpos
        isresult = isFac
        count += AddCount
        result.extend(resultFac)
    else:
        print('Term Error 1 at lexeme ', posval)


    # print("printing the current arg and posval")
    # print(arg[lastpos])
    # print("after printing the current arg and posval")

    #print("Going into isTermPrime inside isTerm")
    isTe, resultTerm, AddCount,newpos = isTermPrime (arg,lastpos)
    #print("Return from isTermPrime inside isTerm")

    # print("printing the current arg and posval")
    # print(arg[newpos])
    # print("after printing the current arg and posval")
        
    if isTe:
        lastpos = newpos
        isresult = isTe
        count += AddCount
        result.extend(resultTerm)
    else:
        print('Term Error 2 at lexeme ',lastpos)

    if isresult:
        return isresult,result,count,lastpos
        

def isTermPrime(arg,posval):
    #print("Inside isTermPrime")

    count = 0

    result = []

    isresult = False

    lastpos = posval
    
    # print("printing the current arg and posval")
    # print(arg[posval])
    # print("after printing the current arg and posval")

    skey,svalue,starpos = getSpecificKV(arg,'*',posval)
    dkey,dvalue, divpos = getSpecificKV(arg,'/',posval)

    if svalue == '*' and starpos < divpos:
        #print("Inside isTermPrime * appending")

        result.append( {
            'Token': skey,
            'Lexeme': svalue,
            'Grammar': '<Term> -> <Term> * <Factor> | <Term> / <Factor> | <Factor>'

            })
        #the +1 is to account for the append
        count += 1

        #print("Inside isTermPrime going into isFactor in *")
        isFac, resultFac, AddCount,newpos = isFactor (arg,lastpos+1)
        #print("Return from isFactor in isTermPrime *")
        
        if isFac:
            lastpos = newpos
            isresult = isFac
            count += AddCount
            result.extend(resultFac)
        else:
            print('TermPrime Error 1 at lexeme ', lastpos)

        #print("Inside isTermPrime going into isTermPrime in *")
        isTe, resultTerm, AddCount,newpos = isTermPrime (arg,lastpos)
        #print("Return from isTermPrime in isTermPrime *")
        
        if isTe:
            lastpos = newpos
            isresult = isTe
            count += AddCount
            result.extend(resultTerm)

        else:
            print('TermPrime Error 2 at lexeme ', lastpos)

    dkey,dvalue, divpos = getSpecificKV(arg,'/',lastpos)
    if dvalue == '/' and divpos < starpos:
        #print("Inside isTermPrime / appending")

        result.append( {
            'Token': dkey,
            'Lexeme': dvalue,
            'Grammar': '<Term> -> <Term> * <Factor> | <Term> / <Factor> | <Factor>'

            })
        #the +1 is to account for the append
        count += 1
        #print("Inside isTermPrime going into isFactor in /")
        isFac, resultFac, AddCount,newpos = isFactor (arg,lastpos+1)
        #print("Return from isFactor in isTermPrime /")
        
        if isFac:
            lastpos = newpos
            isresult = isFac
            count += AddCount
            result.extend(resultFac)
        else:
            print('TermPrime Error 3 at lexeme ', lastpos)

        #print("Inside isTermPrime going into isTermPrime in /")
        isTe, resultTerm, AddCount,newpos = isTermPrime (arg,lastpos)
        #print("Return from isTermPrime in isTermPRime /")
        
        if isTe:
            lastpos = newpos
            isresult = isTe
            count += AddCount
            result.extend(resultTerm)

        else:
            print('TermPrime Error 4 at lexeme ', lastpos)

    if svalue == None and dvalue == None:
        #print("Inside TermPrime Epsilon")
        #This does nothing really it just returns whatever it found which should be nothing

        return True,result,count,lastpos

    if isresult:
        return isresult,result,count,lastpos

#<Factor> -> ( <Expression> ) | <ID> | <num> 
def isFactor (arg,posval):
    #print('Inside isFactor')

    # print("printing the current arg and posval")
    # print(arg[posval])
    # print("after printing the current arg and posval")


    count = 0

    result = []

    isresult = False

    lastpos = posval

    fkey, fvalue , fpos = getSpecificKV(arg,'(',posval)
    bkey, bvalue , bpos = getSpecificKV(arg,')',posval)

    if fvalue == '(' and bvalue == ')':
        #print("Inside isFactor ( ) appending")

        result.append( {
            'Token': fkey,
            'Lexeme': fvalue,
            'Grammar': '<Factor> -> ( <Expression> ) | <ID> | <num> '

            })
        
        #The plus 2 is to account for both parenthesis
        count += 2

        #print("Inside isFactor ( ) going into isExpress")
        isExp, resultExpress, AddCount,newpos = isExpress (arg, lastpos+1)
        #print("Return from isExpress insdie isFactor")
        
        if isExp:
            lastpos = newpos
            isresult = isExp
            count += AddCount
            result.extend(resultExpress)
        else:
            print('isFactor Error 1 at lexeme ', lastpos)

        result.append({
            'Token': bkey,
            'Lexeme': bvalue,
            'Grammar': '<Factor> -> ( <Expression> ) | <ID> | <num> '

            })


    if fvalue == None and bvalue == None:
        #print("Going into isID from isFactor")
        isIDcheck, resultID, AddCount,newpos = isID (arg,lastpos)
        #print("Return from isID in isFactor")
        
        if isIDcheck:
            lastpos = newpos
            isresult = isIDcheck
            count += AddCount
            result.extend(resultID)
        else:
            print('isFactor Error 2 at lexeme ', lastpos)
    
    if isresult:
        return isresult,result,count,lastpos

#<ID> -> id
def isID (arg,posval):
    #print('Inside isID')

    result = []
    isresult = False
    count = 0
    lastpos = posval

    #print('Inside isID getting value')
    key, value = getKeyValue(arg[posval])
    #print('Inside isID key is @@@@@ '+key+' @@@@@ Value is @@@@@ '+value+' @@@@@@@')
    
    #print('Inside isID check key')   
    if key == 'IDENTIFIER' or key == 'KEYWORD' or key == 'FLOAT' or key == 'INT':
        #print('Inside isID check key was true') 
        isresult = True
        lastpos += 1
        result.append( {
                'Token': key,
                'Lexeme': value,
                'Grammar': '<ID> -> id'
            })
        count = count + 1

    #print('Inside isID returning result')
    if isresult:
        return isresult,result,count,lastpos
