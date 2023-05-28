def countEvenSum(arr, n): 
    temp = [1, 0] 
    result = 0
    sum = 0
    for i in range(n): 
        sum = ( (sum + arr[i]) % 2 + 2) % 2
        temp[sum]+= 1
    result = result + (temp[0] * (temp[0] - 1) // 2) 
    result = result + (temp[1] * (temp[1] - 1) // 2) 
    return (result)