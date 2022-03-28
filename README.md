## Extração de dados 

Site faz a extração de dados do site  <a href="https://torrentool.org/">torrentool</a>  fazendo uso framework Scrapy.

### 🎲 Rodando o Back End (servidor)

```bash
# Clone este repositório
$ git clone <https://github.com/Felipe9622/extraindo_filmes_scrapy.git>

# Acesse a pasta do projeto no terminal/cmd
$ cd torrentool/torrentool/torrentool

# Instale as dependências do ambiente virtual 
$ pip3 install virtualenv

#Crie o ambiente
$ source scrapy/bin/activate 

# Instale as bibliotecas nescessarias no arquivo requirements.txt
$ pip install –r requirements.txt

#Executando o servidor 
$ scrapy crawl torrentool -o filmes.csv
```


 ##Demonstração  

https://user-images.githubusercontent.com/51293199/160470701-048b55ec-c5d7-4890-8742-be83c25470c1.mp4

