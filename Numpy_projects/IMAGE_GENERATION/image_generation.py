#image generation
import numpy as np
num=np.random.randint(0,256,size=(5,5))
print(num)
dark=num
dark[dark<128]=0
bright=num
bright[bright>128]=255
print(dark)
print(bright)