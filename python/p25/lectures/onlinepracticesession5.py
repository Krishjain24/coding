"""
Question: Group Words of a Sentence by Their Length

Given a sentence, group all unique words by their length into a
dictionary. Ignore uppercase and lowercase differences.

Example:
Input:  "Eat sleep code and repeat code and eat clean"
Output: {3: ['eat', 'and'], 5: ['sleep', 'clean'], 4: ['code'], 6: ['repeat']}
"""

sen = "Eat sleep code and repeat code and eat clean"
res = ""
for ch in sen:
    if  ord('a') <= ord(ch) <=ord('z'):
        res += chr(ord(ch)-32)
    else:
        res +=ch
print(res)
        





# ans = {}
# words = sen.split(" ")
# for word1  in words:
#     l = len(word1)
#     temp = []
#     for word2 in words:
#         if  len(word2) == l and word2 not in temp:
#             temp.append(word2)
#     ans[l] = temp
# print(ans)

