

def menu():
    print("------ OPERACIONES -----------" +"\n"+
        "Solo es valido suma, resta, multipicacion, division, "+
        "potenciacion y logaritmacion\n\n")

    selection = input("Ingrese su operacion: ")
    print("\n------------------------------------\n\n")
    return selection if len(selection) > 0 else " "

def typeOfOperation(op):
    op = str(op).strip()
    ret = ""

    for a in op:
        if(a == "+"):
            ret = "suma"
        elif(a == "-"):
            ret = "resta"
        elif(a == "*"):
            ret = "mult"
        elif(a == "/"):
            ret = "divi"
        elif(a == "^"):
            ret = "pote"
        elif(a == "l"):
            ret = "l"
        
    if(len(ret) == 0):
        return None

    return ret






























#

def a(op):

    error = False
    num1 = ""
    num2 = ""
    set_ = True 

    for a in op:
        if(a == "+"):
            ret = "suma"
            set_ = False 
        elif():
            ret = "resta"
            set_ = False
        elif():
            ret = "mult"
            set_ = False
        elif(a == "/"):
            ret = "divi"
            set_ = False
        elif(a == "^"):
            ret = "pote"
            set_ = False
        elif(a == "log"):
            ret = "log"
        
        elif(a.isalpha()):
            error = True
        
        elif(set_):
            num1 += num1
        else:
            num2 += num2
        

    if(len(ret) == 0):
        return None

    #if(len(num1) == 0 or len(num2) == 0 or error):
        #return "Operacion no valida", None, None

    return ret