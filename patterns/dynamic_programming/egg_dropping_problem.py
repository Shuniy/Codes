def superEggDrop(k: int, n: int) -> int:
    return superEggDropHelper(k, n, {})

def superEggDropHelper(k: int, n: int, memo: dict) -> int:
    if (k, n) in memo:
        return memo[(k, n)]

    if n == 0 or n == 1:
        memo[(k, n)] = n
        return n

    if k == 0 or k == 1:
        memo[(k, n)] = n
        return n
        
    mn = float("inf")
    low = 1
    high = n
    while low <= high:
        floor = low + (high - low) // 2
        # broken at current floor
        # check below not above
        p1 = superEggDropHelper(k - 1, floor - 1, memo)
        # not broken here, so check above floors
        p2 = superEggDropHelper(k, n - floor, memo)
        # Let there be ‘2’ eggs and ‘2’ floors then-:
        # If we try throwing from ‘1st’ floor: 
        # Number of tries in worst case= 1+max(0, 1) 
        # 0 => If the egg breaks from first floor then it is threshold floor (best case possibility).
        # 1 => If the egg does not break from first floor we will now have ‘2’ eggs and 1 floor to test which will give answer as ‘1’.(worst case possibility) 
        # We take the worst case possibility in account, so 1+max(0, 1)=2
        # If we try throwing from ‘2nd’ floor: 
        # Number of tries in worst case= 1+max(1, 0) 
        # 1=>If the egg breaks from second floor then we will have 1 egg and 1 floor to find threshold floor.(Worst Case) 
        # 0=>If egg does not break from second floor then it is threshold floor.(Best Case) 
        # We take worst case possibility for surety, so 1+max(1, 0)=2.
        ans = 1 + max(p1, p2)
        mn = min(ans, mn)
        if p1 <= p2:
            low = floor + 1
        else:
            high = floor - 1

    memo[(k, n)] = mn
    return memo[(k, n)]

# test cases
print(superEggDrop(2, 6))
print(superEggDrop(3, 14))
print(superEggDrop(4, 18))
print(superEggDrop(5, 100))
print(superEggDrop(6, 85))
print(superEggDrop(7, 100))
print(superEggDrop(8, 100))
print(superEggDrop(9, 100))