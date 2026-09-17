import os
import re #Módulo para expressões regulares (avançadas)
os.system('cls')


registro_bruto = "user-9842; mArIAnA sIlVa; 11-98765-4321 ; Mariana.Silva@Empresa.com; 25/08/1995"

print("===Dado Bruto Recebido===")
print(f"Dado Bruto: {registro_bruto}\n")

#Separação e limpeza inicial
campos_limpos = [campo.strip() for campo in registro_bruto.split(";")]

id_bruto,nome_bruto,fone_bruto,email_bruto,data_bruto = campos_limpos

#Tratamento dos dados
nome_formatado = nome_bruto.title()
contem_apenas_letras = nome_formatado.replace(" ","").isalpha()

prefixo_id = id_bruto[:3]
numero_id = id_bruto[4:]
id_final = f"{prefixo_id}#{numero_id.zfill(6)}" #zfill = preenchye com zeros a esquerda

fone_apenas_numeros = re.sub(r"\D", "", fone_bruto)

email_minusculo = email_bruto.lower()
posicao_arroba = email_minusculo.find("@")
usuario_email = email_minusculo[:posicao_arroba]
dominio_email = email_minusculo[posicao_arroba + 1:]

partes_data = data_bruto.split("/") #["25", "08", "1995"]
data_iso = '-'.join(reversed(partes_data)) #19995-08-25

padrao_email = r"^[\w\,-]+@[\w\,-]+\.w+$"
email_valido = bool(re.match(padrao_email, email_minusculo))
fone_valido = len(fone_apenas_numeros) == 11 and fone_apenas_numeros.isdigit()

relatorio = f"""

============================================================
           Sistema de Processamento de Dados
============================================================

[DADOS INDIVIDUAIS TRATADOS]
- ID Interno............: {id_final} (Prefixo:{prefixo_id})
- Nome Completo.........: {nome_formatado}
- Usuário do Sistema....: {usuario_email.replace('-', '_')}
- Provedor Corporativo..: {dominio_email.center(20, "*")}
- Data de Nascimento....: {data_iso}

[CHECKLIST DE AUDITORIA]
👍Nome possui apenas letras? {'SIM' if contem_apenas_letras else 'NÃO'}
👍Formato de e-mail correto? {'SIM' if email_valido else 'NÃO'}
👍Telefone celular válido?   {'SIM' if fone_valido else 'NÃO'}
👍O e-mail termina em .com?  {email_minusculo.endswith('.com')}

[TELEFONE INTERNACIONAL PADRÃO E.164] 
+ 55{fone_apenas_numeros}
--------------------------------------------------------

"""

print(relatorio)