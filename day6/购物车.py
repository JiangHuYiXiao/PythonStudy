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
# V1

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


# V2优化版
# 将商品列表命名为一个字典，包含商品名称、价格
# 用户添加完产品之后可以删除产品

# 命名商品列表包含商品名称和价格
li = [
    {'name':'香蕉','price':4},
    {'name':'苹果','price':6},
    {'name':'橘子','price':3},
    {'name':'火龙果','price':5},
    ]
shopping_cart ={}
print('欢迎光临江湖一笑水果店')  # 打印欢迎语句
for i,j in enumerate(li):  # 输出商品名称和价格明细
    print(i+1,j)
you_money = input('请输入你的资金:')   # 要求客户输入资金
while 1:
    if int(you_money) >= 3:    # 判断客户资金是否足够买店铺里面最少价格的产品
        goods_num = input('请输入你需要购买的商品序号:')
        if goods_num.isdigit():
            if int(goods_num) >= 1 and int(goods_num) <= len(li):
                num = input('请输入你需要购买商品的数量:')
                if li[int(goods_num )- 1]['name'] in shopping_cart:
                    print(shopping_cart[li[int(goods_num)-1]['name']])
                    shopping_cart[li[int(goods_num)-1]['name']] = shopping_cart[li[int(goods_num)-1]['name']] + int(num)
                else:
                    shopping_cart[li[int(goods_num)-1]['name']] = int(num)
                print('你的购物车产品为:',shopping_cart)
                you_money = int(you_money) -li[int(goods_num)-1]['price']*int(num)
                print('你的资金余额为:',you_money)
                if you_money < 3:
                    print('你的资金不够')
                    break
            else:
                print('你输入商品序号不存在，请重新输入:')
        elif goods_num.upper() == 'Q':
            break

        else:
            print('你输入商品序号错误，请重新输入:')
    else:
        print('资金不够，欢迎下次光临！！！')
        break