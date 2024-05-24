import sys
import time

class Item:
    def __init__(self, index, return_val, cost):
        self.index = index
        self.return_val = return_val
        self.cost = cost

def brute_force_algorithm(items, budget, alpha, correlations):
    solution = []
    max_objective_value = float('-inf')

    for i in range(1 << len(items)):
        subset = [items[j] for j in range(len(items)) if (i & (1 << j))]
        if sum(item.cost for item in subset) <= budget:
            objective_value = calculate_objective_value(subset, alpha, correlations)
            if objective_value > max_objective_value:
                max_objective_value = objective_value
                solution = subset

    return solution, max_objective_value

def calculate_objective_value(subset, alpha, correlations):
    sum_return_vals = sum(item.return_val for item in subset)
    sum_correlations = 0
    for i in range(len(subset)):
        for j in range(i + 1, len(subset)):
            sum_correlations += correlations[subset[i].index][subset[j].index]

    return sum_return_vals - alpha * sum_correlations

def main():
    budget = int(sys.stdin.readline())
    alpha = float(sys.stdin.readline())
    num_items = int(sys.stdin.readline())

    items = []
    for _ in range(num_items):
        index, return_val, cost = map(int, sys.stdin.readline().split())
        items.append(Item(index, return_val, cost))

    correlations = []
    for _ in range(num_items):
        correlations.append(list(map(float, sys.stdin.readline().split())))

    # Medir o tempo de execução da solução de força bruta
    start_time = time.time()
    brute_force_solution, max_objective_value = brute_force_algorithm(items, budget, alpha, correlations)
    end_time = time.time()

    # Calcular o tempo de execução
    execution_time = end_time - start_time

    # Calcular a soma dos valores de retorno e dos custos da solução encontrada
    total_return_val = sum(item.return_val for item in brute_force_solution)
    total_cost = sum(item.cost for item in brute_force_solution)

    # Mostrar o tempo de execução
    print(f'Tempo de execução: {execution_time:.6f} segundos')

    # Mostrar a solução e suas somas de valores
    print('Solução:', ' '.join(str(item.index) for item in brute_force_solution))
    print(f'Soma dos valores de retorno: {total_return_val}')
    print(f'Soma dos custos: {total_cost}')
    print(f'Valor objetivo (considerando correlações): {max_objective_value}')

if __name__ == '__main__':
    main()
