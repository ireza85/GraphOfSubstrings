
def StingToList(str1):
    wordList1=[]
    for i in range(len(str1)-2):
        wordList1.append(str1[i:i+3])
    return wordList1

     
        
def Dict1(wordList1,d):        
    for i in wordList1:
        if d.has_key(i):
            if(wordList1.count(i)>1):
                d.update({i: wordList1.count(i)})
        else: 
                d.update({i:1})

    return d


def Dict2(wordList1,d):        
    for i in wordList1:
        if d.has_key(i):
            if(wordList1.count(i)>1):
                    d.update({i: d[i]+int(wordList1.count(i)/2.0)})
            if(wordList1.count(i)==1): 
                    d.update({i:d[i]+1})
            if(wordList1.count(i)==0): 
                    d.update({i:1})
        else: d.update({i:1})
    return d

def Count(s,str1):
    count=0
    for i in range(len(str1)):
        if (str1[i:i+3]==s):
            count+=1
    if (str1[0]==str1[len(str1)-3] and str1[1]==str1[len(str1)-2] and str1[2]==str1[len(str1)-1] ):
           count-=1
    return count
        
def SumOfWeights(newDict,edgeDict,str1):
    for i in edgeDict.keys():
        for j in i:
            if newDict.has_key(j):
                edgeDict.update({i:Count(j,str1)})
    return edgeDict

strCount = int(input())
wordList1=[]
newDict={}
edgeDict1={}
tempDict={}

str1=raw_input()
wordList1=StingToList(str1)

[edgeDict1.update({tuple([wordList1[i],wordList1[i+1]]):1}) for i in range(len(wordList1)-1)]

newDict=Dict1(wordList1,newDict)
tempDict=Dict1(wordList1,tempDict)

#SumOfWeights(newDict,edgeDict1,str1)

tempDict={}

for i in edgeDict1.keys():
        count = 0
        for k in range(len(wordList1)-1):
            if i[0]==wordList1[k] and i[1]==wordList1[k+1]:
                count+=1
        if count > 1:
            edgeDict1.update({i: edgeDict1[i]+count - 1})

edgeDict2={}

ListOfDicts={}

for k in edgeDict1.items():
    ListOfDicts.update({ k[0] : k[1] })


it=0
while(it<strCount-1):

    str1=raw_input()
    wordList1=StingToList(str1)
    newDict=Dict2(wordList1,newDict)
            
    [edgeDict2.update({tuple([wordList1[i],wordList1[i+1]]):1}) for i in range(len(wordList1)-1)]
    for i in edgeDict2.keys():
        count = 0
        for k in range(len(wordList1)-1):
            if i[0]==wordList1[k] and i[1]==wordList1[k+1]:
                count+=1
        if count > 0:
            edgeDict2.update({i: edgeDict2[i]+count - 1})
    
    tempDict=Dict1(wordList1,tempDict)
  #  SumOfWeights(newDict,edgeDict2,str1)
 
    for p in edgeDict2.items():
        count = 0
        for f in ListOfDicts.items():
            if f[0] == p[0]:
                count +=1
        if count == 0:
            ListOfDicts.update({ p[0]: p[1] })
        if count > 0:
            ListOfDicts.update({ p[0]: f[1]+count })

                    
    it+=1
    wordList1=[]
    edgeDict2={}
    tempDict={}
    
  
       
print len(newDict)
print len(ListOfDicts)

for w in ListOfDicts.items(): 
        s=''
        for j in w[0]:
            s+=str(j)
            s+=' '
        print(s + str(w[1]))
