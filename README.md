# Project Brief: Polynomial Time 2-Approximation Algorithm for Metric TSP

## Abstract
This project delves into the development of a polynomial time 2-approximation algorithm for the metric Traveling Salesperson Problem (TSP). The objective is to derive a Hamiltonian cycle of minimal weight in a fully connected, weighted graph, emphasizing efficiency in the face of NP-Hard complexities.

## Algorithmic Landscape
The project initiates with a meticulous exploration of TSP, strategically narrowing its focus to the metric domain where edge weights adhere to the triangle inequality. A comprehensive analysis unfolds, elucidating the complexities inherent in approximating optimal solutions in this nuanced context.

## Crafting the Approximation Framework
The algorithmic core of the project revolves around a polynomial time 2-approximation algorithm. Leveraging the construct of Minimum Spanning Trees (MSTs), the approach meticulously assembles an approximate Hamiltonian cycle. Each step is meticulously laid out, marrying theoretical underpinnings with pragmatic implementation considerations.

### Exemplary Execution
```bash
$ ./compile.sh
$ ./run.sh input_graph.txt
Hamiltonian cycle of weight 21:
0, 1, 3, 2, 4, 0

