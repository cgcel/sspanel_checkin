# sspanel_checkin.py

## 使用方法

1. 命令行添加参数: 

    > $ python sspanel_checkin.py username password

1. 在代码中添加账密: 

    ```python
    def main():
        ss = SSPanel(username, password)
        ss.login()
        ss.checkin()
    ```

    > $ python sspanel_checkin.py