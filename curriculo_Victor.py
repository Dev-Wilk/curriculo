import sys
import os
from time import sleep
import webbrowser

# nameSkill = []
# nivelSkill = []

def ValidarAcesso(resposta):
    if (resposta == 's'):
        print('Obrigado, espero que goste')
        print("\U0001f600")
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
    elif (resposta == 'n'):
        print('Ta bom')
        print("\U0001F615")
        sys.exit()
    else:
        print('Não comprendi respostao poderia responder denovo')
        print('\U0001F917')
        resposta2= input('Gostaria de ver o Curriculo? s/n   ')
        ValidarAcesso(resposta2)

def link(uri, label=None): # funçao para abrir link no terminal
        if label is None: 
            label = uri
        parameters = ''

        # OSC 8 ; params ; URI ST <name> OSC 8 ;; ST 
        escape_mask = '\033]8;{};{}\033\\{}\033]8;;\033\\'

        return escape_mask.format(parameters, uri, label)

def InfDev():  #funcão para ver dados pessoais
       # Variaveis das informações do desenvolvedor
    name = 'Victor Wagner Wilk'
    idade = '30 anos'
    cidade_mora = 'São José'
    email = 'programadorwilk@gmail.com'
    telefone = '(48) 98446-7769'
    linkedin = ('https://www.linkedin.com/in/victor-wilk-a1371a235/')
    github = ('https://github.com/Dev-Wilk')
    # imprimindo no terminal um pouco mais agradavel
    print('\033[34mNome: \033[m\033[32m{}\033[0m'.format(name))
    print('\033[34mIdade: \033[m\033[32m{}\033[0m'.format(idade))
    print('\033[34mCidade: \033[m\033[32m{}\033[0m'.format(cidade_mora))
    print('\033[33mContato \033[0m')
    print('\033[39mTelefone: \033[m\033[31m{}\033[0m'.format(telefone))
    print('\033[39mEmail: \033[m\033[31m{}\033[0m'.format(email))
    print('\033[39mLinkedin: \033[m\033[31m{}\033[0m'.format(link(linkedin)))
    print('\033[39mGitHub: \033[m\033[31m{}\033[0m'.format(link(github)))
    print('')
    input('Precione ENTER para voltar ao menu')

def Formacao():
    print('')
    print('')
    print('')
    print('\033[32mFormaçao tecnica em desenvolvimento de sistemas(EAD) pelo SENAI\033[0m ')
    print('o curso focou bastante em Java, MySQL, Metodos ageis, Comunicação, deu bastante foco em desenvolvimento das soft skill')
    print('')
    print('\033[32mEntra21 curso de python(EAD)\033[0m: curso rapido e com muito conhecimento conseguio trazer o basico ate o avançado e com praticas para o mercado')
    print('')
    input('Precione ENTER para voltar ao menu')

