#coding:utf-8

from enum import Enum
class CustomerKind(Enum):
    """业务端类型"""

    #: 家长
    parent = 0
    #: 教师
    teacher = 1
    #: 校园
    campus = 2
    #: 学生
    student = 3



print CustomerKind.parent
