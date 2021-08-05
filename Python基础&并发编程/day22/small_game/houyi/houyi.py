# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/8/4 16:57
# @Software       : Python_study
# @Python_verison : 3.7
from small_game.game.game import Game      # 如果导入不了，需要make_directory as-->Sources Root

class HouYi(Game):
    def __init__(self,hp,power):
        super().__init__(hp,power)              # 使用父类的属性
        self.defense = 100                      # 子类自己的派生属性

    def houyi_fight(self,enemy_hp,enemy_power):
        while True:
            self.hp = self.hp + self.defense - enemy_power
            enemy_hp = enemy_hp - self.power
            print('我的血量:{} 敌人的血量：{}'.format(self.hp,enemy_hp))     # 使用format的格式化字符串
            if self.hp <= 0:
                print('我输了')
                break
            elif enemy_hp <=0 :
                print('我赢了')
                break
        # else:
            # raise Exception('没有平局')     # 不存在平局，


HouYi(hp=1000,power=100).houyi_fight(enemy_hp=500,enemy_power=200)