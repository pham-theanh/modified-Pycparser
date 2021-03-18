
from __future__ import print_function
import io
from pycparser import c_parser, c_ast, parse_file
from pycparser import c_parser

parser = c_parser.CParser()
ast = parse_file('test.cpp')
text=''
filename = 'test.cpp'
with io.open(filename) as f:
    text: str = f.read()


ast = parser.parse(text, filename )


ast = parser.parse(text)
ast.show();




