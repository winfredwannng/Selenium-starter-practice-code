import pytest

test_data = [
    {
        'usr': 'admin',  # 正常登入
        'psw': '123456'
    },
    {
        'usr': 'admin1',  # 账号不存在
        'psw': '123456'
    },
    {
        'usr': 'admin',  # 密码错误
        'psw': '12345'
    },
    {
        'usr': '',  # 账号或密码为空
        'psw': ''
    },
]


@pytest.mark.parametrize('param', test_data)
def test_login(param): # 这个param需要和上面的'param'一致
    print(param) # 打印


if __name__ == '__main__':  # 定义主函数
    pytest.main()  # 调用pytest
