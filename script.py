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

"""
Program that decomposes a float F into: N + (P / Q)

N,P,Q integers & P<Q

"""


FLOAT_INPUT=float(input("Enter the number to be decomposed:"))
N=0
POSITIVE_FLOAT_INPUT=PositiveValueOf(FLOAT_INPUT) #if Float_Input is negative, Positive_Float_Input= - Float_Input
while((POSITIVE_FLOAT_INPUT-N)>1):
    N=N+1

PRECISION=DefinePrecisionFor(PositiveValueOf(POSITIVE_FLOAT_INPUT-N)) #Precision is length of the floating number

(P,Q)=(0,1) 

while( PositiveValueOf( (POSITIVE_FLOAT_INPUT-N) - (P/Q) )> 10**(-PRECISION) ):

    if(Q%2!=0):
        (P,Q)=(1,Q+1)
        while( PositiveValueOf( (POSITIVE_FLOAT_INPUT - N) - (P / Q) )>10**(-PRECISION) and P<Q ):
            P+=2

    else:
        (P,Q)=(0,Q+1)
        while( PositiveValueOf( (POSITIVE_FLOAT_INPUT - N)-(P / Q) )>10**(-PRECISION) and P<Q ):
            P+=1

if(FLOAT_INPUT>0):
    print(FLOAT_INPUT,"=",N,"+",P,"/",Q)
else:
    print(FLOAT_INPUT,"=",-N,"-",P,"/",Q)
