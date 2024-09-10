import random

def random_selection(items):
    selected_item = random.choice(items)
    return selected_item

# Example usage
my_list = [1, 2, 3, 4, 5]
selected = random_selection(my_list)
print("Selected item:", selected)