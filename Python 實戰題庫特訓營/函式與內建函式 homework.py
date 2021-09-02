# 1. 完成(1) 計算平方 和(2) 計算平方根 的函式
# 2. 寫一個回傳 n! 的函式


def square(x):
    x = x**2
    return(x)


def sqrt(y):
    y = y**0.5
    return(y)


def n(z):
    ans = 1
    for i in range(1, z+1):
        ans = ans*i
    return(ans)


print(square(3))
print(sqrt(25))
print(n(5))
