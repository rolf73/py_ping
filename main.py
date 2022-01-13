from pythonping import ping


def run():
    ip_list = ['127.0.0.1']
    for i in ip_list:
        ping(i, count=5, verbose=True)
    return


if __name__ == '__main__':
    run()
