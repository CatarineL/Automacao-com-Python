'''
Projeto: Organizador de Arquivos por Extensão

Objetivo
Criar um programa em Python capaz de organizar automaticamente 
os arquivos de uma pasta, movendo-os para subpastas 
com base em suas extensões (como .pdf, .png, .txt, etc.). 
O programa também deve registrar cada movimentação feita em um arquivo de log.
Requisitos
Seu programa deve:
-Percorrer todos os arquivos de uma pasta chamada organizador. (Arquivo anexado)
-Identificar a extensão de cada arquivo (exemplo: .pdf, .jpg, .py, etc.).
-Criar subpastas com os nomes das extensões (caso ainda não existam).
-Mover os arquivos para as subpastas correspondentes.
-Registrar todas as ações feitas em um arquivo registro.log, com data, hora, nome do
arquivo e destino final.
-Ao final da execução, exibir no terminal um resumo com:
    -Quantos arquivos foram organizados
    -Quais extensões foram encontradas
'''
from pathlib import Path
import shutil
from datetime import datetime

pasta = Path("organizador")
arquivos_excel = Path("ArquivosExcel")
arquivos_docx = Path("ArquivosDocx")
arquivos_png = Path("ArquivosPng")
arquivos_pdf = Path("ArquivosPDF")
arquivos_txt = Path("ArquivosTxt")
arquivos_jpg = Path("ArquivosJpg")





#função para colocar nos arquivos
def automacao(extensao, caminhoDestinoArquivo, nomePastaDestino):
    #verificando a existencia de arquivos de excel
    for arquivo in pasta.glob(f"*.{extensao}"):
        caminhoDestinoArquivo.mkdir(exist_ok=True)
        shutil.move(arquivo, f"{nomePastaDestino}")
        
        #registrando ação
        with open("registro.log", 'a', encoding="utf-8") as registro_automatico:
            agora = datetime.now()
            registro_automatico.write(agora.strftime("%d/%m/%Y %H:%M"))
            registro_automatico.write(f" {arquivo} movido para a pasta {nomePastaDestino}\n")
        
    
#contadores de extensao de arquivos
excel = 0
docx = 0
png = 0
pdf = 0
txt = 0
jpg = 0
soma_arquivos = 0


for tipo_arquivo in pasta.iterdir(): #iterdir refere a iteracao em pastas
    if tipo_arquivo.suffix ==  '.xlsx':
        excel=excel + 1
    elif tipo_arquivo.suffix ==  '.docx':
        docx=docx + 1
    elif tipo_arquivo.suffix ==  '.png':
        png=png + 1
    elif tipo_arquivo.suffix ==  '.pdf':
        pdf=pdf + 1
    elif tipo_arquivo.suffix ==  '.txt':
        txt=txt + 1
    elif tipo_arquivo.suffix ==  '.jpg':
        jpg=jpg + 1
    
    soma_arquivos = (excel+docx+png+pdf+txt+jpg)

print(f"O total de arquivos encontrados é {soma_arquivos}")

#excel
automacao('xlsx', arquivos_excel, "ArquivosExcel")
#docx
automacao('docx', arquivos_docx, "ArquivosDocx")
#png
automacao('png', arquivos_png, "ArquivosPng")
#pdf
automacao('pdf', arquivos_pdf, "ArquivosPDF")
#txt
automacao('txt', arquivos_txt, "ArquivosTxt")
#jpg
automacao('jpg', arquivos_jpg, "ArquivosJpg")

