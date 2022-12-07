# signature: (Atom -> Num)
def hello(what):
  return (42.0 if int(what == WORLD) else (10.0 if int(what == MA) else (0.0 - 100.0)))

# signature: (Num -> ([Num] -> Num))
def _sum(x):
  return lambda xs: (x + sum(xs))

# signature: ([Num] -> Num)
def sum(xs):
  return (0.0 if int(xs == []) else _sum(xs[0])(xs[1:]))

FALSE = 0;
TRUE = 1;
WORLD = 2;
MA = 3;


pipes = [];
