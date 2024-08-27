##the input contains a string with alphabets and vowels
##the out put must be a string with only consonents
def cons(con):
    vowels='aeiouAEIOU'
    arr=''
    for char in con:
        if char.isalpha() and char not in vowels:
            arr+=char
    res= ''.join(map(str,arr))
    return res
con='helloworld'
output=cons(con)
print(output)
