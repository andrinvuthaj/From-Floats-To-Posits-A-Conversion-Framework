from decimal import Decimal#avoid rounding
#to avoid unnecessary rounding
from tabulate import tabulate

from decimal import *
getcontext().prec = 28000000000


# (-1)^sign x useed^k x 2^exp x (1+f)
#useed = 2^2^es
the_bits = 64
es = 2

useed = 2**(2**es)
k = 3#default at highest value
#print(useed)
#==================Definitions+=================
sign = 0


the_input = input("Type the number: ")
decimal = float(the_input)
#print("thefirst", Decimal(decimal))
#sign bit
if decimal>=0:
    sign_bit = "0"

else:
    sign_bit = "1"
    decimal = abs(decimal)

#regimebits
regime_bits = ""
#exponent - default to 0,size 2 bc of es=2
exp = "00"
exponent = 0
#fraction
frac = ""
fraction = 0
fraction_exp = -1




#==================================regime bits

to_regime_value = useed**k
if useed**k <= abs(decimal):
    regime_bits = "1111"
elif useed**(k-1) <= abs(decimal):
    regime_bits = "1110"
    k-=1# if we need to use it later it has the exact value
    to_regime_value = useed**k
elif useed**(k-2) <= abs(decimal):
    regime_bits = "110"
    k-=2# if we need to use it later it has the exact value
    to_regime_value = useed**k
elif useed**(k-3) <= abs(decimal):
    regime_bits = "10"
    k-=3# if we need to use it later it has the exact value
    to_regime_value = useed**k
elif useed**(k-4) <= abs(decimal):
    regime_bits = "01"
    k-=4# if we need to use it later it has the exact value
    to_regime_value = useed**k
elif useed**(k-5) <= abs(decimal):#k= -2
    regime_bits = "001"
    k-=5# if we need to use it later it has the exact value
    to_regime_value = useed**k
elif useed**(k-6) <= abs(decimal):#k= -3
    regime_bits = "0001"
    k-=6# if we need to use it later it has the exact value
    to_regime_value = useed**k
elif useed**(k-7) <= abs(decimal):#k= -4
    regime_bits = "0000"
    k-=7# if we need to use it later it has the exact value
    to_regime_value = useed**k


print(to_regime_value)


#==========finding the exponent====
if decimal/to_regime_value >=2:
    if 1<=decimal/(to_regime_value*(2**(exponent+1))) < 2:
        exp = "01"#update the exp
        
        remainder = (decimal/(to_regime_value*(2**(exponent+1))))-1#get the remainder
        exponent +=1#update the exponent value for later usage
    elif 1<=decimal/(to_regime_value*(2**(exponent+2))) < 2:
        exp = "10"
        
        remainder = (decimal/(to_regime_value*(2**(exponent+2))))-1
        exponent +=2
    elif 1<=decimal/(to_regime_value*(2**(exponent+3))) < 2:
        exp = "11"
        
        remainder = (decimal/(to_regime_value*(2**(exponent+3))))-1
        exponent +=3
    else:
        exp = "11"
        remainder = (decimal/to_regime_value)-1
else:
    remainder = (decimal/to_regime_value)-1


#print(exp)
#print(exponent)
print(remainder)



#============================finding the fractiion
current_posit = sign_bit+regime_bits+exp
length = len(current_posit)
run = True

for i in range(the_bits-length):

    if remainder>(fraction+(2**fraction_exp)):
        fraction +=(2**fraction_exp)
        fraction_exp -=1
        frac+="1"
    elif remainder==(fraction+(2**fraction_exp)):
        fraction +=(2**fraction_exp)
        fraction_exp -=1
        frac+="1"
        for j in range(the_bits-length-i-1):
            frac += "0"
        break
    elif remainder<(fraction+(2**fraction_exp)):
        #fraction +=(2**fraction_exp), because in this case we do not add the value to it
        fraction_exp -=1# we still need to check for smalled values
        frac+="0"#we add zero to the fraction bits
    #print(fraction)

    
final_posit = current_posit+frac
print("Decimal to binary:", final_posit)


#print(len(final_posit))







#========================================================================================================================



#posit_input_2es = (input("Input the Posit 2es: "))
posit_input_2es = final_posit

