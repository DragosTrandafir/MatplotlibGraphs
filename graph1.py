import matplotlib.pyplot as plt
import numpy as np

fig, ax=plt.subplots()



clothes=['t-shirt','trousers','hoodie','shirt','socks','shoes']
counts=[102,78,25,100,15,44]
colors=['red','blue','black','yellow','orange','green']
labels=['t-shirt','trousers','hoodie','shirt','socks','shoes']

ax.bar(clothes, counts, label=labels, color=colors)

ax.set_ylabel('Number of items')
ax.set_xlabel('Items')
ax.set_title('Item Distribution In My Shop',fontsize='x-large',fontfamily='Times New Roman')


ax.legend()


plt.show()