"""see https://github.com/patarapolw/cjkradlib """
import pathlib

import os
import sys

from cjkradlib import RadicalFinder
finder = RadicalFinder(lang='zh')  # default is 'zh'

result = finder.search('给') #遢
print(result.compositions)  # ['广', '林']
print(result.supercompositions)  # ['摩', '魔', '磨', '嘛', '麽', '靡', '糜', '麾']
print(result.variants)  # ['菻']

print(result.supercompositions)  # ['摩', '魔', '磨', '嘛', '麽', '靡', '糜', '麾']
HanziFreqList = []
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, "HanziFrequencyList.txt"), "r", encoding="utf-8") as f:
        HanziFreqList = [line.split('\t') for line in f]
SCRIPT_DIR = pathlib.Path(__file__).parent.absolute()

logger = open(SCRIPT_DIR / 'Generate_hanzi_compositions_supercompositions_Log_common_only.txt', 'w', encoding="utf-8")


hanzi_list = [x[1] for x in HanziFreqList[:10000]]
common_hanzi_list = [x[1] for x in HanziFreqList[:4000]]
demo_pure_radical = [x + ": " + str("".join(finder.search(x).supercompositions)) for x in finder.search('给').compositions if x not in hanzi_list]
print(demo_pure_radical)
"""
for hanzi in hanzi_list:
    result = finder.search(hanzi)
    #print(hanzi + " comp: " + str(result.compositions))  # ['广', '林']
    #print(hanzi + " super: " + str(result.supercompositions))  # ['摩', '魔', '磨', '嘛', '麽', '靡', '糜', '麾']
    #supercompositions_common_only = [x for x in result.supercompositions if x in common_hanzi_list]
    #logger.write(hanzi + "\t" + ''.join(result.compositions) + "\t" + ''.join(supercompositions_common_only))
    logger.write(hanzi + "\t" + ''.join(result.compositions) + "\t" + ''.join(result.supercompositions))
    logger.write("\t")
    pure_radicals = [x + ": " + str("".join(finder.search(x).supercompositions)) for x in result.compositions if x not in hanzi_list]
    pure_radicals_len = len(pure_radicals)-1
    for pure_radical in pure_radicals:
        if len(pure_radical) <= 25 and pure_radical[0] not in ['⑤','③','②','④','①','⑥','⑦','⑧','⑨','⑩']:  #ignore too common radical i.e. 辶: 这过道还进通达边运造近远连选速送适述退追遗遇逐避逃迫遍遭迎透途迅迹迷违迟返迪递巡逼逻遵迁逊迈遥遣邀逆遂辽逝遮逢逮逸迦迄逗逾逛遏迂迭逞遁迸逍迥逵遐迢遽邃這過迩逅迳迨遛邂暹迤遨邋邈逡
            logger.write(pure_radical)
            if pure_radicals.index(pure_radical) != pure_radicals_len:
                logger.write("<br>")
    logger.write('\n')
"""

logger.close()
