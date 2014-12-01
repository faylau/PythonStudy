#!/usr/bin/python
#encoding:utf-8

__authors__ = ['"Liu Fei" <liufei83@163.com>']
__version__ = "V0.1"

'''-------------------------------------------------------------------------------------------------------------
1.概述：
1.1 Python有3种XML解析途径：SAX、DOM以及ElementTree。
1.2 xml.dom.* 模块：
（1）是 W3C DOM API 的实现；如果你有处理 DOM API 的需要，那么这个模块适合你。注意：在 xml.dom 包里面有许多模块，注意它们之间的不同；
1.3 xml.sax.* 模块：
（1）是 SAX API 的实现；这个模块牺牲了便捷性来换取速度和内存占用；SAX 是一个基于事件的 API，这就意味着它可以“在空中”(on the fly)处理庞大数量的的文档，不用完全加载进内存(见注释1)；
1.4 xml.parser.expat：
是一个直接的，低级一点的基于 C 的 expat 的语法分析器； expat接口基于事件反馈，有点像 SAX 但又不太像，因为它的接口并不是完全规范于 expat 库的。
1.5 xml.etree.ElementTree (以下简称 ET)：
（1）它提供了轻量级的 Python式的 API ，它由一个 C 实现来提供；
（2）相对于 DOM 来说，ET 快了很多，而且有很多令人愉悦的 API 可以使用；
（3）相对于 SAX 来说，ET 也有 ET.iterparse 提供了 “在空中” 的处理方式，没有必要加载整个文档到内存；
（4）ET 的性能的平均值和 SAX 差不多，但是 API 的效率更高一点而且使用起来很方便。
1.6 通常的建议：尽可能的使用 ET 来处理 XML ，除非你有什么非常特别的需要。

1.1 ElementTree
1.1.1 一个API，两种实现
（1）ElementTree在Python标准库中有两种实现方式，分别是Python的实现和C语言的实现；
（2）纯Python的实现：xml.etree.ElementTree；
（3）C语言的实现：xml.etree.cElementTree；
（4）cElementTree实现的速度更快，可采用以下方式导入：
        try:
            import xml.etree.cElementTree as ET
        except ImportError:
            import xml.etree.ElementTree as ET
1.1.2 将XML解析为树的形式（Example_01_01）
（1）ElementTree将整个XML解析为一棵树（对整个文档级别的操作使用ElementTree，如读、写、寻找元素）；
（2）Element将单个结点解析为树（对单个XML元素和它的子元素通常用Element）；

-------------------------------------------------------------------------------------------------------------'''

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

xml_str = '''
<?xml version="1.0"?>
<doc>
    <branch name="testing" hash="1cdf045c">
        text,source
    </branch>
    <branch name="release01" hash="f200013e">
        <sub-branch name="subrelease01">
            xml,sgml
        </sub-branch>
    </branch>
    <branch name="invalid">
    </branch>
</doc>
'''

tree = ET.ElementTree(xml_str)      # 将xml转换成一个ElementTree对象
root = tree.getroot()               # 获取ElementTree的root结点


