from flask import Flask, render_template
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/')
def home():
    plt.figure(figsize=(7, 5))
    
    x = [1, 2, 3, 4, 5]
    y1 = [1, 4, 9, 16, 25]
    y2 = [1, 8, 27, 64, 125]

    plt.plot(x, y1, label='Quadrados', color='blue', linestyle='-', marker='o')
    plt.plot(x, y2, label='Cubos', color='green', linestyle='--', marker='s')
    plt.title('Gráfico de Quadrados e Cubos')
    plt.xlabel('Valores de X')
    plt.ylabel('Valores de Y')

    plt.grid(True)
    plt.legend()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    buf.close()

    return render_template('index.html', graph=image_base64)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
 