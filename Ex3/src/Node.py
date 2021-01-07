class Node:

    def __init__(self, key: int, tag: int = -1, value: float = 0, pos: tuple = None):
        self.key = key
        self.tag = tag
        self.value = value
        self.pos = pos
        self.inside = {}
        self.outside = {}
        self.prev = None

    def add_inside(self, node_id: int, weight: float) -> bool:
        if self.key is node_id:
            return False
        if self.inside.get(node_id):
            if self.inside.get(node_id) != weight:
                self.inside[node_id] = weight
                return True
            return False
        self.inside.setdefault(node_id, weight)
        return True

    def add_outside(self, node_id: int, weight: float) -> bool:
        if self.key is node_id:
            return False
        if self.outside.get(node_id):
            if self.outside.get(node_id) != weight:
                self.outside[node_id] = weight
                return True
            return False
        self.outside.setdefault(node_id, weight)
        return True

    def remove_inside(self, node_id: int) -> bool:
        if self.inside.get(node_id):
            del self.inside[node_id]
            return True
        return False

    def remove_outside(self, node_id: int) -> bool:
        if self.outside.get(node_id):
            del self.outside[node_id]
            return True
        return False

    def get_outside(self) -> dict:
        return self.outside

    def get_inside(self) -> dict:
        return self.inside

    def set_value(self, v) -> None:
        self.value = v

    def get_value(self) -> float:
        return self.value

    def set_tag(self, t) -> None:
        self.tag = t

    def get_tag(self) -> int:
        return self.tag

    def get_key(self) -> int:
        return self.key

    def set_prev(self, p) -> None:
        self.prev = p

    def get_prev(self):
        return self.prev

    def get_pos(self)->tuple:
        return self.pos
    def set_pos(self,p:tuple)->None:
        self.pos=p
    def __str__(self) -> str:
        return f"key:{self.key},inside:{self.get_inside()},outside:{self.get_outside()}"

    def __repr__(self) -> str:
        return f"key:{self.key},pos:{self.pos},inside:{self.get_inside()},outside:{self.get_outside()}"

    def __eq__(self, other) -> bool:
        return other.key == self.key and other.pos == self.pos

    def __lt__(self, other):
        return self.value < other.value

    def as_dict(self) -> dict:
        tmp_dict= self.__dict__
        return tmp_dict

    # todo make equals function


if __name__ == '__main__':
    n = Node(1)
    print(n.add_outside(2, 2.5))
    print(n.add_outside(22, 2.5))
    print(n.add_inside(22, 2.52))
    print(n)
    print(len(n.outside))
    print(n.remove_inside(22))
    print(n.remove_inside(22))
    print(n.remove_outside(2))
    print(n.remove_outside(2))
    print(n)
