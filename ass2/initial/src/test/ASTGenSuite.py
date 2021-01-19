import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    """ Program structure """
    def test_301(self):
        input = r""" """
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 301))

    def test_302(self):
        input = r""" 
Function: test
    Body:
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 302))

    def test_303(self):
        input = r"""
Var: x,x,y,z,z;
"""
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None),VarDecl(Id("z"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    def test_304(self):
        input = r""" 
Function: test
    Body:
        Var: x,x,y,z,z;
    EndBody.
"""

    def test_305(self):
        input = r"""
Function: foo
    Parameter: a, b, c, xyz
    Body:
    EndBody.
 """
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None),VarDecl(Id("xyz"),[],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 305))

    def test_306(self):
        input = r"""
Var: x,y,zzz;
Function: zzz
    Body:
    EndBody.
"""
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("zzz"),[],None),FuncDecl(Id("zzz"),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 306))

    def test_307(self):
        input = r"""
Var: x,y,zzz;
Var: x[123]=123,y,zzz;
Var: x,y = 0o123,zzz;
Var: x,y,zzz = 0x123ABCDEF;
"""
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("zzz"),[],None),VarDecl(Id("x"),[123],IntLiteral(123)),VarDecl(Id("y"),[],None),VarDecl(Id("zzz"),[],None),VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],IntLiteral(83)),VarDecl(Id("zzz"),[],None),VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("zzz"),[],IntLiteral(4893429231))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 307))

    def test_308(self):
        input = r""" 
Function: test
    Body:
        Var: x,y,zzz;
        Var: x[123]=123,y,zzz;
        Var: x,y = 0o123,zzz;
        Var: x,y,zzz = 0x123ABCDEF;
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("zzz"),[],None),VarDecl(Id("x"),[123],IntLiteral(123)),VarDecl(Id("y"),[],None),VarDecl(Id("zzz"),[],None),VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],IntLiteral(83)),VarDecl(Id("zzz"),[],None),VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("zzz"),[],IntLiteral(4893429231))],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 308))

    def test_309(self):
        input = r"""
Function: first
    Body:
        Var: first = 1;
    EndBody.
Function: second
    Body:
        Var: second = 2;
    EndBody.
Function: third
    Body:
        Var: third = 3;
    EndBody.
"""
        expect = Program([FuncDecl(Id("first"),[],([VarDecl(Id("first"),[],IntLiteral(1))],[])),FuncDecl(Id("second"),[],([VarDecl(Id("second"),[],IntLiteral(2))],[])),FuncDecl(Id("third"),[],([VarDecl(Id("third"),[],IntLiteral(3))],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 309))

    """ VarDecl """

    def test_310(self):
        input = r"""
Var: a[123] = 123456;
Var: b[0x123] = 0x123;
Var: b[0X123] = 0X123;
Var: c[0o123] = 0o123;
Var: c[0O123] = 0O123;
"""
        expect = Program([VarDecl(Id("a"),[123],IntLiteral(123456)),VarDecl(Id("b"),[291],IntLiteral(291)),VarDecl(Id("b"),[291],IntLiteral(291)),VarDecl(Id("c"),[83],IntLiteral(83)),VarDecl(Id("c"),[83],IntLiteral(83))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 310))

    def test_311(self):
        input = r"""
Function: test
    Body:
        Var: a[123] = 123456;
        Var: b[0x123] = 0x123;
        Var: b[0X123] = 0X123;
        Var: c[0o123] = 0o123;
        Var: c[0O123] = 0O123;
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("a"),[123],IntLiteral(123456)),VarDecl(Id("b"),[291],IntLiteral(291)),VarDecl(Id("b"),[291],IntLiteral(291)),VarDecl(Id("c"),[83],IntLiteral(83)),VarDecl(Id("c"),[83],IntLiteral(83))],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 311))

    def test_312(self):
        input = r"""
Var: a;
Var: a[123] = 123;
Var: a[0x123] = 0x123;
Var: a[0o123] = 0o123;
"""
        expect = Program([VarDecl(Id("a"),[],None),VarDecl(Id("a"),[123],IntLiteral(123)),VarDecl(Id("a"),[291],IntLiteral(291)),VarDecl(Id("a"),[83],IntLiteral(83))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))

    def test_313(self):
        input = r"""
Function: main
    Body:
        a = 123 + 0x123 + 0o123 + 0X123 + 0O123;
    EndBody.
"""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(ArrayCell(Id("a"),[]),BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",IntLiteral(123),IntLiteral(291)),IntLiteral(83)),IntLiteral(291)),IntLiteral(83)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))

    def test_314(self):
        input = r"""
Var: a, b = 100, c;
Var: a[100] = 100;
Var: a[1][2][3][4][5] = {123, {123, 10e-4}};
"""
        expect = Program([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],IntLiteral(100)),VarDecl(Id("c"),[],None),VarDecl(Id("a"),[100],IntLiteral(100)),VarDecl(Id("a"),[1,2,3,4,5],ArrayLiteral([IntLiteral(123),ArrayLiteral([IntLiteral(123),FloatLiteral(0.001)])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))

    def test_315(self):
        input = r"""
Function: test
    Body:
        Var: a, b = 100, c;
        Var: a[100] = 100;
        Var: a[1][2][3][4][5] = {123, {123, 10e-4}};
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],IntLiteral(100)),VarDecl(Id("c"),[],None),VarDecl(Id("a"),[100],IntLiteral(100)),VarDecl(Id("a"),[1,2,3,4,5],ArrayLiteral([IntLiteral(123),ArrayLiteral([IntLiteral(123),FloatLiteral(0.001)])]))],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))

    def test_316(self):
        input = r"""
Var: a[123] = 123456.2e-3;
Var: b[0X123] = {123,"123str",0x123,0o3217654};
Var: c[0o123] = "stringgggggggg";
Var: c[0O123] = True, c = False;
"""
        expect = Program([VarDecl(Id("a"),[123],FloatLiteral(123.4562)),VarDecl(Id("b"),[291],ArrayLiteral([IntLiteral(123),StringLiteral(r"""123str"""),IntLiteral(291),IntLiteral(860076)])),VarDecl(Id("c"),[83],StringLiteral(r"""stringgggggggg""")),VarDecl(Id("c"),[83],BooleanLiteral(True)),VarDecl(Id("c"),[],BooleanLiteral(False))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))

    def test_317(self):
        input = r"""
Function: test
    Body:
        Var: a[123] = 123456.2e-3;
        Var: b[0X123] = {123,"123str",0x123,0o3217654};
        Var: c[0o123] = "stringgggggggg";
        Var: c[0O123] = True, c = False;
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("a"),[123],FloatLiteral(123.4562)),VarDecl(Id("b"),[291],ArrayLiteral([IntLiteral(123),StringLiteral(r"""123str"""),IntLiteral(291),IntLiteral(860076)])),VarDecl(Id("c"),[83],StringLiteral(r"""stringgggggggg""")),VarDecl(Id("c"),[83],BooleanLiteral(True)),VarDecl(Id("c"),[],BooleanLiteral(False))],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 317))

    """ FuncDecl """

    def test_318(self):
        input = r"""
