from collections import Counter

max = 10
w = [2, 3, 4, 5, 6]
cal = [400, 500, 800, 900, 1100]
name = 'ABCDE'


table = [[0, 0, []]]
w_max = 0
cal_max = 0
b_max = []


def check(table, ans, i):
    for a in table:
        if a[0] == ans[0] + w[i] and a[i] >= ans[1] + cal[i]:
            return False
    return True


for i in range(len(name)):
    for ans in table:
        if ans[0] + w[i] <= max and name[i] not in ans[2]:
            if check(table, ans, i):
                w_temp = ans[0] + w[i]
                cal_temp = ans[1] + cal[i]
                b_temp = ans[2] + [name[i]]
                table.append([w_temp, cal_temp, b_temp])
                print(w_temp, cal_temp, b_temp)

                if cal_temp > cal_max:
                    w_max = w_temp
                    cal_max = cal_temp
                    b_max = b_temp

print("answer: ", w_max, cal_max, b_max)
