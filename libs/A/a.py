#!/usr/bin/env python
# coding=utf-8
from b import B

class A():
    def __init__(self, name):
        self._name = name

    def run(self):
        print("A: It's your name? %s" % self._name)
        B.hello()