Function: xyz
    Parameter: ab[1][2][0] = {123, "abcde"}
    Body:
        Var: first = 1;
    EndBody.
"""
        expect = Program([FuncDecl(Id("xyz"),[VarDecl(Id("ab"),[1,2,0],ArrayLiteral([IntLiteral(123),StringLiteral(r"""abcde""")]))],([VarDecl(Id("first"),[],IntLiteral(1))],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))

    def test_319(self):
        input = r"""
Function: main
    Body:
        a = ! a * b && c * -d;
    EndBody.
"""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(ArrayCell(Id("a"),[]),BinaryOp("&&",BinaryOp("*",UnaryOp("!",Id("a")),Id("b")),BinaryOp("*",Id("c"),UnaryOp("-",Id("d")))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 319))

    def test_320(self):
        input = r"""
Function: main
    Body:
        foo(0x1,0x2,0x3,0x4,0x5,0x6,0x7,0x8,0x9);
        foo(0xA,0xB,0xC,0xD,0xE,0xF);
        foo(0x10000000,0XABCDEF);
        foo(0x1234,0X8765);
    EndBody.
"""
        expect = Program([FuncDecl(Id("main"),[],([],[CallStmt(Id("foo"),[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5),IntLiteral(6),IntLiteral(7),IntLiteral(8),IntLiteral(9)]),CallStmt(Id("foo"),[IntLiteral(10),IntLiteral(11),IntLiteral(12),IntLiteral(13),IntLiteral(14),IntLiteral(15)]),CallStmt(Id("foo"),[IntLiteral(268435456),IntLiteral(11259375)]),CallStmt(Id("foo"),[IntLiteral(4660),IntLiteral(34661)])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))

    def test_321(self):
        input = r"""
Function: xyz
    Body:
        foo();
        foo(foo());
        foo(xyz);
        abc = foo(abc[123],number)[123];
    EndBody.
"""
        expect = Program([FuncDecl(Id("xyz"),[],([],[CallStmt(Id("foo"),[]),CallStmt(Id("foo"),[CallExpr(Id("foo"),[])]),CallStmt(Id("foo"),[Id("xyz")]),Assign(ArrayCell(Id("abc"),[]),ArrayCell(CallExpr(Id("foo"),[ArrayCell(Id("abc"),[IntLiteral(123)]),Id("number")]),[IntLiteral(123)]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))

    def test_322(self):
        input = r"""
Function: main
    Body:
        a = a * b [c] -. c [d] [e];
    EndBody.
"""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(ArrayCell(Id("a"),[]),BinaryOp("-.",BinaryOp("*",Id("a"),ArrayCell(Id("b"),[Id("c")])),ArrayCell(Id("c"),[Id("d"),Id("e")])))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 322))

    def test_323(self):
        input = r"""
Function: main
    Body:
        foo(1);
        fib(2+42+324\234*24332);
        remove(3);
        get(4);
    EndBody. 
"""
        expect = Program([FuncDecl(Id("main"),[],([],[CallStmt(Id("foo"),[IntLiteral(1)]),CallStmt(Id("fib"),[BinaryOp("+",BinaryOp("+",IntLiteral(2),IntLiteral(42)),BinaryOp("*",BinaryOp("\\",IntLiteral(324),IntLiteral(234)),IntLiteral(24332)))]),CallStmt(Id("remove"),[IntLiteral(3)]),CallStmt(Id("get"),[IntLiteral(4)])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 323))

    """ Literals """
    """ Int Literals """

    def test_324(self):
        input = r""" 
Var: intLit[12][34] = 0, intLit = 1230000987654321;        
Var: hexa[6789] = 0xAAAAA, haxa = 0X1234567890FDCBA;
Var: octa[12][345] = 0o12345670, octa = 0O76543210;
"""
        expect = Program([VarDecl(Id("intLit"),[12,34],IntLiteral(0)),VarDecl(Id("intLit"),[],IntLiteral(1230000987654321)),VarDecl(Id("hexa"),[6789],IntLiteral(699050)),VarDecl(Id("haxa"),[],IntLiteral(81985529206267066)),VarDecl(Id("octa"),[12,345],IntLiteral(2739128)),VarDecl(Id("octa"),[],IntLiteral(16434824))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 324))

    def test_325(self):
        input = r"""
