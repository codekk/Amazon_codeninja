

import sys
#array =map(int,sys.stdin)
#print array
array=[4,3,5,161,27011]

fib=[0 for i in range(2)]
fib[0]=0
fib[1]=1
i=1
while fib[i]<=10**18:
    x=fib[i]+fib[i-1]
    fib.append(x)
    i=i+1
#print fib
#print len(fib)

def factors(num):
    factor_set=[]
    for i in range(1,num/2+1):
        if num%i==0:
            factor_set.append(i)
        else:
            pass
    factor_set.append(num)        
    return factor_set                
    


def factor_match(num1):
    factor_num1=factors(num1)
    common_factors=[]
    corresp_fib=[]
    for i in range(1,len(factor_num1)):
        for j in range(3,len(fib)):
            if fib[j]%factor_num1[i]==0:
                common_factors.append(factor_num1[i])
                corresp_fib.append(fib[j])
            else:
                pass
    if len(corresp_fib)==0:
        print 1,1
    else:
        min_fib=min(corresp_fib)
        com_div=common_factors[corresp_fib.index(min_fib)]
        print min_fib,com_div
    
for i in range(1,len(array)):
    factor_match(array[i])
#def output(arrayi):
#    max_cf_check=1
#    j=1
    #r=0
    #while fib[r]<=arrayi:
    #    r=r+1
#    while (max_cf_check==1)and(j<len(fib)):   
#       max_cf_check=factor_match(arrayi,fib[j])
#       j=j+1
#    if max_cf_check!=1:   
#        print  fib[j-1],max_cf_check
#    else:
#        print 1,1
#for i in range(1,len(array)):
#    output(array[i])
