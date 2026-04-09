def move_zero_start(arr): 
    j=len(arr)-1
    for i in range (len(arr)-1,-1,-1):
        if(arr[i] != 0): 
            arr[j],arr[i]=arr[i],arr[j] 
            j-=1
    return arr

a=[1,245,55,0,6,0,4,6,0]
print("After moving zeros ",move_zero_start(a) )