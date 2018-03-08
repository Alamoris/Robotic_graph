import numpy as np
from PIL import Image

test_dict = {1:2}
test_dict.update({3:4})
k = test_dict.keys()

for x in k:
    print(x)

test_array = np.zeros((8, 8), dtype=int)
for x in test_array:
    print(x)