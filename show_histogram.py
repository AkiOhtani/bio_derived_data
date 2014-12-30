#! /usr/bin/python
# -*- coding: utf-8 -*-

import numpy
from matplotlib import pyplot
from matplotlib.font_manager import FontProperties
import math

nmrData = numpy.loadtxt("nr50_30to200_NMR_ONLY_lengthonly.txt")
xrayData = numpy.loadtxt("nr50_30to200_XRAY_lengthonly.txt")
# data2 = numpy.loadtxt("nr50_30to200_NMR_ONLY_lengthonly.txt")

# ビンの数(階級数)kと幅に関する公式
# スタージェスの公式 k = log2(n) + 1
k = math.ceil(math.log(len(nmrData), 2) + 1) # 天井関数(ceiling)
# スコットの選択
# k = 3.5 * numpy.std(data) / (len(data) ** (1.0 / 3.0))
# 平方根選択
# k = len(data) ** (1.0 / 2.0)

print k

# ヒストグラムを描画
pyplot.hist(nmrData, bins=k, alpha=0.3, color='b')

# スタージェスの公式 k = log2(n) + 1
k = math.ceil(math.log(len(xrayData), 2) + 1) # 天井関数(ceiling)

print k

pyplot.hist(xrayData, bins=k, alpha=0.3, color='r')

fp = FontProperties(fname='font.otf')

pyplot.xlabel(u'タンパク質の配列長(AA)', fontproperties=fp)
pyplot.ylabel(u'タンパク質の個数', fontproperties=fp)

pyplot.show()

