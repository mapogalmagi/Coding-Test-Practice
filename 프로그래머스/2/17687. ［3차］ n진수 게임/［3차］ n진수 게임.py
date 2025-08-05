def p_decimal(n, t, m, p):
    num = 1; string = '0'
    num_dic = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    
    while len(string) < m*t + p + 2:
        # 밖의 진짜 나눠야 하는 값은 stay, number로 진법 계산
        number = num
        mid = ''
        while number > 0:
            if number % n >= 10:
                mid += num_dic[number % n]
            else:
                mid += str(number % n)
            number //= n
            
        num += 1
        string += mid[::-1]
    
    return string

def solution(n, t, m, p):
    return p_decimal(n, t, m ,p)[p-1::m][:t]