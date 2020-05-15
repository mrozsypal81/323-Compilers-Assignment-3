class Syntax_analyzer (object):
    def __init__(self, *arg):
        self.lexemes = arg
        # print('arg = ', arg)

    # statemenize method - create statement list from lexemes
    def syntaxA(self):
        lexemes = list(self.lexemes[0])
        begin = 0
        tablestart = 5000
        resultlist = []

        print('len(lexemes) = ', len(lexemes))


        
        while begin < len(lexemes) and begin >= 0:

            isCheck, result, newBegin,newtablestart = checkAllRules(lexemes, begin,tablestart)

            print('Returned from CheckAllRules')

            resultlist.append(result)
            print('isCheck = ', isCheck)
            for i in result:
                print(i)
           
            begin = newBegin
            tablestart = newtablestart
            print('\n\n')


        print('Done with all Lexemes')
        return resultlist

# ==============================================
# End class here
# ==============================================


def checkAllRules(arg, begin,tablestart):
    count = begin
    tablecount = tablestart
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
