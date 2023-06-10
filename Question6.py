def f1(arr,l,r):
    return arr[l : r : 2]

def f2(arr,l,r):
    ans = []
    for i in range(l,r,2):
        ans.append(arr[i])
    return ans


print(f2([2,3,5,7,11,13,17,19,23,29,31,37,41],2,9))