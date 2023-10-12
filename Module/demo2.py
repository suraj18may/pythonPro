import demo1
from demo1 import x,add,sub
from demo1 import *


print(demo1.x)
demo1.add(10,20)
demo1.sub(20,10)

print(x)
add(20,40)
sub(40,20)

from imp import reload
reload(demo1)
reload(demo1)
