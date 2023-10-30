import networkx as nx
import utils as u
import mvc_brute_force as bf
import mvc_greedy as gr

P = 0.25 # Edge Probability
N = 12   # Vertices

if __name__  == '__main__':

    G = u.read_graph(N, P, '../graphs')
    
    pos = nx.spring_layout(G)

    _, nodes, _ = bf.mvc_brute_force(G)
    u.draw_solution(G, nodes, pos)

    _, nodes, _ = gr.mvc_greedy_highest_incidence(G)
    u.draw_solution(G, nodes, pos)