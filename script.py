"""
Float Decomposition Algorithm, conceived and implemented by: ALAOUI Mehdi 2013
Code reviewed/cleaned: 2016

"""
def PositiveValueOf(INPUT):
    if(INPUT>0):
        return(INPUT)
    else:
        return(-INPUT)

def DefinePrecisionFor(INPUT):
    INPUT=str(INPUT)
    if(len(INPUT)-2<8):
        return(len(INPUT)-3)
    else:
        return(5)




FLOAT_INPUT=float(input("Enter the number to be decomposed:"))
N=int(str(FLOAT_INPUT).split(".")[0])
FLOATING_NUMBER=PositiveValueOf(FLOAT_INPUT- N)
PRECISION=DefinePrecisionFor(PositiveValueOf(FLOATING_NUMBER)) #Precision is length of the floating number

(P,Q)=(0,1) 

while( PositiveValueOf( (FLOATING_NUMBER) - (P/Q) )> 10**(-PRECISION) ):

    if(Q%2!=0):
        (P,Q)=(1,Q+1)
        while( PositiveValueOf( (FLOATING_NUMBER) - (P / Q) )>10**(-PRECISION) and P<Q ):
            P+=2

    else:
        (P,Q)=(0,Q+1)
        while( PositiveValueOf( (FLOATING_NUMBER)-(P / Q) )>10**(-PRECISION) and P<Q ):
            P+=1

print(FLOAT_INPUT,"=",N,((("+" if N>=0 else "-")+str(P)+"/"+str(Q)) if P!=0 else ""))

