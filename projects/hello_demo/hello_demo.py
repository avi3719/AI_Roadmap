# Author: Avishkar
# Project: Hello Demo
# Date: Sep 2025
# Description: Load student marks & plot a bar chart

import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Student": ["Avishkar", "Sam", "Ravi", "Neha"],
    "Marks": [85, 78, 92, 74]
})

print(data)
data.plot(kind="bar", x="Student", y="Marks", title="Student Marks")
plt.show()

