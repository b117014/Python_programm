
def countSub(a,k): 
    n = len(a)  
    p = 1
    res = 0
    start = 0
    end = 0 
    while(end < n): 
  
        # Move right bound by 1 
        # step. Update the product. 
        p *= a[end] 
          
        # Move left bound so guarantee  
        # that p is again less than k. 
        while (start < end and p%k!=0):  
            p =int(p//a[start]) 
            start+=1
        if (p%k==0):  
            l = end - start + 1
            res += l 
          
        end+=1
  
    return res
  
# Driver Code 
n,k = map(int,input().split())
l = list(map(int,input().split()))

size = len(l) 
count = countSub(l, k); 
print (count) 