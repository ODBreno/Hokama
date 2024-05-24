import sys

class Item:
    def __init__(self, index, return_val, cost):
        self.index = index
        self.return_val = return_val
        self.cost = cost

def greedy_algorithm(items, budget, alpha, correlations):
    def calculate_additional_value(item, solution, alpha, correlations):
        # Calcula o valor adicional ao adicionar o item à solução
        return_val = item.return_val
        if solution:
            sum_correlations = sum(correlations[item.index][sol_item.index] for sol_item in solution)
        else:
            sum_correlations = 0
        return return_val - alpha * sum_correlations

    solution = []
    remaining_budget = budget

    # Pega o item com o melhor valor ajustado
    while items and remaining_budget > 0:
        items.sort(
            key=lambda x: calculate_additional_value(x, solution, alpha, correlations) / x.cost,
            reverse=True
        )
        best_item = items.pop(0)
        if best_item.cost <= remaining_budget and calculate_additional_value(best_item, solution, alpha, correlations) > 0:
            solution.append(best_item)
            remaining_budget -= best_item.cost

    return solution

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

    # Solução gulosa (greedy algorithm)
    quick_solution = greedy_algorithm(items, budget, alpha, correlations)
    print(' '.join(str(item.index) for item in quick_solution) + ' ')

if __name__ == '__main__':
    main()
