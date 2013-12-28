# Enter your code here. Read input from STDIN. Print output to STDOUT
#This is one of my first pieces of code after a long winter- November 2013
#The algo is inefficient and crude and mostly Brute Force and lot to be refined- I will do that later.
#This was originally for the Amazon Code Ninja
#You should follow me on twitter here @codeprss

#taking in the values from Stdin

import sys
array=[]
array = [map(int, row.split()) for row in sys.stdin]
#print array

num_tests=array[0][0]
test_sizes=[]


#identifying the various fields such as number of tests,starting indices of the test arrays etc
if num_tests==0:
    print" Does not have any tests"
else:
    test_sizes.append(int(array[1][0]))
    test_array=[1]
    new_sum=1
    for i in range(1,num_tests):
        new_sum+=int(test_sizes[i-1])+1
        test_sizes.append(int(array[new_sum][0]))
        test_array.append(new_sum)
    #print test_sizes
    #print test_array
    
#First function that scans from top down to find out connected sets- 
#We call this check and takes the starting index of the test array and the size of that respective test array
           
def check(size,test_no):
    count=0
    scan=[[0 for i in range(size)] for x in range(size)]
    for i in range(0,size):
        r=i+test_array[test_no-1]+1
        for j in range(0,size):
            if array[r][j]==1:
                if i==0:
                    if j==0:
                        count+=1
                        scan[0][0]=1
                    else: 
                        if array[r][j-1]==1:
                            count=count;
                            scan[i][j]=scan[i][j-1] 
                        else:    
                            count=count+1
                            scan[i][j]=count
                else:
                    if j==0:
                        if array[r-1][j]==1:
                            if array[r-1][j+1]==1:
                                scan[i][j]=scan[i-1][j]
                                count=count
                            else:
                                scan[i][j]=scan[i-1][j]
                                count=count
                        else:
                            if array[r-1][j+1]==1:
                                scan[i][j]=scan[i-1][j+1]
                                count=count
                            else:    
                                count+=1
                                scan[i][j]=count
                    
                    elif j==(size-1):        
                        if array[r-1][j-1]==1:
                                scan[i][j]=scan[i-1][j-1]
                        else:
                            if array[r-1][j]==1:
                                scan[i][j]=scan[i-1][j]
                            else:
                                if array[r][j-1]==1:
                                    scan[i][j]=scan[i][j-1]
                                else:    
                                    count+=1
                                    scan[i][j]=count    
                    else: 
                        if array[r-1][j-1]==1:
                            if array[r-1][j]==1:
                                if array[r-1][j+1]==1:
                                    if array[r][j-1]==1:                                        
                                        scan[i][j]=min(scan[i-1][j-1],scan[i-1][j+1])
                                        scan[i-1][j-1]=scan[i][j]
                                        scan[i-1][j+1]=scan[i][j]
                                        scan[i-1][j]=scan[i][j]
                                        scan[i][j-1]=scan[i][j]
                                    else:
                                        scan[i][j]=scan[i-1][j-1]
                                else:
                                    scan[i][j]=scan[i-1][j-1]
                            else:
                                if array[r-1][j+1]==1:
                                    scan[i][j]=min(scan[i-1][j-1],scan[i-1][j+1])
                                    scan[i-1][j-1]=scan[i][j]
                                    scan[i-1][j+1]=scan[i][j]
                                else:
                                    scan[i][j]=scan[i-1][j-1]
                        else:
                            if array[r-1][j]==1:
                                scan[i][j]=scan[i-1][j]
                            else:
                                if  array[r-1][j+1]==1:
                                    scan[i][j]=scan[i-1][j+1]
                                else:
                                    if array[r][j-1]==1:
                                        scan[i][j]=scan[i][j-1]
                                    else:
                                        count+=1
                                        scan[i][j]=count   
                        
                        
                        ###if array[r-1][j-1]==1:
