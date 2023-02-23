def solution(n):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, 3)
        rev_base += str(mod)
    return int(rev_base,3)
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력
