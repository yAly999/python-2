# 1. Corrigido para 'request' com 'r' minúsculo
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/formulario")
def exibir_formulario():
    return render_template('formulario.html', resultado='Aguardando o envio...')


@app.route('/processar', methods=['POST'])
def processar_formulario():

    nome = request.form.get('nome')
    idade = request.form.get('idade')
    curso = request.form.get('curso')
    
    if not nome or not idade or not curso:
        mensagem_resultado = "ERRO: Todos os campos sao obrigatórios!"
    else:
        idade_int = int(idade)
        mensagem_base = f"Olá {nome}, você tem {idade} anos e está no curso de {curso}!"

    if idade_int < 18:
        mensagem_idade = "Você é menor de idade" 
    elif idade_int > 18 and idade_int < 60:
        mensagem_idade = "você e adulto"
    else:
        mensagem_idade = "Você é experiente!"

    if curso == 'Python':
        mensagem_curso = "Ótima escolha, você é versatil"
    elif curso == 'Flask':
        mensagem_curso = "Excelente escolha gafanhoto!"
    elif curso == 'HTML/CSS':
        mensagem_curso = "funcional pequenino gafanhoto!"             
    else:
        mensagem_curso = "curso interessante!"
                
                
           
    


