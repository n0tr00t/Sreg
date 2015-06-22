#!/usr/bin/env python
# coding=utf8
# author=e0@2015<ff0000team>


def inBlack(s):
    return highlight('') + "%s[30;2m%s%s[0m" % (chr(27), s, chr(27))


def inRed(s):
    return highlight('') + "%s[31;2m%s%s[0m" % (chr(27), s, chr(27))


def inGreen(s):
    return highlight('') + "%s[32;2m%s%s[0m" % (chr(27), s, chr(27))


def inYellow(s):
    return highlight('') + "%s[33;2m%s%s[0m" % (chr(27), s, chr(27))


def inBlue(s):
    return highlight('') + "%s[34;2m%s%s[0m" % (chr(27), s, chr(27))


def inPurple(s):
    return highlight('') + "%s[35;2m%s%s[0m" % (chr(27), s, chr(27))


def inWhite(s):
    return highlight('') + "%s[37;2m%s%s[0m" % (chr(27), s, chr(27))


def highlight(s):
    return "%s[30;2m%s%s[1m" % (chr(27), s, chr(27))
