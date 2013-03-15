all: PyCon-US-2013-dmalcolm-StaticAnalysis.html

PyCon-US-2013-dmalcolm-StaticAnalysis.html: PyCon-US-2013-dmalcolm-StaticAnalysis.txt
	asciidoc --backend slidy PyCon-US-2013-dmalcolm-StaticAnalysis.txt
# slidy backend was added to asciidoc in Version 8.6.2 (2010-10-03)

# Copy up to http://dmalcolm.fedorapeople.org/presentations/PyCon-US-2013
publish:
	scp \
	    PyCon-US-2013-dmalcolm-StaticAnalysis.html \
	    dmalcolm@fedorapeople.org:public_html/presentations/PyCon-US-2013
	scp -r images \
	    dmalcolm@fedorapeople.org:public_html/presentations/PyCon-US-2013
