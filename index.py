# -*- coding: utf-8 -*-
"""
Created on Sun Mar  9 11:56:59 2025

@author: Kaue
"""

import tkinter as tk
from tkinter import messagebox
import random
import string
import sqlite3

# token aleatório
def gerar_token():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))

# banco de dados
def criar_tabela():
    conn = sqlite3.connect('transacoes.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            token TEXT NOT NULL,
            valor REAL NOT NULL,
            conta_remetente TEXT NOT NULL,
            conta_destinatario TEXT NOT NULL,
            identificacao_conta TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# simula o pagamento e armazena no banco de dados
def simular_pagamento():
    valor = entry_valor.get()
    conta_remetente = entry_conta_remetente.get()
    conta_destinatario = entry_conta_destinatario.get()
    identificacao_conta = entry_identificacao_conta.get()
    
    if not valor or not conta_remetente or not conta_destinatario or not identificacao_conta:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
        return
    
    # Gerar token
    token = gerar_token()
    
    # conecta ao banco de dados e insere a transação
    conn = sqlite3.connect('transacoes.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO transacoes (token, valor, conta_remetente, conta_destinatario, identificacao_conta)
        VALUES (?, ?, ?, ?, ?)
    ''', (token, float(valor), conta_remetente, conta_destinatario, identificacao_conta))
    conn.commit()
    conn.close()
    
    # Exibir o token gerado
    messagebox.showinfo("Token Gerado", f"Token: {token}\nValor: {valor}\nRemetente: {conta_remetente}\nDestinatário: {conta_destinatario}\nID Conta: {identificacao_conta}")

# interface gráfica
root = tk.Tk()
root.title("Simulação de Pagamento com Tokenização")

# cria a tabela no banco de dados (se não existir)
criar_tabela()

label_valor = tk.Label(root, text="Valor do Pagamento:")
label_valor.grid(row=0, column=0, padx=10, pady=10)

entry_valor = tk.Entry(root)
entry_valor.grid(row=0, column=1, padx=10, pady=10)

label_conta_remetente = tk.Label(root, text="Conta do Remetente:")
label_conta_remetente.grid(row=1, column=0, padx=10, pady=10)

entry_conta_remetente = tk.Entry(root)
entry_conta_remetente.grid(row=1, column=1, padx=10, pady=10)

label_conta_destinatario = tk.Label(root, text="Conta do Destinatário:")
label_conta_destinatario.grid(row=2, column=0, padx=10, pady=10)

entry_conta_destinatario = tk.Entry(root)
entry_conta_destinatario.grid(row=2, column=1, padx=10, pady=10)

label_identificacao_conta = tk.Label(root, text="Identificação da Conta:")
label_identificacao_conta.grid(row=3, column=0, padx=10, pady=10)

entry_identificacao_conta = tk.Entry(root)
entry_identificacao_conta.grid(row=3, column=1, padx=10, pady=10)

# simular o pagamento
botao_pagamento = tk.Button(root, text="Simular Pagamento", command=simular_pagamento)
botao_pagamento.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()