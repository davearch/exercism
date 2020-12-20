def latest(scores):
    return scores[-1]


def personal_best(scores):
    best = 0
    for s in scores:
        if s > best:
            best = s
    return best


def personal_top_three(scores):
    from heapq import heappush, heapreplace
    minh = []
    for i in range(len(scores)):
        if i < 3:
            heappush(minh, scores[i])
        elif scores[i] > minh[0]:
            heapreplace(minh, scores[i])
    if len(minh) == 3 and minh[1] > minh[2]:
        minh[1], minh[2] = minh[2], minh[1]
    return minh[::-1]