# Generated from Complex.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,9,61,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,
        5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,3,7,40,8,7,1,7,4,7,43,8,7,
        11,7,12,7,44,1,7,1,7,4,7,49,8,7,11,7,12,7,50,3,7,53,8,7,1,8,4,8,
        56,8,8,11,8,12,8,57,1,8,1,8,0,0,9,1,1,3,2,5,3,7,4,9,5,11,6,13,7,
        15,8,17,9,1,0,3,2,0,43,43,45,45,1,0,48,57,3,0,9,10,13,13,32,32,65,
        0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,
        1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,1,19,1,0,0,0,3,21,
        1,0,0,0,5,23,1,0,0,0,7,25,1,0,0,0,9,27,1,0,0,0,11,29,1,0,0,0,13,
        31,1,0,0,0,15,39,1,0,0,0,17,55,1,0,0,0,19,20,5,42,0,0,20,2,1,0,0,
        0,21,22,5,47,0,0,22,4,1,0,0,0,23,24,5,43,0,0,24,6,1,0,0,0,25,26,
        5,45,0,0,26,8,1,0,0,0,27,28,5,40,0,0,28,10,1,0,0,0,29,30,5,41,0,
        0,30,12,1,0,0,0,31,32,5,40,0,0,32,33,3,15,7,0,33,34,7,0,0,0,34,35,
        3,15,7,0,35,36,5,105,0,0,36,37,5,41,0,0,37,14,1,0,0,0,38,40,5,45,
        0,0,39,38,1,0,0,0,39,40,1,0,0,0,40,42,1,0,0,0,41,43,7,1,0,0,42,41,
        1,0,0,0,43,44,1,0,0,0,44,42,1,0,0,0,44,45,1,0,0,0,45,52,1,0,0,0,
        46,48,5,46,0,0,47,49,7,1,0,0,48,47,1,0,0,0,49,50,1,0,0,0,50,48,1,
        0,0,0,50,51,1,0,0,0,51,53,1,0,0,0,52,46,1,0,0,0,52,53,1,0,0,0,53,
        16,1,0,0,0,54,56,7,2,0,0,55,54,1,0,0,0,56,57,1,0,0,0,57,55,1,0,0,
        0,57,58,1,0,0,0,58,59,1,0,0,0,59,60,6,8,0,0,60,18,1,0,0,0,6,0,39,
        44,50,52,57,1,6,0,0
    ]

class ComplexLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    COMPLEX = 7
    NUMBER = 8
    WS = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'*'", "'/'", "'+'", "'-'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "COMPLEX", "NUMBER", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "COMPLEX", 
                  "NUMBER", "WS" ]

    grammarFileName = "Complex.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