Function: test
    Body:
        Var: intLit[12][34] = 0, intLit = 1230000987654321;        
        Var: hexa[6789] = 0xAAAAA, haxa = 0X1234567890FDCBA;
        Var: octa[12][345] = 0o12345670, octa = 0O76543210;
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("intLit"),[12,34],IntLiteral(0)),VarDecl(Id("intLit"),[],IntLiteral(1230000987654321)),VarDecl(Id("hexa"),[6789],IntLiteral(699050)),VarDecl(Id("haxa"),[],IntLiteral(81985529206267066)),VarDecl(Id("octa"),[12,345],IntLiteral(2739128)),VarDecl(Id("octa"),[],IntLiteral(16434824))],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))

    def test_326(self):
        input = r"""
Function: main
    Body:
        foo(0o1,0o2,0o3,0o4,0o5,0o6,0o7);
        foo(0O1,0O2,0O3,0O4,0O5,0O6,0O7);
        foo(0o1234567,0O76543210);
    EndBody.
"""
        expect = Program([FuncDecl(Id("main"),[],([],[CallStmt(Id("foo"),[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5),IntLiteral(6),IntLiteral(7)]),CallStmt(Id("foo"),[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5),IntLiteral(6),IntLiteral(7)]),CallStmt(Id("foo"),[IntLiteral(342391),IntLiteral(16434824)])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 326))

    """ Float Literal """

    def test_327(self):
        input = r"""
Function: main
    Body:
        a = 1E1 + 1E+1 + 1E-1 + 1e1 + 1e+1 + 1e-1;
    EndBody.
"""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(ArrayCell(Id("a"),[]),BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",FloatLiteral(10.0),FloatLiteral(10.0)),FloatLiteral(0.1)),FloatLiteral(10.0)),FloatLiteral(10.0)),FloatLiteral(0.1)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 327))

    def test_328(self):
        input = r"""
Var: x = 123.0123;
Var: x = 10e-4;
Var: x = 100e19;
Var: x = 0e-1999;
Var: x = 1234.;
"""
        expect = Program([VarDecl(Id("x"),[],FloatLiteral(123.0123)),VarDecl(Id("x"),[],FloatLiteral(0.001)),VarDecl(Id("x"),[],FloatLiteral(1e+21)),VarDecl(Id("x"),[],FloatLiteral(0.0)),VarDecl(Id("x"),[],FloatLiteral(1234.0))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 328))

    def test_329(self):
        input = r"""
Function: test
    Body:
        Var: x = 123.0123;
        Var: x = 10e-4;
        Var: x = 100e19;
        Var: x = 0e-1999;
        Var: x = 1234.;
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("x"),[],FloatLiteral(123.0123)),VarDecl(Id("x"),[],FloatLiteral(0.001)),VarDecl(Id("x"),[],FloatLiteral(1e+21)),VarDecl(Id("x"),[],FloatLiteral(0.0)),VarDecl(Id("x"),[],FloatLiteral(1234.0))],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 329))

    """ String Literal"""

    def test_330(self):
        input = r"""
Var: x = "abcdefghijklmnopqrstuvxyz";
Var: x = "1234567890-=~`[]\\;./,.'"";
Var: x = "";
"""
        expect = Program([VarDecl(Id("x"),[],StringLiteral(r"""abcdefghijklmnopqrstuvxyz""")),VarDecl(Id("x"),[],StringLiteral("1234567890-=~`[]\\\\;./,.'\"")),VarDecl(Id("x"),[],StringLiteral(""))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 330))

    def test_331(self):
        input = r"""
Function: test
    Body:
        Var: x = "abcdefghijklmnopqrstuvxyz";
        Var: x = "1234567890-=~`[]\\;./,.'"";
        Var: x = "";
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("x"),[],StringLiteral(r"""abcdefghijklmnopqrstuvxyz""")),VarDecl(Id("x"),[],StringLiteral("1234567890-=~`[]\\\\;./,.'\"")),VarDecl(Id("x"),[],StringLiteral(""))],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))

    def test_332(self):
        input = r"""
Function: main
    Body:
        a = "abc\n\r\f";
        b = "Hello World";
        c = "This is my quote:'" QUOTE'" ";
        d = "\t\f\r\n\'";
    EndBody.
"""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(ArrayCell(Id("a"),[]),StringLiteral(r"""abc\n\r\f""")),Assign(ArrayCell(Id("b"),[]),StringLiteral(r"""Hello World""")),Assign(ArrayCell(Id("c"),[]),StringLiteral(r"""This is my quote:'" QUOTE'" """)),Assign(ArrayCell(Id("d"),[]),StringLiteral(r"""\t\f\r\n\'"""))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))

    """ Boolean Literal """

    def test_333(self):
        input = r"""
Var: x = True;
Var: x = False;
Function: test
    Body:
        x = True || False && False || x;
    EndBody.
"""
        expect = Program([VarDecl(Id("x"),[],BooleanLiteral(True)),VarDecl(Id("x"),[],BooleanLiteral(False)),FuncDecl(Id("test"),[],([],[Assign(ArrayCell(Id("x"),[]),BinaryOp("||",BinaryOp("&&",BinaryOp("||",BooleanLiteral(True),BooleanLiteral(False)),BooleanLiteral(False)),Id("x")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 333))

    def test_334(self):
        input = r"""
Function: test
    Body:
        x = {True, False, {True}};
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[Assign(ArrayCell(Id("x"),[]),ArrayLiteral([BooleanLiteral(True),BooleanLiteral(False),ArrayLiteral([BooleanLiteral(True)])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))

    def test_335(self):
        input = r"""
Function: test
    Body:
        x = True *. False && True;
        x[10] = 20;
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[Assign(ArrayCell(Id("x"),[]),BinaryOp("&&",BinaryOp("*.",BooleanLiteral(True),BooleanLiteral(False)),BooleanLiteral(True))),Assign(ArrayCell(Id("x"),[IntLiteral(10)]),IntLiteral(20))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 335))

    def test_336(self):
        input = r"""
Function: test
    Body:
        Return True;
        Continue;
        true = True;
        false = False;
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[Return(BooleanLiteral(True)),Continue(),Assign(ArrayCell(Id("true"),[]),BooleanLiteral(True)),Assign(ArrayCell(Id("false"),[]),BooleanLiteral(False))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 336))

    def test_337(self):
        input = r"""
Function: test
    Body:
        true = !False;
        fasle = !True;
        true = -False;
        false = -True;
        true = !-True;
        false = !-False;
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[Assign(ArrayCell(Id("true"),[]),UnaryOp("!",BooleanLiteral(False))),Assign(ArrayCell(Id("fasle"),[]),UnaryOp("!",BooleanLiteral(True))),Assign(ArrayCell(Id("true"),[]),UnaryOp("-",BooleanLiteral(False))),Assign(ArrayCell(Id("false"),[]),UnaryOp("-",BooleanLiteral(True))),Assign(ArrayCell(Id("true"),[]),UnaryOp("!",UnaryOp("-",BooleanLiteral(True)))),Assign(ArrayCell(Id("false"),[]),UnaryOp("!",UnaryOp("-",BooleanLiteral(False))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 337))

    """ Array Literal """

    def test_338(self):
        input = r"""
Var: x = {123, {345, {567}}};
Var: x = {True, False, "Hihihi", 0x1234};
"""
        expect = Program([VarDecl(Id("x"),[],ArrayLiteral([IntLiteral(123),ArrayLiteral([IntLiteral(345),ArrayLiteral([IntLiteral(567)])])])),VarDecl(Id("x"),[],ArrayLiteral([BooleanLiteral(True),BooleanLiteral(False),StringLiteral(r"""Hihihi"""),IntLiteral(4660)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 338))

    def test_339(self):
        input = r"""
Function: test
    Body:
        Var: x = {123, {345, {567}}};
        Var: x = {True, False, "Hihihi", 0x1234};
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("x"),[],ArrayLiteral([IntLiteral(123),ArrayLiteral([IntLiteral(345),ArrayLiteral([IntLiteral(567)])])])),VarDecl(Id("x"),[],ArrayLiteral([BooleanLiteral(True),BooleanLiteral(False),StringLiteral(r"""Hihihi"""),IntLiteral(4660)]))],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 339))

    def test_340(self):
        input = r"""
Function: test
    Body:
        x = {1,2,3} + {True, False, True};
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[Assign(ArrayCell(Id("x"),[]),BinaryOp("+",ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]),ArrayLiteral([BooleanLiteral(True),BooleanLiteral(False),BooleanLiteral(True)])))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 340))

    def test_341(self):
        input = r"""
Function: test
    Body:
        x = {False, True, {"Hihi"}};
        x = call({1,2,3});
        Return {1,2,3};
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[Assign(ArrayCell(Id("x"),[]),ArrayLiteral([BooleanLiteral(False),BooleanLiteral(True),ArrayLiteral([StringLiteral(r"""Hihi""")])])),Assign(ArrayCell(Id("x"),[]),CallExpr(Id("call"),[ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])])),Return(ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 341))

    def test_342(self):
        input = r"""
Function: test
    Body:
        If 123 =/= 123.0 Then
            x = {{{{{{{{{123}}}}}}}}};
        ElseIf False Then
            x = call({123})[123];
        Else
            Return {{123}, 123} + call();
        EndIf.
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[If([(BinaryOp("=/=",IntLiteral(123),FloatLiteral(123.0)),[],[Assign(ArrayCell(Id("x"),[]),ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([IntLiteral(123)])])])])])])])])]))]),(BooleanLiteral(False),[],[Assign(ArrayCell(Id("x"),[]),ArrayCell(CallExpr(Id("call"),[ArrayLiteral([IntLiteral(123)])]),[IntLiteral(123)]))])],([],[Return(BinaryOp("+",ArrayLiteral([ArrayLiteral([IntLiteral(123)]),IntLiteral(123)]),CallExpr(Id("call"),[])))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 342))

    """ Test exp """

    def test_343(self):
        input = r"""
Function: test
    Body:
        x = 123 == 456.;
        x = 123 != 456.;
        x = 123 > 456.;
        x = 123 < 456.;
        x = 123 >= 456.;
        x = 123 <= 456.;
        x = 123 =/= 456.;
        x = 123 >. 456.;
        x = 123 <. 456.;
        x = 123 >=. 456.;
        x = 123 <=. 456.;
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[Assign(ArrayCell(Id("x"),[]),BinaryOp("==",IntLiteral(123),FloatLiteral(456.0))),Assign(ArrayCell(Id("x"),[]),BinaryOp("!=",IntLiteral(123),FloatLiteral(456.0))),Assign(ArrayCell(Id("x"),[]),BinaryOp(">",IntLiteral(123),FloatLiteral(456.0))),Assign(ArrayCell(Id("x"),[]),BinaryOp("<",IntLiteral(123),FloatLiteral(456.0))),Assign(ArrayCell(Id("x"),[]),BinaryOp(">=",IntLiteral(123),FloatLiteral(456.0))),Assign(ArrayCell(Id("x"),[]),BinaryOp("<=",IntLiteral(123),FloatLiteral(456.0))),Assign(ArrayCell(Id("x"),[]),BinaryOp("=/=",IntLiteral(123),FloatLiteral(456.0))),Assign(ArrayCell(Id("x"),[]),BinaryOp(">.",IntLiteral(123),FloatLiteral(456.0))),Assign(ArrayCell(Id("x"),[]),BinaryOp("<.",IntLiteral(123),FloatLiteral(456.0))),Assign(ArrayCell(Id("x"),[]),BinaryOp(">=.",IntLiteral(123),FloatLiteral(456.0))),Assign(ArrayCell(Id("x"),[]),BinaryOp("<=.",IntLiteral(123),FloatLiteral(456.0)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 343))

    def test_344(self):
        input = r"""
