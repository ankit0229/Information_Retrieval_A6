#!/usr/bin/env python
# coding: utf-8

# In[89]:


import networkx
from collections import Counter
import matplotlib.pyplot as plt
import math


# In[90]:


Graph_2 = networkx.DiGraph()
fp = open(r'Wiki-Vote.txt', 'r')
text = fp.read()
list_lines = text.split('\n')
del list_lines[0:4]

list_edges = []
for a in list_lines:
    b = a.split()
    edge_nodes = (b[0], b[1])
    list_edges.append(edge_nodes)

Graph_2.add_edges_from(list_edges)


# ## Finding the pagerank values of all nodes of the graph

# In[91]:


dict_page_ranks = networkx.pagerank(Graph_2)
print("The dictionary page rank values with node ids as key and page rank value as the value is printed below:\n")
print(dict_page_ranks)


# ## Finding the hub and authority score of each of the nodes of the graph

# In[92]:


dict_hub_scores, dict_auth_scores = networkx.hits(Graph_2)


# In[93]:


print("The dictionary of hub scores with node ids as key and Hub score as the value is printed below:\n")
print(dict_hub_scores)


# In[94]:


print("The dictionary of Authority scores with node ids as key and Authority score as the value is printed below:\n")
print(dict_auth_scores)


# ## Now plotting the different graphs to do analysis

# In[95]:


list_tuples_indegree = Graph_2.in_degree()
list_tuples_outdegree = Graph_2.out_degree()
dict_outdegree = {}
for f in list_tuples_outdegree:
    dict_outdegree[f[0]] = f[1]
list_indegrees, list_outdegrees, list_hub_scores, list_auth_scores, list_pr_scores = [], [], [], [], []
list_pairs_hub, list_pairs_auth, list_pairs_pr = [], [], []
for t in list_tuples_indegree:
    curr_node = t[0]
    list_indegrees.append(t[1])
    list_outdegrees.append(dict_outdegree[curr_node])
    list_hub_scores.append(dict_hub_scores[curr_node])
    list_auth_scores.append(dict_auth_scores[curr_node])
    list_pr_scores.append(dict_page_ranks[curr_node])
    list_pairs_hub.append([curr_node, dict_hub_scores[curr_node]])
    list_pairs_auth.append([curr_node, dict_auth_scores[curr_node]])
    list_pairs_pr.append([curr_node, dict_page_ranks[curr_node]])


# In[96]:


