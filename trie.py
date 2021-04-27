"""
字典树
"""

class Node(object):
    # 1个node是一个字典书的叶子，它包含两个属性，子节点和直
    def __init__(self,value):
        self._children = {}  # 子节点
        self._value = value

    def _add_child(self,char,value, overwrite=False):
        """
        :param char: 子节点字典的建
        :param value:  子节点的直
        :param overwrite: 是否改写子结点的值
        :return:__add_child
        """
        child = self._children.get(char)  # 通过健去获取节点
        if child is None:
            child = Node(value)  # 如果该子节点不存在则创造节点，并将他添加到树上
            self._children[char] = child
        elif overwrite:  # 判断是否要改写子结点的直
            child._value = value
        return child


class Trie(Node):   # node是树的最小单位

    def __init__(self):
        super().__init__(None)  # 注意此处的None

    def __contains__(self, key):
        return self[key] is not None

    def __getitem__(self, key):
        """
        从上往下遍历，如果走到了根节点就返回None,如果没有就返回该子结点的直
        """
        state = self
        for char in key:
            state = state._children.get(char)
            if state is None:
                return None
        return state._value

    def __setitem__(self, key, value):
        """
        给数添加叶子，并将数值付给最后一个叶子
        """
        state = self
        for i,char in enumerate(key):
            if i < len(key) -1:
                state = state._add_child(char,None)
            else:
                state = state._add_child(char,value, True)

if __name__ == "__main__":
    trie = Trie()
    trie['自然'] = 'nature'
    print(trie.__dict__)