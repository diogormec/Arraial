import matplotlib.pyplot as plt

# Dados para o gráfico
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 50]

# Criar o gráfico
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Crescimento')

# Adicionar título e rótulos
plt.title('Gráfico Simples')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.legend()

# Mostrar o gráfico
plt.show()

