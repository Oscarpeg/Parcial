grammar Complex;


prog: expr EOF;

expr: expr op=('*'|'/') expr     # MulDiv
    | expr op=('+'|'-') expr     # AddSub
    | COMPLEX                    # ComplexNumber
    | '(' expr ')'               # Parens
    ;

COMPLEX: '(' NUMBER ('+'|'-') NUMBER 'i' ')';
NUMBER: '-'? [0-9]+ ('.' [0-9]+)?;
WS: [ \t\r\n]+ -> skip;
