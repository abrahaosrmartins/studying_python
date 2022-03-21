price = float(input('Digite o preço do produto: '))
discount = price * 0.05
new_price = price - discount
print('Com o desconto de R${:.2f}, o novo preço passa ser R${:.2f}' .format(discount, new_price))
