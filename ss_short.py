import re
if __name__=='__main__':
    sentence=raw_input()
    wordnum=int(raw_input())
    sen_list=sentence.split()
    words=dict()
    for i in range(0,wordnum):
        words[raw_input()]=-1
        
    word_limit=200001

    mn=-1
    mx=-1

    for i in range(0,len(sen_list)):
        word=re.sub('[^A-Za-z]','',sen_list[i])
        word=word.lower()
        
        if word not in words:
            continue
        
        words[word]=i
        
        x=min(words.values())
        y=max(words.values())
        
        if (x==-1):
            continue
        else:
            if (word_limit>y-x+1):
                mn,mx,word_limit=x,y,y-x+1
                
        if word_limit==len(words):
            break
            
    if mn==-1:
        print 'NO SUBSEGMENT FOUND'
    else:
        temp=" ".join(sen_list[mn:mx+1])
        print re.sub('[^A-Za-z  ]','',temp)