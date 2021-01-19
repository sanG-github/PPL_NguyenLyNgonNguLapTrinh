import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):

    """ Program structure """

    def test_201(self):
        input = ""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 201))

    def test_202(self):
        input = r"""
Var: a;
Function: main
    Body:
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 202))

    def test_203(self):
        input = r"""
Function: main
    Body:
    EndBody
"""
        expect = r"""Error on line 5 col 0: <EOF>"""
        self.assertTrue(TestParser.checkParser(input, expect, 203))

    def test_204(self):
        input = r"""
Function: main
    Body:
    EndBody.
Var: x = 1;
"""
        expect = r"""Error on line 5 col 0: Var"""
        self.assertTrue(TestParser.checkParser(input, expect, 204))

    """ Variable declaration """

    def test_205(self):
        input = r"""
Var: a;
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 205))

    def test_206(self):
        input = r"""
Var: a = 09999;
"""
        expect = r"""Error on line 2 col 10: 9999"""
        self.assertTrue(TestParser.checkParser(input, expect, 206))

    """ Variable list """

    def test_207(self):
        input = r"""
Var: a, b, c = 10, d = 0x123;
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 207))

    def test_208(self):
        input = r"""
Var: a, b, c[1] = 2, [];
"""
        expect = r"""Error on line 2 col 21: ["""
        self.assertTrue(TestParser.checkParser(input, expect, 208))

    """ Composite variable """

    def test_209(self):
        input = r"""
Var: a[1], a[1][2], a[1][2][3], a[1][2][3][4];
Var: a[0], a[0xA], a[0o80];
"""
        expect = r"""Error on line 3 col 22: o80"""
        self.assertTrue(TestParser.checkParser(input, expect, 209))

    def test_210(self):
        input = r"""
Var: a[-01234];
"""
        expect = r"""Error on line 2 col 7: -"""
        self.assertTrue(TestParser.checkParser(input, expect, 210))

    def test_211(self):
        input = r"""
Var: a[1.0];
"""
        expect = r"""Error on line 2 col 7: 1.0"""
        self.assertTrue(TestParser.checkParser(input, expect, 211))

    def test_212(self):
        input = r"""
Var: a[1] = b;
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 212))

    def test_213(self):
        input = r"""
Var: a[];
"""
        expect = r"""Error on line 2 col 7: ]"""
        self.assertTrue(TestParser.checkParser(input, expect, 213))

    """ Variable with initialization """

    def test_214(self):
        input = r"""
Var: a = 1, b = 1., c = " comment ** abc **", d = True, e = {1};
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 214))

    def test_215(self):
        input = r"""
Var: a = --1;
"""
        expect = r"""Error on line 2 col 9: -"""
        self.assertTrue(TestParser.checkParser(input, expect, 215))

    def test_216(self):
        input = r"""
Var: a = ++a;
"""
        expect = r"""Error on line 2 col 9: +"""
        self.assertTrue(TestParser.checkParser(input, expect, 216))

    def test_217(self):
        input = r"""
Var: a = 00.00;
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 217))

    def test_218(self):
        input = r"""
Var: 1 = a;
"""
        expect = r"""Error on line 2 col 5: 1"""
        self.assertTrue(TestParser.checkParser(input, expect, 218))

    """ Function declaration """

    def test_219(self):
        input = r"""
Function: main
    Body:
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 219))

    def test_220(self):
        input = r"""
Function: main
Parameter: a,b,c
"""
        expect = r"""Error on line 4 col 0: <EOF>"""
        self.assertTrue(TestParser.checkParser(input, expect, 220))

    def test_221(self):
        input = r"""
Function: parameter
Parameter: a
    Body:
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 221))

    def test_222(self):
        input = r"""
Function: main
    Body:
        Var: a;
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 222))

    def test_223(self):
        input = r"""
Function: main
    Body:
        foo(zzzz);
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 223))

    def test_224(self):
        input = r"""
Function: main
    Body:
        Var: a;
        foo(zzzz);
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 224))

    def test_225(self):
        input = r"""
Function: foo
    Body:
        foo(zzzz);
        Var: a;
    EndBody.
"""
        expect = r"""Error on line 5 col 8: Var"""
        self.assertTrue(TestParser.checkParser(input, expect, 225))

    """ Function parameter """

    def test_226(self):
        input = r"""
Function: main
    Parameter: a
    Body:
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 226))

    def test_227(self):
        input = r"""
Function: main
    Parameter: a, b
    Body:
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 227))

    def test_228(self):
        input = r"""