#                            if array[r-1][j+1]==1:
#                                scan[i][j]=min(scan[i-1][j-1],scan[i-1][j+1])
#                                scan[i-1][j-1]=scan[i][j]
#                                scan[i-1][j+1]=scan[i][j]
#                            else:
#                                scan[i][j]=scan[i-1][j-1]
#                        elif array[r-1][j-1]==0:
#                            if array[r-1][j+1]==1:
#                                scan[i][j]=scan[i-1][j+1]
#                            else:
#                                scan[i][j]=scan[i][j]
#                        if array[r-1][j]==1:
#                            scan[i][j]=scan[i-1][j]
#                        if array[r][j-1]==1:
#                                scan[i][j]=scan[i][j-1] ####

#                        else:
#                            count+=1
#                            scan[i][j]=count
            else:
                count=count
                scan[i][j]=0
    return secondcheck(size,scan)    
        
# this is the second function
# this function combs from bottom right most corner 
# checks with the left and botton connections to ensure duplicities    
def secondcheck(size,scan):
    for i in range(0,size):
        for j in range(0,size):
            a=size-i-1
            b=size-j-1
            if scan[a][b]!=0:
                if a==size-1:
                    if b==size-1:
                        scan[a][b]=scan[a][b]
                    else:
                        if scan[a][b+1]!=0:
                            scan[a][b]=scan[a][b+1]
                        else:
                            scan[a][b]=scan[a][b]
                else:
                    if b==size-1:
                        if scan[a+1][b]!=0:
                            if scan[a+1][b-1]!=0:
                                scan[a][b]=min(scan[a+1][b-1],scan[a+1][b])
                                scan[a+1][b-1]=scan[a][b]
                                scan[a+1][b]=scan[a][b]
                            else:
                                scan[a][b]=scan[a+1][b]
                        else:
                            if scan[a+1][b-1]!=0:
                                scan[a][b]=scan[a+1][b-1]
                            else:
                                scan[a][b]=scan[a][b]
                                    
                            
                    elif b==0:
                        if scan[a+1][b+1]!=0:
                            if scan[a+1][b]!=0:
                                scan[a][b]=min(scan[a+1][b+1],scan[a+1][b])
                                scan[a+1][b+1]=scan[a][b]
                                scan[a+1][b]=scan[a][b]
                            else:
                                scan[a][b]=scan[a+1][b+1]
                        else:
                            if scan[a+1][b]!=0:
                                scan[a][b]=scan[a+1][b]
                            else:
                                if scan[a][b+1]!=0:
                                    scan[a][b]=scan[a][b+1]
                                else:
                                    scan[a][b]=scan[a][b]
                    else:
                        if scan[a+1][b+1]!=0:
                            if scan[a+1][b-1]!=0:                         
                                    scan[a][b]=min(scan[a+1][b+1],scan[a+1][b-1])
                                    scan[a+1][b+1]=scan[a][b]
                                    scan[a+1][b-1]=scan[a][b]
                            else:
                                scan[a][b]=scan[a+1][b+1]
                        else:
                            if scan[a+1][b]!=0:
                                scan[a][b]=scan[a+1][b]
                            else:
                                if scan[a+1][b-1]!=0:
                                    scan[a][b]=scan[a+1][b-1]
                                else:
                                    if scan[a][b+1]!=0:
                                        scan[a][b]=scan[a][b+1]
                                    else:
                                        scan[a][b]=scan[a][b]
                         
                                    
                                        
                                        
    # this is a small trick to calculate the number of unique sets identified                
    score=[]
    for i in range(0,size):
        for j in range(0,size):
            if scan[i][j]!=0:
                score.append(scan[i][j])            
    #print score
    return max(score)-min(score)+1
    
# finally we run the test on the input data

#output=open('output00.txt','w') 
#for i in range(0,len(test_sizes)):
#    result=str(check(test_sizes[i],i+1))
#    output.write(result)
#    output.write("\n")
#output.close()

for i in range(0,len(test_sizes)):
    print check(test_sizes[i],i+1)