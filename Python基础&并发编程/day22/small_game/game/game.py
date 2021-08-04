# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/8/4 16:57
# @Software       : Python_study
# @Python_verison : 3.7
'''
要求1：
一个回合制小游戏，每个角色都有hp、power，hp代表血量，power代表攻击力，hp的初始值为1000，power为200.
定义一个fight方法：
hp_final = hp - enemy_power
hp_enemy = enemy_hp - power
两个人的血量对比，剩下多的获胜

要求2：
多了一个角色，叫做后裔，后裔继承了角色的hp和power，但是多了一个护甲的属性
houyi_hp = hp + defense - enemy_power

要求3：
加入模块的改造，将类HouYi与类角色通过两个文件进行管理
加入异常的改造，当存在平局时，抛出异常
'''
class Game():
    def __init__(self,hp,power):
        self.hp = hp
        self.power = power

    def fight(self,enemy_power,enemy_hp):
        '''打斗'''
        hp_final = self.hp - enemy_power
        hp_enemy = enemy_hp - self.power
        if hp_final > hp_enemy:
            print('我赢了')
        elif hp_final < hp_enemy:
            print('敌人赢了')
        else:
            print('平局')

# Game(1000,300).fight(1000,500)
