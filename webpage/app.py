from flask import Flask, render_template, request
from materiais import materiais_info

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    mtrl = materiais_info
    
    nome_material = request.form.get('material')
    selecionado = next((m for m in materiais_info if m['nome'] == nome_material), None)
    return render_template('index.html', mtrl=mtrl, selecionado=selecionado)

if __name__ == '__main__':
    app.run(debug=True)