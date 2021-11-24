import csv
from bs4 import BeautifulSoup
from fastapi import FastAPI

app = FastAPI()

productos = []

@app.get('/')
def Home():
    return{"bienvenido:"" aun no tengo serializador"}


@app.get('/productos')
def ver_productos():
    return productos

@app.post('/productos')
def crear_productos(int):
    return productos

@app.delete('/productos/{id}')
def eliminar_productos(int):
    return productos

@app.put('/productos/{id}')
def editar_productos(int):
    return productos

#from selenium import webdriver
#from webdriver_manager.firefox import GeckoDriverManager

#driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#url = "https://www.amazon.com/-/es/s?k=rtx+2060+12gb&i=computers&rh=n%3A284822&page=3&language=es&__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1636608076&ref=sr_pg_1"
#driver.get(url)
