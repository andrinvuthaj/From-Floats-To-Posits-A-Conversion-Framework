from tabulate import tabulate

posit_input_1es = (input("Input the Posit 1es: "))
posit_input_2es = (input("Input the Posit 2es: "))
posit_input_3es = (input("Input the Posit 3es: "))


def table_convertor(posit, es, bits):
        #es-expnent size
    #useed - (2^2)^es
    # ====================== signbit * useed^k *2^exponent*fraction
    # Let m be the number of identical bits in the run; if the bits are 0, then k = −m; if they are 1, then k = m − 1
    
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
    exponent = posit[n:n+es]
    fraction = posit[n+es:bits+1]


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

    def evaluate(signbit,k, exponent, fraction):
        #print(f'{signbit} {k} {exponent} {fraction}')
        exponent = value_binary(exponent)
        #print(useed)
        #print(exponent)
        fraction = value_fraction(fraction)
        #print(fraction)
        result = signbit*((useed)**k)*(2**exponent)*(1+fraction)
        return result
    answer = evaluate(sign,k, exponent, fraction)
    return answer
    

posit81 = table_convertor(posit_input_1es,1,8)
posit82 = table_convertor(posit_input_2es,2,8)
posit83 = table_convertor(posit_input_3es,3,8)
posit161 = table_convertor(posit_input_1es,1,16)
posit162 = table_convertor(posit_input_2es,2,16)
posit163 = table_convertor(posit_input_3es,3,16)
posit321 = table_convertor(posit_input_1es,1,32)
posit322 = table_convertor(posit_input_2es,2,64)
posit323 = table_convertor(posit_input_3es,3,32)

data = [["8",posit81, posit82,posit83],['16', posit161,posit162,posit163],['32',posit321,posit322,posit323]
]
column_names = ['bits/es','1','2','3']
print(tabulate(data, headers = column_names))

table1 = [" bits/es", "1", '            2', '         3']
table2 = ['8', f'   {posit81}', f'      {posit82}',f'            {posit83}']
table3 = ['16', f'  {posit161}', f'     {posit162}',f'           {posit163}']
table4 = ['32', f'  {posit321}', f'     {posit322}',f'          {posit323}']
print(f'p81: {posit81}')
print(f'p82: {posit82}')
print(f'p83: {posit83}')
print(f'p161: {posit161}')
print(f'p162: {posit162}')
print(f'p163: {posit163}')
print(f'p321: {posit321}')
print(f'p322: {posit322}')
print(f'p323: {posit323}')

print(table1, "\n", table2, '\n', table3, '\n', table4)

#table = [[first row],[second row],[thirs row],[fourth row]]


import pandas as pd
import numpy as np
trial_df = pd.DataFrame({"bits/es": [1,2,3],
              "8": [posit81, posit82,posit83],
              "16": [ posit161,posit162,posit163],
              "32": [posit321,posit322,posit323]})
trial_df.head()