from flask import Flask, render_template, request, redirect, session, flash

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console
jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of War', 'Rack n Slash', 'PS2')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS2')
lista = [jogo1, jogo2, jogo3]

app = Flask(__name__)
app.secret_key = "lista de jogos"

@app.route('/lista')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/lista')

@app.route('/')
def logar():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def aut():
    if 'alohomora' == request.form['senha']:
        session['Usuario_logado'] = request.form['usuario']
        flash(session['Usuario_logado'] + ' logado com sucesso!')
        return redirect('/lista')
    else:
        flash('Usuário não logado.')
        return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
