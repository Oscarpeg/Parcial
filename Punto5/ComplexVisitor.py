# Generated from Complex.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ComplexParser import ComplexParser
else:
    from ComplexParser import ComplexParser

# This class defines a complete generic visitor for a parse tree produced by ComplexParser.

class ComplexVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ComplexParser#prog.
    def visitProg(self, ctx:ComplexParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexParser#MulDiv.
    def visitMulDiv(self, ctx:ComplexParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexParser#AddSub.
    def visitAddSub(self, ctx:ComplexParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexParser#Parens.
    def visitParens(self, ctx:ComplexParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexParser#ComplexNumber.
    def visitComplexNumber(self, ctx:ComplexParser.ComplexNumberContext):
        return self.visitChildren(ctx)



del ComplexParser