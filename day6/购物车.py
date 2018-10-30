#-*- coding:utf-8 -*-

#4、输出商品列表，用户输入序号，显示用户输入的商品，
# li = ['香蕉','苹果','橘子','火龙果']
# 各个商品的价格为：4,6,5,8
# 要求：
# 1、首先让用户输入资产金额
# 2、页面显示序号+商品名称，如：
# 1 香蕉
# 2 苹果
# ...
# 3、用户输入选择的商品序号，然后打印商品名称并且添加到购物车列表中
# 4、如果用户输入的商品序号有错误，则提示输入有误，请重新输入。
# 5、如果用户添加到购物车列表的所有商品金额大于用户输入的资产则，提示用户超过资产，不能添加到购物车
# 6、用户输入q或者Q退出程序。
shopping_cart = []
you_money = input('请输入你的资产:')
print('你的资产为：',you_money)
li = ['香蕉','苹果','橘子','火龙果']
li_money = {'香蕉':4,'苹果':6,'橘子':5,'火龙果':8}
for i,j in enumerate(li):
    print(i+1,j)
while int(you_money) >= 4:
        goods_num = input('请输入你需要购买的商品序号:')
        if goods_num.isdigit():
            if int(goods_num) >= 1 and int(goods_num) <= len(li):
                goods = li[int(goods_num)-1]
                print(goods)
                shopping_cart.append(goods)
                print(shopping_cart)
                banana = shopping_cart.count('香蕉') * li_money['香蕉']
                apple = shopping_cart.count('苹果') * li_money['苹果']
                orange = shopping_cart.count('橘子') * li_money['橘子']
                pitaya = shopping_cart.count('火龙果') * li_money['火龙果']
                remain_money = int(you_money) -banana - apple - orange - pitaya
                print('你的剩余资产为:' , remain_money)
                if remain_money < 4:
                    print('你的资产不够，欢迎下次光临')
            else:
                print('你输入的商品序号有误，请重新输入:')

        elif goods_num.upper() == 'Q':
            break
        else:
            print('你输入的商品序号有误，请重新输入:')

if int(you_money) < 4:
    print('你的资产不够，欢迎下次光临')
