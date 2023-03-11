"""
该模块中super_lotto()函数功能为随机生成一注大乐透，double_chromosphere()函数功能为随机生成一注双色球。
"""

import random

def super_lotto():
    red_ball = sorted(random.sample(range(1 , 36) , 5))
    blue_ball = sorted(random.sample(range(1 , 13) , 2))
    
    return f"本次大乐透结果——红球：{red_ball}，蓝球：{blue_ball}。"

def double_chromosphere():
    red_ball = sorted(random.sample(range(1 , 34) , 6))
    blue_ball = sorted(random.sample(range(1 , 17) , 1))
    
    return f"本次双色球结果——红球：{red_ball}，蓝球：{blue_ball}。"