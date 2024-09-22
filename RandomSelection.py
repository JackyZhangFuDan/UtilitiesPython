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
    "hxy",]
selected = random_selection(my_list[23:])
print("被选中:", selected)