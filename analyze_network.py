import numpy as np
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# img = mpimg.imread('data/icon/1.jpg')
# ax = plt.gca()
# fig = plt.gcf()
# trans = ax.transData.transform
# trans2 = fig.transFigure.inverted().transform
# imsize = 7

members = pd.read_csv("data/hololiver_url.csv", header=0, encoding="utf_8", delimiter=',')
member_names = members["name"].tolist()
idx = [n for n in range(27)]
labels = dict(zip(idx,member_names))
am = pd.read_csv("data/am.csv", encoding="utf_8", header=None, delimiter=',')
am = np.array(am)
G = nx.from_numpy_matrix(am)

print(nx.number_of_nodes(G))
print(nx.number_of_edges(G))

# レイアウトの取得
pos = nx.spring_layout(G)

# 可視化
plt.figure(figsize=(20, 20))
edge_width = [d['weight']*1 for (u,v,d) in G.edges(data=True)]
nx.draw_networkx_edges(G, pos, alpha=0.5, width=edge_width)
nx.draw_networkx_nodes(G, pos, node_color="c", node_size=2000)
nx.draw_networkx_labels(G, pos, fontsize=6, font_color="r", font_family="Yu Gothic", font_weight="bold", labels=labels)
# (x,y) = nx.spring_layout(G, scale=10)[0]
# xx,yy = trans((x, y))
# xa,ya = trans2((xx, yy))
# a = plt.axes([xa-imsize/2.0, ya-imsize/2.0, imsize, imsize])
# a.imshow(img)
# a.set_aspect('equal')
# a.axis('off')

plt.axis('off')
plt.savefig("data/graph_image/weight")
plt.show()

# pagerank の計算
pr = nx.pagerank(G)
pr_values = [p * 80000 for p in list(pr.values())]

# 可視化
plt.figure(figsize=(20, 20))
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_nodes(G, pos, node_size=pr_values, node_color=list(pr.values()), cmap=plt.cm.Reds)
nx.draw_networkx_labels(G, pos, fontsize=6, font_color="g", font_family="Yu Gothic", font_weight="bold", labels=labels)
plt.axis('off')
plt.savefig("data/graph_image/page_rank")
plt.show()

print(pr.values())