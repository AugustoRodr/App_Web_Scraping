from selenium import webdriver #
from selenium.webdriver.support.wait import WebDriverWait #hasta que no cargue la pagina por completo no vamos a regresar ninguna operacion
from selenium.webdriver.support import expected_conditions as EC # condiciones que cumplir para ejecuar cierta accion
from selenium.webdriver.common.by import By
import pandas as pd

#opcinoes de navegacion
opciones= webdriver.ChromeOptions()
opciones.add_argument('--start-maximized')
opciones.add_argument('--disable-extensions')
driver_path='C:\\Users\\augus\\Downloads\\chromedriver_win32\\chromedriver.exe'
driver=webdriver.Chrome(driver_path,chrome_options=opciones)
#driver=webdriver.Chrome(driver_path)


#inicializamos el navegador
driver.get('https://google.com')

WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CLASS_NAME,'gLFyf'))).send_keys('Tabla de posiciones')

WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CLASS_NAME,'gNO89b'))).click()

WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CLASS_NAME,'LC20lb MBeuO DKV0Md'.replace(' ','.')))).click()

WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]')))


equipos= driver.find_element(By.CLASS_NAME,'Table__TBODY')
equipos=equipos.text

solo_equipos=[i for i in equipos.split('\n') if not i.isdigit()]

puntajes= driver.find_element(by=By.CLASS_NAME,value='Table__Scroller').text
puntajes= puntajes.split('\n')[1:]

p_jugados,p_ganados,p_empatados,p_perdidos,g_favor,g_contra,diferencia,puntos=[],[],[],[],[],[],[],[]


for i in range(0,len(puntajes),8):
    p_jugados.append(puntajes[i])
    p_ganados.append(puntajes[i+1])
    p_empatados.append(puntajes[i+2])
    p_perdidos.append(puntajes[i+3])
    g_favor.append(puntajes[i+4])
    g_contra.append(puntajes[i+5])
    diferencia.append(puntajes[i+6])
    puntos.append(puntajes[i+7])


#print(equipos)

#print(p_jugados,p_ganados,p_empatados,p_perdidos,g_favor,g_contra,diferencia,puntos)

df=pd.DataFrame({'Equipos':solo_equipos,
                'Partidos_jugados':p_jugados,
                'Partidos_ganados':p_ganados,
                'Partidos_empatados':p_empatados,
                'Partidos_perdidos':p_perdidos,
                'Goles_a_favor':g_favor,
                'Goles_en_contra':g_contra,
                'Diferencia':diferencia,
                'Puntos':puntos})


print(df)

df.to_csv('resultado_scraping.csv',index=False)


driver.quit()