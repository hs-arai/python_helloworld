import sys
import datetime
from time import timezone
from turtle import st

def main():

    try:
        int(sys.argv[1])
    except ValueError:
        print('Error: 数字変換できない', file=sys.stderr)
        sys.exit(1)
    else:
        ()

    if (int(sys.argv[1]) < 0):
        print('Error: 0未満', file=sys.stderr)
        sys.exit(1)

    # print(sys.argv[1].format(str))
    # 引数が0以上の整数じゃなかった場合
    dt = datetime.datetime.fromtimestamp(int(sys.argv[1]))
    # print(dt)
    # print(dt.strftime('%Y-%m-%dT%H:%M:%S%z'))

    t_delta = datetime.timedelta(hours=9)
    JST = datetime.timezone(t_delta, 'JST')
    dt2 = datetime.datetime.fromtimestamp(int(sys.argv[1]), JST)
    print(dt2.strftime('%Y-%m-%dT%H:%M:%S%z'))

if __name__ == "__main__":
    main()
    # print("end")