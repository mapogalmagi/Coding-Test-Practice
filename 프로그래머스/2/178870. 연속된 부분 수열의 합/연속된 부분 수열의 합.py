def solution(sequence, k):
    n = len(sequence)
    left, right = 0, 0
    total = sequence[0]
    answer = None

    while right < n:
        if total == k:
            length = right - left
            if (answer is None or
                length < answer[0] or
                (length == answer[0] and left < answer[1])):
                answer = (length, left, right)
            total -= sequence[left]
            left += 1

        elif total < k:
            right += 1
            if right < n:
                total += sequence[right]

        else:  # total > k
            total -= sequence[left]
            left += 1

    return [answer[1], answer[2]]