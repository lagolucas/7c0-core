def cria(arroba, id, link):
    string = '<!DOCTYPE html><html><head>    <meta charset="utf-8">    <meta name="viewport" content="width=device-width">    <meta name="description" content="Website do Projeto 7C0.">    <meta name="keywords" content="Projeto 7C0, monitoramento, politicos, atores publicos">    <link rel="icon" type="image/x-icon" href="./img/eye.ico" />    <title>Projeto 7C0 | Politicos | @account_handle</title>    <link rel="stylesheet" href="../../css/style.css">    <script type="text/javascript" src="../../js/scripts.js"></script></head><body>    <header>        <div class="container">            <div id="branding">                <h1>                    Projeto 7C0 | @account_handle                </h1>            </div>            <nav>                <ul>                    <li><a href="../../index.html">Home</a></li>                    <li><a href="../../about.html">Sobre</a></li>                    <li><a href="../../source.html">Codigo-Fonte</a></li>                </ul>            </nav>        </div>    </header>    <section id="main">        <div class="container">            <article id="main-col-single">			<ul id="services">                        <div class="tweet"><h3>Pergunte porque o politico apagou esse tweet </h3></div>						<div class="tweet">							<a href="https://twitter.com/share?ref_src=twsrc%5Etfw" class="twitter-share-button tweet" data-size="large" data-text="Esse tweet sumiu, o que aconteceu @account_handle? " data-url="archive_link" data-via="projeto7c0" data-related="projeto7c0" data-lang="pt" data-show-count="false">Tweet</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>						</div>		                </ul>				<div><iframe name="interno" width="100%" height="500" src="archive_link"></iframe></div>				<p>&nbsp;</p>                            </article>        </div>        </div>    </section>    <section id="newsletter">        <div class="container">            <h3>Receba atualizações do projeto &nbsp;</h3>            <form action="https://projeto7c0.us20.list-manage.com/subscribe/post?u=984470f280d60b82c247e3d7b&amp;id=00a31b0d4a"                method="post" target="_blank" novalidate>                <input class="button_1" type="submit" value="Inscreva-se" name="subscribe">            </form>        </div>    </section>    <footer>        <p>Projeto 7C0, Copyright &copy; 2019</p>    </footer></body></html><!-- Browser Sync --><!--     You can sync this code using VSCode Browser Sync by typing "Server mode in browser" and then    chosing the following files to be sync "*.html|./css/*.css".-->'

    string = string.replace("account_handle", arroba)
    string = string.replace("archive_link", link)
    print("Criando arquivo...")
    f = open(arroba+"/"+str(id)+".html", "w+")
    f.write(string)
    f.close()


if __name__ == '__main__':
    import database, contas, os

    arrobas = contas.pega_contas()

    for arroba in arrobas:
        print(arroba)
        lista = database.list_apagados(arroba)
        os.makedirs(arroba, exist_ok=True)

        for tweet in lista:
            cria(arroba, tweet[0], str(tweet[1]).replace("http", "https", 1))

