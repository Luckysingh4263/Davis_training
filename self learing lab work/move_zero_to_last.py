def move_zero(arr): 
    j=0
    for i in range (len(arr)):
        if(arr[i] != 0):
            arr[j],arr[i]=arr[i],arr[j] 
            j+=1
    return arr

arr=[1,245,55,0,6,0,4,6,0]
print("After moving zeros ",move_zero(arr) )