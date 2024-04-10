Um utilitário para verificar e obter atributos de um arquivo baixado usando ChromeOptions no Selenium.

## **Instalação**

Este utilitário pode ser instalado via pip:

```bash
bashCopy code
pip install selenium-network-intercept

```

## **Uso**

### **Uso Básico**

```python
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from pathlib import Path
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium_search_file import search_file

pasta_downloads = str(
    Path().absolute() / 'downloads'
    )

options = ChromeOptions()
prefs = {
    'download.default_directory': pasta_downloads,
    "download.prompt_for_download": False,
    'directory_upgrade': True,
}

options.add_experimental_option("prefs",prefs)
options.page_load_strategy = 'eager'
options.add_argument('--headless')
options.add_argument('--log-level=3')

brw = Chrome(options=options)

brw.get('URL')

WebDriverWait(brw,10).until(EC.element_to_be_clickable(('xpath','elemento'))).click()

file = file_verify(options)
print(file.file_name)

brw.quit()
```

### **Parâmetros**

- **`chromeOptions`**: Objeto ChromeOptions do Selenium para verificar a configuração correta do diretório de download.
- **`delete_folder`**: Defina como **`True`** se deseja excluir os arquivos baixados e o diretório de download após a verificação, **`False`** caso contrário.
- **`rec`**: Contador para chamadas recursivas. Padrão é 1. Recomandado Não Alterar
- **`slp`**: Tempo de espera em segundos. Padrão é 1, enviar outro valor significa o valor enviado vezes 10 | 2.9) = 29 segundos esperando o download.
- **`allow_more_time`**: Defina como **`True`** para permitir que o programa procure por um arquivo por mais de 30 segundos. Padrão é **`False`**.

### **Retorno**

Retorna um objeto **`File`** contendo os atributos do arquivo baixado.

## **Classe File**

### **Atributos**

- **`nome_arquivo`**: Nome do arquivo baixado.

## **Instruções**

Certifique-se de que não há arquivos dentro da pasta do diretório enviado, pois isso causará conflitos. Deixe o diretório onde o download será feito apenas para este propósito.