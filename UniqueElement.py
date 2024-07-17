#Given an array of integers, where all elements but one occur twice, find the unique element.
def unique_elements(arr):
    unique={}
    for i in arr:
        if i in unique:
            unique[i]+=1
        else:
            unique[i]=1
    unique_list=[element for element,count in unique.items() if count==1]
    return  unique_list
arr=list(map(int,input().split()))
print(unique_elements(arr))