#Plotting for indegree
plt.style.use('seaborn-darkgrid')
plt.figure(figsize=(6,6))
zip_cord = zip(list_indegrees, list_hub_scores)
list_zip_cord = list(zip_cord)
sort_zip_cord = sorted(list_zip_cord, key = lambda x: x[0]) 
list_x_cord = [w[0] for w in sort_zip_cord]
list_y_cord = [x[1] for x in sort_zip_cord]
plt.ylim(top=max(list_y_cord))  # adjust the top leaving bottom unchanged
plt.ylim(bottom=min(list_y_cord)) 
plt.plot(list_x_cord, list_y_cord, label = 'Hub scores')
plt.xlabel('In-degrees', fontsize = 14)
plt.ylabel('Hub Scores', fontsize = 14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.title(label = 'Graph for in-degree vs Hub scores',fontsize = 14 )
plt.legend()
plt.show()


# In[97]:


#Plotting for indegree
plt.style.use('seaborn-darkgrid')
plt.figure(figsize=(6,6))
zip_cord = zip(list_indegrees, list_auth_scores)
list_zip_cord = list(zip_cord)
sort_zip_cord = sorted(list_zip_cord, key = lambda x: x[0]) 
list_x_cord = [w[0] for w in sort_zip_cord]
list_y_cord = [x[1] for x in sort_zip_cord]
plt.ylim(top=max(list_y_cord))  # adjust the top leaving bottom unchanged
plt.ylim(bottom=min(list_y_cord)) 
plt.plot(list_x_cord, list_y_cord, label = 'Auth scores')
plt.xlabel('In-degrees', fontsize = 14)
plt.ylabel('Authority Scores', fontsize = 14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.title(label = 'Graph for in-degree vs Authority scores',fontsize = 14 )
plt.legend()
plt.show()


# In[98]:


#Plotting for indegree
plt.style.use('seaborn-darkgrid')
plt.figure(figsize=(6,6))
zip_cord = zip(list_indegrees, list_pr_scores)
list_zip_cord = list(zip_cord)
sort_zip_cord = sorted(list_zip_cord, key = lambda x: x[0]) 
list_x_cord = [w[0] for w in sort_zip_cord]
list_y_cord = [x[1] for x in sort_zip_cord]
plt.ylim(top=max(list_y_cord))  # adjust the top leaving bottom unchanged
plt.ylim(bottom=min(list_y_cord)) 
plt.plot(list_x_cord, list_y_cord, label = 'Page Rank scores')
plt.xlabel('In-degrees', fontsize = 14)
plt.ylabel('Page Rank Scores', fontsize = 14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.title(label = 'Graph for in-degree vs Page Rank scores',fontsize = 14 )
plt.legend()
plt.show()


# In[99]:


#Plotting for outdegree
plt.style.use('seaborn-darkgrid')
plt.figure(figsize=(6,6))
zip_cord = zip(list_outdegrees, list_hub_scores)
list_zip_cord = list(zip_cord)
sort_zip_cord = sorted(list_zip_cord, key = lambda x: x[0]) 
list_x_cord = [w[0] for w in sort_zip_cord]
list_y_cord = [x[1] for x in sort_zip_cord]
plt.ylim(top=max(list_y_cord))  # adjust the top leaving bottom unchanged
plt.ylim(bottom=min(list_y_cord)) 
plt.plot(list_x_cord, list_y_cord, label = 'Hub scores')
plt.xlabel('Out-degrees', fontsize = 14)
plt.ylabel('Hub Scores', fontsize = 14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.title(label = 'Graph for out-degree vs Hub scores',fontsize = 14 )
plt.legend()
plt.show()


# In[100]:


#Plotting for outdegree
plt.style.use('seaborn-darkgrid')
plt.figure(figsize=(6,6))
zip_cord = zip(list_outdegrees, list_auth_scores)
list_zip_cord = list(zip_cord)
sort_zip_cord = sorted(list_zip_cord, key = lambda x: x[0]) 
list_x_cord = [w[0] for w in sort_zip_cord]
list_y_cord = [x[1] for x in sort_zip_cord]
plt.ylim(top=max(list_y_cord))  # adjust the top leaving bottom unchanged
plt.ylim(bottom=min(list_y_cord)) 
plt.plot(list_x_cord, list_y_cord, label = 'Authority scores')

plt.xlabel('Out-degrees', fontsize = 14)
plt.ylabel('Authority Scores', fontsize = 14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.title(label = 'Graph for out-degree vs Authority scores',fontsize = 14 )
plt.legend()
plt.show()


# In[101]:


plt.style.use('seaborn-darkgrid')
plt.figure(figsize=(6,6))
zip_cord = zip(list_outdegrees, list_pr_scores)
list_zip_cord = list(zip_cord)
sort_zip_cord = sorted(list_zip_cord, key = lambda x: x[0]) 
list_x_cord = [w[0] for w in sort_zip_cord]
list_y_cord = [x[1] for x in sort_zip_cord]
plt.ylim(top=max(list_y_cord))  # adjust the top leaving bottom unchanged
plt.ylim(bottom=min(list_y_cord)) 
plt.plot(list_x_cord, list_y_cord, label = 'PageRank scores')
plt.xlabel('Out-degrees', fontsize = 14)
plt.ylabel('Page rank Scores', fontsize = 14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.title(label = 'Graph for out-degree vs Page Rank scores',fontsize = 14 )
plt.legend()
plt.show()


# In[102]:


#Making list of top 10 nodes according to Hub score
list_pairs_hub.sort(key = lambda x:x[1], reverse=True)
list_pairs_auth.sort(key = lambda x:x[1], reverse= True)
list_pairs_pr.sort(key = lambda x:x[1], reverse= True)

list_top10_hub = [list_pairs_hub[i][0] for i in range(10)]
list_top10_auth = [list_pairs_auth[j][0] for j in range(10)]
list_top10_pr = [list_pairs_pr[k][0] for k in range(10)]

#For top 10 hubs finding the successors i.e. nodes to which outlinks are there and they are also in Top 10 authorities
print("The top 10 hubs along with top 10 authorites that are also their successors")
for de in range(len(list_top10_hub)):
    d = list_top10_hub[de]
    list_successor = [w for w in Graph_2.successors(d)]
    list_intersection = []
    print(f"\n{de+1}. {d}")
    for e in list_top10_auth:
        if e in list_successor:
            list_intersection.append(e)
    print(list_intersection)


# In[103]:


#For top 10 Authorities finding the predecessos i.e. nodes from which inlinks are there and they are also in Top 10 Hubs
print("The top 10 Authorities along with top 10 Hubs that are also their predecessors")
for de in range(len(list_top10_auth)):
    d = list_top10_auth[de]
    list_predecessor = [w for w in Graph_2.predecessors(d)]
    list_intersection = []
    print(f"\n{de+1}. {d}")
    for e in list_top10_hub:
        if e in list_predecessor:
            list_intersection.append(e)
    print(list_intersection)


# In[104]:


#For top 10 Page rank finding the predecessos i.e. nodes from which inlinks are there and they are also in 
#Top 10 Page Rank Nodes list
print("The top 10 Page Rank nodes along with top 10 Page rank nodes that are also their predecessors")
for de in range(len(list_top10_pr)):
    d = list_top10_pr[de]
    list_predecessor = [w for w in Graph_2.predecessors(d)]
    list_intersection = []
    print(f"\n{de+1}. {d}")
    for e in list_top10_pr:
        if e in list_predecessor:
            list_intersection.append(e)
    print(list_intersection)


# In[105]:


print("The top 10 nodes according to the hub score along with their hub score are:\n")
print("  Node id     Hub score")
for y in range(10):
    print(f"{y+1}.)  {list_pairs_hub[y][0]}     {list_pairs_hub[y][1]}")


# In[106]:


print("The top 10 nodes according to the Authority score along with their Authority score are:\n")
print("  Node id     Authority score")
for y in range(10):
    print(f"{y+1}.)  {list_pairs_auth[y][0]}     {list_pairs_auth[y][1]}")


# In[107]:


print("The top 10 nodes according to the PageRank score along with their PageRank score are:\n")
print("  Node id     PageRank score")
for y in range(10):
    print(f"{y+1}.)  {list_pairs_pr[y][0]}     {list_pairs_pr[y][1]}")

