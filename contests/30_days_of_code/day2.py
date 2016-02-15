import sys
import math

price = float(sys.stdin.next())
tip = float(sys.stdin.next()) / 100
tax = float(sys.stdin.next()) / 100
total = price + price * tip + price * tax

print "The final price of the meal is $%s." % int(round(total))