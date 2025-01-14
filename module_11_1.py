import requests
import matplotlib.pyplot as plt
from PIL import Image

# data = {'key': 'value'}
# response = requests.post('https://api.example.com/submit', data=data)
# print(response.text)  # Ответ сервера



# sizes = [15, 30, 45, 10]
# labels = ['A', 'B', 'C', 'D']
#
# plt.pie(sizes, labels=labels)
# plt.title('Круговая диаграмма')
# plt.show()

img = Image.open('image.jpg')
img.show()

