#1 def biggiesize(arr):
#     for i in range(0, len(arr)):
#         if arr[i]>0:
#             arr[i]="big"   
#     return arr
# print(biggiesize([-1, 1, 4, -5]))
#
#2 xix=[]
# def count_positives(arr):
#     for i in range(0, len(arr)):
#         if arr[i]>0:
#             xix.append(arr[i])
#     arr[-1]=len(xix)
#     return arr
# print(count_positives([-1,1,1,1]))

# def sum_total(arr):
#     summation=0
#     for i in range(0, len(arr), 1):
#         summation+=arr[i]
#     return summation 
# print(sum_total([1, 2, 3, 4]))

# def average(arr):
#     av=0
#     for i in range(len(arr)):
#         av= av+arr[i]
#     av=av/len(arr)
#     return(av)
# print(average([1, 2, 3, 4]))

# def length(arr):
#     x= len(arr)
#     return x
# print(length([1, 2, 3, 4]))

# def min(arr):
#     x=[arr[0]]
#     for i in range(len(arr)):
#         if x[0]>arr[i]:
#             x.pop(0)
#             x.append(arr[i])
#     return x
# print(min([35, 5, 6, 8]))

# #7
# def maximum(arr):
#     max = arr[0]
#     if len(arr) == 0:
#         return False
#     for i in arr:
#         if i>max:
#             max = i
#     return max
# print(maximum([35, 2, 6, 8]))

#9
# def reversed(arr):
#     x=[]
#     for i in range(len(arr)-1, -1, -1):
#         x.append(arr[i])
#     return(x)
# print(reversed(([37,2,1,-9])))




