#-*- coding:utf-8 -*-

# 登录
def login():
    ls = []
    i = 3
    login_name = input('请输入账号:')
    login_password = input('请输入密码:')
    with open(file='info', mode='r+', encoding='utf-8') as file:
        for line in file:
            ls.append(line)
    if ls[0].strip() == login_name.strip() and ls[1].strip() == login_password.strip():
        print('恭喜你登錄成功')
        return('欢迎{}登录系统，你的身份是{}'.format(login_name.strip(),ls[2].strip()))
    else:
        print('登錄失敗')

def main():
    if __name__ == '__main__':
        print('欢迎进入江西理工大学校园管理系统')
    user_name,user_role = login()
    if user_role == 'student':
        print('登录','查看课程','查看班级')
    elif user_role == 'teacher':
        print('教学班级','教学课程')
    else:
        print('创建讲师','创建班级','创建课程')

