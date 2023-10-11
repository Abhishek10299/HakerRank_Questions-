if __name__ == "__main__":
    std_list = []
    scr_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        std_list.append([name, score])
        scr_list.append(score)

    desired_score = list(sorted(set(scr_list)))[1]

    for name, score in sorted(std_list):
        if score == desired_score:
            print(name)
