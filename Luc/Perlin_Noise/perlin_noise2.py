
try:
    noise = ximport("noise")
except ImportError:
   
    noise = ximport("__init__")
    reload(noise)

size(200,200)

noise.seed()
noise.shape( [0,1,2,3]*10 )
w = 200
h = 200
for i in range(w):
	for j in range(h):
		d = noise.generate(i, j, width=w, height=h, scale=0.1 )
		fill(0,0,0,d*1.2)
		rect(i, j, 1, 1)
