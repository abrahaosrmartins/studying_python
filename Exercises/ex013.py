salary = float(input('Digite o salário: '))
increase = salary * 0.15
new_salary = salary + increase
print('Com o aumento de R${:.2f}, o novo salário passa ser R${:.2f}' .format(increase, new_salary))