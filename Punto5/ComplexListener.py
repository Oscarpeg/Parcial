# Generated from Complex.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ComplexParser import ComplexParser
else:
    from ComplexParser import ComplexParser

# This class defines a complete listener for a parse tree produced by ComplexParser.
class ComplexListener(ParseTreeListener):

    # Enter a parse tree produced by ComplexParser#prog.
    def enterProg(self, ctx:ComplexParser.ProgContext):
        pass

    # Exit a parse tree produced by ComplexParser#prog.
    def exitProg(self, ctx:ComplexParser.ProgContext):
        pass


    # Enter a parse tree produced by ComplexParser#MulDiv.
    def enterMulDiv(self, ctx:ComplexParser.MulDivContext):
        pass

    # Exit a parse tree produced by ComplexParser#MulDiv.
    def exitMulDiv(self, ctx:ComplexParser.MulDivContext):
        pass


    # Enter a parse tree produced by ComplexParser#AddSub.
    def enterAddSub(self, ctx:ComplexParser.AddSubContext):
        pass

    # Exit a parse tree produced by ComplexParser#AddSub.
    def exitAddSub(self, ctx:ComplexParser.AddSubContext):
        pass


    # Enter a parse tree produced by ComplexParser#Parens.
    def enterParens(self, ctx:ComplexParser.ParensContext):
        pass

    # Exit a parse tree produced by ComplexParser#Parens.
    def exitParens(self, ctx:ComplexParser.ParensContext):
        pass


    # Enter a parse tree produced by ComplexParser#ComplexNumber.
    def enterComplexNumber(self, ctx:ComplexParser.ComplexNumberContext):
        pass

    # Exit a parse tree produced by ComplexParser#ComplexNumber.
    def exitComplexNumber(self, ctx:ComplexParser.ComplexNumberContext):
        pass



del ComplexParser