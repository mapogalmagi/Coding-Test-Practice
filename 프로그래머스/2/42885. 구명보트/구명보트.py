def solution(people, limit):
    left, right = 0, len(people)-1
    answer = len(people)
    sorted_list = sorted(people)
    
    while left < right:
        if sorted_list[left] + sorted_list[right] > limit:
            right -= 1
        else:
            answer -= 1
            left += 1
            right -= 1
    
    return answer