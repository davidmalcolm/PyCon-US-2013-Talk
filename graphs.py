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
def all_errors():
    ALL_ERRORS = [
            ((u'clang-analyzer', None), 5349),
            ((u'cpychecker', u'mismatching-type-in-format-string'), 2962),
            ((u'cpychecker', u'refcount-too-high'), 2614),
            ((u'gcc', u'unused-but-set-variable'), 2360),
            ((u'gcc', u'strict-aliasing'), 1861),
            ((u'cpychecker', u'returns-NULL-without-setting-exception'), 1641),
            ((u'gcc', u'unused-result'), 1037),
            ((u'cpychecker', u'null-ptr-dereference'), 907),
            ((u'cpychecker', u'null-ptr-argument'), 857),
            ((u'cppcheck', u'nullPointer'), 817),
            ((u'gcc', u'unused-variable'), 765),
            ((u'cppcheck', u'syntaxError'), 648),
            ((u'gcc', None), 558),
            ((u'cpychecker', u'refcount-too-low'), 524),
            ((u'cpychecker', u'flags-within-PyMethodDef'), 521),
            ((u'gcc', u'switch'), 495),
            ((u'gcc', u'sign-compare'), 495),
            ((u'gcc', u'maybe-uninitialized'), 407),
            ((u'gcc', u'parentheses'), 333),
            ((u'gcc', u'format'), 316),
            ((u'cpychecker', u'usage-of-uninitialized-data'), 303),
            ((u'gcc', u'implicit-function-declaration'), 284),
            ((u'gcc', u'write-strings'), 284),
            ((u'cppcheck', u'memleak'), 233),
            ((u'cppcheck', u'uninitvar'), 227),
            ((u'gcc', u'pointer-to-int-cast'), 163),
            ((u'gcc', u'narrowing'), 160),
            ((u'cppcheck', u'memleakOnRealloc'), 158),
            ((u'cppcheck', u'resourceLeak'), 136),
            ((u'gcc', u'deprecated-declarations'), 106),
            ((u'gcc', u'int-to-pointer-cast'), 95),
            ((u'gcc', u'uninitialized'), 95),
            ((u'gcc', u'pointer-sign'), 90),
            ((u'gcc', u'old-style-definition'), 89),
            ((u'gcc', u'unused-value'), 85),
            ((u'gcc', u'nonnull'), 85),
            ((u'gcc', u'address'), 67),
            ((u'gcc', u'unused-label'), 54),
            ((u'gcc', u'delete-non-virtual-dtor'), 53),
            ((u'gcc', u'unused-function'), 52),
            ((u'gcc', u'conversion-null'), 41),
            ((u'gcc', u'unused-parameter'), 40),
            ((u'gcc', u'return-type'), 38),
            ((u'gcc', u'shadow'), 32),
            ((u'gcc', u'sequence-point'), 26),
            ((u'cppcheck', u'uninitstring'), 17),
            ((u'cppcheck', u'doubleFree'), 14),
            ((u'cppcheck', u'fflushOnInputStream'), 12),
            ((u'cppcheck', u'deallocDealloc'), 12),
            ((u'cpychecker', u'returns-pointer-to-deallocated-memory'), 9),
            ((u'gcc', u'enum-compare'), 8),
            ((u'gcc', u'missing-field-initializers'), 8),
            ((u'gcc', u'strict-overflow'), 8),
            ((u'cpychecker', u'too-many-vars-in-format-string'), 8),
            ((u'cpychecker', u'passing-pointer-to-deallocated-memory'), 8),
            ((u'cppcheck', u'useClosedFile'), 8),
            ((u'cpychecker', u'missing-keyword-argument'), 7),
            ((u'cpychecker', u'read-from-deallocated-memory'), 7),
            ((u'cpychecker', u'not-enough-vars-in-format-string'), 6),
            ((u'cppcheck', u'deallocuse'), 6),
            ((u'cppcheck', u'wrongmathcall'), 5),
            ((u'cpychecker', u'call-of-null-function-ptr'), 4),
            ((u'cpychecker', u'arg-was-not-PyObject-ptr'), 4),
            ((u'gcc', u'undef'), 4),
            ((u'gcc', u'array-bounds'), 4),
            ((u'cppcheck', u'arrayIndexOutOfBounds'), 4),
            ((u'gcc', u'implicit-int'), 4),
            ((u'gcc', u'extra'), 4),
            ((u'gcc', u'unused-but-set-parameter'), 4),
            ((u'cppcheck', u'deallocret'), 4),
            ((u'cppcheck', u'sizeofwithsilentarraypointer'), 4),
            ((u'gcc', u'comment'), 3),
            ((u'cppcheck', u'leakNoVarFunctionCall'), 3),
            ((u'gcc', u'missing-braces'), 3),
            ((u'gcc', u'format-extra-args'), 3),
            ((u'cpychecker', u'unknown-format-char'), 2),
            ((u'cppcheck', u'invalidScanfFormatWidth'), 2),
            ((u'cppcheck', u'bufferAccessOutOfBounds'), 2),
            ((u'gcc', u'overflow'), 2),
            ((u'gcc', u'nested-externs'), 1),
            ((u'cppcheck', u'IOWithoutPositioning'), 1),
            ((u'cpychecker', u'missing-NULL-terminator-in-PyMethodDef-table'), 1),
            ((u'cpychecker', u'arithmetic-error'), 1),
            ((u'cppcheck', u'wrongPrintfScanfArgNum'), 1),
            ((u'gcc', u'overlength-strings'), 1),
            ((u'gcc', u'char-subscripts'), 1),
            ((u'cppcheck', u'mismatchAllocDealloc'), 1),
            ((u'cppcheck', u'zerodiv'), 1),
            ((u'cppcheck', u'autoVariables'), 1),
            ((u'gcc', u'vla'), 1)]
    return ([('%s: %s' % (checker, test if test else '(all)'), count)
             for (checker, test), count in ALL_ERRORS][:20], # top 20
            '# seen', 'Kinds of warning (top 20)')

def cpychecker_errors():
    return ([(u'mismatching-type-in-format-string', 2962),
             (u'refcount-too-high', 2614),
             (u'returns-NULL-without-setting-exception', 1641),
             (u'null-ptr-dereference', 907),
             (u'null-ptr-argument', 857),
             (u'refcount-too-low', 524),
             (u'flags-within-PyMethodDef', 521),
             (u'usage-of-uninitialized-data', 303),
             (u'returns-pointer-to-deallocated-memory', 9),
             (u'passing-pointer-to-deallocated-memory', 8),
             (u'too-many-vars-in-format-string', 8),
             (u'missing-keyword-argument', 7),
             (u'read-from-deallocated-memory', 7),
             (u'not-enough-vars-in-format-string', 6),
             (u'arg-was-not-PyObject-ptr', 4),
             (u'call-of-null-function-ptr', 4),
             (u'unknown-format-char', 2),
             (u'arithmetic-error', 1),
             (u'missing-NULL-terminator-in-PyMethodDef-table', 1)],
            '# seen', 'cpychecker errors')

#fn = most_common_entrypoints
#fn = cyclomatic
fn = all_errors
#fn = cpychecker_errors
data, xlabel, title = fn()

pprint(data)
make_chart(data, 'foo.png', xlabel, title)
