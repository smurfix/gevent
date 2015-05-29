# this produces syntax error on Python3


__all__ = ['reraise']


def reraise(type, value, tb):
    exec("raise type, value, tb")
