a=[1,2,3,4,5,6,7,8,9,10]
print(a)
def function(a:list[int])->list[int]:
    n=len(a)
    m=a[1:n-1]
    return m
print(function(a))