Function: mainParameter
    Parameter: a
    Body:
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 228))

    def test_229(self):
        input = r"""
Function: main
    Parameter: a, Parameter
    Body:
    EndBody.
"""
        expect = r"""Error on line 3 col 18: Parameter"""
        self.assertTrue(TestParser.checkParser(input, expect, 229))

    def test_230(self):
        input = r"""
Function: main
    Parameter:
    Body:
        Var: x = 10100;
    EndBody.
"""
        expect = r"""Error on line 4 col 4: Body"""
        self.assertTrue(TestParser.checkParser(input, expect, 230))

    def test_231(self):
        input = r"""
Function: main
    Parameter: a = 1;
    Body:
    EndBody.
"""
        expect = r"""Error on line 3 col 20: ;"""
        self.assertTrue(TestParser.checkParser(input, expect, 231))

    def test_232(self):
        input = r"""
Function: main
    Body:
        Body:
        EndBody.
    EndBody.
"""
        expect = r"""Error on line 4 col 8: Body"""
        self.assertTrue(TestParser.checkParser(input, expect, 232))

    """ If statement """

    def test_233(self):
        input = r"""
Function: main
    Body:
        If True Then
        EndIf.
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 233))

    def test_234(self):
        input = r"""
Function: main
    Body:
        EndBody.
    EndBody.
"""
        expect = r"""Error on line 5 col 4: EndBody"""
        self.assertTrue(TestParser.checkParser(input, expect, 234))

    def test_235(self):
        input = r"""
Function: main
    Body:
        If a Then
            Var: a = 1;
        EndIf.
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 235))

    def test_236(self):
        input = r"""
Function: main
    Body:
        If a Then
            foo(zzzz);
        EndIf.
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 236))

    def test_237(self):
        input = r"""
Function: main
    Body:
        If a Then
            Var: a = 1;
            foo(zzzz);
        EndIf.
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 237))

    def test_238(self):
        input = r"""
Function: main
    Body:
        If a Then
            Var: a = 1;
            foo(zzzz);
        EndIf.
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 238))

    """ ElseIf """

    def test_239(self):
        input = r"""
Function: main
    Body:
        If True Then
        ElseIf True Then
        EndIf.
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 239))

    def test_240(self):
        input = r"""
Function: main
    Body:
        If True Then
        EndIf.
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 240))

    def test_241(self):
        input = r"""
Function: main
    Body:
        If True Then
        ElseIf True Then
        EndIf.
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 241))

    def test_242(self):
        input = r"""
Function: main
    Body:
        If True Then
        ElseIf True Then
        ElseIf True Then
        EndIf.
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 242))

    def test_243(self):
        input = r"""
Function: main
    Body:
        If True Then
        ElseIf a Then
        ElseIf b Then
        EndIf.
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 243))

    def test_244(self):
        input = r"""
Function: main
    Body:
        If True Then
        ElseIf True Then
            Var: a = 1;
        EndIf.
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 244))

    def test_245(self):
        input = r"""
Function: main
    Body:
        If True Then
        ElseIf True Then
            foo(zzz);
        EndIf.
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 245))

    def test_246(self):
        input = r"""
Function: main
    Body:
        If True Then
        ElseIf True Then
            Var: a = 1;
            foo(zzzz);
        EndIf.
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 246))

    def test_247(self):
        input = r"""
Function: main
    Body:
        If True Then
        ElseIf True Then
            foo(zzzz);
            Var: a = 1;
        EndIf.
    EndBody.
"""
        expect = r"""Error on line 7 col 12: Var"""
        self.assertTrue(TestParser.checkParser(input, expect, 247))
    """ Else """
    def test_248(self):
        input = r"""
Function: main
    Body:
        If True Then
        ElseIf True Then
        Else
        EndIf.
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 248))

    def test_249(self):
        input = r"""
Function: main
    Body:
        If True Then
        Else
        EndIf.
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 249))

    def test_250(self):
        input = r"""
Function: main
    Body:
        If True Then
        EndIf.
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 250))

    def test_251(self):
        input = r"""
Function: main
    Body:
        If True Then
        Else Then
        EndIf.
    EndBody.
"""
        expect = r"""Error on line 5 col 13: Then"""
        self.assertTrue(TestParser.checkParser(input, expect, 251))

    def test_252(self):
        input = r"""
Function: main
    Body:
        If True Then
        Else
            Var: a;
        EndIf.
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 252))

    def test_253(self):
        input = r"""
Function: main
    Body:
        If True Then
        Else
            foo();
        EndIf.
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 253))

    def test_254(self):
        input = r"""
Function: main
    Body:
        If True Then
        Else
            Var: a;
            foo(zzzz);
        EndIf.
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 254))

    def test_255(self):
        input = r"""
