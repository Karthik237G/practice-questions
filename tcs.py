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

