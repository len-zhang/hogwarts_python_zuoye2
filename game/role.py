# -*- coding:utf-8 -*-
class TongLao:
    def __init__(self, power, hp):
        self.power = power
        self.hp = hp

    def see_people(self, name):
        if name == "WYZ":
            print("师弟！！！！")
        elif name == "LQS":
            print("呸，贱人")
        elif name == "DCQ":
            print("叛徒！我杀了你")

    def fight_zms(self, enemy_hp, enemy_power):
        new_power = self.power * 10
        new_hp = self.hp / 2
        enemy_final_hp = enemy_hp - new_power
        my_final_hp = new_hp - enemy_power
        print(f"本轮折梅手后的攻击是{new_power}, 折梅手后的血量是{new_hp}")
        return enemy_final_hp, my_final_hp


class XuZhu(TongLao):
    def __init__(self, power, hp):
        super().__init__(power, hp)

    def read(self):
        print("罪过罪过")
        final_hp = self.hp + 1
        return final_hp


# if __name__ == "__main__":
#     x = TongLao()
#     x.see_people("WYZ")