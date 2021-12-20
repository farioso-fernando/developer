# Cockroach

Depois da versão *0.3.0* do pacote, a equipe focou-se em densenvolver para o Cockroach, varios modulos de auto ajuda para os densevolvedores python. Além de produzir logs destacados e nomeálos, que até foi primeiramente o objetivo inicial do pacote, melhorar a forma em que programamos.

Até a verão *0.4.1* do pacote, o pacote apenas fornece o log() do modulo developing_cockroach.py.
Para as versão usamos a seguite nomeclatura de versionamento.

1.2.3
1 -> Function of great importance incorporated.
2 -> Improvement.
3 -> Bug fixes.

A equipe decidiu liberar a nomeclatura de releases por entendermos que seria de grande importancia as usuarios do pacote.

*Nota: Está documentação só é válida para as versões apartir do 0.3.0*

## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

Consulte **Implantação** para saber como implantar o projeto.

### 📋 Pré-requisitos

De que coisas você precisa para instalar o software e como instalá-lo?

```
Qualquer versão do Python3 acima e ter o pip instalado em sua maquina.
```

Não necessitarás de grandes coisas para executar o projeto. Apenas ter uma versão do python3 em sua maquina já o suficiente. Se houverem mais requisitos necessários para a execução, iremos documentar.

### 🔧 Instalação

Exemplos passo-a-passo para que você tenha um ambiente de desenvolvimento em execução.

Veja os exemplos a seguir:

Abra o seu emulador de terminal execute o seguinte comando:

```
pip install Developing-Cockroach == 0.3.0
```

ou

```
pip3 install Developing-Cockroach == 0.3.0
```

Terás o software total em sua maquina.

## 📦 Desenvolvimento

Em um arquivo python:

```
from cockroach import developing_cockroach as developer
developer.log(message= "This is a log message.")

Sáida:
[Log]: This is a log message.
```

### 🔩 Analise de ponta a ponta

A linha *cockroach* é o modulo principal do nosso pacote e é dele que os modulos originam.
O *developing_cockroach* é o modulo principal com assunto que tenham haver com o gerar logs personalizados.

```
developing_cockroach.log('Hello World!')
```

## 🛠️ Construído com

As ferramentas que usadas para criação do projeto

* [Visual Studio Code](https://code.visualstudio.com/) - O Visual Studio Code é um editor de código-fonte desenvolvido pela Microsoft para Windows, Linux e macOS.
* [pip](https://pypi.org/project/pip/) - Gerente de Dependência
* [Git](https://git-scm.com/) - Ssistema de controle de versões distribuído.

## 🖇️ Colaborando

Por favor, leia o [COLLABORATION.md](https://github.com/farioso-fernando/developer/blob/main/COLLABORATION.md) para obter detalhes sobre o nosso código de conduta e o processo para nos enviar pedidos de solicitação.

## 📌 Versão

Nós usamos [Git] e [GitHub](https://git-scm.com/)(https://github.com/) para controle de versão. Para as versões disponíveis, observe as [tags neste repositório](#).

## ✒️ Autores

Aqueles que ajudaram a levantar o projeto desde o seu início

* **Farioso Fernando** - *Trabalho Inicial* - [umdesenvolvedor](https://github.com/farioso-fernando)
* **Farioso Fernando** - *Documentação* - [fulanodetal](https://github.com/farioso-fernando)

Você também pode ver a lista de todos os [colaboradores](https://github.com/farioso-fernando/developer/contributors.md) que participaram deste projeto.

## 📄 Licença

Este projeto está sob a licença (MIT License) - veja o arquivo [LICENSE.md](https://github.com/farioso-fernando/developer/blob/main/LICENSE) para detalhes.

## 🎁 Expressões de gratidão

* Conte a outras pessoas sobre este projeto 📢
* Convide alguém da equipe para uma cerveja 🍺
* Obrigado publicamente 🤓.
* etc.

---

⌨️ com ❤️ por [Farioso Fernando](https://gist.github.com/farioso-fernando) 😊