Function: test
    Body:
        y = True && False && True && False;
        y = True || False || True || False;
        y = True && False || True && False || True;
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[Assign(ArrayCell(Id("y"),[]),BinaryOp("&&",BinaryOp("&&",BinaryOp("&&",BooleanLiteral(True),BooleanLiteral(False)),BooleanLiteral(True)),BooleanLiteral(False))),Assign(ArrayCell(Id("y"),[]),BinaryOp("||",BinaryOp("||",BinaryOp("||",BooleanLiteral(True),BooleanLiteral(False)),BooleanLiteral(True)),BooleanLiteral(False))),Assign(ArrayCell(Id("y"),[]),BinaryOp("||",BinaryOp("&&",BinaryOp("||",BinaryOp("&&",BooleanLiteral(True),BooleanLiteral(False)),BooleanLiteral(True)),BooleanLiteral(False)),BooleanLiteral(True)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 344))

    def test_345(self):
        input = r"""
Function: main
    Body:
        a = 1. + 1.1 + 1.11 + 1.111;
    EndBody.
"""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(ArrayCell(Id("a"),[]),BinaryOp("+",BinaryOp("+",BinaryOp("+",FloatLiteral(1.0),FloatLiteral(1.1)),FloatLiteral(1.11)),FloatLiteral(1.111)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 345))

    def test_346(self):
        input = r"""
Function: test
    Body:
        x = 123 + 456. - 12e-9 +. True -. False;
        y = 0 +. 0 +. 0 +. 0 +. 0 +. 1.1 -. 1.1 -. 1.1 -. 1.1 -. 1.1;
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[Assign(ArrayCell(Id("x"),[]),BinaryOp("-.",BinaryOp("+.",BinaryOp("-",BinaryOp("+",IntLiteral(123),FloatLiteral(456.0)),FloatLiteral(1.2e-08)),BooleanLiteral(True)),BooleanLiteral(False))),Assign(ArrayCell(Id("y"),[]),BinaryOp("-.",BinaryOp("-.",BinaryOp("-.",BinaryOp("-.",BinaryOp("+.",BinaryOp("+.",BinaryOp("+.",BinaryOp("+.",BinaryOp("+.",IntLiteral(0),IntLiteral(0)),IntLiteral(0)),IntLiteral(0)),IntLiteral(0)),FloatLiteral(1.1)),FloatLiteral(1.1)),FloatLiteral(1.1)),FloatLiteral(1.1)),FloatLiteral(1.1)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 346))

    def test_347(self):
        input = r"""
Function: test
    Body:
    x = x * 123 * 123.0 * True * False;
    y = y \ 123 \ 123.0 \ True \ False;
    z = z % 123 % 123.0 % True % False;
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[Assign(ArrayCell(Id("x"),[]),BinaryOp("*",BinaryOp("*",BinaryOp("*",BinaryOp("*",Id("x"),IntLiteral(123)),FloatLiteral(123.0)),BooleanLiteral(True)),BooleanLiteral(False))),Assign(ArrayCell(Id("y"),[]),BinaryOp("\\",BinaryOp("\\",BinaryOp("\\",BinaryOp("\\",Id("y"),IntLiteral(123)),FloatLiteral(123.0)),BooleanLiteral(True)),BooleanLiteral(False))),Assign(ArrayCell(Id("z"),[]),BinaryOp("%",BinaryOp("%",BinaryOp("%",BinaryOp("%",Id("z"),IntLiteral(123)),FloatLiteral(123.0)),BooleanLiteral(True)),BooleanLiteral(False)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 347))

    def test_348(self):
        input = r"""
Function: test
    Body:
        x = !True + !False - !123 * !123.0;
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[Assign(ArrayCell(Id("x"),[]),BinaryOp("-",BinaryOp("+",UnaryOp("!",BooleanLiteral(True)),UnaryOp("!",BooleanLiteral(False))),BinaryOp("*",UnaryOp("!",IntLiteral(123)),UnaryOp("!",FloatLiteral(123.0)))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 348))

    def test_349(self):
        input = r"""
Function: test
    Body:
        x = -123 + -123.0 * -True \ -False;
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[Assign(ArrayCell(Id("x"),[]),BinaryOp("+",UnaryOp("-",IntLiteral(123)),BinaryOp("\\",BinaryOp("*",UnaryOp("-",FloatLiteral(123.0)),UnaryOp("-",BooleanLiteral(True))),UnaryOp("-",BooleanLiteral(False)))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 349))

    def test_350(self):
        input = r"""
Function: test
    Body:
        x = -123[123] + !True[12.0e2] * False[123+123];
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[Assign(ArrayCell(Id("x"),[]),BinaryOp("+",UnaryOp("-",ArrayCell(IntLiteral(123),[IntLiteral(123)])),BinaryOp("*",UnaryOp("!",ArrayCell(BooleanLiteral(True),[FloatLiteral(1200.0)])),ArrayCell(BooleanLiteral(False),[BinaryOp("+",IntLiteral(123),IntLiteral(123))]))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 350))

    def test_351(self):
        input = r"""
Function: test
    Body:
        x = !True[123][123.0][True][False][!True[123][123.0][True][False]];
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[Assign(ArrayCell(Id("x"),[]),UnaryOp("!",ArrayCell(BooleanLiteral(True),[IntLiteral(123),FloatLiteral(123.0),BooleanLiteral(True),BooleanLiteral(False),UnaryOp("!",ArrayCell(BooleanLiteral(True),[IntLiteral(123),FloatLiteral(123.0),BooleanLiteral(True),BooleanLiteral(False)]))])))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 351))

    def test_352(self):
        input = r"""
Function: main
    Body:
        x = ((((x))));
    EndBody.
"""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(ArrayCell(Id("x"),[]),Id("x"))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 352))

    def test_353(self):
        input = r"""
Function: main
    Body:
        x = {1,{1,{1,{1,{1,{1,{1,{1}}}}}}}};
    EndBody.
"""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(ArrayCell(Id("x"),[]),ArrayLiteral([IntLiteral(1),ArrayLiteral([IntLiteral(1),ArrayLiteral([IntLiteral(1),ArrayLiteral([IntLiteral(1),ArrayLiteral([IntLiteral(1),ArrayLiteral([IntLiteral(1),ArrayLiteral([IntLiteral(1),ArrayLiteral([IntLiteral(1)])])])])])])])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 353))

    def test_354(self):
        input = r"""
Function: main
    Body:
        x = {{{{{{{{{{{11111}}}}}}}}}}};
    EndBody.
"""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(ArrayCell(Id("x"),[]),ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([IntLiteral(11111)])])])])])])])])])])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 354))

    def test_355(self):
        input = r"""
Function: test
    Body:
        x = call();
        x = call(x, y, z);
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[Assign(ArrayCell(Id("x"),[]),CallExpr(Id("call"),[])),Assign(ArrayCell(Id("x"),[]),CallExpr(Id("call"),[Id("x"),Id("y"),Id("z")]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 355))

    def test_356(self):
        input = r"""
