import pandas as pd

def espiadinha(db, collection_name, linhas):
    """Serve para ver quais colunas a base possui:
    -> db: Nome da variável é db (cliente alexandria)
    -> collection_name: Nome da base a ser explorada
    -> linhas: Numero de linhas a ser lida, recomenda-se 1"""
    lista_rows=[]
    collection = db[collection_name]
    query = collection.find()
    for n,x in enumerate(query):
        if n<linhas:
            lista_rows.append(x)
            n= n+1
        else:
            break
    df_esp=pd.DataFrame(lista_rows)
    return df_esp


def get_df(db, collection_name,colunas):
    """Serve para ler a base na íntegra, filtrando as colunas para preservar memória:
    -> db: Nome da variável é db (cliente alexandria)
    -> collection_name: Nome da base a ser explorada
    -> colunas: lista com os nomes das colunas"""
    lista_rows=[]
    collection = db[collection_name]
    query = collection.find()
    for x in query:
        filtered_row = {key: x.get(key) for key in colunas}
        lista_rows.append(filtered_row)
    df=pd.DataFrame(lista_rows)
    return df

def trata_alternativas(texto):
    itens = re.findall(r"\{(.*?)\}", texto)
    alternativas=[]
    correcoes=[]
    for item in itens:
        alternativa=item.split('",')[0].split('"text": ')[1]
        alternativas.append(alternativa)
        
        correcao=item.split('"isRightAnswer": ')[1].split(',')[0]
        correcoes.append(correcao)
        alternativa_correta = alternativas[correcoes.index('True')]
        
    return alternativas, alternativa_correta

def from_html_to_text(tag):
    tag=tag.encode("utf-8")
    soup = BeautifulSoup(tag, features="html.parser")
    for script in soup(["script", "style"]):
        script.extract()   
    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)
    return text