def Certificados():
    # link dos certificados
    certificado1 = ('https://sgn.sesisenai.org.br/arquivos/certificacao/75/57/cc/7557cc2770db1ba03d5a9a1824df98c2/pfx12728585101158094603sfx.pdf') # certificado tecnico senai
    certificado2 = ('https://sgn.sesisenai.org.br/arquivos/certificacao/93/a3/1e/93a31eedd3213d90fc11df6c700ccc78/pfx12000498391916805638sfx.pdf') # certificado front end senai
    certificado3 = ('https://www.dio.me/certificate/488BF6BC/share') # certificado git e github dio
    certificado4 = ('https://www.dio.me/certificate/9700E982/share') # certificado html5 e css3 dio
    certificado5 = ('https://www.dio.me/certificate/AA037040/share') # certificado oop dio
    certificado6 = ('https://externo.proway.com.br/empregabilidade/arquivos/projetos/11/certificados/certificado-entra212022-ead5837-2022-09-30.pdf') # certificado python entra21
    certificado7 = ('https://coursera.org/share/93e7f7f49d548773ea943ed40fbc8a0c')# certificado cloud coursera

    opcao = 0
    while ( opcao != 8):
        print('+'.ljust(43,'-')+'+')
        print('|               Certificados               |')
        print('+'.ljust(43,'-')+'+')
        print('| 1- Tecnico SENAI    | 2- Front-end Senai |')
        print('| 3- Python Entra21   | 4- Git/Github DIO  |')
        print('| 5- Cloud Coursera   | 6- html5/CSS5 DDIO |')
        print('| 7- OOP DIO          | 8- SAIR            |')       
        print('+'.ljust(43,'-')+'+')
        try:
            opcao = int(input('Opção desejada: '))
        except:
            pass
        finally:
            pass
        if (opcao == 1):
            webbrowser.open(certificado1)
            os.system('cls' if os.name == 'nt' else 'clear')
        elif (opcao == 2):
            webbrowser.open(certificado2)
            os.system('cls' if os.name == 'nt' else 'clear')
        elif (opcao == 3):
            webbrowser.open(certificado6)
            os.system('cls' if os.name == 'nt' else 'clear')
        elif (opcao == 4):
            webbrowser.open(certificado3)
            os.system('cls' if os.name == 'nt' else 'clear')
        elif (opcao == 5):
            webbrowser.open(certificado7)
            os.system('cls' if os.name == 'nt' else 'clear')
        elif (opcao == 6):
            webbrowser.open(certificado4)
            os.system('cls' if os.name == 'nt' else 'clear')
        elif (opcao == 7):
            webbrowser.open(certificado5)
            os.system('cls' if os.name == 'nt' else 'clear')
        elif (opcao == 2):
            print('Voltando menu principal')
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print('Opção invalida')  

   
def Perfil():
    print(' Em busca de uma nova etapa da minha vida, em busca de novos desafios e descobrindo talentos que se conhecidiram na area de programação(aonde encontrei meu logos), com uma vasta area de conhecimento e sempre podendo se atualizar e podendo evoluir sem ter grande dependencias de outros.')
    print(' Alem da curiosidade tenho facilidade para achar falhas, antes usava essa habilidade para area de segurança agora aprendendo sobre softwares e automaticamente ja busco falhas ou jeitos de burla sistemas e descobrir o que esta ocacionando erros e me empolgo e paro ate me sentir satisfeito.')
    print(' Busco alguma empresa que permita evoluir, que tenha um ambiente organizado e com bom café nada melhor para estimular competencias que uma bela xicara de café')
    print('')
    print('Uma vida sem desafios não vale a pena ser vivida. \033[32m-Sócrates\033[0m')
    print('')
    print('')
    print('')
    input('Precione ENTER para voltar ao menu')

def HardSkill():
    linha = '-'*47
    # lista com nome das habilidades tecnicas
    nameHardSkill = ['Cloud','CSS','Git','java','javascript','html','linux','logica de programação','metodologias ageis','mysql','python'] 
    # lista com o nivel numerico das habilidades tecnicas (Conheço-Básico-Intermediário-Avançado)
    nivelHardSkill = ['Conheço','Intermediário','Básico','Básico','Intermediário','Intermediário','Básico','Intermediário','Básico','Intermediário','Intermediário'] 
    # tabela mostrando hardskill
    print(linha)
    print('Competência Técnica   |   Nivel de Conhecimento')
    print('----------------------|------------------------')
    for x in range(0,len(nameHardSkill)):
        if (nivelHardSkill[x] == 'Conheço'):
            print(nameHardSkill[x]+''.ljust(22-len(nameHardSkill[x]))+'|   '+nivelHardSkill[x])
        elif (nivelHardSkill[x] == 'Básico'):
            print('\033[32m'+nameHardSkill[x]+''.ljust(22-len(nameHardSkill[x]))+'\033[0m'+ '|   '+'\033[32m'+nivelHardSkill[x]+'\033[0m')
        elif (nivelHardSkill[x] == 'Intermediário'):
            print('\033[33m'+nameHardSkill[x]+''.ljust(22-len(nameHardSkill[x]))+'\033[0m'+ '|   '+'\033[33m'+nivelHardSkill[x]+'\033[0m')
        elif (nivelHardSkill[x] == 'Avançado'):
            print('\033[34m'+nameHardSkill[x]+''.ljust(22-len(nameHardSkill[x]))+'\033[0m'+ '|   '+'\033[34m'+nivelHardSkill[x]+'\033[0m')
    print('')
    input('Precione ENTER para voltar ao menu')




