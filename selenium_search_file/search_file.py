import shutil
from pathlib import Path
from dataclasses import dataclass
from time import sleep

@dataclass
class File:
    
    """
    Esta classe é usada para retornar atributos de um arquivo que foi baixado.
    
    attr:
        file_name: str
    """
    
    _file_name : str = None

    @property
    def file_name(self):
        if self._file_name is None:
            return None
        return self._file_name

    @file_name.setter
    def file_name(self,name : str):
            self._file_name = name






def search_file(chromeOptions,/,delete_folder=True,* , rec=1, slp=1, allow_more_time : bool = False) -> File:        
    """summary
    Instructions:
    Garanta que não tenha nenhum arquivo dentro da pasta do diretório enviado pois isso causará conflitos, deixe o diretório onde o download será feito somente para esta finalidade.
    
    args:
        
        chromeOptions (ChromeOptions): opções do Google Chrome para verificar se existe o diretório configurado corretamente
        delete_folder : Caso queira manter artefatos para uso posterior coloque como False
        rec (int, opcional): contador
        slp (int, opcional): tempo usado para dormir, slp*10
        permitir_more_time: padrão = False (bool, opcional): Defina como verdadeiro para permitir que o programa procure um arquivo por mais de 30 segundos
        
    returns:
        Arquivo: Arquivo (Objeto)
    """

    try:
        directory = chromeOptions.to_capabilities()['goog:chromeOptions']['prefs']['download.default_directory']
    except (AttributeError,KeyError):
        raise Exception ("""Não foi configurado o diretório de downloads do selenium, considere rever as ChromeOptions para os seguintes valores:

prefs = {
'download.default_directory': %DIRETÓRIO_DOWNLOAD%/DOWNLOADS',
"download.prompt_for_download": False,
'directory_upgrade': True,
}

options.add_experimental_option("prefs",prefs)""")


    file = File()
    
    if slp > 2.9 and allow_more_time == False:  
        raise ValueError("O valor máximo permitido para ‘slp’ é 2,9 (29 segundos), caso seu download esteja demorando mais de 30 segundos considere analisar o desempenho da aplicação. Ou permita esperar mais enviando o parâmetro 'allow_more_time' = True")
    
    path_builder = Path(directory)
    
    sleep(slp)
    if not path_builder.exists():
        if rec > 10:
            raise FileNotFoundError (f"O download do arquivo não foi feito apesar de esperar {slp*10} segundos")
        return search_file(chromeOptions,delete_folder=delete_folder, rec=rec+1)
    else:
        try:
            assert len(list(path_builder.iterdir())) != 0
        except:
            if rec > 10:
                raise FileNotFoundError  ('O arquivo não foi baixado, considere aumentar o parâmetro slp para no máximo 2,9.')
            return search_file(chromeOptions,delete_folder=delete_folder, rec=rec+1)
        
        
        for temp_file in path_builder.iterdir():      
            file.file_name = temp_file.name
            
            if delete_folder:
                for temp_file in path_builder.iterdir():
                    temp_file.unlink()
                path_builder.rmdir()
            return file


if __name__ == '__main__':
    # search_file(str(Path().absolute()/'downloads'))
    ...