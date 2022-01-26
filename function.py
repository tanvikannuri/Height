def CountWordsFromFile():
    FileName=input("Enter the file name: ")
    numberOfWords=0
    File=open(FileName,'r')
    for Line in File:
        words=Line.split()
        numberOfWords=numberOfWords+len(words)
    print("Number of words are: ")
    print(numberOfWords)

CountWordsFromFile()