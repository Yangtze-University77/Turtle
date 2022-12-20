import turtle as t
s = t.Shape("compound")
poly1 = ((0,0),(100,-50),(0,100),(-100,-50))
s.addcomponent(poly1, "red", "blue")
poly2 = ((0,0),(100,-50),(-100,-50))
s.addcomponent(poly2, "blue", "red")

t.register_shape("myshape", s)
t.shape("myshape")
