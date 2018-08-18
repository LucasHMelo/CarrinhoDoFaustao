# Título: conta-alevinos
## Autor: Hemerson Pistori


## Resumo: 

Código em python que de um contador de alevinos (versão preliminar ainda precisa melhorar muito para entrar em produção)

## Dependências

- kubuntu trusty 14.04.2 TLS
- Python 2.7.6 
- Opencv 2.7

## Dependências Windows

- Instale o [Anaconda](http://continuum.io/downloads) que contém todas as dependências, inclusive o Python. Basta fazer o download do arquivo .exe e executa-lo.


## Como instalar o OpenCV

  Seguir as instruções disponíveis em http://docs.opencv.org/doc/tutorials/introduction/linux_install/linux_install.html#linux-installation
  Lí em algum lugar que dá para instalar com o comando abaixo, não testei mas pode funcionar:
  ```
  $ sudo apt-get install python-opencv
  ```

## Como instalar o OpenCV no Windows
 - [OpenCV-Python](https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_setup/py_setup_in_windows/py_setup_in_windows.html#install-opencv-python-in-windows).
	1. Baixe o [Opencv](https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_setup/py_setup_in_windows/py_setup_in_windows.html#install-opencv-python-in-windows)
	2. Extraia os arquivos no local desejado.
	3. Vá para a pasta opencv/build/python/2.7.
	4. Copie o arquivo cv2.pyd para C:/Python27/lib/site-packages.
	5. Abra o terminal e digite python para executar o interpretador.
	6. Digite:

    	``` 
        >>> import cv2
        >>> print cv2.__version__
        ```
    Pronto!




## Como Usar
 
- Entre na pasta com o código fonte (que também é 'executável/interpretável' no caso do python):
  ``` 
  $ cd src 
  ```  
- Execute o código: 
  ```
  $ python ./contaAlevinos.py 
  ```
- Utilize ESC para sair antes do final do vídeo 



