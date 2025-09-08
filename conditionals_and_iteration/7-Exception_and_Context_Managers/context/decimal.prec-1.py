import decimal
from decimal import localcontext, Context

with localcontext(Context(prec=5, rounding=decimal.ROUND_DOWN)) as ctx:
    print(ctx)
    print(one / three)
print(one / three)