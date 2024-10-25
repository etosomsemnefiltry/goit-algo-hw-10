import pulp

# Создаем задачу линейного программирования
problem = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)
lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat='Continuous')
fruit_juice = pulp.LpVariable("Fruit_Juice", lowBound=0, cat='Continuous')
problem += lemonade + fruit_juice, "Total_Products"

# Ограничения ресрусов
problem += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Limit"
problem += 1 * lemonade <= 50, "Sugar_Limit"
problem += 1 * lemonade <= 30, "Lemon_Juice_Limit"
problem += 2 * fruit_juice <= 40, "Fruit_Puree_Limit"

problem.solve()

print(f"Status: {pulp.LpStatus[problem.status]}")
print(f"Количество лимонада: {lemonade.varValue}")
print(f"Количество фруктового соку: {fruit_juice.varValue}")
print(f"Максимальна кількість продуктів: {pulp.value(problem.objective)}")
