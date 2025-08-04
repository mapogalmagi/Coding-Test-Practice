def check_num(s):
    cnt = 0
    num = s[0]
    for w in s:
        if w == num:
            cnt += 1
        else:
            return s[cnt:], cnt
    return s[cnt:], cnt  # 끝까지 동일 문자일 경우 처리

word = list(input())
first = True
cnt_w = 0
cnt_others = 0
idx = 0
answer = True
word_list = ['w', 'o', 'l', 'f']

while word:
    if first:
        if word[0] != 'w':
            answer = False
            break
        word, cnt_w = check_num(word)
        idx = 1       # ← 여기! idx를 1로 바로 세팅해야 다음은 'o'부터 체크함
        first = False
    else:
        if not word or word_list[idx] != word[0]:
            answer = False
            break
        word, cnt_others = check_num(word)
        if cnt_w != cnt_others:
            answer = False
            break

        if idx in (1, 2):
            idx += 1
        elif idx == 3:
            idx = 0
            first = True

# 마지막에 남은 상태가 'f'까지 정확히 끝났는지 확인
if answer and not word and idx == 0 and first:
    print(1)
else:
    print(0)