import pandas as pd
import numpy as np
data = [1,2,3,4]
A = np.reshape(data, (-1, 4))
print (A)
dataFrame = pd.DataFrame(A)
dataFrame.to_csv("b.csv", header=False, index=False)
