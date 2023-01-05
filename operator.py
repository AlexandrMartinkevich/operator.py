#print("Стороны")
#b = int(input("b = "))
#c = int(input("c = "))
#if a+b > c and a+c > b and b+c > a:
    #print("Треугольник существует")
#else:
   # print("Треугольник не существует")

n = int(input("Введите возраст (от 1 до 99 лет): "))
float = n%10 # остаток от деления на 10
if 10<n<20:
    print('мне', n, 'лет')
elif 1<float<5:
    print('мне', n, 'года')
elif float==1:
    print('мне', n, 'год')
else:
    print('мне', n, 'лет')
