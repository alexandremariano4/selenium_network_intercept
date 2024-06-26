## Atualização 1.0.2

Trazendo novidades, agora é possível em vez de pesquisar diretamente pela rota desejada, você buscar todas requisições já realizadas pelo navegador, podendo ser verificado no [repositório oficial](https://github.com/alexandremariano4/selenium_network_intercept/tree/main) utilizando o arquivo `example3.py`.

**Agora tem a possibilida de além de somente fazer uma busca assim:**

```powershell
request = intercept_http(driver,'/route')
```

**É possível utilizar também desta forma:**

```python
request = intercept_http(driver,only_request=True)
```

Que trará um objeto que terá dois atributos importantes para esta funcionalidade 

- requests
- responses

Estes atributos trarão a possibilidade de você mesmo validar todas as requisições que foram feitas desde o momento da abertura do navegador, sem preocupar com a implementação interna da biblioteca.

***Mas lembre-se que ainda é possível buscar diretamente pela rota desejada***

---

**Use** 

`request.requests`  Para ter acesso a todas requisições realizadas até o momento da chamada da função

Para atualizar essa lista, utilize `request.update()`

Itere sobre esta lista para fazer a própria varredura e verificar o que desejar por exemplo, buscar pela URL:

```python
for req in request.requests:
    print(req.url)
```

atributos disponíveis para as `requests` e as `responses` 

- type
- network_method
- url
- status_code
- headers

E especificamente para os tipos “response”

- body

---

**Ao chamar a função, as vezes pode ter a necessidade de atualizar as requisições já passadas para verificar se a requisição específica que você deseja buscar, finalmente apareceu.**

**Use**

```python
request = intercept_http(driver,only_request=True)
#O resto da sua automação
request.update()
```

Desta maneira, você poderá atualizar constantemente as requisições e atualizar a lista de requisições realizadas.

---

A função `intercept_http` possuí novos parâmetros, alguns desses não sendo necessários envio de nenhum dado, outros, sendo opcionais.

Os adicionados foram:

- update ❌ *Não envie nada neste parâmetro*
- update_object ❌ *Não envie nada neste parâmetro*
- static_resource → Enviar como False caso queira que a função valide e retorne requisições para arquivos estáticos como “css,svg,png,jpeg” entre outros.
- only_request  → Enviar como True caso queira receber somente a lista de requisições para utilizar assim como ensinado aqui no 1.0.2, caso envie como False, que é o padrão, será buscado a rota enviada.


## Atualização 1.0.1

Com a atualização da biblioteca agora é possível verificar se ao interagir com algum elemento em tela usando o selenium, se foi baixado um arquivo em um diretório específico.

Siga o [repositório oficial](https://github.com/alexandremariano4/selenium_network_intercept/tree/main/selenium_search_file) desta funcionalidade para entendê-la e aplicá-la.



## Atualização 1.0.1

Agora é possível recuperar os parâmetros de queries e também é retornado a URL que foi capturado os parâmetros.
Altamente recomendado utilizar o arquivo exemplo3.py do [repositório oficial](https://github.com/alexandremariano4/selenium_network_intercept/tree/main) para ter entendimento e aplicabilidade ao seu cenário.
Em algumas situações não será viável usar essa funcionalidade, somente a busca do objeto com body,status e url terão que satisfazer.


## Get Started

1. Instale o Python a partir do link: https://www.python.org/downloads/ e adicione ao PATH o executável
2. Faça o clone deste repositório utilizando o git
3. Vá para a pasta onde foi clonado e abra a pasta “selenium-network-intercept”
4. No terminal, caso queira (Eu recomendo), use o comando `python -m venv .venv` para instalar as dependências em um ambiente virtual que poderá ser excluído caso queira
5. Para ativar o ambiente virtual, para windows use o comando `.\.venv\Scripts\activate` em Linux `source .venv\Scripts\Activate`, caso não tenha conseguido, recomendo seguir este vídeo: [https://www.youtube.com/watch?v=m1TYpvIYm74&ab_channel=OtávioMiranda](https://www.youtube.com/watch?v=m1TYpvIYm74&ab_channel=Ot%C3%A1vioMiranda)
6. No seu terminal, use o comando `pip install -r requirements.txt` (Este comando fará a instalação de todas dependências necessárias para rodar seu código)
7. Pronto para usar o código!

Os arquivos “example.py” no [repositório oficial](https://github.com/alexandremariano4/selenium_network_intercept/tree/main) são um bom ponto de partida para o entendimento, a partir dele, é possível você já conseguir implementar em qualquer situação para si.

Mas, caso não queira utilizá-lo, explicarei abaixo.

---

### Instanciando Driver

Faça a importação do seu driver como de costume, porém, dessa vez, adicione nas Options, a seguinte capability:  `'goog:loggingPrefs', {'performance': 'ALL'}`

```python
from selenium import webdriver
from selenium.webdriver import ChromeOptions

options = ChromeOptions()
#Considere as opções abaixo para otimizar o tempo da execução do código no geral
options.add_argument('--headless') #Alerto que em algumas situações, pode não ser encontrado a requisição por conta de rodar em modo headless, faça o teste e verifique isso.
options.page_load_strategy = 'eager'
########################################

options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})

driver = webdriver.Chrome(options=options)
```

A partir desta configuração, é possível receber os LOGS que trarão todas requisições feitas durante a execução do navegador pela instância `driver`.

---

Após realizada a instância, importe a função `intercept_http` do pacote network, e módulo intercept.

```python
from selenium_network_intercept import intercept_http
```

Feito isso, você já tem todas funcionalidades do pacote em uma chamada, apenas sendo necessários alterar parâmetros, vamos as explicações de como usá-la.

---

### Buscando as requisições

A função `intercept_http` pede dois argumentos como parâmetros obrigatórios, e um opcional, sendo estes respectivamente:

**driver** → Instância que você realizou do seu webdriver

**route** → Rota que vai ser buscada na lista dos responses

**delay** → Delay utilizado em situações que a requisição pode estar demorando e a função não está sendo efetiva.

**⚠️⚠️⚠️Para usar a função corretamente, atente-se aos detalhes ⚠️⚠️⚠️**

No parâmetro route, você deve enviar ou uma parte da rota, ou ela inteira (sem considerar parâmetros de query).

Por exemplo, use:

```python
intercept_http(
		driver = driver,
		route = '/conteudos/publicos'
)
```

Não use:

```python
intercept_http(
		driver = driver,
		route = '/conteudos/publicos?id=50&nome="teste"'
)
```

O motivo desta diferença é simples, a função é feita para retornar dados que podem fazer o usuário que está testando monitorar se a requisição foi feita com sucesso, não sendo necessário qualquer dado referente a query que foi feita, ou algum tipo de payload de request.

Também é possível usar:

```python
intercept_http(
		driver = driver,
		route = 'https://www.meuendereco.com.br/conteudos/publicos'
)
```

É possível, mas, o ideal é usar uma parte da rota que corresponda exatamente a requisição que você busca validar.

---

Ao chamar a função, ela retornará um objeto do tipo **ObjectedIntercepted**, que possui como atributos principais: 

- body → Corpo da resposta que a requisição obteve (Quando ter, quando não ter, não retornará erro, mas retornará um dicionário com informações que auxiliam a dar manutenção em caso de necessidade)
- status_code → Status da requisição (200,404,500)
- url → URL completa da requisição, então por exemplo, se você fez como o exemplo acima `'/conteudos/publicos'`, ele retornará algo como `'https://www.meuendereco.com.br/conteudos/publicos'`
- method → Método utilizado na requisição (GET,POST,DELETE,PUT)
- list_of_responses → Lista das responses que o navegador obteve até o momento da chamada da função
- list_of_requests  →  Lista das requests que o navegador obteve até o momento da chamada da função (Essa tende a ser uma lista bem maior, recomendo utilizar pprint para exibir caso deseje)

### Exemplo de retorno da função

Abaixo é um exemplo do objeto retornado com as informações necessárias para realizarmos validações

```python
ObjectIntercepted(_body={'channelNumber': 33,
                         'code': 'BH',
                         'name': 'GLOBO MINAS',
                         'serviceIDHD': '23104',
                         'serviceIDOneSeg': '23128'},
                  _status_code=200,
                  _url='https://affiliates.video.globo.com/affiliates/info',
                  _method='GET')
```

---