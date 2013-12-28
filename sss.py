#shortest_sub_segment_0000_23_Nov_2013
"""# reader.py- alternate implementation
import fileinput
content = []
for line in fileinput.input():
    content.append(line.strip())
fileinput.close()
print content"""
import sys
"""array=[]
for row in sys.stdin:
    array.append(row.strip())"""
#array=['This is a test. This is a programming test. This is a programming test in any language.', '4', 'this', 'a', 'test', 'language']    
#array=['This is a test. This is a programming test. This is a programming test in any language.', '2', 'this','language']    
array=['roger Kallan is a test. This is a programming test. This est. This is a programming test. Thiest. This is a programming test. Thiest. This is a programming test. Thiest. This is a programming test. Thiest. This is a programming test. Thiest. This is a programming test. Thiis a programming test in any language.', '4', 'roger', 'a', 'test', 'language']    

#print array
sentence=list(array[0])
count=int(array[1])
words=[]
for i in range(0,count):
    words.append(array[i+2])

def clean_sentence(sentence):
    i=0
    j=len(sentence)
    while (i<len(sentence)):
        if ((ord(sentence[i])<65) or ((ord(sentence[i])>90)and(ord(sentence[i])<97)) or (ord(sentence[i]))>122) and (ord(sentence[i])!=32) :
            sentence.pop(i)
            i=i
        else:
            i=i+1
    return sentence

clean_sen= ''.join(clean_sentence(sentence))
clean_sen= clean_sen.split()
#print clean_sen
def word_match(word1, word2):
    match=0
    word1=list(word1)
    word2=list(word2)
    if len(word1)==len(word2):    
        for i in range(0,len(word1)):
            if word1[i]==word2[i]:
                match=1
            else:
                match=0
                return match
    else:
        match=0
    return match
def word_array_match(start,size,sentence,words):
    temp=[]
    score=0
    tick=0
    output=0
    for i in range(start,(start+size)):
        temp.append(sentence[i].lower())
    for i in range(0,len(words)):        
        tick=0
        j=0
        #print score
        #print words
        #for j in range(0,len(temp)):
        while (tick==0)and (j<len(temp)):
            if word_match(words[i],temp[j])==1:
                #print words[i]
                #print temp[j]
                #print temp
                tick=tick+1
                j+=1
                #print "*******************^^^^^^^^^^^^^^^^^^^*"
            else:
                tick=tick
                j+=1
                #print words[i]
                #print temp[j]
                #print "$$$$"
        if tick>=1:
            score=score+1
        else:
            score=score                     
    if score==len(words):
        output= score            
    else:
        pass
    return output
    #print sentence[start]
    #print "****************"    
        
   
def segment(words,sentence):
    if sentence==[]:
        return
    else:
        match=0
        for j in range(len(words),(len(sentence)+1)):    
            for i in range(0,(len(sentence)-j+1)):
                match=word_array_match(i,j,sentence,words)
                #print match
                if match==len(words):
                    for k in range(i,i+j):
                        print sentence[k],
                    return
                else:
                    match=match
        if match!=len(words):
            print "NO SUBSEGMENT FOUND"

segment(words,clean_sen)                