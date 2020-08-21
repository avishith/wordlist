import os

a=os.getcwd()
a=a+"/passs.txt"


f= open(a,"w+")
A=int(input("ENTER THE STARTING NUMBER :- "))
B=int(input("ENTER THE ENDINGING NUMBER :- "))



for i in range(B):
     f.write("%d\r\n" % (A))
     A+=1
    
f.close()
print("\n  SUCESS wordlist  saved in"+a)






