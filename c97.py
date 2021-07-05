introstring = input("enter your introduction : -") 
print(introstring)
charactercount=0 
wordcount = 1
for i in  introstring:
    charactercount= charactercount+1
    print(charactercount)
    if (i==' '):
        wordcount = wordcount+1
print("number of words:-")
print(wordcount)  
print("number of characters:-")
print(charactercount) 

