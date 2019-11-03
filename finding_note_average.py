name=["ALI","SULTAN","KEVIN"]
quiz1=[95,30,65]
quiz2=[90,50,75]
quiz3=[85,80,90]
midterm=[100,82,91]
final=[100,90,95]
avg=[]
for i in range(len(name)):
    avg1=(quiz1[i]+quiz2[i]+quiz3[i])*0.05 + (midterm[i])*0.35 + (final[i])*0.5
    avg.append(avg1)
print("Their note's avarage is ordered like that, Ali Sultan and Kevin", avg)

totalavg=0

for i in avg:
    totalavg +=i

totalavg=totalavg/len(avg)

print("Total avarage is " ,totalavg)

for i in range(len(name)):
    if totalavg < avg[i]:
        print(name[i] , "Passed")
    else:
        print(name[i], "Failed")