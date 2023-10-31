from flask import Flask, render_template, request, redirect, session, flash, url_for 


app = Flask(__name__)

app.secret_key = "lista de jogos"

# app.config['SQLALCHEMY_DATABASE_URI'] = \
#     'SGBD://{usuario}:{senha}@{servidor}/{database}'.format(
#         SGBD = 'mysql+mysqlconnector',
#         usuario = 'root',
#         senha = 'root',
#         database = 'root'
#     )

# db = SQLAlchemy(app)


@app.route('/')
def index():
    lista = ['jogo1']
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST'])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + ' logado com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
        
    else:
        flash('Usuário não logado.')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Sessão encerrada')
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
