# def tokenize1(lines: list[str]) -> list[str]:
#     '''
#     INPUT: List of lines from a file 
#     Output: List of tokens (words)
#     Processing: tokenaizes all words, punctuation marks, symbols etc into list of tokens
#     '''

#     words = []
#     for line in lines:
#         start = 0
#         end = start
#         if line:
#             while end < len(line):
#                 ch = line[end]

#                 if ch.isspace():                
#                     word = line[start:end]
#                     start = end+1
#                     if word:
#                         words.append(word.lower())

#                 elif not (ch.isalpha() or ch.isdigit()):
#                     word = line[start:end]                
#                     end+=1
#                     start = end+1
#                     if word:
#                         words.append(word.lower())
#                     words.append(ch)
                
#                 elif end == len(line)-1:
#                     word = line[start:end+1]
#                     words.append(word)

#                 end+=1


#     return words 




# def tokenize(lines):
#     for line in lines:
#         start = end = 0
#         words = []

#         # print(f'{len(line)} length')
        
#         word = ''
#         typ = 'alpha' if line[0].isalpha() else 'num'
#         for ch in line:            
            
#             if ch.isalpha():
#                 if typ == 'num':
#                     words.append(word)
#                     word = ''
#                     typ = 'alpha'
#                 word+=ch
#                 typ = 'alpha'
#                 print(word)

#             elif ch.isdigit():
#                 if typ == 'alpha':
#                     words.append(word)
#                     word = ''
#                     type = 'num'
#                 word+=ch
#                 type = 'num'

#             elif ch.isspace():
#                 if word: 
#                     words.append(word)
#                     word = ''

#             else: 
#                 words.append(word)
#                 words.append(ch)
#                 word = ''

#             end+=1
#             # print(f'{start} and {end}')

#     return words

# print(tokenize(['   ']))
# print(tokenize(['25Dec 28told you!']))
# print(tokenize(['On December 10, 2013, two of the physicists', 'Peter Higgs and François Englert']))


# if __name__ == '__main__':
#     main()


def tokenize(lines):
    tokens = []
    for line in lines:
        word = ""
        kind = None
        for ch in line:
            if ch.isalpha() or ch.isdigit():
                new_kind = "alpha" if ch.isalpha() else "digit"
                if word and new_kind != kind:
                    tokens.append(word.lower())
                    word = ""
                word += ch
                kind = new_kind
            else:
                if word:
                    tokens.append(word.lower())
                    word = ""
                    kind = None
                if not ch.isspace():
                    tokens.append(ch)
        if word:
            tokens.append(word.lower())
    return tokens

def countWords(words, stopWords):
    counting = {}
    for word in words:
        if word not in stopWords:
            count = counting.setdefault(word, 0)
            counting[word]+=1

    return counting

def printTopMost(frequencies, n):    
    topMost = sorted(frequencies.items(), key=(lambda item: -item[1]))
    for i in range(n):
        if i < len(topMost):
            print(f'{topMost[i][0]:<20}{topMost[i][1]:>5}')

test = {'text': 9, 'word': 30, 'fiction': 6, 'count': 11, 'counting': 7, 'novel': 6}
n = 3

if __name__ == '__main__':
    printTopMost(test, n)


