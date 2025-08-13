import time
import random
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuração de logs
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def iniciar_automacao():
    """
    Função principal que inicia o loop de automação.
    """
    logging.info("Iniciando o loop de automação...")

    # Configura as opções do Chrome para rodar sem interface gráfica (headless)
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = None
    iteracoes_concluidas = 0

    try:
        # Instala e configura o ChromeDriver automaticamente
        logging.info("Configurando o ChromeDriver...")
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        logging.info("ChromeDriver configurado com sucesso.")

        # O loop principal. Defina 'True' para rodar infinitamente ou um número para rodar um número de vezes.
        while True:
            iteracoes_concluidas += 1
            logging.info(f"--------------------------------------------------")
            logging.info(f"Iniciando a iteração número: {iteracoes_concluidas}")
            
            url = "https://unitconverter.sp1.br.saveincloud.net.br/"
            
            try:
                # Acessa a página
                driver.get(url)
                logging.info(f"Página acessada: {url}")
                
                # Espera até que pelo menos um elemento clicável esteja presente na página.
                # A espera é de no máximo 10 segundos. Se nada for encontrado, irá gerar um TimeOutException.
                logging.info("Aguardando elementos clicáveis...")
                wait = WebDriverWait(driver, 10)
                wait.until(EC.presence_of_element_located((By.XPATH, "//*[self::a or self::button]")))
                
                # Simula um clique aleatório
                logging.info("Simulando um clique aleatório...")
                
                # Procura por links ('a') OU botões ('button') na página
                elements = driver.find_elements(By.XPATH, "//*[self::a or self::button]")
                
                if elements:
                    random_element = random.choice(elements)
                    random_element.click()
                    logging.info(f"Clicou no elemento: {random_element.text or 'Sem texto'}")
                else:
                    # Este bloco será executado se a espera falhar (o que é improvável com o WebDriverWait)
                    logging.warning("Nenhum elemento clicável (link ou botão) encontrado para clicar.")

                # Tempo de espera aleatório entre 150 e 200 segundos
                tempo_de_espera = random.randint(150, 200)
                logging.info(f"Aguardando {tempo_de_espera} segundos para a próxima iteração...")
                time.sleep(tempo_de_espera)

            except Exception as e:
                logging.error(f"Ocorreu um erro na iteração {iteracoes_concluidas}: {e}")
                logging.info("Tentando reiniciar o processo...")
                # Opcional: Adicionar uma pausa curta antes de reiniciar
                time.sleep(5) 
                
    except KeyboardInterrupt:
        logging.info("Processo encerrado pelo utilizador (KeyboardInterrupt).")
    except Exception as e:
        logging.error(f"Ocorreu um erro fatal: {e}")
    finally:
        if driver:
            driver.quit()
            logging.info("Fechando o navegador...")
            logging.info("Processo finalizado.")
            logging.info("--------------------------------------------------")

if __name__ == "__main__":
    iniciar_automacao()
