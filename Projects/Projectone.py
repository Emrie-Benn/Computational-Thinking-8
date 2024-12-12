###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################
stage.set_background ("grey")



q1 = codesters.Square(100, 100, 200, 'pink')
q2 = codesters.Square(-100, 100, 200, 'yellow')
q3 = codesters.Square(-100, -100, 200, 'pink')
q4 = codesters.Square(100, -100, 200, 'yellow')
r1 = codesters.Rectangle(-50, -100, -108, 200, "grey")
r2 = codesters.Rectangle(50, 100, -108, 200, "grey"   )


s1 = codesters.Sprite("abook", 100, 100)
s1. set_size(0.2)
s2 = codesters.Sprite("videogame", -100, -100)
s2. set_size(0.1)
s3 = codesters.Sprite("pen", 100, -100)
s3. set_size(0.4)
s4 = codesters.Sprite("puppy", -100, 100)
s4. set_size(0.3)


message1 = codesters.Text("Emrie Ada Benn", 0, 220, "pink" )
message2 = codesters.Text("A book a day keeps the doctor away", 0, -220, "pink")