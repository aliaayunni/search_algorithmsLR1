import streamlit as st
from collections import deque
from PIL import Image

st.title("Lab Report 1: BFS & DFS")
st.markdown("**Course:** BSD2513/BSD3513 Introduction to Artificial Intelligence")

image = Image.open("LabReport_BSD2513_#1.jpg")
st.image(image, caption = "Directed Graph from Lab Report", use_container_width= True)

st.divider()


graph = {
    'A' : ['B','D'],
    'B' : ['C','E','G'],
    'C' : ['A'],
    'D' : ['C'],
    'E' : ['H'],
    'G' : ['F'],
    'H' : ['F','G'],
    'F' : []
}

def bfs(start_node):
    visited = []
    from collections import deque
    queue = deque([start_node])
    seen = set([start_node])
    while queue:
        node = queue.popleft()
        visited.append(node)
        for nb in sorted(graph.get(node, [])):
            if nb not in seen:
                seen.add(nb)
                queue.append(nb)
    return visited

def dfs(start_node, visited=None):
    if visited is None:
        visited = []
    if start_node not in visited:
        visited.append(start_node)
        for nb in sorted(graph.get(start_node, [])):
            if nb not in visited:
                dfs(nb, visited)
    return visited

st.title("BFS & DFS Traversal")
start = st.selectbox("Start node", sorted(graph.keys()), index=0)
algo = st.radio("Algorithm", ["BFS", "DFS"])
if st.button("Run"):
    order = bfs(start) if algo == "BFS" else dfs(start)
    st.success(f"{algo} order from {start}: {order}")