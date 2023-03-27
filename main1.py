n=int(input('Son kiriting : '));
i=2;
j=2;
while i<=n:
 tub=True;
 i=i+1;
 while j<=i/2:
    if i%j==0:
        tub=False;
        break;
 j=j+1;

if tub==False:
 print("Tub son");
else:
 print("Murakkab son");