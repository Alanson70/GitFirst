#this program checks if point belongs to circle

x1=int(input('Введите координату х для точки O'))
y1=int(input('Введите координату у для точки O'))
x2=int(input('Введите координату х для точки A'))
y2=int(input('Введите координату у для точки A'))
R=int(input('Введите радиус окружности'))

if R**2==(x2-x1)**2+(y2-y1)**2:
 print ('Да, точка лежит в окружности')
else:
 print ('Нет, точка не лежит в окружности')
