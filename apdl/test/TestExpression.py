import unittest
from workhelper.apdl.Expression import Expression

class TestStatement(unittest.TestCase):

    def test_statement(self):
        stmt = Expression("statement")
        assert str(stmt) == "statement"

    def test_add(self):
        stmt = Expression("a")
        assert str(stmt+1) == "a+1"
        assert str(stmt+1.0) == "a+1.0"
        assert str(stmt+"b") == "a+b"
        assert str(stmt+Expression("c")+"b") == "a+c+b"

    def test_radd(self):
        stmt = Expression("a")
        assert str(1+stmt) == "1+a"
        assert str(1.0+stmt) == "1.0+a"
        assert str("b"+stmt) == "b+a"
        assert str("b"+Expression("c")+stmt) == "b+c+a"

    def test_sub(self):
        stmt = Expression("a")
        assert str(stmt-1) == "a-1"
        assert str(stmt-1.0) == "a-1.0"
        assert str(stmt-"b") == "a-b"
        assert str(stmt-Expression("c")-"b") == "a-c-b"

    def test_rsub(self):
        stmt = Expression("a")
        assert str(1-stmt) == "1-a"
        assert str(1.0-stmt) == "1.0-a"
        assert str("b"-stmt) == "b-a"
        assert str("b"-Expression("c")-stmt) == "b-c-a"

    def test_mul(self):
        stmt = Expression("a")
        assert str(stmt*1) == "a*1"
        assert str(stmt*1.0) == "a*1.0"
        assert str(stmt*"b") == "a*b"
        assert str(stmt*Expression("c")*"b") == "(a*c)*b"
    
    def test_rmul(self):
        stmt = Expression("a")
        assert str(1*stmt) == "1*a"
        assert str(1.0*stmt) == "1.0*a"
        assert str("b"*stmt) == "b*a"
        assert str("b"*Expression("c")*stmt) == "(b*c)*a"

    def test_truediv(self):
        stmt = Expression("a")
        assert str(stmt/1) == "a/1"
        assert str(stmt/1.0) == "a/1.0"
        assert str(stmt/"b") == "a/b"
        assert str(stmt/Expression("c")/"b") == "(a/c)/b"

    def test_rtruediv(self):
        stmt = Expression("a")
        assert str(1/stmt) == "1/a"
        assert str(1.0/stmt) == "1.0/a"
        assert str("b"/stmt) == "b/a"
        assert str("b"/Expression("c")/stmt) == "(b/c)/a"

    def test_pow(self):
        stmt = Expression("a")
        assert str(stmt**1) == "a**1"
        assert str(stmt**1.0) == "a**1.0"
        assert str(stmt**"b") == "a**b"
        assert str(stmt**Expression("c")**"b") == "a**(c**b)"

    def test_rpow(self):
        stmt = Expression("a")
        assert str(1**stmt) == "1**a"
        assert str(1.0**stmt) == "1.0**a"
        assert str("b"**stmt) == "b**a"
        assert str("b"**Expression("c")**stmt) == "b**(c**a)"

    def test_neg(self):
        stmt = Expression("a")
        assert str(-stmt) == "-a"
        stmt = Expression("a+b")
        assert str(-stmt) == "-(a+b)"
        stmt = Expression("-a")
        assert str(-stmt) == "-(-a)"

    def test_lt(self):
        stmt = Expression("a")
        assert str(stmt<1) == "a,LT,1"
        assert str(stmt<1.0) == "a,LT,1.0"
        assert str(stmt<"b") == "a,LT,b"

    def test_le(self):
        stmt = Expression("a")
        assert str(stmt<=1) == "a,LE,1"
        assert str(stmt<=1.0) == "a,LE,1.0"
        assert str(stmt<="b") == "a,LE,b"
    
    def test_eq(self):
        stmt = Expression("a")
        assert str(stmt==1) == "a,EQ,1"
        assert str(stmt==1.0) == "a,EQ,1.0"
        assert str(stmt=="b") == "a,EQ,b"
    
    def test_ne(self):
        stmt = Expression("a")
        assert str(stmt!=1) == "a,NE,1"
        assert str(stmt!=1.0) == "a,NE,1.0"
        assert str(stmt!="b") == "a,NE,b"

    def test_gt(self):
        stmt = Expression("a")
        assert str(stmt>1) == "a,GT,1"
        assert str(stmt>1.0) == "a,GT,1.0"
        assert str(stmt>"b") == "a,GT,b"
    
    def test_ge(self):
        stmt = Expression("a")
        assert str(stmt>=1) == "a,GE,1"
        assert str(stmt>=1.0) == "a,GE,1.0"
        assert str(stmt>="b") == "a,GE,b"

    def test_sqrt(self):
        stmt = Expression("a")
        assert str(stmt.sqrt()) == "SQRT(a)"
        stmt = Expression("a+b")
        assert str(stmt.sqrt()) == "SQRT(a+b)"
        stmt = Expression("SQRT(a)")
        assert str(stmt.sqrt()) == "SQRT(SQRT(a))"

    def test_mix(self):
        stmt1 = Expression("a+b")
        stmt2 = Expression("c")
        stmt3 = Expression("e-f")
        stmt4 = 1.5
        assert str(stmt1*stmt2) == "(a+b)*c"
        assert str(stmt1-stmt3) == "a+b-(e-f)"
        assert str(stmt1/stmt2) == "(a+b)/c"
        assert str(stmt1**stmt2) == "(a+b)**c"
        assert str(stmt1+stmt2) == "a+b+c"
        assert str(stmt1-stmt2) == "a+b-c"
        assert str(stmt1*stmt2+stmt3) == "(a+b)*c+e-f"
        assert str(stmt1*stmt2-stmt3) == "(a+b)*c-(e-f)"
        assert str(stmt1*stmt2*stmt3) == "((a+b)*c)*(e-f)"
        assert str(stmt1*stmt2/stmt3) == "((a+b)*c)/(e-f)"
        assert str(stmt1*stmt2**stmt3) == "(a+b)*(c**(e-f))"
        assert str(stmt1/stmt2+stmt3) == "(a+b)/c+e-f"
        assert str(stmt4+stmt1) == "1.5+a+b"
        assert str(stmt4-stmt1) == "1.5-(a+b)"
        assert str(stmt4*stmt1) == "1.5*(a+b)"
        assert str(stmt4/stmt1) == "1.5/(a+b)"
        assert str(stmt4**stmt1) == "1.5**(a+b)"
        assert str(stmt4+stmt1+stmt2) == "1.5+a+b+c"
        assert str(stmt4-stmt1-stmt2) == "1.5-(a+b)-c"
        assert str(stmt4*stmt1*stmt2) == "(1.5*(a+b))*c"
        assert str(stmt4/stmt1/stmt2) == "(1.5/(a+b))/c"
        assert str(stmt4**stmt1**stmt2) == "1.5**((a+b)**c)"
        assert str(stmt4+stmt1+stmt2+stmt3) == "1.5+a+b+c+e-f"
        assert str(stmt4-stmt1-stmt2-stmt3) == "1.5-(a+b)-c-(e-f)"
        assert str(stmt4*stmt1*stmt2*stmt3) == "((1.5*(a+b))*c)*(e-f)"
        assert str(stmt4/stmt1/stmt2/stmt3) == "((1.5/(a+b))/c)/(e-f)"
        assert str(stmt4**stmt1**stmt2**stmt3) == "1.5**((a+b)**(c**(e-f)))"
        assert str(stmt1+stmt2+stmt3+stmt4) == "a+b+c+e-f+1.5"

if __name__ == "__main__":
    unittest.main()