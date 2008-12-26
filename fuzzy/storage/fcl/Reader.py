#!/usr/bin/env python
import sys
import antlr3

from FCLLexer import FCLLexer
from FCLParser import FCLParser

class Reader(object):

    def __init__(self):
        pass

    def __load(self,char_stream):
        lexer = FCLLexer(char_stream)
        tokens = antlr3.CommonTokenStream(lexer)
        parser = FCLParser(tokens)
        return parser.main()

    def load_from_file(self,filename):
        return self.__load(antlr3.ANTLRFileStream(filename))

    def load_from_stream(self,stream):
        return self.__load(antlr3.ANTLRInputStream(stream))

    def load_from_string(self,str):
        return self.__load(antlr3.ANTLRStringStream(str))

