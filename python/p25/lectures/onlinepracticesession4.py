
"""
Question: Find Duplicate Words in a Sentence

Find all words that appear more than once.
Ignore uppercase and lowercase differences.

Input:
"Python is easy and python is powerful and easy"

Output:
['python', 'is', 'easy', 'and']
"""
sen = "Python.is.easY.and.python.is.powerfuL.and.Easy"
sen = sen.lower()
print(sen)
words = [] 
# words = sen.split(" ")
# word =""

# for ch in sen:
#     if ch!=".":
#         word+=ch
#     else:
#         words.append(word)
#         word =""
# words.append(word)
# print(word)
# print(words)

# ['python', 'is', 'easy', 'and', 'python', 'is', 'powerful', 'and' ,'easy]
dup = []

for i in range(len(words)):
    count =0
    for j in range(len(words)):
        if words[i] == words[j]:
            count +=1
    if count>=2 and words[i] not in dup:
        dup.append(words[i])
print(dup)
    
