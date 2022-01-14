import matplotlib.pyplot as plt


def plot_result(result_list):
    columns = []
    data = []
    for item in result_list:
        print(item)
        columns.append(item[0])
        data.append(float(item[1]))

    plt.bar(columns, data)
    plt.ylabel('rtt_avg')
    plt.show()


if __name__ == '__main__':
    result_list = []
    infile = open('result.txt', 'r')
    for line in infile:
        result_list.append(line.strip().split(','))
    infile.close()
    print(result_list)
    plot_result(result_list)
