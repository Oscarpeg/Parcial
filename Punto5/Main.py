import sys
from antlr4 import *
from ComplexLexer import ComplexLexer
from ComplexParser import ComplexParser
from ComplexEvalVisitor import ComplexEvalVisitor  

def main():
    
    input_expr = input("Ingrese una expresión con números complejos: ")
    
    
    lexer = ComplexLexer(InputStream(input_expr))
    stream = CommonTokenStream(lexer)
    parser = ComplexParser(stream)
    
    
    tree = parser.prog()  
    
   
    visitor = ComplexEvalVisitor()
    result = visitor.visit(tree.expr())  
    
    
    print("Resultado:", result)

if __name__ == "__main__":
    main()
