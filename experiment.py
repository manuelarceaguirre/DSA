


def counter(nums,target):
    d = {}
    def dp(n):
        if n in d:
            return d[n]

        if n == 0:
            return 1 
        if n < 0:
            return 0 
        ways = 0
        for num in nums:    
            ways += dp(n - num)
        d[n] = ways
        return ways

    result = dp(target)
    print(result)


counter([1, 2, 3], 4)


        
