from pythonping import ping
import sys


def ping_list(ip_list):

    for i in ip_list:
        result = ping(i[0], count=10, verbose=False)
        if len(i) == 2:
            print("{0}, {1}, {2}".format(i[0], i[1], result.rtt_avg))
        else:
            print("{0}, {1}".format(i[0], result.rtt_avg))


if __name__ == '__main__':
    data = sys.stdin.readlines()
    host_list = []
    for line in data:
        if line[0] != '#':
            line = line.replace('\n', '').replace('"', '').strip().split(',')
            host_list.append(line)
    ping_list(host_list)
