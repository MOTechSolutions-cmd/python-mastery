import re
from datetime import datetime

def monitor_logs(log_file):
    print(f"--- Iniciando Monitoramento de Logs: {datetime.now()} ---")
    
    # Regex Sênior para capturar erros críticos
    error_pattern = re.compile(r"ERROR|CRITICAL|FAIL")
    
    try:
        with open(log_file, 'r') as file:
            logs = file.readlines()
            
        error_count = 0
        for line in logs:
            if error_pattern.search(line):
                print(f"⚠️ Alerta detectado: {line.strip()}")
                error_count += 1
        
        print(f"\nResumo: {error_count} erros encontrados.")
        
    except FileNotFoundError:
        print("Arquivo de log não encontrado.")

if __name__ == "__main__":
    monitor_logs("server.log")
