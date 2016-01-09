import sys
import re

numlines = int(sys.stdin.next())
regex = r'^\d+ (C|CPP|JAVA|PYTHON|PERL|PHP|RUBY|CSHARP|HASKELL|CLOJURE|BASH|SCALA|ERLANG|CLISP|LUA|BRAINFUCK|JAVASCRIPT|GO|D|OCAML|R|PASCAL|SBCL|DART|GROOVY|OBJECTIVEC)$'


for i in range(0, numlines):
    line = sys.stdin.next().strip()
    m = re.match(regex, line)

    if m == None:
        print "INVALID"
    else:
        print "VALID"

