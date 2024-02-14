List = []
Grade_List  = []

for _ in range(int(input())):
    name = input()
    score= float(input())
    List.append([name,score])
    Grade_List.append(score)

first = min(Grade_List)
while(first in Grade_List):
   Grade_List.remove(first)

second = min(Grade_List)
List.sort()
for i in range(len(List)):
     if(List[i][1]==second):
           print(List[i][0])
