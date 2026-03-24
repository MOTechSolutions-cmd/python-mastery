import pandas as pd
import numpy as np

def clean_data(file_path):
    print(f"Lendo arquivo: {file_path}")
    try:
        # Carregando dados
        df = pd.read_csv(file_path)
        
        # Lógica Sênior: Limpeza e Transformação
        df.drop_duplicates(inplace=True) # Remove duplicatas
        df.fillna("N/A", inplace=True)   # Trata valores nulos
        
        # Filtro de exemplo: Apenas vendas acima de 0
        if 'vendas' in df.columns:
            df = df[df['vendas'] > 0]
            
        # Salva o resultado limpo
        output = "dados_limpos.xlsx"
        df.to_excel(output, index=False)
        print(f"Sucesso! Relatório gerado: {output}")
        
    except Exception as e:
        print(f"Erro no processamento: {e}")

if __name__ == "__main__":
    # Simulação de uso
    clean_data("vendas_brutas.csv")
