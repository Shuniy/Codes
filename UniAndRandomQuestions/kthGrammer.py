def kthGrammer(n: int, k: int) -> int:
    if k <= 1:
        return 0

    if n <= 1 and k <= 1:
        return 0
    
    mid = 2 ** (n - 1)
    if k <= mid:
        return kthGrammer(n - 1, k)
    else:
        return 1 if not kthGrammer(n - 1, k - mid) else 0

print("Kth Grammer", kthGrammer(2, 3))