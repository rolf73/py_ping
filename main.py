from pythonping import ping
import matplotlib.pyplot as plt

def ping_list(ip_list):
    
    result_list = []
    rtt_avg_list = []
    for i in ip_list:
        result = ping(i, count=1, verbose=False)
        rtt_avg_list.append(result.rtt_avg)
        print("host: {0} rtt_avg: {1}".format(i, result.rtt_avg))

    #plt.plot(rtt_avg_list)
    plt.bar(ip_list, rtt_avg_list)
    plt.ylabel('rtt_avg')
    plt.show()

    return 


if __name__ == '__main__':
    ip_list = ['127.0.0.1', 'rpi4-20211030', 'OnePlus-7T', 'dr.dk', 'Chromecast', 'LGwebOSTV', '192.168.1.114']
    ping_list(ip_list)
