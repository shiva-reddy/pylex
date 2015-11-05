import re
import sys
%%
Digit=[0-9]
Let=[A-z|a-z]
%%
Digit { print "Found digit" }
Let { print "Found letter"}
%%