# sspanel_checkin.py

## 使用方法

1. 命令行添加参数 (`账号`, `密码`, `域名`): 

    > $ python sspanel_checkin.py username password domain

2. 在代码中添加参数 (`账号`, `密码`, `域名`): 

    ```python
    def main():
        ss = SSPanel(username, password, domain)
        ss.login()
        ss.checkin()
    ```

    > $ python sspanel_checkin.py