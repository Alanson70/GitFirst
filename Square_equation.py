##(a*x)**2+b*x+c
a=float(input('Введите коэфиценет a'))
b=float(input('Введите коэфиценет b'))
c=float(input('Введите коэфиценет c'))   
##(a*x)**2+b*x+c
D=b**2-4*a*c
if D>0:
    x1=(-b+D**0.5)/(2*a)
    x2=(-b-D**0.5)/(2*a)
    print('Корень x1=',(x1))
    print('Корень x2=',(x2))
elif D==0:
    x=-b/2*a
    print('Корень ='(x))
elif D<0:
    print('Корней нет')
#-4<=x<2
#x>=5

     
