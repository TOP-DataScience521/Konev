
def tree_leaves(tree: list) -> int:
    """
    рекурсивную функцию с именем tree_leaves, которая считает количество листьев на дереве.

    параметры:
        tree (list): Древовидная структура, представленная в виде списка, 
                    где листья обозначены строкой 'leaf', а ветви - вложенными списками.

    return:
        int: Общее количество листьев 'leaf' во всем древе.

    """


    sheet = 0
    for i in tree:
        if i == 'leaf':
            sheet += 1
            # print (f'иф {sheet}')   
        elif isinstance(i,list):
            sheet += tree_leaves (i) 
            # print (f'эндиф {sheet}')    
    return sheet


    

# >>> tree = [[[['leaf', 'leaf', 'leaf', 'leaf'], 'leaf', 'leaf', 'leaf'], [['leaf', 'leaf'], 'leaf', 'leaf'], ['leaf', 'leaf', 'leaf']], [['leaf', 'leaf'], ['leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf'], 'leaf', 'leaf', 'leaf'], [['leaf'], ['leaf', 'leaf', ['leaf', 'leaf', 'leaf']], 'leaf', 'leaf'], ['leaf', 'leaf', ['leaf', 'leaf'], 'leaf']]
# >>> tree_leaves(tree)
# 38
# >>>
