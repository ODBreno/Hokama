import sys

class Item:
    def __init__(self, index, return_val, cost):
        self.index = index
        self.return_val = return_val
        self.cost = cost

def greedy_algorithm(items, budget, alpha, correlations):
    actives = items.copy()
    def calculate_additional_value(item, solution, alpha, correlations):
        # Calcula o valor adicional ao adicionar o item à solução
        return_val = item.return_val
        sum_correlations = sum(correlations[item.index][sol_item.index] for sol_item in solution)
        return return_val - alpha * sum_correlations

    solution = []
    remaining_budget = budget

    actives.sort(
        key=lambda x: calculate_additional_value(x, solution, alpha, correlations) / x.cost,
        reverse=True
    )

    # Pega o item com o melhor valor ajustado
    for active in actives:
        if active.cost <= remaining_budget:
            solution.append(active)
            remaining_budget -= active.cost

    return solution

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

    return solution

def calculate_objective_value(subset, alpha, correlations):
    sum_return_vals = sum(item.return_val for item in subset)
    sum_correlations = sum(correlations[item1.index][item2.index] for item1 in subset for item2 in subset if item1 != item2)

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

    # Quick solution (greedy algorithm)
    quick_solution = greedy_algorithm(items, budget, alpha, correlations)
    print(' '.join(str(item.index) for item in quick_solution) + ' ')

    # Brute-force solution (exhaustive search)
    brute_force_solution = brute_force_algorithm(items, budget, alpha, correlations)
    print(' '.join(str(item.index) for item in brute_force_solution) + ' ')

if __name__ == '__main__':
    main()
