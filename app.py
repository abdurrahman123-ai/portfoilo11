import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


np.random.seed(42)
days=np.arange(1,11)

sales=np.random.randint(50,150,size=10)
costes=np.random.randint(30,100,size=10)

data={
    
    'day':days,
    'sale':sales,
    'coste':costes,
    'income':sales-costes
}

df=pd.DataFrame(data)
print(df)


plt.figure(figsize=(10,6))
plt.plot(df['day'], df['sale'],label='Sales',marker='o',linestyle='-',color='blue')
plt.plot(df['day'],df['coste'],label='Costes',marker='s',linestyle='--',color='red')
plt.plot(df['day'],df['income'],label='Incomes',marker='^',linestyle='-.',color='green')
plt.title('company Analyzes')
plt.xlabel('Dayes')
plt.ylabel('count')
plt.legend()#its for clarifying
plt.grid(True)
plt.tight_layout()
plt.show()






