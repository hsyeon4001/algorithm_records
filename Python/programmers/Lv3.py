# 베스트앨범
def solution(genres, plays):
    answer = []
    gp_dict = {}
    sum_dict = {}

    for i in range(len(genres)):
        if genres[i] in gp_dict:
            gp_dict[genres[i]].append((i, plays[i]))
            sum_dict[genres[i]] += plays[i]
        else:
            gp_dict[genres[i]] = [(i, plays[i])]
            sum_dict[genres[i]] = plays[i]

    for genre in gp_dict.keys():
        gp_dict[genre] = sorted(gp_dict[genre], key=lambda x: x[1], reverse=True)

    sum_dict = sorted(sum_dict.items(), key=lambda x: x[1], reverse=True)
    print(gp_dict, sum_dict)
    for genre, play in sum_dict:
        if len(gp_dict[genre]) > 1:
            print(gp_dict[genre][1])
            answer.extend([gp_dict[genre][0][0], gp_dict[genre][1][0]])
        else:
            answer.append(gp_dict[genre][0][0])

    return answer
print(solution(["a", "b", "a", "b", "c"], [100, 200, 300, 400, 500]))