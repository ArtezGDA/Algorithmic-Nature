# Import the library
try:
    # This is the statement you normally use.
    noise = ximport("noise")
except ImportError:
    # But since these examples are "inside" the library
    # we may need to try something different when
    # the library is not located in /Application Support
    noise = ximport("__init__")
    reload(noise)

size(200,200)

noise.seed()
w = 200
h = 200
for i in range(w):
	for j in range(h):
		d = noise.generate(i, j, width=w, height=h, scale=0.1 )
		# I'm multypling d by 1.2 to crank the blackness up a bit.
		fill(0,0,0,d*1.2)
		rect(i, j, 2, 2)
