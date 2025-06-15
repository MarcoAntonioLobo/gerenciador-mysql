from flask import Flask, render_template, request, redirect, url_for, flash
import docker
import secrets
import string
from threading import Thread

app = Flask(__name__)
app.secret_key = 'chave-secreta-qualquer'  # só para flash msgs

con = docker.from_env()

def gerar_senha():
    return ''.join(secrets.choice(string.ascii_letters) for i in range(8))

def obter_variavel(lista, chave):
    variaveis = list(filter(lambda x: chave in x, lista))
    if variaveis:
        return variaveis[0].replace(f"{chave}=", "")
    return ''

def exibir_banco(container):
    lista = container.attrs.get("Config").get("Env")
    root_string = obter_variavel(lista, "MYSQL_ROOT_PASSWORD")
    database_string = obter_variavel(lista, "MYSQL_DATABASE")
    user_string = obter_variavel(lista, "MYSQL_USER")
    password_string = obter_variavel(lista, "MYSQL_PASSWORD")
    porta_acesso = container.ports.get("3306/tcp")[0].get("HostPort")
    return {
        'id': container.id,
        'nome_banco': database_string,
        'porta': porta_acesso,
        'root_pwd': root_string,
        'usuario': user_string,
        'senha_usuario': password_string,
    }

@app.route('/')
def index():
    containers = con.containers.list(filters={"label": ["gerador.banco=true"]})
    bancos = [exibir_banco(c) for c in containers]
    return render_template('index.html', bancos=bancos)

@app.route('/criar', methods=['GET', 'POST'])
def criar():
    if request.method == 'POST':
        nome_banco = request.form.get('nome_banco', '')
        usuario = request.form.get('usuario', '')
        senha_usuario = request.form.get('senha_usuario', '')
        senha_root = request.form.get('senha_root', '')

        if not senha_root:
            senha_root = gerar_senha()

        parametros = [f"MYSQL_ROOT_PASSWORD={senha_root}"]

        if usuario:
            parametros.append(f"MYSQL_USER={usuario}")
        if senha_usuario:
            parametros.append(f"MYSQL_PASSWORD={senha_usuario}")
        if nome_banco:
            parametros.append(f"MYSQL_DATABASE={nome_banco}")

        container = con.containers.run("mysql", detach=True, publish_all_ports=True,
                                       environment=parametros, labels={"gerador.banco": "true"})
        flash(f"Banco criado com ID: {container.id[:12]}")
        return redirect(url_for('index'))

    return render_template('criar.html')

@app.route('/remover/<id>')
def remover(id):
    try:
        container = con.containers.get(id)
        container.remove(force=True)
        flash(f"Banco removido: {id[:12]}")
    except Exception as e:
        flash(f"Erro ao remover banco: {str(e)}")
    return redirect(url_for('index'))


def run_app():
    app.run(port=8080, debug=False, threaded=True)

if __name__ == '__main__':
    thread = Thread(target=run_app)
    thread.daemon = True  # para o thread morrer se o processo principal encerrar
    thread.start()
    print("Servidor Flask rodando em background na porta 8080")
    # Aqui você pode colocar outras coisas no seu script, o terminal não trava
    # Se quiser deixar o script ativo, você pode por um input() ou loop infinito
    input("Pressione Enter para encerrar...\n")