Function: main
    Body:
        If True Then
        Else
            foo(zzzz);
            Var: a;
        EndIf.
    EndBody.
"""
        expect = r"""Error on line 7 col 12: Var"""
        self.assertTrue(TestParser.checkParser(input, expect, 255))

    """ While """

    def test_256(self):
        input = r"""
Function: main
    Body:
        While True Do
        EndWhile.
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 256))

    def test_257(self):
        input = r"""
Function: main
    Body:
        While True Do
            Var: a = 3;
        EndWhile.
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 257))

    def test_258(self):
        input = r"""
Function: main
    Body:
        While True Do
            foo(zzzz);
        EndWhile.
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 258))

    def test_259(self):
        input = r"""
Function: main
    Body:
        While True Do
            Var: a;
            foo(zzzz);
        EndWhile.
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 259))

    def test_260(self):
        input = r"""
Function: main
    Body:
        While True Do
            foo(zzzz);
            Var: a;
        EndWhile.
    EndBody.
"""
        expect = r"""Error on line 6 col 12: Var"""
        self.assertTrue(TestParser.checkParser(input, expect, 260))

    """ Do """

    def test_261(self):
        input = r"""
Function: main
    Body:
        Do
        While True
        EndDo.
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 261))

    def test_262(self):
        input = r"""
Function: main
    Body:
        Do
            Var: a;
        While True
        EndDo.
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 262))

    def test_263(self):
        input = r"""
Function: main
    Body:
        Do
            foo();
        While True
        EndDo.
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 263))

    def test_264(self):
        input = r"""
Function: main
    Body:
        Do
            Var: a;
            foo();
        While True
        EndDo.
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 264))

    def test_265(self):
        input = r"""
Function: main
    Body:
        Do
            foo(zzzz);
            Var: a;
        While True
        EndDo.
    EndBody.
"""
        expect = r"""Error on line 6 col 12: Var"""
        self.assertTrue(TestParser.checkParser(input, expect, 265))

    """ For """

    def test_266(self):
        input = r"""
Function: main
    Body:
        For (a = 1 + 1, 1.0, --1) Do
        EndFor.
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 266))

    def test_267(self):
        input = r"""
Function: main
    Body:
        For (a, a < 9, 101) Do
        EndFor.
    EndBody.
"""
        expect = r"""Error on line 4 col 14: ,"""
        self.assertTrue(TestParser.checkParser(input, expect, 267))

    def test_268(self):
        input = r"""
Function: main
    Body:
        For (Var: a = 1, a < 29, 1021) Do
        EndFor.
    EndBody.
"""
        expect = r"""Error on line 4 col 13: Var"""
        self.assertTrue(TestParser.checkParser(input, expect, 268))

    def test_269(self):
        input = r"""
Function: main
    Body:
        For (a[1] = 1, a < 29, 1021) Do
        EndFor.
    EndBody.
"""
        expect = r"""Error on line 4 col 14: ["""
        self.assertTrue(TestParser.checkParser(input, expect, 269))

    def test_270(self):
        input = r"""
Function: main
    Body:
        For (a = 1, a < 29, 1021) Do
            Var: a;
        EndFor.
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 270))

    def test_271(self):
        input = r"""
Function: main
    Body:
        For (a = 1, a < 10, 1) Do
            foo(zzzz);
        EndFor.
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 271))

    def test_272(self):
        input = r"""
Function: main
    Body:
        For (a = 1, a < 10, 1) Do
            Var: a;
            foo(zzzz);
        EndFor.
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 272))

    def test_273(self):
        input = r"""
Function: main
    Body:
        For (a = 1, a < 10, 1) Do
            foo(zzz);
            Var: a;
        EndFor.
    EndBody.
"""
        expect = r"""Error on line 6 col 12: Var"""
        self.assertTrue(TestParser.checkParser(input, expect, 273))

    """ Break """

    def test_274(self):
        input = r"""
Function: main
    Body:
        Break;
        Break;
        Break;
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 274))

    """ Continue """

    def test_275(self):
        input = r"""
Function: main
    Body:
        Continue;
        Continue;
        Continue;
        Continue;
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 275))

    """ Return """

    def test_276(self):
        input = r"""
Function: main
    Body:
        Return;
        Return;
        Return;
        Return;
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 276))

    def test_277(self):
        input = r"""
Function: main
    Body:
        Return 1;
        Return 1;
        Return 1;
        Return 1;
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 277))

    """ Function call """

    def test_278(self):
        input = r"""
Function: main
    Body:
        foo(zzzz);
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 278))

    def test_279(self):
        input = r"""
Function: main
    Body:
        foo(zzzz);
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 279))

    def test_280(self):
        input = r"""
