import random

def random_selection(items):
    selected_item = random.choice(items)
    return selected_item

# Example usage
my_list = [
    "hi", 
    "J",
    "同花顺",
    "Codfish",
    "蓝胖子",
    "Yuichi",
    "run",
    "jayz3",
    "笔尖微凉",
    "阿童木",
    "侃豺小哥",
    "mil",
    "2kod",
    "灵虚",
    "李明",
    "oldfo4",
    "knative",
    "Hello",
    "Risk off",
    "曦月",
    "NiGO",
    "Gale",
    "请务必优秀",
    
    "FORWARD",
    "Lis",
    "hxy",
    
    "Fan",
    "温雅的岚岚",
    "糖",
    "杜欣远",
    "你怎么连话都说不清楚",
    "一定能好",
    "小妖怪的夏天",
    "GuoXiaogang",
    "无悔",
    "David.Hu",
    "Cheng",
    "m的二次方",
    "冲向未来",
    "王宇",
    "彩虹",
    "知足常乐",
    "z",
    "多宝鱼鱼",
    "Xlh",
    "无糖美式加冰",
    "HotelSugar"]
print("参与抽奖的读者:\n" + str(my_list[26:]))
selected = random_selection(my_list[27:])
print("------------------------------------- \n被选中:", selected)