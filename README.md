# SSPanel 签到脚本

## 使用方法

1. 命令行添加参数 (`账号`, `密码`, `域名`):

    ```
    $ python sspanel_checkin.py username password domain
    ```

1. 在代码中添加参数 (`账号`, `密码`, `域名`): 

    ```python
    if __name__ == '__main__':
        SSPanel(username, password, domain)
        # SSPanel()
    ```

    保存后在命令行中运行:

    ```
    $ python sspanel_checkin.py
    ```
