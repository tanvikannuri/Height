introstring=input("Enter your introduction")
print(introstring)
charactercount=0
wordcount=1
for i in introstring:
    charactercount=charactercount+1
    if(i==" "):
        wordcount=wordcount+1
print(wordcount)  
print(charactercount)