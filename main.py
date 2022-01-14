from pythonping import ping
import matplotlib.pyplot as plt

def ping_list(ip_list):
    
    result_list = []
    rtt_avg_list = []
    for i in ip_list:
        result = ping(i, count=10, verbose=True)
        rtt_avg_list.append(result.rtt_avg)
        print("host: {0} rtt_avg: {1}".format(i, result.rtt_avg))

    #plt.plot(rtt_avg_list)
    plt.bar(ip_list, rtt_avg_list)
    plt.ylabel('rtt_avg')
    plt.show()

    return 


if __name__ == '__main__':
    ip_list = ["geosearch1.kmsext.dk",
               "geosearch2.kmsext.dk",
               "gw1.kmsext.dk",
               "gw2.kmsext.dk",
               "gw3.kmsext.dk",
               "gw4.kmsext.dk",
               "kmsload106.kmsext.dk",
               "kmsload110.kmsext.dk",
               "kmsload125.kmsext.dk",
               "kmsload126.kmsext.dk",
               "kmsload127.kmsext.dk",
               "kmsload129.kmsext.dk",
               "kmsload130.kmsext.dk",
               "kmsload133.kmsext.dk",
               "kmsload157.kmsext.dk",
               "kmsload159.kmsext.dk",
               "kmsload69.kmsext.dk",
               "kmsload77.kmsext.dk",
               "kmsload80.kmsext.dk",
               "kmsload85.kmsext.dk",
               "kmsloadfs4.kmsext.dk",
               "kmsloadfs5.kmsext.dk",
               "load188.kmsext.dk",
               "load189.kmsext.dk",
               "load190.kmsext.dk",
               "load191.kmsext.dk",
               "load194.kmsext.dk",
               "load195.kmsext.dk",
               "load196.kmsext.dk",
               "load197.kmsext.dk",
               "load198.kmsext.dk",
               "load199.kmsext.dk",
               "load201.kmsext.dk",
               "load202.kmsext.dk",
               "load204.kmsext.dk",
               "load205.kmsext.dk",
               "load206.kmsext.dk",
               "load210.kmsext.dk",
               "load211.kmsext.dk",
               "load214.kmsext.dk",
               "load215.kmsext.dk",
               "load216.kmsext.dk",
               "load217.kmsext.dk",
               "load222.kmsext.dk",
               "load223.kmsext.dk",
               "load224.kmsext.dk",
               "load225.kmsext.dk",
               "loaddb11.kmsext.dk",
               "loaddb12.kmsext.dk",
               "loaddb13.kmsext.dk",
               "loaddb14.kmsext.dk",
               "loaddb15.kmsext.dk",
               "loaddb16.kmsext.dk",
               "loadfs7.kmsext.dk",
               "splind1.kmsext.dk",
               "splind2.kmsext.dk",
               "splseh1.kmsext.dk",
               "swbd20.kmsext.dk",
               "swbd21.kmsext.dk",
               "swbd22.kmsext.dk",
               "swbd23.kmsext.dk",
               "swbd24.kmsext.dk",
               "swbd25.kmsext.dk",
               "w3live3.kmsext.dk"]
    ip_list_test = ["127.0.0.1", "rpi4-20211030", "OnePlus-7T", "dr.dk", "Chromecast", "192.168.1.114"]
    ping_list(ip_list_test)
