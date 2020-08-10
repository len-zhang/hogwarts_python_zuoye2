# -*- coding:utf-8 -*-
from game.role import TongLao, XuZhu
import random

tonglao_init_hp = 4000
qiushui_init_hp = 10000
tonglao_power = random.randint(100, 200)
qiushui_power = random.randint(300, 400)
tonglao = TongLao(tonglao_power, tonglao_init_hp)
xuzhu = XuZhu(0, 100)


def fight():
    game_round = 0
    qiushui_hp = qiushui_init_hp  # 最开始时将秋水初始血量赋值给秋水血量
    while True:
        game_round = game_round + 1
        print(f"轮次：{game_round}")
        tonglao.power = random.randint(100, 200)  # 将童姥实例的攻击重新随机
        qiushui_power = random.randint(300, 400)  # 将秋水的攻击重新随机
        tonglao.see_people("LQS")  # 调用看到李秋水方法
        xuzhu_hp = xuzhu.read()  # 调用虚竹念经方法的同时，将念经方法return的血量赋值给虚竹血量
        xuzhu.hp = xuzhu_hp  # 将虚竹血量重新赋值给虚竹实例血量，用于下一次循环时调用念经方法时使用
        qiushui_hp, tonglao_hp = tonglao.fight_zms(qiushui_hp, qiushui_power)  # 调用童姥折梅手方法，将return返回值分别传给秋水血量和童姥血量
        tonglao.hp = tonglao_hp  # 将童姥血量重新赋值给童姥实例血量，用于下一次循环时调用折梅手方法时使用
        print("秋水血量为{:.2f}, 童姥血量为{:.2f}, 虚竹血量为{:.2f}".format(qiushui_hp, tonglao_hp, xuzhu_hp))
        if qiushui_hp <= 0:
            print("秋水失败")
            break
        elif tonglao_hp <= 0:
            print("童姥失败")
            break


if __name__ == "__main__":
    fight()
