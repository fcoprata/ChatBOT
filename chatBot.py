from selenium import webdriver
import time

class ChatBot:
    def __init__(self):
        self.mensagem = "Bom dia"
        self.grupos = ["Thiago Viana"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', chrome_options=options)
        print("Chrome Browser Invoked successfully")
        
    def Enviar(self):
        
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(30)
        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(3)
            grupo.click()
            chatbox = self.driver.find_element_by_class_name('p3_M1')
            time.sleep(3)
            chatbox.click()
            chatbox.send_keys(self.mensagem)
            botao = self.driver.find_element_by_xpath('//span[@data-icon="send"]')
            time.sleep(3)
            botao.click()
            time.sleep(5)

bot = ChatBot()
bot.Enviar()
  