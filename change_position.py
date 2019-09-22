"""
有一组“+”和“-”符号，要求将“+”排到左边，“-”排到右边，写出具体的实现方法。
"""


def change_position(s: str):
    """
    将+替换为0，—替换为1，然后排序，最后换回来
    :param s:字符str
    :return:排好后的结果
    """
    return ''.join(sorted(s.replace('+', '0').replace('-', '1'))).replace('0', '+').replace('1', '-')


if __name__ == '__main__':
    ss = "++++++----+++----"
    print(change_position(ss))
