
def twoArrays(k, A, B):
    run=len(A)
    for c in range(run):
        low = (min(A))
        flag=0
        for i in B:
            if i + low>=k:
                A.remove(low)
                B.remove(i)
                flag+=1
                if A == []:
                    return f"YES"
                break
        if B[-1] !=k and flag==0:
            return f"NO"




a = [2, 1, 3]
b = [7, 8, 9]
k = 10




print(twoArrays(k,a,b))


#
# t = input()
#
# for i in range(t):
#     n,k = map(int, raw_input().strip().split())
#
#     A = map(int, raw_input().strip().split())
#     A.sort()
#
#     B = map(int, raw_input().strip().split())
#     B.sort(reverse=True)
#
#     answer = True
#     for a,b in zip(A,B):
#         if a+b < k:
#             answer = False
#     if answer:
#         print "YES"
#     else:
#         print "NO"
#
#
#
#