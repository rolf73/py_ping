import matplotlib.pyplot as plt
import sys


def plot_result(result_list):
    columns = []
    data = []
    for item in result_list:
        print(item)
        if len(item) == 3:
            columns.append(item[1])
            data.append(float(item[2]))
        else:
            columns.append(item[0])
            data.append(float(item[1]))

    plt.xticks(rotation=90)
    plt.bar(columns, data)
    plt.ylabel('rtt_avg')
    plt.show()


if __name__ == '__main__':
    data = sys.stdin.readlines()
    result_list = []
    for line in data:
        result_list.append(line.strip().split(','))
    print(result_list)
    plot_result(result_list)
