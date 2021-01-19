/** Huynh Thanh Sang / 1813796 **/
grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_TOKEN:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options{
	language=Python3;
}

program: varDecl* funcDecl* EOF;

funcDecl:
	FUNCTION COLON ID
	(PARAMETER COLON varDeclaration (COMMA varDeclaration)*)? 
	BODY COLON stmtInFunc
	ENDBODY DOT;

varDecl: VAR COLON varDeclaration (COMMA varDeclaration)* SEMI;

varDeclaration
	: ID (indexInt)* (ASSIGN literals)?
	;

indexInt : LSB intLiteral RSB;

/** 4. Type and Value **/
literals
	: intLiteral
	| FLOAT_LITERAL
	| STRING_LITERAL
	| booleanLiteral
	| arrayLiteral
	| ID
	;

intLiteral
	: INTLIT
	| HEXA
	| OCTA
	;

INTLIT: [1-9] [0-9]* | '0';
HEXA: '0'[xX][1-9A-F][0-9A-F]*;
OCTA: '0'[oO][1-7][0-7]*;

FLOAT_LITERAL
	: DIGIT+ DOT DIGIT* EXPONENT? // 1.(1)(e-1)
	| DIGIT+ EXPONENT			  // 1e-1
	;

STRING_LITERAL
	: '"' STR_CHAR* '"' 
	{
		self.text = self.text[1:-1]
	}
	;

booleanLiteral
	: TRUE | FALSE 
	;

arrayLiteral
	: LCB (literals (COMMA literals)*)? RCB
	;

fragment EXPONENT: [eE] SIGN? DIGIT+;
fragment DIGIT: [0-9];
fragment SIGN: [+-];
fragment QUOTE: '\'"';
fragment ESC_SEQ: '\\'[btnfr'\\];
fragment STR_CHAR: ~[\b\t\n\f\r"'\\] | QUOTE | ESC_SEQ;	

/** 5. Variable **/

/** 6. exp **/	
exp: exp1 ( EQ | NEQ | GT | LT | GTE | LTE | EQF | GTF | LTF | GTEF | LTEF ) exp1 | exp1 ;

exp1: exp1 (AND | OR) exp2 | exp2;

exp2: exp2 ( ADD | SUB |  ADDF | SUBF ) exp3 | exp3;

exp3: exp3 ( DIV | MUL | MODULE | DIVF | MULF ) exp4 | exp4;

exp4: NOT exp4 | exp5 ;

exp5: ( SUB | SUBF ) exp5 | exp6;

exp6: exp6 indexes+ | exp7;

exp7: callExpr | exp8;

exp8: LP exp RP | literals;

indexes: LSB exp RSB ;

callExpr: ID LP listExp? RP;

listExp: exp (COMMA exp)*;

/** 7. Statements **/
stmt
	: assignStmt
	| ifStmt
	| forStmt
	| whileStmt
	| dowhileStmt
	| breakStmt
	| continueStmt
	| callStmt
	| returnStmt
	;

stmtInFunc : (varDecl)* (stmt)*;

/** ASSIGNMENT **/
assignStmt: exp ASSIGN exp SEMI;

/** IF **/
ifStmt: IF ifComponent (ELSEIF ifComponent)* (ELSE stmtInFunc)? ENDIF DOT;

ifComponent: exp THEN stmtInFunc;

/** FOR **/
forStmt: 	FOR LP ID ASSIGN exp COMMA exp COMMA exp RP DO
			stmtInFunc 
			ENDFOR DOT;

/** WHILE **/
whileStmt: WHILE exp DO stmtInFunc ENDWHILE DOT;

/** DO WHILE **/
dowhileStmt: DO stmtInFunc WHILE exp ENDDO DOT;

/** BREAK **/
breakStmt: BREAK SEMI;

/** CONTINUE **/
continueStmt: CONTINUE SEMI;

/** CALL STMT **/
callStmt: ID LP listExp? RP SEMI;

/** RETURN **/
returnStmt: RETURN exp? SEMI;

// 2.2 Function declaration

/** Operators **/
ASSIGN: '=';
// Boolean Type
AND: '&&';
OR: '||';
NOT: '!';

// Integer Type
ADD: '+';
SUB: '-';
MUL: '*';
MODULE: '%';
DIV: '\\';
LTE: '<=';
GTE: '>=';
NEQ: '!=';
EQ : '==' ;
LT : '<' ;
GT : '>' ;

// Float Type
ADDF: '+.';
SUBF: '-.';
MULF: '*.';
DIVF: '\\.';
LTEF: '<=.';
GTEF: '>=.';
EQF : '=/=' ;
LTF : '<.' ;
GTF : '>.' ;

/** Separators **/
LP: '('; // Left Parenthesis
RP: ')'; // Right Parenthesis
LCB: '{'; // Left Curly Bracket
RCB: '}'; // Right Curly Bracket
LSB: '['; // Left Square Bracket
RSB: ']'; // Right Square Bracket

SEMI: ';'; // Semicolon
COMMA: ','; // Comma
COLON: ':'; // Colon
DOT: '.';

/** 3.1 Character Set **/
WS : [ \t\r\f\n]+ -> skip ; // skip spaces, tabs, newlines

/** 3.2 Program Comment **/
BLOCK_COMMENT : '**'.*?'**' -> skip ;

/** 3.3 Tokens Set **/
// Identifiers
ID : [a-z][a-zA-Z0-9_]* ;

// Keywords
BODY : 'Body';
ELSE : 'Else';
ENDFOR : 'EndFor';
IF : 'If';
VAR : 'Var';
ENDDO : 'EndDo';
BREAK : 'Break';
ELSEIF : 'ElseIf';
ENDWHILE : 'EndWhile';
PARAMETER : 'Parameter';
WHILE : 'While';
CONTINUE : 'Continue';
ENDBODY : 'EndBody';
FOR : 'For';
RETURN : 'Return';
DO : 'Do';
ENDIF : 'EndIf';
FUNCTION : 'Function';
THEN : 'Then';
TRUE : 'True';
FALSE : 'False';

/** Catch ERROR **/
fragment ESC_ILLEGAL: '\\' ~[btnfr'\\] | '\'' ~["] ;

ERROR_TOKEN: .
	{
		raise ErrorToken(self.text)
	}
	;
	
UNCLOSE_STRING: '"' STR_CHAR* ([\b\t\n\f\r"'\\] | EOF)?
	{
		y = str(self.text)
		possible = ['\b', '\t', '\n', '\f', '\r', "'", '\\']
		if y[-1] in possible:
			raise UncloseString(y[1:-1])
		else:
			raise UncloseString(y[1:])
	}
	;


ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL
	{
		y = str(self.text)
		raise IllegalEscape(y[1:])
	}
	;
	
UNTERMINATED_COMMENT: '**' .?
	{
		y = str(self.text)
		raise UnterminatedComment()
	}
	;