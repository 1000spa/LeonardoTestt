def factorial(a):
    mul = 1
    for i in range(1,a +1):
        mul *= i
    print(mul)

ipt = int(input())
try:
	factorial(ipt)
except ValueError:
	print("값이 올바르지 않습니다!")
#제가 예전에 만들어둔 코드입니다!