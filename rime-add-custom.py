#!/usr/bin/python
# -*- coding: utf-8 -*-
# 你需要首先安装 pypinyin 包：
# /usr/bin/python -m ensurepip
# /usr/bin/python -m pip install pypinyin
# 此脚本应用于自然码, 或者可以通过修改码表来实现其他双拼
# 使用此脚本前请确保custom phrase文件尾部有空行
IsCodeReformating = True # 修改为False关闭三字词转换，修改为True开启三字词转换

import sys
import os
import codecs

def reformat_code(code):
    code = str(code)  # for comp
    code = code.replace(' ', '')
    if len(code) == 6:  # 3字词
        newcode = code[0] + code[2] + code[-2:]
    if len(code) >= 8:  # 四字及以上
        newcode = code[0] + code[2] + code[4] + code[-2]
    return newcode

try:
    home = os.path.expanduser("~")
    custom_phrase = codecs.open(
        home + "/Library/Rime/custom_phrase.txt", "a", "utf-8")
except Exception as e:
    print e
    sys.exit()

gap_space = False  # 字字之间是否有空格
is_workflow_mode = True

Initials_translation_table = {
    u'zh': 'v',
    u'sh': 'u',
    u'ch': 'i'
}

Finals_translation_table = {
    u'iu': 'q',
    u'ia': 'w',
    u'ua': 'w',
    u'uan': 'r',
    u'ue': 't',
    u've': 't',
    u'ing': 'y',
    u'uai': 'y',
    u'uo': 'o',
    u'un': 'p',
    u'iong': 's',
    u'ong': 's',
    u'iang': 'd',
    u'uang': 'd',
    u'en': 'f',
    u'eng': 'g',
    u'ang': 'h',
    u'an': 'j',
    u'ao': 'k',
    u'ai': 'l',
    u'ei': 'z',
    u'ie': 'x',
    u'iao': 'c',
    u'ui': 'v',
    u'ou': 'b',
    u'in': 'n',
    u'ian': 'm'
}

if not is_workflow_mode:
    argv = sys.argv
    base = 0
else:
    argv = sys.argv[1].split(' ')
    base = -1

word = argv[base + 1] if len(argv) > base + 1 else None
code = argv[base + 2] if len(argv) > base + 2 else None
freq = argv[base + 3] if len(argv) > base + 3 else None

if word is None:
    sys.exit()

if word.isalpha() == True and code is None:
    code = word

res = code

if code is None:
    try:
        from pypinyin import pinyin, lazy_pinyin, Style
    except:
        sys.exit()
    initials = pinyin(word.decode('utf-8'), style=Style.INITIALS, strict=False)
    finals = pinyin(word.decode('utf-8'), style=Style.FINALS, strict=False)
    res = ""
    for initial in initials:
        initial_ori = initial
        initial = initial[0]
        if initial != '':
            res += initial if initial not in Initials_translation_table.keys(
            ) else Initials_translation_table[initial]
        else:
            res += finals[initials.index(initial_ori)][0] if len(finals[initials.index(
                initial_ori)][0]) > 1 else finals[initials.index(initial_ori)][0] * 2
            res += " " if gap_space is True else ""
            continue
        final = finals[initials.index(initial_ori)][0]
        res += final if final not in Finals_translation_table.keys(
        ) else Finals_translation_table[final]
        res += " " if gap_space is True else ""
    if IsCodeReformating is True:
        res = reformat_code(res)

line = word.decode('utf-8') + "	" + res.decode('utf-8') + \
    (("	" + str(freq)) if freq != None else "") + '\n'
custom_phrase.write(line)
custom_phrase.close()

print u"成功添加：",
print line,