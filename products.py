#讀取檔案

products = []
with open('products.csv', 'r') as f:
	for line in f:
		name, price = line.strip().split(',')
		products.append([name, price])
print(products)



products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	products.append([name, price])
print(products)

for p in products:
	print(p[0], "的價格是", p[1])

with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品名稱, 商品價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')