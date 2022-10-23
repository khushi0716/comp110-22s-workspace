import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datas.csv')
df.plot.line(x='Time', y='Hertz')
plt.title('Sleep Quality')
plt.xlabel('Time (hours)')
plt.ylabel('Hertz (Hz)')

plt.show()
