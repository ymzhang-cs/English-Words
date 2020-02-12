print("单词默写程序(V1.1) 2/12/2020 Powered by zymzs")
print("本程序源代码按照GNU General Public License v3.0在Github上发布(https://github.com/zymzs/English-Words)")
print("本程序依靠同目录下单词表（wordList.txt）进行工作。单词表（wordList.txt）可按照需求自行修改。修改格式：单词@中文，支持多国语言")

from random import choice
wordDictionary = {}
num = 0
try:
    f = open("wordList.txt", "r", encoding = "utf-8")
    for line in f:
        wordDictionary[line.split("@")[0]] = line.split("@")[1]
    
    wordEnList = list(wordDictionary.keys())
    wordZhList0 = list(wordDictionary.values())
    wordZhList = []
    for item in wordZhList0:
        wordZhList.append(item.replace("\n", ""))
    num = len(wordZhList)
except:
    print("\n[ERROR]打开单词表错误")
corList = []
counter = 0
miss = 0

print("\n开始。本次共{}个单词。".format(str(num)))

while True:
    counter += 1
    if len(corList) == num:
        break
    print("======第{}轮======".format(str(counter)))
    while True:
        thisTime = choice(range(num))
        if wordEnList[thisTime] in corList:
            pass
        else:
            break
    back = input(wordZhList[thisTime]+":")
    if back == wordEnList[thisTime]:
        print("Correct!")
        corList.append(wordEnList[thisTime])
        continue
    else:
        back = input("One more choice:")
        if back == wordEnList[thisTime]:
            print("Correct!")
            continue
        else:
            print("Wrong! The word is \""+wordEnList[thisTime]+"\"")
            miss += 1
            continue
print("默写完成。共{}个单词，错误{}次。".format(str(num), str(miss)))
strg = input("按任意键退出")