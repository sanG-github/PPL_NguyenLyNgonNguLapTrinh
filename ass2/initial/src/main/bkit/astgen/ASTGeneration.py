from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from functools import reduce
from AST import *

class ASTGeneration(BKITVisitor):
    def visitProgram(self, ctx: BKITParser.ProgramContext):
        varDecl = reduce(lambda acc, ele: acc + self.visitVarDecl(ele), ctx.varDecl(), [])
        FuncDecl = reduce(lambda acc, ele: acc + [self.visitFuncDecl(ele)], ctx.funcDecl(), [])
        return Program(varDecl + FuncDecl)

    def visitVarDecl(self, ctx: BKITParser.VarDeclContext):
        return [self.visitVarDeclaration(x) for x in ctx.varDeclaration()]

    def visitVarDeclaration(self, ctx: BKITParser.VarDeclarationContext):
        dimen = [self.visitIndexInt(x) for x in ctx.indexInt()] if ctx.indexInt() else []
        return VarDecl(Id(ctx.ID().getText()), dimen, self.visit(ctx.literals()) if ctx.literals() else None)

    def visitIndexInt(self, ctx: BKITParser.IndexIntContext):
        return self.visit(ctx.intLiteral())
        
    def visitFuncDecl(self, ctx: BKITParser.FuncDeclContext):
        varDeclList = list(map(lambda x: self.visitVarDeclaration(x), ctx.varDeclaration())) if ctx.varDeclaration() else []
        return FuncDecl(Id(ctx.ID().getText()), varDeclList, self.visit(ctx.stmtInFunc()))

    def visitCallExpr(self, ctx: BKITParser.CallExprContext):
        return CallExpr(Id(ctx.ID().getText()), self.visit(ctx.listExp()) if ctx.listExp() else [])

    def visitStmt(self, ctx: BKITParser.StmtContext):
        return self.visit(ctx.getChild(0))

    def visitAssignStmt(self, ctx: BKITParser.AssignStmtContext):
        return (
            Assign(ArrayCell(Id(ctx.ID().getText()), [self.visitIndexes(x) for x in ctx.indexes()]), self.visit(ctx.exp(0))) if ctx.ID() else
            Assign(ArrayCell(self.visit(ctx.exp(0)), [self.visitIndexes(x) for x in ctx.indexes()]), self.visit(ctx.exp(1)))
        )

    def visitIfStmt(self, ctx: BKITParser.IfStmtContext):
        ifComponent = reduce(lambda acc, ele: acc + [self.visitIfComponent(ele)], ctx.ifComponent(), [])
        elseComponent = self.visit(ctx.stmtInFunc()) if ctx.stmtInFunc() else ([],[])
        return If(ifComponent, elseComponent)

    def visitIfComponent(self, ctx: BKITParser.IfComponentContext):
        exp = self.visit(ctx.exp())
        (_var, _stmt) = self.visit(ctx.stmtInFunc())
        return (exp, _var, _stmt)

    def visitContinueStmt(self, ctx: BKITParser.ContinueStmtContext):
        return Continue()

    def visitBreakStmt(self, ctx: BKITParser.BreakStmtContext):
        return Break()

    def visitReturnStmt(self, ctx: BKITParser.ReturnStmtContext):
        return Return(self.visit(ctx.exp())) if ctx.exp() else Return(None)

    def visitForStmt(self, ctx: BKITParser.ForStmtContext):
        return For(Id(ctx.ID().getText()), self.visit(ctx.exp(0)), self.visit(ctx.exp(1)), self.visit(ctx.exp(2)), self.visit(ctx.stmtInFunc()))

    def visitDowhileStmt(self, ctx: BKITParser.DowhileStmtContext):
        return Dowhile(self.visit(ctx.stmtInFunc()), self.visit(ctx.exp()))

    def visitWhileStmt(self, ctx: BKITParser.WhileStmtContext):
        return While(self.visit(ctx.exp()), self.visit(ctx.stmtInFunc()))

    def visitStmtInFunc(self, ctx: BKITParser.StmtInFuncContext):
        varDeclList = reduce(lambda acc, ele: acc + self.visitVarDecl(ele), ctx.varDecl(), []) if ctx.varDecl() else []
        return (varDeclList, [self.visitStmt(x) for x in ctx.stmt()])

    def visitCallStmt(self, ctx: BKITParser.CallStmtContext):
        return (
            CallStmt(Id(ctx.ID().getText()), self.visit(ctx.listExp())) if ctx.listExp() else
            CallStmt(Id(ctx.ID().getText()), [])
        )

    def visitLiterals(self, ctx: BKITParser.LiteralsContext):
        return(
            IntLiteral(self.visit(ctx.intLiteral())) if ctx.intLiteral() else
            FloatLiteral(float(ctx.FLOAT_LITERAL().getText())) if ctx.FLOAT_LITERAL() else
            StringLiteral(ctx.STRING_LITERAL().getText()) if ctx.STRING_LITERAL() else
            self.visit(ctx.booleanLiteral()) if ctx.booleanLiteral() else
            self.visit(ctx.arrayLiteral())
        )

    def visitIntLiteral(self, ctx: BKITParser.IntLiteralContext):
        return (
            int(ctx.INTLIT().getText()) if ctx.INTLIT() else
            int(ctx.HEXA().getText(), 16) if ctx.HEXA() else
            int(ctx.OCTA().getText(), 8)
        )

    def visitBooleanLiteral(self, ctx: BKITParser.BooleanLiteralContext):
        return BooleanLiteral(True if ctx.TRUE() else False)

    def visitArrayLiteral(self, ctx: BKITParser.ArrayLiteralContext):
        return ArrayLiteral([self.visitLiterals(x) for x in ctx.literals()])

    def visitExp(self, ctx: BKITParser.ExpContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp1(0)) 
        else:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.exp1(0)), self.visit(ctx.exp1(1)))
    
    def visitExp1(self, ctx: BKITParser.Exp1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp2()) 
        else:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.exp1()), self.visit(ctx.exp2()))

    def visitExp2(self, ctx: BKITParser.Exp2Context):
        return (
            self.visit(ctx.exp3()) if ctx.getChildCount() == 1 else 
            BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.exp2()), self.visit(ctx.exp3()))
        )
    
    def visitExp3(self, ctx: BKITParser.Exp3Context):
        return (
            self.visit(ctx.exp4()) if ctx.getChildCount() == 1 else 
            BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.exp3()), self.visit(ctx.exp4()))
        )

    def visitExp4(self, ctx: BKITParser.Exp4Context):
        return (
            self.visit(ctx.exp5()) if ctx.getChildCount() == 1 else 
            UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.exp4()))
        )

    def visitExp5(self, ctx: BKITParser.Exp5Context):
        return (
            self.visit(ctx.exp6()) if ctx.getChildCount() == 1 else 
            UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.exp5()))
        )

    def visitExp6(self, ctx: BKITParser.Exp6Context):
        return (
            self.visit(ctx.exp7()) if ctx.getChildCount() == 1 else 
            ArrayCell(self.visit(ctx.exp6()), [self.visitIndexes(x) for x in ctx.indexes()])
        )

    def visitExp7(self, ctx: BKITParser.Exp7Context):
        return self.visit(ctx.getChild(0))
    
    def visitExp8(self, ctx: BKITParser.Exp8Context):
        return self.visit(ctx.operand()) if ctx.getChildCount() == 1 else self.visit(ctx.exp())

    def visitOperand(self, ctx: BKITParser.OperandContext):
        return Id(ctx.ID().getText()) if ctx.ID() else self.visit(ctx.literals())

    def visitIndexes(self, ctx: BKITParser.IndexesContext):
        return self.visit(ctx.exp())

    def visitListExp(self, ctx: BKITParser.ListExpContext):
        return [self.visitExp(x) for x in ctx.exp()]
