'''
n = 1260
count = 0

coin_type = [500, 100, 50, 10]

for coin in coin_type:
    count = count + (n//coin)
    n = n % coin

print(count)
# 알고리즘 시간 복잡도는 금액과는 무관하며 동전 갯수만큼의
# 시간 복잡도이다.
'''

'''
a,b,c = input().split()

a1 = int(a)
b1 = int(b)
c1 = int(c)

arr = [a1,b1,c1]

# print(arr[0])
# print(arr[1])
# print(arr[2])


for i in arr:
    if i % 2 == 0:
        print("even")
    else:
        print("odd")
'''

'''
a = int(input())

while True:
    print(a)
    a -= 1

    if a == 0: 
        break
'''

'''
a = input()
a1 = ord(a)

i = 0

while True:
    print(chr(97 + i), end=' ')
    i += 1
    
    if chr(97 + i) > a:
        break
'''

'''
n,m = input().split()

n1 = int(n)
m1 = int(m)

for i in range(1,n1+1):
    for j in range(1,m1+1):
        print(i,j, end=' ')
        print(' ')
'''

'''
a = input()
a1 = int(a,16)

for i in range(1,16):
    print("%X"%a1,"*%X"%i, "=%X"%(a1*i), sep='')
'''

'''
a = int(input())

for i in range(1,a+1):
    if i%10==3 or i%10==6 or i%10==9:
        i = 'X'
        print(i, end=' ')
    else:
        print(i, end=' ')
'''

'''
r,g,b = input().split()

r = int(r)
g = int(g)
b = int(b)

for i in range(0, r):
    # print(i,j,k)
    for j in range(0, g):
        # print(i,j,k)
        for k in range(0,b):
            print(i,j,k)
print(r*g*b)
'''

'''
i=1
while i<=a:
    if(i%3==0): 
        continue
    
    print(i)
    i += 1
'''

'''
a, m, d, n = input().split()

a = int(a) # 시작값
m = int(m) # 곱할값
d = int(d) # 더할값 
n = int(n) # 몇 번째 정수

result = a
for i in range(1, n):
    result = result * m + d
print(result)
'''


'''
n0 = int(input())
n1 = input().split() # n1은 리스트
# print(n1)

result = [] # result도 리스트
count = 0

for i in range(n0):
    n1[i] = int(n1[i])
    # print(n1[i], end=' ')

for i in range(24):
    result.append(0)
# print(result)

for i in range(n0):
    result[n1[i]] += 1

for i in range(1, 24):
    print(result[i], end=' ')
'''

'''
n = int(input())
k = input().split()

for i in range(n):
    k[i] = int(k[i])
    # print(k[i], end=' ')

for i in range(n-1,-1,-1):
    print(k[i], end=' ')
'''

'''
n = int(input())
k = input().split()

min = int(k[0])
for i in range(n):
    k[i] = int(k[i])
    # print(k[i], end=' ')
    # min = k[0]
    # print(min)
    
    if min > k[i]:
        min = k[i]
    else:
        continue
print(min)
'''

'''
n = int(input())
# x,y = input().split() # 하나가 입력되면 이렇게.
# k = [x, y]

pan = []
for i in range(1,20):
    for j in range(1,20):
        pan.append(0)
# print(pan)

for i in range(n):
    x,y = input().split()
    pan[int(x)][int(y)] = 1

for i in range(1,20):
    for j in range(1,20):
        print(pan[i][j], end=' ')
'''

'''
d=[]                   # 대괄호 [ ] 를 이용해 아무것도 없는 빈 리스트 만들기
for i in range(20):
    d.append([])         # 리스트 안에 다른 리스트 추가해 넣기
    for j in range(20): 
        d[i].append(0)     # 리스트 안에 들어있는 리스트 안에 0 추가해 넣기
        print(d[i][j], end=' ')
    print(' ')

n = int(input())
for i in range(n):
    x, y = input().split()
    d[int(x)][int(y)] = 1

for i in range(1,20):
    for j in range(1,20): 
        print(d[i][j], end=' ')    #공백을 두고 한 줄로 출력
    print()                          #줄 바꿈
'''



d = []
for i in range(20):
    d.append([])
    for j in range(20):
        d[i].append(0) # 되는 코드
        # d[i].append(input().split())
        # d[i].append(list(map(int, input().split())))
    # print(d[i])
# print(d)

for i in range(19):
    a = input().split()
    for j in range(19):
        d[i+1][j+1] = int(a[j])
# print()

# 일단 0으로 다 채워진 2차배열을 만들어놓고,
# 다시 포문을 하나 더 파서 값을 채워넣는 식으로 초기화
# 해주어야 한다.
# range(n)과 range(1,n)의 차이는 무엇인가...?
# 이게 해결이 안되면 아무것도 안된다...

n = int(input())
for i in range(n):
    x,y = input().split()
    x = int(x)
    y = int(y)
    for j in range(1,20):
        if d[j][y] == 0:
            d[j][y] = 1
        else:
            d[j][y] = 0

        if d[x][j] == 0:
            d[x][j] = 1
        else:
            d[x][j] = 0

for i in range(1,20):
    for j in range(1,20):
        # d[i][j] = int(d[i][j])
        # d[i] = list(map(int, d))
        # int_d = [int(i) for i in d]
        print(d[i][j], end =' ')
    print()































































