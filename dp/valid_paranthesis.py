# Valid paranthesis

def backtrack(s: str , open_cnt , back_cnt , n):
    if len(s) == 2*n:
        print(s)

    if open_cnt < n:
        backtrack(s + '(' , open_cnt + 1 , back_cnt , n)

    if back_cnt < open_cnt:
        backtrack(s + ')' , open_cnt , back_cnt + 1 , n)

def generate(n):
    if n % 2 :
        raise Exception(f" should be even number no odd")
    n //=2
    backtrack('' , 0 , 0 , n)

generate(6)