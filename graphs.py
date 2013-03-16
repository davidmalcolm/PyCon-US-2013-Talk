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

import csv
with open('20-most-common-entrypoints.csv') as f:
    data = [(k, int(v)) for k, v in csv.reader(f)]

#data = zip(('Tom', 'Dick', 'Harry', 'Slim', 'Jim'),
#           3+10*pylab.rand(5))
pprint(data)
make_chart(data, 'foo.png',
           '# uses',
           'What are the 20 most commonly used Py/_Py entrypoints?')
