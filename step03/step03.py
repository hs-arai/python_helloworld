import sys
import datetime
from time import timezone

def main():
    print(sys.argv[1].format(str))
    # 引数が0以上の整数じゃなかった場合
    # dt = datetime.datetime.fromtimestamp(1654663852)
    dt = datetime.datetime.fromtimestamp(int(sys.argv[1]))
    print(dt)

    t_delta = datetime.timedelta(hours=9)
    JST = datetime.timezone(t_delta, 'JST')
    dt2 = datetime.datetime.fromtimestamp(int(sys.argv[1]), JST)
    print(dt2.strftime('%Y-%m-%dT%H:%M:%S%z'))

    # now = datetime.fromtimestamp(dt2, JST)
    # print(repr(now))
    # print(now)

    # サンプルと表示される時間が違う！？

if __name__ == "__main__":
    main()
    print("end")