def SoftSkill():
    linha = '_'*30
    titulo = 'Soft Skills'
     # lista com nome das habilidades Comportamentais
    nameSoft = ['Criatividade','Organização','Resolução de Problemas','Trabalhar sob pressão','Pensamento Critico','Neurodivergente','Curioso','Perfeccionista']
    nameSoftSkill = sorted(nameSoft)  
    # tabela mostrando hardskill
    # print(linha)
    print('\033[33m'+linha)
    print(titulo.center(30,))
    print(linha)
    print('')
    for x in range(0,len(nameSoftSkill)):
        print('\033[35m{}\033[0m'.format(nameSoftSkill[x].center(30,)))
    print('')
    input('Precione ENTER para voltar ao menu')


def Motivo():
    print('Alem das habilidades mostrada no menu principal acredito que tenho muito agregar na empresa, com as metas proposta dessa startup de facilitar a vida dos empreendores do ramo de franquias, o desafio de atender 30.000 franquias em todo Brasil.')
    print('Por ser uma uma empresa nova com pensamentos no futuro e com uma cultura nova, e até na linguagem de programação ultilizada é umas de maior expansão tornando um projeto duradouro e facilmente expansível.')
    print('Com a meta de expandir 4x o numero de franquiados em 4 anos vai ser otima oportunidade de crescer junto com todos desafios, podendo ser util a equipe toda.')
    print('Adoraria a chance dessa nova experiencia futurista')
    print('')
    input('Precione ENTER para voltar ao menu')


def MostrarMenuPrincipal():
    opcao = 0
    while ( opcao != 7):
        print('+'.ljust(38,'-')+'+')
        print('| 1- Dados Pessoais   | 2- Formação   |')
        print('| 3- Certificados     | 4- Perfil     |')
        print('| 5- Hard Skill       | 6- Soft Skill |')
        print('| 7- Porque contra    | 8- Sair       |')
        print('+'.ljust(38,'-')+'+')
        try:
            opcao = int(input('Opção desejada: '))
        except:
            pass
        finally:
            pass
        
        if (opcao == 1):
            os.system('cls' if os.name == 'nt' else 'clear')
            InfDev()
            os.system('cls' if os.name == 'nt' else 'clear')
        
        elif (opcao == 2):
            os.system('cls' if os.name == 'nt' else 'clear')
            Formacao()
            os.system('cls' if os.name == 'nt' else 'clear')

        elif (opcao == 3):
            os.system('cls' if os.name == 'nt' else 'clear')
            Certificados()
            os.system('cls' if os.name == 'nt' else 'clear')

        elif (opcao == 4):
            os.system('cls' if os.name == 'nt' else 'clear')
            Perfil()
            os.system('cls' if os.name == 'nt' else 'clear')

        elif (opcao == 5):
            os.system('cls' if os.name == 'nt' else 'clear')
            HardSkill()
            os.system('cls' if os.name == 'nt' else 'clear')

        elif (opcao == 6):
            os.system('cls' if os.name == 'nt' else 'clear')
            SoftSkill()
            os.system('cls' if os.name == 'nt' else 'clear')
        
        elif (opcao == 7):
            os.system('cls' if os.name == 'nt' else 'clear')
            Motivo()
            os.system('cls' if os.name == 'nt' else 'clear')
        
        elif (opcao == 8):
            print('Sistema finalizado')
            print('\U0001f600Espero que tenha gostado\U0001f600')
            sleep(2)

print('Bem vindo ao curriculo em Python')
ver = input('Gostaria de ver o menu do curriculo? (s/n) ')

ValidarAcesso(ver)
MostrarMenuPrincipal()