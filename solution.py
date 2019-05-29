
def solution(N):

    if N is None:
        raise ValueError("N is None")

    if not isinstance(N, int):
        raise TypeError("N must to be int, not a " % str(type(N)))

    if N < 0:
        raise ValueError("N value must to be greater tham 0")
     
    if N == 0:
        return 1
    else:
        return N*solution(N-1)