import sys
from antlr4 import *
from ComplexLexer import ComplexLexer
from ComplexParser import ComplexParser
from ComplexVisitor import ComplexVisitor
import cmath

class ComplexEvalVisitor(ComplexVisitor):
    def visitMulDiv(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left * right if ctx.op.type == ComplexParser.T__2 else left / right

    def visitAddSub(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left + right if ctx.op.type == ComplexParser.T__0 else left - right

    def visitComplexNumber(self, ctx):
        text = ctx.COMPLEX().getText()
        text = text.replace('(', '').replace(')', '').replace('i', '')
        parts = text.replace('+', ' +').replace('-', ' -').split()
        real, imag = float(parts[0]), float(parts[1])
        return complex(real, imag)

    def visitParens(self, ctx):
        return self.visit(ctx.expr())

def main():
    input_expr = input("Ingrese una expresión con números complejos: ")
    lexer = ComplexLexer(InputStream(input_expr))
    stream = CommonTokenStream(lexer)
    parser = ComplexParser(stream)
    tree = parser.expr()
    visitor = ComplexEvalVisitor()
    result = visitor.visit(tree)
    print("Resultado:", result)

if __name__ == "__main__":
    main()
