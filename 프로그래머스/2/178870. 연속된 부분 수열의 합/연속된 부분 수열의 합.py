def solution(sequence, k):
    n = len(sequence)
    left = 0
    current = 0
    
    best = None   # (Length, left, right)
    for right in range(n):
        current += sequence[right]
        
        while current >= k and left<= right:
            if current == k:
                length = right - left
                
                if best is None or length < best[0] or (length == best[0] and left < best[1]):
                    best = (length, left, right)
            current -= sequence[left]
            left += 1
    return [best[1], best[2]]
            
    return answer