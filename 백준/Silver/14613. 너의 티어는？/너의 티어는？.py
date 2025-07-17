from itertools import combinations

# 팩토리얼 정의 부분 : list에 애초에 담아서 반복처리하지 않도록 처리
fact_list = [1]
num = 1
for i in range(1,21):
    num *= i
    fact_list.append(num)

a, b, c = map(float, input().split())

bronze, silver, gold, platinum, dia = 0,0,0,0,0

for z in range(21):
    for x in range(21-z):
        y = 20-z-x
        score = 2000+50*x-50*y
        prob = fact_list[20]/(fact_list[x]*fact_list[y]*fact_list[z])*(a**x)*(b**y)*(c**z)

        if score>=1000 and score<1500:
            bronze += prob
        elif score>=1500 and score<2000:
            silver += prob
        elif score>=2000 and score<2500:
            gold += prob
        elif score>=2500 and score<3000:
            platinum += prob
        elif score>=3000 and score<3500:
            dia += prob

print("{:.8f}".format(bronze))
print("{:.8f}".format(silver))
print("{:.8f}".format(gold))
print("{:.8f}".format(platinum))
print("{:.8f}".format(dia))