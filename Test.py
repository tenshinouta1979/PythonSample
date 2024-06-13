import sys
import re
#sys.stdin = open('input.txt', 'r') as file:
#    lines = file.readlines()


# Bool Function: finds pattern in word and return True or False 
def re_search(self, wrd, pttn):    
    dpl = re.findall(wrd,pttn)
    if dpl == []:   
       return False
    else:       
       True


# Driver code
with open('./input.txt', 'r') as file:
     input_lines = [line.strip() for line in file]
     
     s = []
     n = len(input_lines)
     for i in range(n):
        s.insert(i,input_lines[i])
     
     #find the longest word
     longword=""
     
     #/ /g to search this pattern more than once
     #() group within
     #[^] Match any character that is not in the set, which is everything
     #\1 Matches the result of capture group1
     #+ Match 1 or more
     pttn=r'/([^])\1+/g'
     for i in range(n):                              
          #Duplicate is NOT found
          if re_search(any,s[i],pttn) == False:             
             if len(longword) < len(s[i]):
                longword = s[i]
print(longword)

#dog valid
#rabbit NOT valid because of 'b'

#-->1.need to check string by char... another loop?
#2.regular expression or..
