#conversion of des into bin
def fun(num):
  res=bin(num)[2:]
  print(res)
if __name__=='__main__':
  num=50
  fun(50)

#toggling of bin and printing it in int
#toggling refers to the conversion of 1 bit to 0 and vice versa
def fun(num):
  res=bin(num)[2:]
  tog=(''.join("1" if bit=="0" else "0" for bit in res))
  tog=int(tog,2)
  print(tog)
if __name__=='__main__':
  num=50
  fun(50)

#count of greater numbers
def fun(n,arr):
    count=0
    for i in range(len(arr)):
        if arr[i]>n:
            count+=1
    print(count)
num=5
arr=[4,5,8,6,7,9,10]
fun(num,arr)

#product of digits in string
def fun(n):
    prod=1
    for digit in str(n):
        prod=prod*int(digit)
    print(prod)
n=1589
fun(n)

