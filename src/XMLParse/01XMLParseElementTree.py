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
-------------------------------------------------------------------------------------------------------------'''

'''-------------------------------------------------------------------------------------------------------------
2.具体内容：
2.1 ElementTree
2.1.1 一个API，两种实现
（1）ElementTree在Python标准库中有两种实现方式，分别是Python的实现和C语言的实现；
（2）纯Python的实现：xml.etree.ElementTree；
（3）C语言的实现：xml.etree.cElementTree；
（4）cElementTree实现的速度更快，可采用以下方式导入：
        try:
            import xml.etree.cElementTree as ET
        except ImportError:
            import xml.etree.ElementTree as ET
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

'''-------------------------------------------------------------------------------------------------------------
2.1.2 将XML解析为树的形式（Example_01_01）
（1）ElementTree将整个XML解析为一棵树（对整个文档级别的操作使用ElementTree，如读、写、寻找元素）；
（2）Element将单个结点解析为树（对单个XML元素和它的子元素通常用Element）；
-------------------------------------------------------------------------------------------------------------'''
# Example_01_01
print "------------Example_01_01---------------"
tree = ET.ElementTree(file="01_doc1.xml")     # 将xml转换成一个ElementTree对象
# tree = ET.parse("01_doc1.xml")                  # 第二种解析xml的方法，使用ET.parse(filename)。
root = tree.getroot()                         # 获取ElementTree的root结点，是一个Element元素。
print root.tag, root.attrib                   # 结果：doc {} ；可以看到，在获取根元素的时候没有任何状态。
# 对root元素的子结点进行遍历
for child_of_root in root:
    print child_of_root.tag, child_of_root.attrib
# 访问一个指定的子结点
print root[0].tag, root[0].text

'''-------------------------------------------------------------------------------------------------------------
2.1.3 寻找我们感兴趣的元素（Example_01_02）
（1）Element对象的iter方法可以对子结点进行深度优先遍历；
（2）ElementTree对象也有iter方法，该方法具有tag参数；
-------------------------------------------------------------------------------------------------------------'''
# Example_01_02
print "------------Example_01_02---------------"
# （1）使用ElementTree对象的iter方法，对该ElementTree对象的全部子结点进行遍历；
for element in tree.iter():
    print element.tag, element.attrib
# （2）iter也可以接受一个tag作为参数，遍历那些有指定tag的结点；
for element in tree.iter(tag="sub-branch"):
    print element.tag, element.attrib

'''-------------------------------------------------------------------------------------------------------------
2.1.4 对XPATH的支持（Example_01_03）
（1）Element有一些关于寻找的方法可以接受XPath作为参数；
（2）find 返回第一个匹配的子元素；
（3）findall 以列表的形式返回所有匹配的子元素；
（4）iterfind 为所有匹配项提供迭代器；
（5）这些方法在 ElementTree 里面也有。
-------------------------------------------------------------------------------------------------------------'''
# Example_01_03
print "------------Example_01_03---------------"
for element in tree.iterfind('branch/sub-branch'):
    print element.tag, element.attrib
for element in tree.iterfind('branch[@name="release01"]'):
    print element.tag, element.attrib

'''-------------------------------------------------------------------------------------------------------------
2.1.5 建立XML文档
（1）ElementTree对象提供了write方法（Example_01_04）；
（2）修改XML文档可以使用Element的相关方法；
（3）建立一个全新元素，可以使用SubElement函数；
-------------------------------------------------------------------------------------------------------------'''
# Example_01_04
print "------------Example_01_04---------------"
# （1）在ElementTree中修改XML（修改Element）
del root[2]
root[0].set('foo', 'bar')
for subelem in root:
    print subelem.tag, subelem.attrib
# （2）将修改写入XML文件
# tree.write("01_doc1.xml")

'''-------------------------------------------------------------------------------------------------------------
2.1.6 使用iterparse处理XML流
（1）使用 ET 来将较大的 XML 读入内存也会碰到和 DOM 一样的内存问题；
（2）ET提供一个特殊的工具iterparse，用来处理大型文档，并且解决了内存问题；
（3）以下面的例子，简要说明 iterparse 和 iter 方法的区别：
    * iter：所有XML树中的元素都会被检验（加载）；当处理一个大约100MB的XML文件时，占用的内存大约是560MB，耗时2.9秒；
    * iterparese：检测“闭合的”(end)事件并且寻找location标签和指定的值；仍然建立一棵树，但不需要全部加载进内存（elem.clear()是关键）；
    * 处理同样的文件，iterparse占用内存只需要仅仅7MB ，耗时2.5秒；
    * 速度的提升归功于生成树的时候只遍历一次；相比较来说，parse方法首先建立了整个树，然后再次遍历来寻找我们需要的元素(所以慢了一点)。
-------------------------------------------------------------------------------------------------------------'''
# 遍历方法一：使用ElementTree.iter()方法
tree = ET.parse(sys.argv[2])
count = 0
for elem in tree.iter(tag='location'):
    if elem.text == 'Zimbabwe':
        count += 1
print count

# 遍历方法二：使用ElementTree.iterparse()方法
count = 0
for event, elem in ET.iterparse(sys.argv[2]):
    if event == 'end':
        if elem.tag == 'location' and elem.text == 'Zimbabwe':
            count += 1
    elem.clear() # discard the element
print count