# ProFiler

Boas-vindas ao repositório do projeto ProFiler


Aqui, você vai encontrar os detalhes de como foi estruturar o desenvolvimento do projeto a partir desse repositório.

  
<details>
<summary><strong>🧑‍💻 O que foi desenvolvido</strong></summary>

Trablhei com uma aplicação com uma interface de linha de comando (CLI) que recebe como entrada um caminho (diretório ou arquivo) e gera um relatório com informações sobre o caminho informado.

Para executar a aplicação:

1. Siga os passos do tópico [**🏕️ Ambiente Virtual**]
2. Configure o auto-complete da aplicação com o comando `pro-filer --install-completion` e reinicie o terminal;
3. Execute o comando `pro-filer` seguido de um caminho (diretório ou arquivo) e uma ação. Por exemplo:

```bash
pro-filer . preview
```

![pro-filer preview](./images/pro-filer-preview.gif)

A aplicação já está funcional, mas possui dois problemas:

1. alguns bugs precisam ser corrigidos;
2. mais testes precisam ser implementados.

Você deverá corrigir os bugs e implementar os testes para garantir que a aplicação funcione corretamente. Será o momento de aplicar tudo o que você aprendeu sobre debugging e testes automatizados em Python!

</details>
  
<details>
  <summary><strong>:memo: Habilidades trabalhadas </strong></summary>

Neste projeto, sou capaz de:

- Encontrar bugs no código de uma aplicação escrita em Python;
- Corrigir bugs no código de uma aplicação escrita em Python;
- Criar testes para uma aplicação escrita em Python;
- Utilizar o `pytest` para criar testes automatizados em uma aplicação escrita em Python.

<!-- 🤔 [HS] Escrevam as habilidade utilizando a Taxonomia de Bloom. -->

</details>

<details>
<summary><strong>‼ Antes de começar a desenvolver</strong></summary>

1. Clone o repositório

- Use o comando: `git clone git@github.com:p4n1k0/pro_filer.git`
- Entre na pasta do repositório que você acabou de clonar:
  - `cd pro_filer`

2. Instale as dependências

    - Siga os passos do tópico [**🏕️ Ambiente Virtual**]

</details>

<details>
  <summary><strong>🏕️ Ambiente Virtual</strong></summary>
  O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **criar o ambiente virtual**

  ```bash
  python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
  source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
  python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  Quando precisar desativar o ambiente virtual, execute o comando `deactivate`. Lembre-se de ativar novamente quando voltar a trabalhar no projeto.

  O arquivo `dev-requirements.txt` instalará todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`. Se você desejar instalar uma nova dependência, basta adicioná-la no arquivo `dev-requirements.txt` e executar o comando `python3 -m pip install -r dev-requirements.txt` novamente.

  Se o VS Code não reconhecer as dependências instaladas no ambiente virtual criado, será necessário informar o caminho do interpretador Python. Para isso, abra o VS Code e pressione `Ctrl + Shift + P` (no Mac, `Cmd + Shift + P`) e digite `Python: Select Interpreter`. Selecione o interpretador que possui o caminho `./.venv/bin/python` no nome.
</details>


<details>
  <summary><strong>🛠 Testes</strong></summary>

  Para executar os testes certifique-se de que você está com o ambiente virtual ativado.

  <strong>Executar os testes</strong>

  ```bash
  python3 -m pytest
  ```

  O arquivo `pyproject.toml` já configura corretamente o `pytest`. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:

  ```bash
  python3 -m pytest -s -vv --continue-on-collection-errors
  ```

  O `pytest` possui diversos parâmetros que podem ser utilizados para executar os testes de diferentes formas. Alguns exemplos são:

  ```bash
  python3 -m pytest tests/test_nome_do_arquivo.py  # Executa todos os testes do arquivo de testes especificado
  python3 -m pytest tests/test_nome_do_arquivo.py::test_nome_do_teste  # Executa apenas o teste especificado
  python3 -m pytest -k expressao  # Executa apenas os testes que contém a expressão informada como substring
  python3 -m pytest -x  # Executa os testes até encontrar o primeiro erro
  ```
Obs: Alguns testes foram desenvolvidos pelo time da trybe.

  Você pode combinar os parâmetros para executar os testes da forma que desejar! Para mais informações, consulte a [documentação do pytest](https://docs.pytest.org/en/7.3.x/contents.html).
</details>

---
  
<details>
<summary><strong>🗣 Me dê feedbacks sobre o projeto!</strong></summary>

</details>
  

