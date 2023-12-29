#o
'''양의 정수를 입력받아 역으로 보여주고 각 자리 숫자의 합을 구하는 프로그램을 작성하라.

입력
21억 이하의 양의 정수를 입력받는다. 잘못된 데이터는 입력되지 않는다.

하나의 결과가 나온 후에도 계속 새로운 입력을 받다가 0이 입력되면 프로그램을 종료한다.

최대 10개의 양의 정수가 입력될 수 있다.

출력
입력받은 수의 역과 각 자리 숫자의 합을 공백으로 구분하여 출력한다.

유효하지않은 "0"은 출력하지 않는다.

입력받은 수의 역도 21억 이하의 정수이다.


예제
입력
453
123456
0

출력
354 12
654321 21'''
#정수
n=[]
#출력할 리스트
l=[]

sum=[]

#n에 넣기
for i in range(0,10):
    m=int(input())
    sum.append(0)
    if m==0:
        break

    n.append(m)
#l에 나눠서 넣기
for i in range(0,len(n)):
    l.append([])
    while True:
        if n[i]==0:
            break
        k=n[i]%10
        l[i].append(k)
        n[i]=n[i]//10
#print(l)

'''for i in range(0,len(n)):
    for j in l[i]:
        sum[i]=sum[i]+j'''

'''for i in range(0,len(n)):
    for j in range(0,len(l[i])):
        print(" %d %d"%(l[i][j],sum[i]))'''

t1=0
rn=[]

#거꾸로 넣기
for k in range(0,len(n)):
    t1=0
    for i in range(0,len(l[k])):
        sum[k]=sum[k]+l[k][i]
        j=l[k][i]
        t1=t1+j
        t1=t1*10
    t1=t1//10
    rn.append(t1)

for i in range(0,len(n)):
    print(rn[i],sum[i],sep=" ")
