""" Este módulo contiene las siguientes funciones destinadas a la validación de variables """
""" 1) valInt()
    2) valFloat()
    3) valComplex()
    4) valList() """
    
def valInt(*var):    #Validacion de datos de tipo entero. valInt(int,list/tuple).
    if len(var)==1:
        result=print(type(var[0])==int)
    else:
        if type(var[1])==list or type(var[1])==tuple:
            if var[1][0]>var[1][1] or len(var[1])>2:
                result=print("ValueError")
            elif type(var[1])==tuple:
                result=print(var[0]<var[1][1] and var[0]>var[1][0])
            else:
                result=print(var[0]<=var[1][1] and var[0]>=var[1][0])
        else:
            result=print("TypeError")
    return result



def valFloat(*var):    #Validacion de datos tipo flotantes. valFloat(float,list/tuple).
    if len(var)==1:
        result=print(type(var[0])==float)
    else:
        if type(var[1])==list or type(var[1])==tuple:
            if var[1][0]>var[1][1] or len(var[1])>2:
                result=print("ValueError")
            elif type(var[1])==tuple:
                result=print(var[0]<var[1][1] and var[0]>var[1][0])
            else:
                result=print(var[0]<=var[1][1] and var[0]>=var[1][0])
        else:
            result=print("TypeError")
    return result



def valComplex(*var):    #Validacion de datos de tipo complejos. valComplex(complex,list/tuple).
    if len(var)==1:
        result=print(type(var[0])==complex)
    else:
        if type(var[1])==list or type(var[1])==tuple:
            if var[1][0]>var[1][1] or len(var[1])>2:
                result=print("ValueError")
            elif type(var[1])==tuple:
                result=print(abs(var[0])<var[1][1] and abs(var[0])>var[1][0])
            else:
                result=print(abs(var[0])<=var[1][1] and abs(var[0])>=var[1][0])
        else:
            result=print("TypeError")
    return result  



def valList(*var):    #Validacion de datos tipo lista. valList(list,list/int,len/value)
    if len(var)==3:
        if type(var[2])==str and (type(var[1])==int or type(var[1])==list):
            if var[2]=="value":
                result=print(type(var[0])==list and type(var[1])==list and var[0]==var[1])
            elif var[2]=="len":
                result=print(type(var[0])==list and type(var[1])==int and len(var[0])==var[1])
            else:
                result=print("ValueError")
        else:
            result=print("TypeError")
    elif len(var)==1:
        result=print(type(var[0])==list)
    return result
        



