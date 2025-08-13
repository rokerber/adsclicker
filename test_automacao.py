import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import logging

# Configuração de logs
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Iniciando o script auto_clicker...")

# Configura as opções do Chrome para rodar sem interface gráfica (headless)
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920,1080")

try:
    # Instala e configura o ChromeDriver automaticamente
    logging.info("Configurando o ChromeDriver...")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    logging.info("ChromeDriver configurado com sucesso.")

    # Abre a página
    driver.get("https://unitconverter.sp1.br.saveincloud.net.br/")
    logging.info(f"Página carregada: {driver.title}")

    # Exemplo de interação
    time.sleep(5)

except Exception as e:
    logging.error(f"Ocorreu um erro: {e}")

finally:
    # Fecha o navegador
    if 'driver' in locals():
        driver.quit()
        logging.info("Navegador fechado. Script finalizado.")
