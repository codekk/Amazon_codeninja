import sys
#array = [map(int, row.split()) for row in sys.stdin]
#print array
#array=[[4, 20], [10, 0, 14, 0], [12, 0, 15, 0], [15, 0, 18, 0],[23, 0 , 23,20]]
array=[[1,1],[0,30,23,30]]
M_bs=array[0][0]
k_dur=array[0][1]
start_call=0
end_call=24*60

time=[[0 for i in range(2)] for x in range(M_bs)]
start_time=[]
end_time=[]

time_start=0
time_end=0
for i in range(1,M_bs+1):
    time_start=array[i][0]*60+array[i][1]
    time_end=array[i][2]*60+array[i][3]
    #print time_start
    #print time_end
    time[i-1]=(time_start,time_end)
    start_time.append(time_start)
    end_time.append(time_end)

"""Quicksort using a partitioning function"""
def qsort1(list):
   
    if list==[]:
        return []
    else:
        pivot=list[0]
        lesser=qsort1([x for x in list[1:] if x<pivot])
        greater=qsort1([x for x in list[1:] if x>=pivot])
        return lesser+[pivot]+greater
 
start_time= qsort1(start_time) 
end_time=qsort1(end_time)

print start_time
print end_time

free_min=[]
for i in range(start_time[0],end_time[len(end_time)-1]):
    count=0
    for j in range(0,len(time)):
        if time[j][1]>i>time[j][0]:
            count=count+1
        else:
            count=count
    if count==0:
        free_min.append(i)

for i in range(start_call,(start_time[0])):
    free_min.append(i)
for i in range((end_time[len(end_time)-1]),(end_call+1)):   
    free_min.append(i)

free_min=qsort1(free_min)    
print free_min
def free_check(time,free_min):
    if len(free_min)<2:
        return
    elif len(free_min)<time:
        return
    else:    
        i=0
        end_index=[]
        span_index=[]
        while(i<(len(free_min)-2)):
            count=1
            span=0
            while count==1:
                if free_min[i+1]-free_min[i]==1:
                    count=1
                    span=span+1
                    if (i<(len(free_min)-2)):
                        i=i+1
                    else:
                        i=i
                        count=0
                        end=free_min[i+1]
                        if span>0:
                            span_index.append(span)
                            end_index.append(end)
                        else:
                            pass
                else:
                    count=0
                    end=free_min[i]
                    if span>0:
                        span_index.append(span)
                        end_index.append(end)
                    else:
                        pass
                    i=i+1
        print end_index
        print span_index
        for i in range(0, len(span_index)):
            if span_index[i]>=time:
                print convert_back(end_index[i]-span_index[i]),convert_back(end_index[i])

def convert_back(time):
    hours= time/60
    minutes=time%60
    if hours<10:
        if minutes<10:
            return "0%r 0%r" %(hours,minutes)
        else:
            return "0%r %r" %(hours,minutes)
    elif hours==24:
        return "00 00"
    else:
        if minutes<10:
            return "%r 0%r" %(hours,minutes)
        else:
            return "%r %r" %(hours,minutes)
                 
free_check(k_dur,free_min)    