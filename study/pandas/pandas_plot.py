
import pandas as pd
import matplotlib.pyplot as plt
Core_Dataframe = pd.DataFrame({'A' :  [ 3.67, 6.66, 14.5, 13.4, 21.44, 10.344],
'B' :  [ 2.345, 745.5, 12.4, 13.4, 22.35, 10.344  ]})
print("   THE CORE DATAFRAME ")
print(Core_Dataframe)
print("")
Core_Dataframe.plot(x ='A', y='B', kind = 'scatter')
plt.show()
# plt.savefig("test")

