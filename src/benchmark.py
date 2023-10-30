import networkx as nx
import time
import utils as u
import mvc_brute_force as bf
import mvc_greedy as gr

P = [0.125, 0.25, 0.5, 0.75] # Edge Probabilities
N = [4, 256, 1]              # Vertices [start, stop, step]

def benchmark(G, algorithm):
    """
    Benchmark the given algorithm on the given graph.
    """
    ts = time.time()
    mvc_val, mvc_set, mvc_ops = algorithm(G)
    te = time.time()
    return mvc_val, f'"{",".join(map(str, list(mvc_set)))}"', mvc_ops, te - ts

if __name__  == '__main__':

    header = ['n', 'mvc_val', 'mvc_set', 'ops', 'time']

    for p in P:

        d_brute_force = []
        d_greedy_highest_incidence = []
        
        for n in [i for i in range(*N)]:

            G = u.read_graph(n, p, '../graphs')
            print(f'Graph: n={n}, p={p:.3f}.')

            #if n < 30:
            #    res = benchmark(G, bf.mvc_brute_force)
            #    print(f'Brute-Force: done in {res[3]} seconds.')
            #    d_brute_force.append([n, *res])

            res = benchmark(G, gr.mvc_greedy_highest_incidence)
            print(f'Greedy, Highest Incidence: done in {res[3]} seconds.')
            d_greedy_highest_incidence.append([n, *res])
        
            print()

        #u.write_benchmark(header, d_brute_force, 'brute-force', p, '../benchmarks')
        u.write_benchmark(header, d_greedy_highest_incidence, 'greedy-highest-incidence', p, '../benchmarks')
            
            





