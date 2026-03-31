"""
129 137
"""

# M, N = map(int, input().split())
# nums = [0,0,0,0,0,0,0,0,0,0]
#
#
# for i in range(M, N + 1):
#     for j in range(0, 10):
#         nums[j] += str(i).count(str(j))
#
# result = ' '.join(map(str, nums))
# print(result)

M, N = map(int, input().split())
nums = [0,0,0,0,0,0,0,0,0,0]

for i in range(M,N+1):
    while i>0:
        digit = i % 10
        nums[digit]+=1
        i//=10
result=' '.join(map(str,nums))
print(result)

