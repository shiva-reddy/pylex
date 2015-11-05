import re
import sys
%%
Digit=[0-9]
Let=[A-z|a-z]
Lparen=[{]
Rparen=[}]
Integer_datatype=[int]
Lbrace=[(]
Rbrace=[)]
Equals=[=]
Plus=[+]
%%
Digit { print "DIGIT" }
Let { print "CHARACTER"}
Lparen { print "LPAREN"}
Rparen { print "RPAREN"}
Integer_datatype {print "INT"}
Equals {print "EQUAL"}
Lbrace {print "LBRACE"}
Rbrace {print "RBRACE"}
Plus {print "PLUS"}
%%