def table_convertor(in_posit, es, bits):
        #es-expnent size
    #useed - (2^2)^es
    # ====================== signbit * useed^k *2^exponent*fraction
    # Let m be the number of identical bits in the run; if the bits are 0, then k = −m; if they are 1, then k = m − 1
    
    #taking outs spaces
    posit = ''
    for i in range(len(in_posit)-1):
            if in_posit[i] == " " or in_posit[i] == "|":
                pass
            else:
                posit += in_posit[i]



    #es =int(float(input("input the es value: ")))
    useed = (2)**(2**es)
    #print(useed)

    sign_bit = posit[0]
    if sign_bit =='0':
        sign = 1
    else:
        sign = -1


    regime = posit[1:5]

    if regime == '0000':
        n=5#last regime is a position5
        
        k =-4
    elif regime == '0001':
        n=5#last regime is a position5
        
        k=-3
    elif regime == '001' or regime == '0010' or regime == '0011':#add the other to check for 4
        n =4
        
        k =-2
    elif regime == '01' or regime =='0100' or regime =='0111' or regime == '0110' or regime == '0101':
        n =3
        
        k =-1
    elif regime == '10' or regime == '1000' or regime == '1010' or regime == '1011' or regime =='1001':
        n =3
        
        k =0
    elif regime == '110'or regime =='1100' or regime == '1101':
        n =4
        
        k =1
    elif regime == '1110':
        n =5
        
        k =2
        
    elif regime == '1111':
        n=5
        k =3

    regime = posit[1:n]
    #print(regime)
    exponent = posit[n:n+es]
    #print(exponent)
    fraction = posit[n+es:bits+1]
    #print(fraction)


    #print(f'{sign_bit} {regime} {exponent} {fraction}')
    def value_binary(exponent):
        int_version = int(exponent)
        counter = len(exponent)
        summation = 0
        for i in exponent:
            i = int(i)
            
            added = i*(2**(counter-1))
            counter -=1
            summation += added
        #print(summation)
        return summation

    #print(value_binary('111'))

    def value_fraction(fraction):
        length = len(fraction)
        counter = length
        summ = 0
        reversed_fraction =fraction[::-1]
        #print(reversed_fraction)
        for i in reversed_fraction:
            i =int(i)

            added = i*(2**(-counter))
            counter -=1
            #print(added)
            summ += added

        #print(summ)
        return summ

    #value_fraction('0111001000100110')
    #print(value_binary('101'))
    def evaluate(signbit,k, exponent, fraction):
        #print(f'{signbit} {k} {exponent} {fraction}')
        exponent = value_binary(exponent)
        #print(useed)
        #print(exponent)
        fraction = value_fraction(fraction)
        #print(fraction)
        #print(k)
        result = signbit*((useed)**k)*(2**exponent)*(1+fraction)
        return result
    answer = evaluate(sign,k, exponent, fraction)
    return answer
    


posit642 = table_convertor(posit_input_2es,es,the_bits)


print("Binary to decimal part:",posit642)



#========================================ERROR if present=======================

#posit642 = Decimal(posit642)
#decimal = Decimal(decimal)
if final_posit == posit642:
    print("EXACT!!")
else:
    error = decimal-posit642
    #error = abs(posit642)-abs(decimal)
    #error = Decimal(error)
    print("ERROR is: ",error)

str_decimal = str(decimal)
str_posit642 = str(posit642)
final_error =""
#if  len(the_input)> len(str_posit642):

for i in range(0,len(the_input)):
    if the_input[i] == ".":
        final_error += "."
    elif i>= len(str_posit642):
        current = abs(int(the_input[i]) - 0)
        str_current = str(current)
        final_error += str_current
    else:
        current = abs(int(the_input[i]) - int(str_posit642[i]))
        str_current = str(current)
        final_error += str_current
'''else:
    for i in range(0,len(the_input)):
        if str_posit642[i] == ".":
            final_error += "."
        elif i>= len(the_input):
            current = int(str_posit642[i]) - 0
            str_current = str(current)
            final_error += str_current
        else:
            current = int(str_posit642[i]) - int(the_input[i])
            str_current = str(current)
            final_error += str_current'''
'''# Function for converting decimal to binary
def float_bin(my_number, places = 3):
    my_whole, my_dec = my_number.split(".")
    my_whole = int(my_whole)
    res = (str(bin(my_whole))+".").replace('0b','')
 
    for x in range(places):
        my_dec = str('0.')+str(my_dec)
        temp = '%1.20f' %(float(my_dec)*2)
        my_whole, my_dec = temp.split(".")
        res += my_whole
    return res
print("IEEE return", float_bin(the_input))'''
#print("string input", str_decimal)
print("unrounded",final_error)