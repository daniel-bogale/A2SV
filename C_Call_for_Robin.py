def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        
        if n == 1:
            print(-1)
            continue
        
        arr_sorted = sorted(arr)
        total = sum(arr)
        left = 0
        right = 10**18 
        
        def is_condition_met(x):
            new_total = total + x
            half_avg = new_total / (2 * n)
            
            count_less = 0

            left_pos = 0
            right_pos = n
            while left_pos < right_pos:
                mid = (left_pos + right_pos) // 2
                if arr_sorted[mid] < half_avg:
                    left_pos = mid + 1
                else:
                    right_pos = mid
            count_less = left_pos

            original_max = arr_sorted[-1]
            if original_max < half_avg:
                if (original_max + x) < half_avg:
                    pass  
                else:
                    count_less -= 1

            return count_less > n / 2
        

        if is_condition_met(0):
            print(0)
            continue
        
        left = 0
        right = 2 * 10**18
        answer = -1
        while left <= right:
            mid = (left + right) // 2
            if is_condition_met(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        print(answer)

solve()