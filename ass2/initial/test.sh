#!/bin/bash

cd $(dirname $0)
cd src

echo "START TESTING"
python3 run.py gen
python3 run.py test LexerSuite > ../log.lexer.txt
python3 run.py test ParserSuite > ../log.parser.txt
python3 run.py test ASTGenSuite > ../log.ASTGen.txt

echo "DONE"