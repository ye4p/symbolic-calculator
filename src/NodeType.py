from enum import IntEnum 

class NodeType(IntEnum):
    SYMBOL=0
    FRACTION=1
    POWER=2
    TERM=3
    EXPRESSION=4
    FUNCTION=5
