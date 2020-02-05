import random
wordDictionary = {}

f = open("wordList.txt", "r", encoding = "utf-8")
for line in f:
    wordDictionary[line.split("@")[0]] = line.split("@")[1]

wordEnList = list(wordDictionary.keys())
wordZhList0 = list(wordDictionary.values())
wordZhList = []
for item in wordZhList0:
    wordZhList.append(item.replace("\n", ""))
num = len(wordZhList)


while True:
    thisTime = random.choice(range(num))
    back = input(wordZhList[thisTime]+":")
    if back == wordEnList[thisTime]:
        print("Correct!")
        continue
    else:
        back = input("One more choice:")
        if back == wordEnList[thisTime]:
            print("Correct!")
            continue
        else:
            print("Wrong! The word is \""+wordEnList[thisTime]+"\"")
            continue