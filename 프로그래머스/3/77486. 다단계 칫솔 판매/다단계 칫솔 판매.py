def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)
    name_to_parent = dict(zip(enroll, referral))
    idx_map = {name: i for i, name in enumerate(enroll)}

    for name, cnt in zip(seller, amount):
        money = cnt * 100

        while name != '-' and money > 0:
            commission = money // 10
            profit = money - commission
            answer[idx_map[name]] += profit
            name = name_to_parent[name]
            money = commission

    return answer