Function: main
    Body:
        foo(1, a[2], True, "", 1.);
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 280))

    def test_281(self):
        input = r"""
Function: main
    Body:
        foo(foo(foo(zzzz)));
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 281))

    def test_282(self):
        input = r"""
Function: main
    Body:
        foo(zzz)(zzzzz);
    EndBody.
"""
        expect = r"""Error on line 4 col 16: ("""
        self.assertTrue(TestParser.checkParser(input, expect, 282))

    """ Assignment """

    def test_283(self):
        input = r"""
Function: main
    Body:
        a = 1 + 1;
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 283))

    def test_284(self):
        input = r"""
Function: main
    Body:
        a = b = 1;
    EndBody.
"""
        expect = r"""Error on line 4 col 14: ="""
        self.assertTrue(TestParser.checkParser(input, expect, 284))

    def test_285(self):
        input = r"""
Function: main
    Body:
        a[-1][foo(zzzz) + a] = 1;
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 285))

    """ Expressionn """

    def test_286(self):
        input = r"""
Function: main
    Body:
        a = 1 * 1;
        a = 1 *. 1;
        a = 1 - 1;
        a = 1 -. 1;
        a = 1 && 1;
        a = 1 || 1;
        a = 1 == 1;
        a = 1 != 1;
        a = 1 =/= 1;
        a = 1 =/= 1;
        a = 1 =/= 1;
        a = 1 =/= 1;
        a = 1 \ 1;
        a = 1 \. 1;
        a = 1 % 1;
        a = 1 + 1;
        a = 1 +. 1;
        a = 1 < 1;
        a = 1 <. 1;
        a = 1 > 1;
        a = 1 >. 1;
        a = 1 <= 1;
        a = 1 <=. 1;
        a = 1 >= 1;
        a = 1 >=. 1;
        a = !1;
        a = -1;
        a = -.1;
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 286))

    def test_287(self):
        input = r"""
Function: main
    Body:
        a = 1;
        a = 1.0;
        a = True;
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 287))

    def test_288(self):
        input = r"""
Function: main
    Body:
        a = { 1, 2, 3, 4 };
        a = { True, False };
        a = { {1,2}, {3,4} };
        a = {{{{{1}}}}, {1}, 1};
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 288))

    def test_289(self):
        input = r"""
Function: main
    Body:
        a = { -1 };
    EndBody.
"""
        expect = r"""Error on line 4 col 14: -"""
        self.assertTrue(TestParser.checkParser(input, expect, 289))

    def test_290(self):
        input = r"""
Function: main
    Body:
        a = b;
        a = foo(zzzz);
        a = foo(1,True);
        a = a[1];
        a = foo(zzzz)[1];
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 290))

    def test_291(self):
        input = r"""
Function: main
    Body:
        a = (aazaza);
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 291))

    def test_292(self):
        input = r"""
Function: main
    Body:
        a = ();
    EndBody.
"""
        expect = r"""Error on line 4 col 13: )"""
        self.assertTrue(TestParser.checkParser(input, expect, 292))

    def test_293(self):
        input = r"""
Function: main
    Body:
        a = (((azazaza)));
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 293))

    def test_294(self):
        input = r"""
Function: main
    Body:
        a = --1;
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 294))

    def test_295(self):
        input = r"""
Function: main
    Body:
        a = +12345;
    EndBody.
"""
        expect = r"""Error on line 4 col 12: +"""
        self.assertTrue(TestParser.checkParser(input, expect, 295))

    def test_296(self):
        input = r"""
Function: main
    Body:
        a = 1++12345;
    EndBody.
"""
        expect = r"""Error on line 4 col 14: +"""
        self.assertTrue(TestParser.checkParser(input, expect, 296))

    def test_297(self):
        input = r"""
Function: main
    Body:
        a = !a > b || c + d * e[2];
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 297))

    def test_298(self):
        input = r"""
Function: main
    Body:
        a = !--.1;
        a = 3----------------1;
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 298))

    def test_299(self):
        input = r"""
Function: main
    Body:
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 299))

    """ Free style """

    def test_300(self):
        input = r"""
Var: a, b[1], c[1][1], d = 1, e = 1e1, f = "Hello", g = True, i = {{1,2}};

Function: main
    Parameter: a, a[1], a[1][1]
    Body:
        Var: a = 1, b = 1., c = "", d = True;
        Var: sum = 0;
        While a < 10 Do
            Var: b = 1, prod = 1;
            While b < 10 Do
                prod = prod * b;
                b = b + 1;
            EndWhile.
            sum = sum + prod;
            a = a + 1;
        EndWhile.
    EndBody.
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 300))
