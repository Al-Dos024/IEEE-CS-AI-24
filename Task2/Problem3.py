#by remove the max number , the second will be the max 
n = int(input())
list = list(map(int, input().split()))
    
max_num=max(list)
cont =list.count(max_num)
    
for i in range(cont):
    list.remove(max_num)
print(max(list))

# # didnt work in hackerrank

# n=int(input("enter the number of list : "))
# list = []
# for i in range(n):
#     nums=int(input("enter numbers :"))
#     list.append(nums)
# # print(list)

# laggest = list[0]
# second = list[1]

# for i in list:
#     if(i>laggest):
#         laggest=i
# # print(laggest)

# for j in list:
#     if(j>second and j<laggest):
#         second=j
# print("second largest number",second)
