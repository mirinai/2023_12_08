#test

#o
'''컴퓨터는 내부적으로 0과 1 두 개의 숫자만을 사용하여 모든 프로그램이 동작된다.
이렇게 두 개의 숫자만으로 이루어진 수를 이진수라 한다. 2진수를 입력받아 10진수로 변환하여 출력하는 프로그램을 작성하시오.

입력
0과 1로만 이루어져 있는 30자리 이하의 2진수를 입력받는다.

출력
입력된 2진수를 10진수로 변환하여 출력한다.


예제
입력
10101

출력
21'''
'''n=input()
l=[]
tn=0
sum=0
for i in n:
    l.append(int(i))
for i in range(len(l)-1,-1,-1):

    sum=sum+2**tn*l[i]
    tn+=1
print(sum)'''


'''input
첫째 줄에 정수 N,K,L이 주어진다. 
N은 팀의 수, 
K는 팀원 3명의 레이팅 합에 대한 클럽 가입 조건, 
L은 개인 레이팅에 대한 클럽 가입 조건이다. (1 <= N <= 500,000, , 0 <= K <= 12,000, 0 <= L <= 4000)

둘째 줄부터 N개 줄에 VIP 클럽에 신청한 팀의 팀원들의 레이팅 정보를 나타내는 정수 
x_1, x_2, x_3이 한 줄에 한 팀씩 주어진다. (0 <= x_1,x_2,x_3 <= 4,000)

output
첫째 줄에 VIP 클럽에 가입이 가능한 팀의 수를 출력한다.

둘째 줄에 VIP 회원들의 레이팅을 입력받은 순서대로 공백으로 구분해 하나씩 출력한다.

예제
5 5000 1600
1621 1928 1809
2300 2300 1499
1805 1211 1699
1600 1700 1800
1792 1617 1830

출력
3
1621 1928 1809 1600 1700 1800 1792 1617 1830'''
#N,K,L=map(int,input().split(" "))
'''def count_vip_teams(N, K, L, teams):
    vip_members = []
    vip_count = 0

    for team in teams:
        if sum(team) >= K and max(team) >= L:
            vip_members.extend(team)
            vip_count += 1

    return vip_count, vip_members

# 입력 받기
N, K, L = map(int, input().split())
teams = []
for _ in range(N):
    ratings = list(map(int, input().split()))
    teams.append(ratings)

# VIP 클럽 가입 조건 확인 및 출력
count, members = count_vip_teams(N, K, L, teams)
print(count)
print(*members)
print(ratings)'''
def list_of_std(K,L,evTeam):
    #기준 넘은 팀 세기 리스트
    count=0
    #기준 넘은 팀들의 값들을 넣을 리스트
    std_team=[]
    t=True
    for team in evTeam:
        if sum(team)>=K:
            for j in team:
                if j>=L:
                    t=True
                else:
                    t=False
                    break
        if t==True:
            count+=1
            std_team.extend(team)
        t=True
    print(count)
    print(*std_team)



#N : 팀들, K : 한팀의 모든 점수 기준, L : 한명의 점수 기준
N,K,L=map(int,input().split(" "))

#모든 팀의 리스트
evTeam=[]

for i in range(0,N):
    #한팀씩 넣음
    score = list(map(int, input().split(" ")))
    evTeam.append(score)
#print(evTeam)


list_of_std(K,L,evTeam)





