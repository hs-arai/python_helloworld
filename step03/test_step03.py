import pytest
import sys

from step03 import main

# 正常系確認
def test_main(capfd, mocker):
    test_argments = ['', '100']
    mocker.patch('sys.argv', return_value=test_argments)
    main()
    out, err = capfd.readouterr()
    assert out == '1970-01-01T09:00:01+0900\n'
    assert err == ''

# from datetime import datetime, timezone, timedelta
# from src.unixtime2dateformat import

# # 正常系を含む境界値試験
# @pytest.mark.parametrize(('argv', 'expected'),[
#     (['', '-100'], 1),
#     (['', '-1'], -1)
# ])
