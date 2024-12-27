import os
import time
import webbrowser


projeto_name = input('Nome do Projeto: ') # Criação do Nome do Projeto
os.mkdir(f'./{projeto_name}') # Cria pasta com Nome do projeto escolhido
os.chdir(f'./{projeto_name}') # Seleciona a pasta criada ./{project_name}


time.sleep(2)

with open('index.js','w') as index: # cria um arquivo Padrão rodando o servidor
    index.write("const express = require('express')\n")
    index.write("const app = express()\n")
    index.write("\n")
    index.write("const port = 3300\n")
    index.write("\n")
    index.write("// Middlewares para json, e arquivos estaticos\n")
    index.write("app.use(express.urlencoded({extended:true}))\n")
    index.write("app.use(express.static('public'))\n")
    index.write("app.get('/',(req,res)=>{res.send('ola')})\n")
    index.write("\n")
    index.write("// Configuração engine EJS\n")
    index.write("app.set('view engine', 'ejs');\n")
    index.write("app.listen(port,()=>{console.log('Rodando na porta 3300')})\n")
    

# criação de todas as pastas MVC Basica
os.mkdir('./models')
os.mkdir('./database')
os.mkdir('./views')
os.mkdir('./controllers')
os.mkdir('./static')
os.mkdir('./routes')
os.system('echo Criando arquivo Init')



time.sleep(1)
 # Instalando arquivo Json Init
os.system('npm init -y')

time.sleep(1)
os.system('echo Instalando Express')

time.sleep(1)
# Instalando npm Express
os.system('npm i express')

time.sleep(1)
os.system('echo Abrindo O localhost')
#Abrindo o servidor no WebBrowser
webbrowser.open('http://localhost:3300/') 

time.sleep(2)
# Iniciando o servidor
os.system('node index.js')  
