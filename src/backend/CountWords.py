def Countwords(list):
    cnt = {}
    for i in list:
        cnt[i] = cnt.get(i, 0)+1
    return cnt
