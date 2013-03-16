from pprint import pprint

import pylab

def make_chart(data, dstfilename, xlabel, title):
    """
    data : list of name, value pairs
    """

    pos = pylab.arange(len(data))+.5    # the bar centers on the y axis
    val = [kv[1] for kv in data]

    pylab.figure(1)#, figsize=(1024/64,768/64), dpi=64)
    pylab.barh(pos, val, align='center')
    pylab.yticks(pos, [kv[0] for kv in data])
    pylab.xlabel(xlabel)
    pylab.title(title)
    pylab.grid(True)

    pylab.show()
    #pylab.savefig(dstfilename)

def most_common_entrypoints():
    import csv
    with open('20-most-common-entrypoints.csv') as f:
        data = [(k, int(v)) for k, v in csv.reader(f)]
    return (data,
            '# uses', 
            'What are the 20 most commonly used Py/_Py entrypoints?')

def cyclomatic():
    return ([
        ('python-4Suite-XML-1.0.2:Ft/Xml/XPath/XPathParser.c:parser_parse', 1601),
        ('Cython-0.15.1:Cython/Compiler/Lexicon.c:__pyx_pf_6Cython_8Compiler_7Lexicon_make_lexicon', 627),
        ('ntop-4.1.0:http.c:returnHTTPPage', 567),
        ('scipy-0.10.0:scipy/spatial/qhull/src/global.c:qh_initflags', 471),
        ('scipy-0.10.0:scipy/spatial/qhull/src/global.c:qh_initflags', 471),
        ('python-4Suite-XML-1.0.2:Ft/Xml/XPointer/XPointerParser.c:parser_parse', 455),
        ('python-zmq-2.1.9:zmq/core/constants.c:PyInit_constants', 428),
        ('pymol-1.4.1:layer2/Sculpt.c:SculptMeasureObject', 387),
        ('pymol-1.4.1:layer2/RepCylBond.c:RepCylBondNew', 386),
        ('pymol-1.4.1:layer2/RepWireBond.c:RepWireBondNew', 325),
        ],
            'cylcomatic complexity',
            'What were the 10 most complicated functions?')

fn = most_common_entrypoints
fn = cyclomatic
data, xlabel, title = fn()

pprint(data)
make_chart(data, 'foo.png', xlabel, title)
