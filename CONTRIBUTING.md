-- Para Contribuir

    01 - Instale na sua máquina o Python e o PIP para instalações de pacotes.

        * [Instalar no Windows][0]

        * [Instalar no Mac ou Linux (via pyenv)][1]

    02 - Instale o VirtualEnv. (*No Python 3.x o VirtualEnv já vem embutido*).

    01 - Logue com sua conta no GitHub e faça um Fork e do projeto sborganicos.

	02 - clone o repositório em um diretório na sua maquina:

        ```
		Ubuntu = "git clone https://github.com/[seuUsuario]/sborganicos sborganicos"
        ```
	03 - entre no diretório criado:

        No Terminal do Linux:
        ```
		cd sborganicos
        ```

    04 - Crie o virtualenv com o Python 3.x

        ```
        python -m venv .venv
        ```


    05 - Execute o comando de ativação do virtualenv

        No Terminal do Linux/Mac:

        ```
        source .venv/bin/activate
        ```

        No Windows:

        ```
        .venv\Scripts\activate.bat
        ```

    06 - Faça a migração do banco

        ```
        python manage.py migrate
        ```

	06 - Desative o virtualenv

        No Terminal do Linux:
        ```
        deactivate
        ```

	04 - Inicie o git flow (Caso você não tenha ele instalado ou não saiba como acesse o link: https://github.com/nvie/gitflow/wiki/Installation):

        No Terminal do Linux:
        ```
        git flow init
        ```

		Nota: Mantenha todos os branchs padrões

	-- Passos que se repetem em cada modificação

	05 - Crie uma nova feature branch para fazer uma modificação:

        No Terminal do Linux:
        ```
		git flow feature start adicionando-meu-nome-no-readme"
        ```

		Nota: modifique adicionando-meu-nome-no-readme pelo nome da modificação.

    06 - Ative o virtual env

        No Terminal do Linux:
        ```
        source venv/bin/activate"
        ```

	07 - Faça a modificação (No exemplo o seu nome no campo Contribuições do readme).

    08 - Saia do virtual env

        No Terminal do Linux:
        ```
        deactivate"
        ```

	09 - Adicione a modificação:

        No Terminal do Linux:
        ```
        git add .
		git commit -m Finished feature
        ```

	10 - junte a modificação ao branch develop

        No Terminal do Linux:
        ```
        git flow feature finish adicionando-meu-nome-no-readme"
		```

		Nota: modifique adicionando-meu-nome-no-readme pelo nome da modificação.

	11 - crie um release da modificação:

        No Terminal do Linux:
        ```
        git flow release start 0.0.1"
        ```

	12 - finalise o release da modificação:

        No Terminal do Linux:
        ```
        git flow release finish 0.0.1"
        ```

		Nota 2: O Git Flow abre o editor de texto três vezes:

    			Uma para você editar o texto do merge commit relacionado ao merge entre a release branch 0.0.1 e 				a branch master (sugiro para que você deixe o texto padrão deixado pelo Git.);
    			Um para a descrição da tag 0.0.1, que será criada pelo Git Flow para facilitar mudanças de versão 				no software (Descreva exatamente o que foi adicionado e/ou modificado);
    			Uma para você editar o texto do merge commit relacionado ao merge entre a branch master e a 				branch develop (sugiro para que você deixe o texto padrão deixado pelo Git.);

	13 - faça um push:

        No Terminal do Linux:
        ```
        git push origin master"
        ```

	14 - Agora faça um PULL REQUEST
		Vá a sua página no GitHub e clique em "Pull Request", será aberta uma página 			para que você descreva algum comentário, preencha os campos e clique em "send Pull Request".

Agora é só esperar o mantenedor aceita-la ou não.

[0]: https://www.python.org/downloads/
[1]: http://blog.abraseucodigo.com.br/instalando-qualquer-versao-do-python-no-linux-macosx-utilizando-pyenv.html
