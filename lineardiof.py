def linear_diofant(a,b,c):
    import math
    d=math.gcd(math.gcd(a,b),c)
    a,b,c=a//d,b//d,c//d
    if math.gcd(a,b)>1:
        print('Нет целых решений')
    else:
        x0=0
        while True:
            if (1-a*x0)%b==0:
                y0=(1-a*x0)//b
                print('x,y =',str(c*x0)+'+'+str(b)+'t'+','+str(c*y0)+'-'+str(a)+'t'+',t is integer')
                break
            else:
                x0+=1
input()        
