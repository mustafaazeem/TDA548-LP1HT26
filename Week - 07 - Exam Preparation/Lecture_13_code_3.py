# Exam question 2: 2026 - August  

def bwt(s):
    str_list = []
    string = ''

    for i in range(len(s)):
        str_list.append( s[i:]+s[:i] )

    str_list.sort()
    # string = ''.join(rotation[-1] for rotation in str_list)
    
    for a_string in str_list:
        
        string += a_string[-1]
        # print(string)

    # return str_list
    return string 

print(bwt('hello'))
