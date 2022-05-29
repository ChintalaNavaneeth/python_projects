import speedtest

def test():
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    return res["download"], res["upload"], res["ping"]


def main():
    for i in range(3):
        print("making test #{}".format(i+1))
        d, u, p = test()
        print(f"Test {i+1}")
        print(f"Download {d}")
        print(f"Upload {u}")
        print(f"Ping {p}")


if __name__ == "__main__":
    main()