# Generated from /home/sang/Desktop/PPL/ass-ppl/ass1/initial/src/main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2E")
        buf.write("\u0208\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\3\2")
        buf.write("\3\2\7\2\u009a\n\2\f\2\16\2\u009d\13\2\3\2\5\2\u00a0\n")
        buf.write("\2\3\3\3\3\3\3\3\3\7\3\u00a6\n\3\f\3\16\3\u00a9\13\3\3")
        buf.write("\4\3\4\3\4\3\4\7\4\u00af\n\4\f\4\16\4\u00b2\13\4\3\5\6")
        buf.write("\5\u00b5\n\5\r\5\16\5\u00b6\3\5\3\5\7\5\u00bb\n\5\f\5")
        buf.write("\16\5\u00be\13\5\3\5\5\5\u00c1\n\5\3\5\6\5\u00c4\n\5\r")
        buf.write("\5\16\5\u00c5\3\5\3\5\5\5\u00ca\n\5\3\6\3\6\7\6\u00ce")
        buf.write("\n\6\f\6\16\6\u00d1\13\6\3\6\3\6\3\6\3\7\3\7\5\7\u00d8")
        buf.write("\n\7\3\7\6\7\u00db\n\7\r\7\16\7\u00dc\3\b\3\b\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\5\f\u00ec\n\f")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\21")
        buf.write("\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3 \3 \3 \3 \3!\3!\3!\3!\3\"\3\"\3")
        buf.write("\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)")
        buf.write("\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\6/\u0145\n/\r/\16")
        buf.write("/\u0146\3/\3/\3\60\3\60\3\60\3\60\7\60\u014f\n\60\f\60")
        buf.write("\16\60\u0152\13\60\3\60\3\60\3\60\3\60\3\60\3\61\3\61")
        buf.write("\7\61\u015b\n\61\f\61\16\61\u015e\13\61\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\67")
        buf.write("\3\67\3\67\3\67\3\67\3\67\38\38\38\38\38\38\39\39\39\3")
        buf.write("9\39\39\39\3:\3:\3:\3:\3:\3:\3:\3:\3:\3;\3;\3;\3;\3;\3")
        buf.write(";\3;\3;\3;\3;\3<\3<\3<\3<\3<\3<\3=\3=\3=\3=\3=\3=\3=\3")
        buf.write("=\3=\3>\3>\3>\3>\3>\3>\3>\3>\3?\3?\3?\3?\3@\3@\3@\3@\3")
        buf.write("@\3@\3@\3A\3A\3A\3B\3B\3B\3B\3B\3B\3C\3C\3C\3C\3C\3C\3")
        buf.write("C\3C\3C\3D\3D\3D\3D\3D\3E\3E\3E\3E\3E\3F\3F\3F\3F\3F\3")
        buf.write("F\3G\3G\3G\3G\5G\u01e6\nG\3H\3H\3H\3I\3I\7I\u01ed\nI\f")
        buf.write("I\16I\u01f0\13I\3I\5I\u01f3\nI\3I\3I\3J\3J\7J\u01f9\n")
        buf.write("J\fJ\16J\u01fc\13J\3J\3J\3J\3K\3K\3K\3K\5K\u0205\nK\3")
        buf.write("K\3K\3\u0150\2L\3\3\5\4\7\5\t\6\13\7\r\2\17\2\21\2\23")
        buf.write("\2\25\2\27\2\31\b\33\t\35\n\37\13!\f#\r%\16\'\17)\20+")
        buf.write("\21-\22/\23\61\24\63\25\65\26\67\279\30;\31=\32?\33A\34")
        buf.write("C\35E\36G\37I K!M\"O#Q$S%U&W\'Y([)]*_+a,c-e.g/i\60k\61")
        buf.write("m\62o\63q\64s\65u\66w\67y8{9}:\177;\u0081<\u0083=\u0085")
        buf.write(">\u0087?\u0089@\u008bA\u008d\2\u008fB\u0091C\u0093D\u0095")
        buf.write("E\3\2\23\3\2\63;\3\2\62;\4\2ZZzz\4\2\63;CH\4\2\62;CH\4")
        buf.write("\2QQqq\3\2\639\3\2\629\4\2GGgg\4\2--//\t\2))^^ddhhppt")
        buf.write("tvv\7\2\n\f\16\17$$))^^\5\2\13\f\16\17\"\"\3\2c|\6\2\62")
        buf.write(";C\\aac|\3\2$$\7\3\n\f\16\17$$))^^\2\u0216\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3")
        buf.write("\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2")
        buf.write("\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3")
        buf.write("\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G")
        buf.write("\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2")
        buf.write("Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2")
        buf.write("\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2")
        buf.write("\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2")
        buf.write("\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3")
        buf.write("\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2")
        buf.write("\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008f\3\2\2")
        buf.write("\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\3\u009f")
        buf.write("\3\2\2\2\5\u00a1\3\2\2\2\7\u00aa\3\2\2\2\t\u00c9\3\2\2")
        buf.write("\2\13\u00cb\3\2\2\2\r\u00d5\3\2\2\2\17\u00de\3\2\2\2\21")
        buf.write("\u00e0\3\2\2\2\23\u00e2\3\2\2\2\25\u00e5\3\2\2\2\27\u00eb")
        buf.write("\3\2\2\2\31\u00ed\3\2\2\2\33\u00ef\3\2\2\2\35\u00f2\3")
        buf.write("\2\2\2\37\u00f5\3\2\2\2!\u00f7\3\2\2\2#\u00f9\3\2\2\2")
        buf.write("%\u00fb\3\2\2\2\'\u00fd\3\2\2\2)\u00ff\3\2\2\2+\u0101")
        buf.write("\3\2\2\2-\u0104\3\2\2\2/\u0107\3\2\2\2\61\u010a\3\2\2")
        buf.write("\2\63\u010d\3\2\2\2\65\u010f\3\2\2\2\67\u0111\3\2\2\2")
        buf.write("9\u0114\3\2\2\2;\u0117\3\2\2\2=\u011a\3\2\2\2?\u011d\3")
        buf.write("\2\2\2A\u0121\3\2\2\2C\u0125\3\2\2\2E\u0129\3\2\2\2G\u012c")
        buf.write("\3\2\2\2I\u012f\3\2\2\2K\u0131\3\2\2\2M\u0133\3\2\2\2")
        buf.write("O\u0135\3\2\2\2Q\u0137\3\2\2\2S\u0139\3\2\2\2U\u013b\3")
        buf.write("\2\2\2W\u013d\3\2\2\2Y\u013f\3\2\2\2[\u0141\3\2\2\2]\u0144")
        buf.write("\3\2\2\2_\u014a\3\2\2\2a\u0158\3\2\2\2c\u015f\3\2\2\2")
        buf.write("e\u0164\3\2\2\2g\u0169\3\2\2\2i\u0170\3\2\2\2k\u0173\3")
        buf.write("\2\2\2m\u0177\3\2\2\2o\u017d\3\2\2\2q\u0183\3\2\2\2s\u018a")
        buf.write("\3\2\2\2u\u0193\3\2\2\2w\u019d\3\2\2\2y\u01a3\3\2\2\2")
        buf.write("{\u01ac\3\2\2\2}\u01b4\3\2\2\2\177\u01b8\3\2\2\2\u0081")
        buf.write("\u01bf\3\2\2\2\u0083\u01c2\3\2\2\2\u0085\u01c8\3\2\2\2")
        buf.write("\u0087\u01d1\3\2\2\2\u0089\u01d6\3\2\2\2\u008b\u01db\3")
        buf.write("\2\2\2\u008d\u01e5\3\2\2\2\u008f\u01e7\3\2\2\2\u0091\u01ea")
        buf.write("\3\2\2\2\u0093\u01f6\3\2\2\2\u0095\u0200\3\2\2\2\u0097")
        buf.write("\u009b\t\2\2\2\u0098\u009a\t\3\2\2\u0099\u0098\3\2\2\2")
        buf.write("\u009a\u009d\3\2\2\2\u009b\u0099\3\2\2\2\u009b\u009c\3")
        buf.write("\2\2\2\u009c\u00a0\3\2\2\2\u009d\u009b\3\2\2\2\u009e\u00a0")
        buf.write("\7\62\2\2\u009f\u0097\3\2\2\2\u009f\u009e\3\2\2\2\u00a0")
        buf.write("\4\3\2\2\2\u00a1\u00a2\7\62\2\2\u00a2\u00a3\t\4\2\2\u00a3")
        buf.write("\u00a7\t\5\2\2\u00a4\u00a6\t\6\2\2\u00a5\u00a4\3\2\2\2")
        buf.write("\u00a6\u00a9\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a7\u00a8\3")
        buf.write("\2\2\2\u00a8\6\3\2\2\2\u00a9\u00a7\3\2\2\2\u00aa\u00ab")
        buf.write("\7\62\2\2\u00ab\u00ac\t\7\2\2\u00ac\u00b0\t\b\2\2\u00ad")
        buf.write("\u00af\t\t\2\2\u00ae\u00ad\3\2\2\2\u00af\u00b2\3\2\2\2")
        buf.write("\u00b0\u00ae\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\b\3\2\2")
        buf.write("\2\u00b2\u00b0\3\2\2\2\u00b3\u00b5\5\17\b\2\u00b4\u00b3")
        buf.write("\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b6")
        buf.write("\u00b7\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00bc\5[.\2\u00b9")
        buf.write("\u00bb\5\17\b\2\u00ba\u00b9\3\2\2\2\u00bb\u00be\3\2\2")
        buf.write("\2\u00bc\u00ba\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\u00c0")
        buf.write("\3\2\2\2\u00be\u00bc\3\2\2\2\u00bf\u00c1\5\r\7\2\u00c0")
        buf.write("\u00bf\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00ca\3\2\2\2")
        buf.write("\u00c2\u00c4\5\17\b\2\u00c3\u00c2\3\2\2\2\u00c4\u00c5")
        buf.write("\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6")
        buf.write("\u00c7\3\2\2\2\u00c7\u00c8\5\r\7\2\u00c8\u00ca\3\2\2\2")
        buf.write("\u00c9\u00b4\3\2\2\2\u00c9\u00c3\3\2\2\2\u00ca\n\3\2\2")
        buf.write("\2\u00cb\u00cf\7$\2\2\u00cc\u00ce\5\27\f\2\u00cd\u00cc")
        buf.write("\3\2\2\2\u00ce\u00d1\3\2\2\2\u00cf\u00cd\3\2\2\2\u00cf")
        buf.write("\u00d0\3\2\2\2\u00d0\u00d2\3\2\2\2\u00d1\u00cf\3\2\2\2")
        buf.write("\u00d2\u00d3\7$\2\2\u00d3\u00d4\b\6\2\2\u00d4\f\3\2\2")
        buf.write("\2\u00d5\u00d7\t\n\2\2\u00d6\u00d8\5\21\t\2\u00d7\u00d6")
        buf.write("\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8\u00da\3\2\2\2\u00d9")
        buf.write("\u00db\5\17\b\2\u00da\u00d9\3\2\2\2\u00db\u00dc\3\2\2")
        buf.write("\2\u00dc\u00da\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\16\3")
        buf.write("\2\2\2\u00de\u00df\t\3\2\2\u00df\20\3\2\2\2\u00e0\u00e1")
        buf.write("\t\13\2\2\u00e1\22\3\2\2\2\u00e2\u00e3\7)\2\2\u00e3\u00e4")
        buf.write("\7$\2\2\u00e4\24\3\2\2\2\u00e5\u00e6\7^\2\2\u00e6\u00e7")
        buf.write("\t\f\2\2\u00e7\26\3\2\2\2\u00e8\u00ec\n\r\2\2\u00e9\u00ec")
        buf.write("\5\23\n\2\u00ea\u00ec\5\25\13\2\u00eb\u00e8\3\2\2\2\u00eb")
        buf.write("\u00e9\3\2\2\2\u00eb\u00ea\3\2\2\2\u00ec\30\3\2\2\2\u00ed")
        buf.write("\u00ee\7?\2\2\u00ee\32\3\2\2\2\u00ef\u00f0\7(\2\2\u00f0")
        buf.write("\u00f1\7(\2\2\u00f1\34\3\2\2\2\u00f2\u00f3\7~\2\2\u00f3")
        buf.write("\u00f4\7~\2\2\u00f4\36\3\2\2\2\u00f5\u00f6\7#\2\2\u00f6")
        buf.write(" \3\2\2\2\u00f7\u00f8\7-\2\2\u00f8\"\3\2\2\2\u00f9\u00fa")
        buf.write("\7/\2\2\u00fa$\3\2\2\2\u00fb\u00fc\7,\2\2\u00fc&\3\2\2")
        buf.write("\2\u00fd\u00fe\7\'\2\2\u00fe(\3\2\2\2\u00ff\u0100\7^\2")
        buf.write("\2\u0100*\3\2\2\2\u0101\u0102\7>\2\2\u0102\u0103\7?\2")
        buf.write("\2\u0103,\3\2\2\2\u0104\u0105\7@\2\2\u0105\u0106\7?\2")
        buf.write("\2\u0106.\3\2\2\2\u0107\u0108\7#\2\2\u0108\u0109\7?\2")
        buf.write("\2\u0109\60\3\2\2\2\u010a\u010b\7?\2\2\u010b\u010c\7?")
        buf.write("\2\2\u010c\62\3\2\2\2\u010d\u010e\7>\2\2\u010e\64\3\2")
        buf.write("\2\2\u010f\u0110\7@\2\2\u0110\66\3\2\2\2\u0111\u0112\7")
        buf.write("-\2\2\u0112\u0113\7\60\2\2\u01138\3\2\2\2\u0114\u0115")
        buf.write("\7/\2\2\u0115\u0116\7\60\2\2\u0116:\3\2\2\2\u0117\u0118")
        buf.write("\7,\2\2\u0118\u0119\7\60\2\2\u0119<\3\2\2\2\u011a\u011b")
        buf.write("\7^\2\2\u011b\u011c\7\60\2\2\u011c>\3\2\2\2\u011d\u011e")
        buf.write("\7>\2\2\u011e\u011f\7?\2\2\u011f\u0120\7\60\2\2\u0120")
        buf.write("@\3\2\2\2\u0121\u0122\7@\2\2\u0122\u0123\7?\2\2\u0123")
        buf.write("\u0124\7\60\2\2\u0124B\3\2\2\2\u0125\u0126\7?\2\2\u0126")
        buf.write("\u0127\7\61\2\2\u0127\u0128\7?\2\2\u0128D\3\2\2\2\u0129")
        buf.write("\u012a\7>\2\2\u012a\u012b\7\60\2\2\u012bF\3\2\2\2\u012c")
        buf.write("\u012d\7@\2\2\u012d\u012e\7\60\2\2\u012eH\3\2\2\2\u012f")
        buf.write("\u0130\7*\2\2\u0130J\3\2\2\2\u0131\u0132\7+\2\2\u0132")
        buf.write("L\3\2\2\2\u0133\u0134\7}\2\2\u0134N\3\2\2\2\u0135\u0136")
        buf.write("\7\177\2\2\u0136P\3\2\2\2\u0137\u0138\7]\2\2\u0138R\3")
        buf.write("\2\2\2\u0139\u013a\7_\2\2\u013aT\3\2\2\2\u013b\u013c\7")
        buf.write("=\2\2\u013cV\3\2\2\2\u013d\u013e\7.\2\2\u013eX\3\2\2\2")
        buf.write("\u013f\u0140\7<\2\2\u0140Z\3\2\2\2\u0141\u0142\7\60\2")
        buf.write("\2\u0142\\\3\2\2\2\u0143\u0145\t\16\2\2\u0144\u0143\3")
        buf.write("\2\2\2\u0145\u0146\3\2\2\2\u0146\u0144\3\2\2\2\u0146\u0147")
        buf.write("\3\2\2\2\u0147\u0148\3\2\2\2\u0148\u0149\b/\3\2\u0149")
        buf.write("^\3\2\2\2\u014a\u014b\7,\2\2\u014b\u014c\7,\2\2\u014c")
        buf.write("\u0150\3\2\2\2\u014d\u014f\13\2\2\2\u014e\u014d\3\2\2")
        buf.write("\2\u014f\u0152\3\2\2\2\u0150\u0151\3\2\2\2\u0150\u014e")
        buf.write("\3\2\2\2\u0151\u0153\3\2\2\2\u0152\u0150\3\2\2\2\u0153")
        buf.write("\u0154\7,\2\2\u0154\u0155\7,\2\2\u0155\u0156\3\2\2\2\u0156")
        buf.write("\u0157\b\60\3\2\u0157`\3\2\2\2\u0158\u015c\t\17\2\2\u0159")
        buf.write("\u015b\t\20\2\2\u015a\u0159\3\2\2\2\u015b\u015e\3\2\2")
        buf.write("\2\u015c\u015a\3\2\2\2\u015c\u015d\3\2\2\2\u015db\3\2")
        buf.write("\2\2\u015e\u015c\3\2\2\2\u015f\u0160\7D\2\2\u0160\u0161")
        buf.write("\7q\2\2\u0161\u0162\7f\2\2\u0162\u0163\7{\2\2\u0163d\3")
        buf.write("\2\2\2\u0164\u0165\7G\2\2\u0165\u0166\7n\2\2\u0166\u0167")
        buf.write("\7u\2\2\u0167\u0168\7g\2\2\u0168f\3\2\2\2\u0169\u016a")
        buf.write("\7G\2\2\u016a\u016b\7p\2\2\u016b\u016c\7f\2\2\u016c\u016d")
        buf.write("\7H\2\2\u016d\u016e\7q\2\2\u016e\u016f\7t\2\2\u016fh\3")
        buf.write("\2\2\2\u0170\u0171\7K\2\2\u0171\u0172\7h\2\2\u0172j\3")
        buf.write("\2\2\2\u0173\u0174\7X\2\2\u0174\u0175\7c\2\2\u0175\u0176")
        buf.write("\7t\2\2\u0176l\3\2\2\2\u0177\u0178\7G\2\2\u0178\u0179")
        buf.write("\7p\2\2\u0179\u017a\7f\2\2\u017a\u017b\7F\2\2\u017b\u017c")
        buf.write("\7q\2\2\u017cn\3\2\2\2\u017d\u017e\7D\2\2\u017e\u017f")
        buf.write("\7t\2\2\u017f\u0180\7g\2\2\u0180\u0181\7c\2\2\u0181\u0182")
        buf.write("\7m\2\2\u0182p\3\2\2\2\u0183\u0184\7G\2\2\u0184\u0185")
        buf.write("\7n\2\2\u0185\u0186\7u\2\2\u0186\u0187\7g\2\2\u0187\u0188")
        buf.write("\7K\2\2\u0188\u0189\7h\2\2\u0189r\3\2\2\2\u018a\u018b")
        buf.write("\7G\2\2\u018b\u018c\7p\2\2\u018c\u018d\7f\2\2\u018d\u018e")
        buf.write("\7Y\2\2\u018e\u018f\7j\2\2\u018f\u0190\7k\2\2\u0190\u0191")
        buf.write("\7n\2\2\u0191\u0192\7g\2\2\u0192t\3\2\2\2\u0193\u0194")
        buf.write("\7R\2\2\u0194\u0195\7c\2\2\u0195\u0196\7t\2\2\u0196\u0197")
        buf.write("\7c\2\2\u0197\u0198\7o\2\2\u0198\u0199\7g\2\2\u0199\u019a")
        buf.write("\7v\2\2\u019a\u019b\7g\2\2\u019b\u019c\7t\2\2\u019cv\3")
        buf.write("\2\2\2\u019d\u019e\7Y\2\2\u019e\u019f\7j\2\2\u019f\u01a0")
        buf.write("\7k\2\2\u01a0\u01a1\7n\2\2\u01a1\u01a2\7g\2\2\u01a2x\3")
        buf.write("\2\2\2\u01a3\u01a4\7E\2\2\u01a4\u01a5\7q\2\2\u01a5\u01a6")
        buf.write("\7p\2\2\u01a6\u01a7\7v\2\2\u01a7\u01a8\7k\2\2\u01a8\u01a9")
        buf.write("\7p\2\2\u01a9\u01aa\7w\2\2\u01aa\u01ab\7g\2\2\u01abz\3")
        buf.write("\2\2\2\u01ac\u01ad\7G\2\2\u01ad\u01ae\7p\2\2\u01ae\u01af")
        buf.write("\7f\2\2\u01af\u01b0\7D\2\2\u01b0\u01b1\7q\2\2\u01b1\u01b2")
        buf.write("\7f\2\2\u01b2\u01b3\7{\2\2\u01b3|\3\2\2\2\u01b4\u01b5")
        buf.write("\7H\2\2\u01b5\u01b6\7q\2\2\u01b6\u01b7\7t\2\2\u01b7~\3")
        buf.write("\2\2\2\u01b8\u01b9\7T\2\2\u01b9\u01ba\7g\2\2\u01ba\u01bb")
        buf.write("\7v\2\2\u01bb\u01bc\7w\2\2\u01bc\u01bd\7t\2\2\u01bd\u01be")
        buf.write("\7p\2\2\u01be\u0080\3\2\2\2\u01bf\u01c0\7F\2\2\u01c0\u01c1")
        buf.write("\7q\2\2\u01c1\u0082\3\2\2\2\u01c2\u01c3\7G\2\2\u01c3\u01c4")
        buf.write("\7p\2\2\u01c4\u01c5\7f\2\2\u01c5\u01c6\7K\2\2\u01c6\u01c7")
        buf.write("\7h\2\2\u01c7\u0084\3\2\2\2\u01c8\u01c9\7H\2\2\u01c9\u01ca")
        buf.write("\7w\2\2\u01ca\u01cb\7p\2\2\u01cb\u01cc\7e\2\2\u01cc\u01cd")
        buf.write("\7v\2\2\u01cd\u01ce\7k\2\2\u01ce\u01cf\7q\2\2\u01cf\u01d0")
        buf.write("\7p\2\2\u01d0\u0086\3\2\2\2\u01d1\u01d2\7V\2\2\u01d2\u01d3")
        buf.write("\7j\2\2\u01d3\u01d4\7g\2\2\u01d4\u01d5\7p\2\2\u01d5\u0088")
        buf.write("\3\2\2\2\u01d6\u01d7\7V\2\2\u01d7\u01d8\7t\2\2\u01d8\u01d9")
        buf.write("\7w\2\2\u01d9\u01da\7g\2\2\u01da\u008a\3\2\2\2\u01db\u01dc")
        buf.write("\7H\2\2\u01dc\u01dd\7c\2\2\u01dd\u01de\7n\2\2\u01de\u01df")
        buf.write("\7u\2\2\u01df\u01e0\7g\2\2\u01e0\u008c\3\2\2\2\u01e1\u01e2")
        buf.write("\7^\2\2\u01e2\u01e6\n\f\2\2\u01e3\u01e4\7)\2\2\u01e4\u01e6")
        buf.write("\n\21\2\2\u01e5\u01e1\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e6")
        buf.write("\u008e\3\2\2\2\u01e7\u01e8\13\2\2\2\u01e8\u01e9\bH\4\2")
        buf.write("\u01e9\u0090\3\2\2\2\u01ea\u01ee\7$\2\2\u01eb\u01ed\5")
        buf.write("\27\f\2\u01ec\u01eb\3\2\2\2\u01ed\u01f0\3\2\2\2\u01ee")
        buf.write("\u01ec\3\2\2\2\u01ee\u01ef\3\2\2\2\u01ef\u01f2\3\2\2\2")
        buf.write("\u01f0\u01ee\3\2\2\2\u01f1\u01f3\t\22\2\2\u01f2\u01f1")
        buf.write("\3\2\2\2\u01f2\u01f3\3\2\2\2\u01f3\u01f4\3\2\2\2\u01f4")
        buf.write("\u01f5\bI\5\2\u01f5\u0092\3\2\2\2\u01f6\u01fa\7$\2\2\u01f7")
        buf.write("\u01f9\5\27\f\2\u01f8\u01f7\3\2\2\2\u01f9\u01fc\3\2\2")
        buf.write("\2\u01fa\u01f8\3\2\2\2\u01fa\u01fb\3\2\2\2\u01fb\u01fd")
        buf.write("\3\2\2\2\u01fc\u01fa\3\2\2\2\u01fd\u01fe\5\u008dG\2\u01fe")
        buf.write("\u01ff\bJ\6\2\u01ff\u0094\3\2\2\2\u0200\u0201\7,\2\2\u0201")
        buf.write("\u0202\7,\2\2\u0202\u0204\3\2\2\2\u0203\u0205\13\2\2\2")
        buf.write("\u0204\u0203\3\2\2\2\u0204\u0205\3\2\2\2\u0205\u0206\3")
        buf.write("\2\2\2\u0206\u0207\bK\7\2\u0207\u0096\3\2\2\2\30\2\u009b")
        buf.write("\u009f\u00a7\u00b0\u00b6\u00bc\u00c0\u00c5\u00c9\u00cf")
        buf.write("\u00d7\u00dc\u00eb\u0146\u0150\u015c\u01e5\u01ee\u01f2")
        buf.write("\u01fa\u0204\b\3\6\2\b\2\2\3H\3\3I\4\3J\5\3K\6")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTLIT = 1
    HEXA = 2
    OCTA = 3
    FLOAT_LITERAL = 4
    STRING_LITERAL = 5
    ASSIGN = 6
    AND = 7
    OR = 8
    NOT = 9
    ADD = 10
    SUB = 11
    MUL = 12
    MODULE = 13
    DIV = 14
    LTE = 15
    GTE = 16
    NEQ = 17
    EQ = 18
    LT = 19
    GT = 20
    ADDF = 21
    SUBF = 22
    MULF = 23
    DIVF = 24
    LTEF = 25
    GTEF = 26
    EQF = 27
    LTF = 28
    GTF = 29
    LP = 30
    RP = 31
    LCB = 32
    RCB = 33
    LSB = 34
    RSB = 35
    SEMI = 36
    COMMA = 37
    COLON = 38
    DOT = 39
    WS = 40
    BLOCK_COMMENT = 41
    ID = 42
    BODY = 43
    ELSE = 44
    ENDFOR = 45
    IF = 46
    VAR = 47
    ENDDO = 48
    BREAK = 49
    ELSEIF = 50
    ENDWHILE = 51
    PARAMETER = 52
    WHILE = 53
    CONTINUE = 54
    ENDBODY = 55
    FOR = 56
    RETURN = 57
    DO = 58
    ENDIF = 59
    FUNCTION = 60
    THEN = 61
    TRUE = 62
    FALSE = 63
    ERROR_TOKEN = 64
    UNCLOSE_STRING = 65
    ILLEGAL_ESCAPE = 66
    UNTERMINATED_COMMENT = 67

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'&&'", "'||'", "'!'", "'+'", "'-'", "'*'", "'%'", "'\\'", 
            "'<='", "'>='", "'!='", "'=='", "'<'", "'>'", "'+.'", "'-.'", 
            "'*.'", "'\\.'", "'<=.'", "'>=.'", "'=/='", "'<.'", "'>.'", 
            "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "','", "':'", 
            "'.'", "'Body'", "'Else'", "'EndFor'", "'If'", "'Var'", "'EndDo'", 
            "'Break'", "'ElseIf'", "'EndWhile'", "'Parameter'", "'While'", 
            "'Continue'", "'EndBody'", "'For'", "'Return'", "'Do'", "'EndIf'", 
            "'Function'", "'Then'", "'True'", "'False'" ]

    symbolicNames = [ "<INVALID>",
            "INTLIT", "HEXA", "OCTA", "FLOAT_LITERAL", "STRING_LITERAL", 
            "ASSIGN", "AND", "OR", "NOT", "ADD", "SUB", "MUL", "MODULE", 
            "DIV", "LTE", "GTE", "NEQ", "EQ", "LT", "GT", "ADDF", "SUBF", 
            "MULF", "DIVF", "LTEF", "GTEF", "EQF", "LTF", "GTF", "LP", "RP", 
            "LCB", "RCB", "LSB", "RSB", "SEMI", "COMMA", "COLON", "DOT", 
            "WS", "BLOCK_COMMENT", "ID", "BODY", "ELSE", "ENDFOR", "IF", 
            "VAR", "ENDDO", "BREAK", "ELSEIF", "ENDWHILE", "PARAMETER", 
            "WHILE", "CONTINUE", "ENDBODY", "FOR", "RETURN", "DO", "ENDIF", 
            "FUNCTION", "THEN", "TRUE", "FALSE", "ERROR_TOKEN", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "INTLIT", "HEXA", "OCTA", "FLOAT_LITERAL", "STRING_LITERAL", 
                  "EXPONENT", "DIGIT", "SIGN", "QUOTE", "ESC_SEQ", "STR_CHAR", 
                  "ASSIGN", "AND", "OR", "NOT", "ADD", "SUB", "MUL", "MODULE", 
                  "DIV", "LTE", "GTE", "NEQ", "EQ", "LT", "GT", "ADDF", 
                  "SUBF", "MULF", "DIVF", "LTEF", "GTEF", "EQF", "LTF", 
                  "GTF", "LP", "RP", "LCB", "RCB", "LSB", "RSB", "SEMI", 
                  "COMMA", "COLON", "DOT", "WS", "BLOCK_COMMENT", "ID", 
                  "BODY", "ELSE", "ENDFOR", "IF", "VAR", "ENDDO", "BREAK", 
                  "ELSEIF", "ENDWHILE", "PARAMETER", "WHILE", "CONTINUE", 
                  "ENDBODY", "FOR", "RETURN", "DO", "ENDIF", "FUNCTION", 
                  "THEN", "TRUE", "FALSE", "ESC_ILLEGAL", "ERROR_TOKEN", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


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


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[4] = self.STRING_LITERAL_action 
            actions[70] = self.ERROR_TOKEN_action 
            actions[71] = self.UNCLOSE_STRING_action 
            actions[72] = self.ILLEGAL_ESCAPE_action 
            actions[73] = self.UNTERMINATED_COMMENT_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            		self.text = self.text[1:-1]
            	
     

    def ERROR_TOKEN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            		raise ErrorToken(self.text)
            	
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            		y = str(self.text)
            		possible = ['\b', '\t', '\n', '\f', '\r', "'", '\\']
            		if y[-1] in possible:
            			raise UncloseString(y[1:-1])
            		else:
            			raise UncloseString(y[1:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            		y = str(self.text)
            		raise IllegalEscape(y[1:])
            	
     

    def UNTERMINATED_COMMENT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            		y = str(self.text)
            		raise UnterminatedComment()
            	
     


