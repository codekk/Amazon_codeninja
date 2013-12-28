import sys
#array=[]
#array = [map(int, row.split()) for row in sys.stdin]
#print array

array=[[5], [4], [0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [4], [1, 0, 0, 1], [0, 0, 0, 0], [0, 1, 1, 0], [1, 0, 0, 1], [5], [1, 0, 0, 1, 1], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [8], [0, 0, 1, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 1, 1, 0], [1, 0, 1, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0],[4], [0, 0, 1, 1], [1, 0, 1, 1], [0, 1, 1, 1], [1, 1, 1, 1]]

num_tests=array[0][0]
test_sizes=[]

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
    

def find(i,j,array,size):
    array[i][j]=2
    #North_west
    if (array[i-1][j-1]==1)and (i>0) and (j>0) and (i<size) and (j<size):      
        find(i-1,j-1,array,size)  
    #North
    if (array[i-1][j]==1)and (i>0) and (j>=0) and (i<size) and (j<size):    
        find(i-1,j,array,size)
    #North_East    
    if (array[i-1][j+1]==1)and (i>0) and (j>=0) and (i<size) and (j<size):      
        find(i-1,j+1,array,size)
    #West
    if (array[i][j-1]==1)and (i>=0) and (j>0) and (i<size) and (j<size):      
        find(i,j-1,array,size)
    #East
    if (array[i][j+1]==1)and (i>=0) and (j>=0) and (i<size) and (j<size):      
        find(i,j+1,array,size)  
    #South_west    
    if (array[i+1][j-1]==1)and (i>=0) and (j>0) and (i<size) and (j<size):      
        find(i+1,j-1,array,size)
    #South    
    if (array[i+1][j]==1)and (i>=0) and (j>=0) and (i<size) and (j<size):      
        find(i+1,j,array,size)
    #South_east
    if (array[i+1][j+1]==1)and (i>=0) and (j>=0) and (i<size) and (j<size):      
        find(i+1,j+1,array,size)   
    return 1              
    
 
 #[4, 4, 5, 8]
#[1, 6, 11, 17]   
if max(test_array)>1009:
    return
else:
    for k in range(0,len(test_sizes)):
        temp_array=[[0 for i in range(1015)] for x in range(1015)]
        for i in range(0,test_sizes[k]):
            for j in range(0,test_sizes[k]):
                temp_array[i][j]=array[(test_array[k]+1+i)][j]
        #print temp_array
        count=0
        #print count
        for i in range(0,test_sizes[k]):
            for j in range(0,test_sizes[k]):
                #r=i+test_array[k]+1
                if temp_array[i][j]==1:
                    if(find(i,j,temp_array,test_sizes[k])):
                        count+=1
                    else:
                        count=count
                else: 
                    count=count
        print count  
        #print temp_array