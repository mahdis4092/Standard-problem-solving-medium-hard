#symbol=['I','V','X','L','C','D','M']
#value=[1,5,10,50,100,500,1000]

#print(type(I))
def translate(r):
    if r=='I':
        return 1
    elif r=='V':
        return 5
    elif r=='X':
        return 10
    elif r=='L':
        return 50
    elif r=='C':
        return 100
    elif r=='D':
        return 500
    elif r=='M':
        return 1000
    else:
        return -1


string="MCMXCIV"
str_len=len(string)
count=0
for i in range(str_len):
    new_str=string[i]
    count+=translate(new_str)
print(count)






