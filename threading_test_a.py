from threading import Thread
import time


def test(id):
    print("hello word %s !"%id)
    time.sleep(1)
    print("123")


def main():
    for i in range(10):
        p = Thread(target=test,args=(i,))
        p.start()

    # for i in range(10):
    #     test()



if __name__ == '__main__':
    main()