Function: test
    Body:
        x = call({123,456},123,123);
        x = call(!False, -True, -123.123);
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[Assign(ArrayCell(Id("x"),[]),CallExpr(Id("call"),[ArrayLiteral([IntLiteral(123),IntLiteral(456)]),IntLiteral(123),IntLiteral(123)])),Assign(ArrayCell(Id("x"),[]),CallExpr(Id("call"),[UnaryOp("!",BooleanLiteral(False)),UnaryOp("-",BooleanLiteral(True)),UnaryOp("-",FloatLiteral(123.123))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))

    def test_357(self):
        input = r"""
Function: test
    Body:
        x = ((call(call()) +. True) - call(exp));
        x = call()[123] + call(call[123]);
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[Assign(ArrayCell(Id("x"),[]),BinaryOp("-",BinaryOp("+.",CallExpr(Id("call"),[CallExpr(Id("call"),[])]),BooleanLiteral(True)),CallExpr(Id("call"),[Id("exp")]))),Assign(ArrayCell(Id("x"),[]),BinaryOp("+",ArrayCell(CallExpr(Id("call"),[]),[IntLiteral(123)]),CallExpr(Id("call"),[ArrayCell(Id("call"),[IntLiteral(123)])])))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 357))

    """ Stmts """

    def test_358(self):
        input = r"""
Function: test
    Body:
        true[123] = False && True;
        call(call()) = call(call(!False));
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[Assign(ArrayCell(Id("true"),[IntLiteral(123)]),BinaryOp("&&",BooleanLiteral(False),BooleanLiteral(True))),Assign(ArrayCell(CallExpr(Id("call"),[CallExpr(Id("call"),[])]),[]),CallExpr(Id("call"),[CallExpr(Id("call"),[UnaryOp("!",BooleanLiteral(False))])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 358))

    def test_359(self):
        input = r"""
Function: test
    Body:
        If True Then
        EndIf.
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[If([(BooleanLiteral(True),[],[])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))

    def test_360(self):
        input = r"""
Function: test
    Body:
        If True Then
            true = True == False;
        EndIf.
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[If([(BooleanLiteral(True),[],[Assign(ArrayCell(Id("true"),[]),BinaryOp("==",BooleanLiteral(True),BooleanLiteral(False)))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 360))

    def test_361(self):
        input = r"""
Function: test
    Body:
        If nothing 
            Then 
                Var: x = 100;
                call(x + True);
        ElseIf True 
            Then
                Var: x = False;
                call(x + -True);
        EndIf.
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[If([(Id("nothing"),[VarDecl(Id("x"),[],IntLiteral(100))],[CallStmt(Id("call"),[BinaryOp("+",Id("x"),BooleanLiteral(True))])]),(BooleanLiteral(True),[VarDecl(Id("x"),[],BooleanLiteral(False))],[CallStmt(Id("call"),[BinaryOp("+",Id("x"),UnaryOp("-",BooleanLiteral(True)))])])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 361))

    def test_362(self):
        input = r"""
Function: test
    Body:
        If nothing 
            Then 
                Var: x = 100;
                call(x + True);
        Else
            Var: x = False;
            call(x + -True);
        EndIf.
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[If([(Id("nothing"),[VarDecl(Id("x"),[],IntLiteral(100))],[CallStmt(Id("call"),[BinaryOp("+",Id("x"),BooleanLiteral(True))])])],([VarDecl(Id("x"),[],BooleanLiteral(False))],[CallStmt(Id("call"),[BinaryOp("+",Id("x"),UnaryOp("-",BooleanLiteral(True)))])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 362))

    def test_363(self):
        input = r"""
Function: main
    Body:
        If True Then
        Else
            Var: a, b;
            call();
            callcall(call());
        EndIf.
    EndBody.
"""
        expect = Program([FuncDecl(Id("main"),[],([],[If([(BooleanLiteral(True),[],[])],([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],[CallStmt(Id("call"),[]),CallStmt(Id("callcall"),[CallExpr(Id("call"),[])])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 363))

    def test_364(self):
        input = r"""
Function: test
    Body:
        If True 
            Then 
                x = False;
        ElseIf False
            Then
                x = True;
                call();
        ElseIf False
            Then
                x = True;
                call(call());
        ElseIf False
            Then
                x = True;
                call(call(call()));
        ElseIf False
            Then
                x = True;
                call(test());
        Else
            call(test);
        EndIf.
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[If([(BooleanLiteral(True),[],[Assign(ArrayCell(Id("x"),[]),BooleanLiteral(False))]),(BooleanLiteral(False),[],[Assign(ArrayCell(Id("x"),[]),BooleanLiteral(True)),CallStmt(Id("call"),[])]),(BooleanLiteral(False),[],[Assign(ArrayCell(Id("x"),[]),BooleanLiteral(True)),CallStmt(Id("call"),[CallExpr(Id("call"),[])])]),(BooleanLiteral(False),[],[Assign(ArrayCell(Id("x"),[]),BooleanLiteral(True)),CallStmt(Id("call"),[CallExpr(Id("call"),[CallExpr(Id("call"),[])])])]),(BooleanLiteral(False),[],[Assign(ArrayCell(Id("x"),[]),BooleanLiteral(True)),CallStmt(Id("call"),[CallExpr(Id("test"),[])])])],([],[CallStmt(Id("call"),[Id("test")])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 364))

    def test_365(self):
        input = r"""
Function: test
    Body:
        For (x = 1, x < 100, 1) Do
        EndFor.
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[For(Id("x"),IntLiteral(1),BinaryOp("<",Id("x"),IntLiteral(100)),IntLiteral(1),([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 365))

    def test_366(self):
        input = r"""
Function: test
    Body:
        For (x = 1, x < 100, x - 1) Do
            Var: x = {"test"};
        EndFor.
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[For(Id("x"),IntLiteral(1),BinaryOp("<",Id("x"),IntLiteral(100)),BinaryOp("-",Id("x"),IntLiteral(1)),([VarDecl(Id("x"),[],ArrayLiteral([StringLiteral(r"""test""")]))],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))

    def test_367(self):
        input = r"""
Function: main
    Body:
        For (x = 1, x < 100, x + -1) Do
            If True Then
            EndIf.
        EndFor.
    EndBody.
"""
        expect = Program([FuncDecl(Id("main"),[],([],[For(Id("x"),IntLiteral(1),BinaryOp("<",Id("x"),IntLiteral(100)),BinaryOp("+",Id("x"),UnaryOp("-",IntLiteral(1))),([],[If([(BooleanLiteral(True),[],[])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))

    def test_368(self):
        input = r"""
Function: test
    Body:
        For (x = x, x < 100, True && True) Do
            Var: x = "ifStmt()";
            call();
            If True Then
                x = call();
            EndIf.
        EndFor.
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[For(Id("x"),Id("x"),BinaryOp("<",Id("x"),IntLiteral(100)),BinaryOp("&&",BooleanLiteral(True),BooleanLiteral(True)),([VarDecl(Id("x"),[],StringLiteral(r"""ifStmt()"""))],[CallStmt(Id("call"),[]),If([(BooleanLiteral(True),[],[Assign(ArrayCell(Id("x"),[]),CallExpr(Id("call"),[]))])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 368))

    def test_369(self):
        input = r"""
Function: test
    Body:
        For (x = x, x < 100, True && True) Do
            For (x = 100*x, x == 100, x % 20 == 100) Do
                call(x);
            EndFor.
        EndFor.
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[For(Id("x"),Id("x"),BinaryOp("<",Id("x"),IntLiteral(100)),BinaryOp("&&",BooleanLiteral(True),BooleanLiteral(True)),([],[For(Id("x"),BinaryOp("*",IntLiteral(100),Id("x")),BinaryOp("==",Id("x"),IntLiteral(100)),BinaryOp("==",BinaryOp("%",Id("x"),IntLiteral(20)),IntLiteral(100)),([],[CallStmt(Id("call"),[Id("x")])]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))

    def test_370(self):
        input = r"""
Function: test
    Body:
        While True Do
            Var: x;
            Var: x[100];
            Var: x[100] = 100;
        EndWhile.
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[While(BooleanLiteral(True),([VarDecl(Id("x"),[],None),VarDecl(Id("x"),[100],None),VarDecl(Id("x"),[100],IntLiteral(100))],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))

    def test_371(self):
        input = r"""
Function: test
    Body:
        While False Do
            Var: x[10];
            call();
            If True Then
                true = True == False;
            EndIf.
        EndWhile.
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[While(BooleanLiteral(False),([VarDecl(Id("x"),[10],None)],[CallStmt(Id("call"),[]),If([(BooleanLiteral(True),[],[Assign(ArrayCell(Id("true"),[]),BinaryOp("==",BooleanLiteral(True),BooleanLiteral(False)))])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 371))

    def test_372(self):
        input = r"""
Function: test
    Body:
        Do 
            Var: x[10];
            call();
            If True Then
                true = True == False;
            EndIf.
        While !True
        EndDo.
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[Dowhile(([VarDecl(Id("x"),[10],None)],[CallStmt(Id("call"),[]),If([(BooleanLiteral(True),[],[Assign(ArrayCell(Id("true"),[]),BinaryOp("==",BooleanLiteral(True),BooleanLiteral(False)))])],([],[]))]),UnaryOp("!",BooleanLiteral(True)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))

    def test_373(self):
        input = r"""
Function: test
    Body:
        Break;
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[Break()]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))

    def test_374(self):
        input = r"""
Function: test
    Body:
        If True Then
            Break;
        Else
            call(break);
        EndIf.
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[If([(BooleanLiteral(True),[],[Break()])],([],[CallStmt(Id("call"),[Id("break")])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 374))

    def test_375(self):
        input = r"""
Function: test
    Body:
        If True Then
            Break;
        ElseIf False Then
            call(break);
        Else
            cal(break(call()));
        EndIf.
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[If([(BooleanLiteral(True),[],[Break()]),(BooleanLiteral(False),[],[CallStmt(Id("call"),[Id("break")])])],([],[CallStmt(Id("cal"),[CallExpr(Id("break"),[CallExpr(Id("call"),[])])])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))

    def test_376(self):
        input = r"""
Function: test
    Body:
        Continue;
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[Continue()]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))

    def test_377(self):
        input = r"""
Function: test
    Body:
        If True Then
            Continue;
        Else
            call(continue);
        EndIf.
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[If([(BooleanLiteral(True),[],[Continue()])],([],[CallStmt(Id("call"),[Id("continue")])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 377))

    def test_378(self):
        input = r"""
Function: test
    Body:
        If True Then
            Continue;
        ElseIf False Then
            call(continue);
        Else
            cal(continue(call()));
        EndIf.
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[If([(BooleanLiteral(True),[],[Continue()]),(BooleanLiteral(False),[],[CallStmt(Id("call"),[Id("continue")])])],([],[CallStmt(Id("cal"),[CallExpr(Id("continue"),[CallExpr(Id("call"),[])])])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 378))

    def test_379(self):
        input = r"""
Function: test
    Body:
        If a Then
            a = a;
        ElseIf a Then
            a = a;
        Else
            a(a);
        EndIf.
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[If([(Id("a"),[],[Assign(ArrayCell(Id("a"),[]),Id("a"))]),(Id("a"),[],[Assign(ArrayCell(Id("a"),[]),Id("a"))])],([],[CallStmt(Id("a"),[Id("a")])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 379))

    def test_380(self):
        input = r"""
Function: test
    Body:
        Return;
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 380))

    def test_381(self):
        input = r"""
Function: test
    Body:
        If True Then
            Return;
        Else
            call(return);
        EndIf.
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[If([(BooleanLiteral(True),[],[Return(None)])],([],[CallStmt(Id("call"),[Id("return")])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 381))

    def test_382(self):
        input = r"""
Function: test
    Body:
        If True Then
            Return;
        ElseIf False Then
            call(return);
        Else
            cal(return(call()));
        EndIf.
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[If([(BooleanLiteral(True),[],[Return(None)]),(BooleanLiteral(False),[],[CallStmt(Id("call"),[Id("return")])])],([],[CallStmt(Id("cal"),[CallExpr(Id("return"),[CallExpr(Id("call"),[])])])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 382))

    def test_383(self):
        input = r"""
Function: test
    Body:
        If True Then
            Return(True);
        ElseIf False Then
            Return(False);
        ElseIf False Then
            Return(False);
        ElseIf False Then
            Return(False);
        ElseIf False Then
            Return(False);
        Else
            Return;
        EndIf.
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[If([(BooleanLiteral(True),[],[Return(BooleanLiteral(True))]),(BooleanLiteral(False),[],[Return(BooleanLiteral(False))]),(BooleanLiteral(False),[],[Return(BooleanLiteral(False))]),(BooleanLiteral(False),[],[Return(BooleanLiteral(False))]),(BooleanLiteral(False),[],[Return(BooleanLiteral(False))])],([],[Return(None)]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 383))

    def test_384(self):
        input = r"""
Function: test
    Body:
        If 123 == 123.0 Then
            Continue;
        ElseIf True != False Then
            Break;
        Else
            Return;
            Return test;
            Return(test);
            Return test();
        EndIf.
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[If([(BinaryOp("==",IntLiteral(123),FloatLiteral(123.0)),[],[Continue()]),(BinaryOp("!=",BooleanLiteral(True),BooleanLiteral(False)),[],[Break()])],([],[Return(None),Return(Id("test")),Return(Id("test")),Return(CallExpr(Id("test"),[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 384))

    def test_385(self):
        input = r"""
Function: test
    Body:
        For (x = 0, x < 100, x + y + z + 10e10) Do
            Continue;
            If True Then
                x = x * 10;
            EndIf.
            Return test();
        EndFor.
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[For(Id("x"),IntLiteral(0),BinaryOp("<",Id("x"),IntLiteral(100)),BinaryOp("+",BinaryOp("+",BinaryOp("+",Id("x"),Id("y")),Id("z")),FloatLiteral(100000000000.0)),([],[Continue(),If([(BooleanLiteral(True),[],[Assign(ArrayCell(Id("x"),[]),BinaryOp("*",Id("x"),IntLiteral(10)))])],([],[])),Return(CallExpr(Id("test"),[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 385))

    """ Mix """

    def test_386(self):
        input = r"""
Function: test
    Body:
        Var: x[10], x;
        x = x +. x;
        x = x[0] + x[10];
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("x"),[10],None),VarDecl(Id("x"),[],None)],[Assign(ArrayCell(Id("x"),[]),BinaryOp("+.",Id("x"),Id("x"))),Assign(ArrayCell(Id("x"),[]),BinaryOp("+",ArrayCell(Id("x"),[IntLiteral(0)]),ArrayCell(Id("x"),[IntLiteral(10)])))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))

    def test_387(self):
        input = r"""
Function: main
    Body:
        a = 1 * 2;
        a = 1 *. 2;
        a = 1 \ 2;
        a = 1 \. 2;
        a = 1 % 2;
        a = 1 + 2;
        a = 1 +. 2;
        a = 1 - 2;
        a = 1 -. 2;
        a = 1 && 2;
        a = 1 || 2;
        a = 1 == 2;
        a = 1 != 2;
        a = !1;
        a = -1;
        a = -.1;
        a = 1 =/= 2;
        a = 1 < 2;
        a = 1 <. 2;
        a = 1 > 2;
        a = 1 >. 2;
        a = 1 <= 2;
        a = 1 <=. 2;
        a = 1 >= 2;
        a = 1 >=. 2;
    EndBody.
"""
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(ArrayCell(Id("a"),[]),BinaryOp("*",IntLiteral(1),IntLiteral(2))),Assign(ArrayCell(Id("a"),[]),BinaryOp("*.",IntLiteral(1),IntLiteral(2))),Assign(ArrayCell(Id("a"),[]),BinaryOp("\\",IntLiteral(1),IntLiteral(2))),Assign(ArrayCell(Id("a"),[]),BinaryOp("\\.",IntLiteral(1),IntLiteral(2))),Assign(ArrayCell(Id("a"),[]),BinaryOp("%",IntLiteral(1),IntLiteral(2))),Assign(ArrayCell(Id("a"),[]),BinaryOp("+",IntLiteral(1),IntLiteral(2))),Assign(ArrayCell(Id("a"),[]),BinaryOp("+.",IntLiteral(1),IntLiteral(2))),Assign(ArrayCell(Id("a"),[]),BinaryOp("-",IntLiteral(1),IntLiteral(2))),Assign(ArrayCell(Id("a"),[]),BinaryOp("-.",IntLiteral(1),IntLiteral(2))),Assign(ArrayCell(Id("a"),[]),BinaryOp("&&",IntLiteral(1),IntLiteral(2))),Assign(ArrayCell(Id("a"),[]),BinaryOp("||",IntLiteral(1),IntLiteral(2))),Assign(ArrayCell(Id("a"),[]),BinaryOp("==",IntLiteral(1),IntLiteral(2))),Assign(ArrayCell(Id("a"),[]),BinaryOp("!=",IntLiteral(1),IntLiteral(2))),Assign(ArrayCell(Id("a"),[]),UnaryOp("!",IntLiteral(1))),Assign(ArrayCell(Id("a"),[]),UnaryOp("-",IntLiteral(1))),Assign(ArrayCell(Id("a"),[]),UnaryOp("-.",IntLiteral(1))),Assign(ArrayCell(Id("a"),[]),BinaryOp("=/=",IntLiteral(1),IntLiteral(2))),Assign(ArrayCell(Id("a"),[]),BinaryOp("<",IntLiteral(1),IntLiteral(2))),Assign(ArrayCell(Id("a"),[]),BinaryOp("<.",IntLiteral(1),IntLiteral(2))),Assign(ArrayCell(Id("a"),[]),BinaryOp(">",IntLiteral(1),IntLiteral(2))),Assign(ArrayCell(Id("a"),[]),BinaryOp(">.",IntLiteral(1),IntLiteral(2))),Assign(ArrayCell(Id("a"),[]),BinaryOp("<=",IntLiteral(1),IntLiteral(2))),Assign(ArrayCell(Id("a"),[]),BinaryOp("<=.",IntLiteral(1),IntLiteral(2))),Assign(ArrayCell(Id("a"),[]),BinaryOp(">=",IntLiteral(1),IntLiteral(2))),Assign(ArrayCell(Id("a"),[]),BinaryOp(">=.",IntLiteral(1),IntLiteral(2)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 387))

    def test_388(self):
        input = r"""
Function: test
    Body:
        While True Do
            call();
        EndWhile.
    EndBody.
Function: main
    Body:
        While True Do
            call();
        EndWhile.
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[While(BooleanLiteral(True),([],[CallStmt(Id("call"),[])]))])),FuncDecl(Id("main"),[],([],[While(BooleanLiteral(True),([],[CallStmt(Id("call"),[])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 388))

    def test_389(self):
        input = r"""
Function: test
    Body:
        x = 1000 != True && 1000 || False;
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[Assign(ArrayCell(Id("x"),[]),BinaryOp("!=",IntLiteral(1000),BinaryOp("||",BinaryOp("&&",BooleanLiteral(True),IntLiteral(1000)),BooleanLiteral(False))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 389))

    def test_390(self):
        input = r"""
Function: test
    Body:
        x = call()[100];
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[Assign(ArrayCell(Id("x"),[]),ArrayCell(CallExpr(Id("call"),[]),[IntLiteral(100)]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 390))

    def test_391(self):
        input = r"""
Function: max
    Parameter: x, y, z
    Body:
        Return max(x,y,z);
    EndBody.
"""
        expect = Program([FuncDecl(Id("max"),[VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None)],([],[Return(CallExpr(Id("max"),[Id("x"),Id("y"),Id("z")]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 391))

    def test_392(self):
        input = r"""
Function: min
    Parameter: x, y, z
    Body:
        Return min(x,y,z);
    EndBody.
"""
        expect = Program([FuncDecl(Id("min"),[VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None)],([],[Return(CallExpr(Id("min"),[Id("x"),Id("y"),Id("z")]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 392))

    def test_393(self):
        input = r"""
Function: test
    Body:
        For (a = a, a, a) Do
            For (a = a, a, a) Do
                For (a = a, a, a) Do
                    For (a = a, a, a) Do
                    EndFor.
                EndFor.
            EndFor.         
        EndFor.
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[For(Id("a"),Id("a"),Id("a"),Id("a"),([],[For(Id("a"),Id("a"),Id("a"),Id("a"),([],[For(Id("a"),Id("a"),Id("a"),Id("a"),([],[For(Id("a"),Id("a"),Id("a"),Id("a"),([],[]))]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 393))

    def test_394(self):
        input = r"""
Function: test
    Body:
        Do 
            Do 
                Do 
                    Do 
                    While True EndDo.
                While True EndDo.
            While True EndDo.
        While True EndDo.
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[Dowhile(([],[Dowhile(([],[Dowhile(([],[Dowhile(([],[]),BooleanLiteral(True))]),BooleanLiteral(True))]),BooleanLiteral(True))]),BooleanLiteral(True))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 394))

    def test_395(self):
        input = r"""
Function: test
    Body:
        If True Then
            If True Then
                If True Then
                    If True Then
                    EndIf.
                EndIf.
            EndIf.
        EndIf.
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[If([(BooleanLiteral(True),[],[If([(BooleanLiteral(True),[],[If([(BooleanLiteral(True),[],[If([(BooleanLiteral(True),[],[])],([],[]))])],([],[]))])],([],[]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 395))

    def test_396(self):
        input = r"""
Function: test
    Body:
        If True Then
            Break;
            If True Then
                Break;
                If True Then
                    Break;
                    If True Then
                        Break;
                    EndIf.
                EndIf.
            EndIf.
        EndIf.
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[If([(BooleanLiteral(True),[],[Break(),If([(BooleanLiteral(True),[],[Break(),If([(BooleanLiteral(True),[],[Break(),If([(BooleanLiteral(True),[],[Break()])],([],[]))])],([],[]))])],([],[]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 396))

    def test_397(self):
        input = r"""
Function: test
    Body:
        Do 
            Continue;
            Do 
                Continue;
                Do 
                    Continue;
                    Do 
                        Continue;
                    While True EndDo.
                While True EndDo.
            While True EndDo.
        While True EndDo.
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[Dowhile(([],[Continue(),Dowhile(([],[Continue(),Dowhile(([],[Continue(),Dowhile(([],[Continue()]),BooleanLiteral(True))]),BooleanLiteral(True))]),BooleanLiteral(True))]),BooleanLiteral(True))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 397))

    def test_398(self):
        input = r"""
Function: test
    Body:
        For (a = a, a, a) Do
            Return(True);
            For (a = a, a, a) Do
                Return(False);
                For (a = a, a, a) Do
                    Return for();
                    For (a = a, a, a) Do
                        Return return();
                    EndFor.
                EndFor.
            EndFor.         
        EndFor.
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([],[For(Id("a"),Id("a"),Id("a"),Id("a"),([],[Return(BooleanLiteral(True)),For(Id("a"),Id("a"),Id("a"),Id("a"),([],[Return(BooleanLiteral(False)),For(Id("a"),Id("a"),Id("a"),Id("a"),([],[Return(CallExpr(Id("for"),[])),For(Id("a"),Id("a"),Id("a"),Id("a"),([],[Return(CallExpr(Id("return"),[]))]))]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 398))

    def test_399(self):
        input = r"""
Function: test
    Body:
    EndBody.
        Function: test
            Body:
            EndBody.
                Function: test
                    Body:
                    EndBody.
                        Function: test
                            Body:
                                Var: none = "function()";
                            EndBody.            
"""
        expect = Program([FuncDecl(Id("test"),[],([],[])),FuncDecl(Id("test"),[],([],[])),FuncDecl(Id("test"),[],([],[])),FuncDecl(Id("test"),[],([VarDecl(Id("none"),[],StringLiteral(r"""function()"""))],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 399))

    def test_400(self):
        input = r"""
Function: test
    Body:
        Var: x = "GOOD BYE, EOF";
    EndBody.
"""
        expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("x"),[],StringLiteral(r"""GOOD BYE, EOF"""))],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 400))

