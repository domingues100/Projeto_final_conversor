#Projeto Final - Gabriel Montagni Domingues Filho
import gi
import pandas 
import requests
from bs4 import BeautifulSoup as bp
import re
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from os.path import abspath, dirname, join

class TheApp:

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file('combo_ex.glade')
        self.window = self.builder.get_object('window')
        self.liststore = Gtk.ListStore(str, str)

        colors = [
            ['#ID:1', 'Pressão'],
            ['#ID:2', 'Massa'],
             ['#ID:3', 'Moedas']]

        for color in colors:
            self.liststore.append(color)

        self.combo = self.builder.get_object('combo')
        self.combo.set_model(self.liststore)
        renderer_text = Gtk.CellRendererText()
        self.combo.pack_start(renderer_text, True)
        self.combo.add_attribute(renderer_text, "text", 1)
        self.combo.set_active(0)
        self.builder.connect_signals(self)

        colors2 = [
            ['#ID:1', 'Atmosfera'],
            ['#ID:2', 'Bar'],
            ['#ID:2', 'Pascal'],
            ['#ID:2', 'Psi'],
            ['#ID:2', 'Torr'],
            ]   

        constructor(self, colors2)

    def on_window_destroy(self, widget):
        Gtk.main_quit()

    def on_combo_changed(self, widget):
        model = widget.get_model()
        active = widget.get_active()
        global id
        id = active

        if id == 1 :
            colors2 = [['#ID:1', 'Quilograma'], ['#ID:2', 'Tonelada Métrica'], ['#ID:3', 'Grama'], ['#ID:4', 'Miligrama'],
                ['#ID:5', 'Micrograma'], ['#ID:6', 'Tonelada de Deslocamento'], ['#ID:7', 'Tonelada Curta'], ['#ID:8', 'Stone'],
                ['#ID:9', 'Libra'], ['#ID:10', 'Onça']]   

            constructor(self, colors2)

        elif id == 2: 
            colors2 = [['#ID:1', 'Real'], ['#ID:2', 'Dólar'], ['#ID:3', 'Euro'], ['#ID:4', 'Pesos Argentinos'],
                ['#ID:5', 'Dólar Canadense'], ['#ID:6', 'Yuan'], ['#ID:7', 'Iene']]   

            constructor(self, colors2)

        else:
            colors2 = [
                ['#ID:1', 'Atmosfera'], ['#ID:2', 'Bar'], ['#ID:2', 'Pascal'],
                ['#ID:2', 'Psi'], ['#ID:2', 'Torr']]    

            constructor(self, colors2) 

    def on_entrada_changed(self, widget): #função que quando a entrada muda faz a conversão em tempo real, pega os ids de cada elemento e olha na tabela de cada grandeza (ID)
        entrada = self.builder.get_object('entry1')
        try:
            entry = int(entrada.get_text())
        except:
            entry = 0
            pass

        id_entrada = int(self.combo1.get_active())
        id_saida = int(self.combo2.get_active()) 

        if id == 1:
            list = [1, 0.001, 1000, 1000000, 1000000000, 0.000984207, 0.00110231183999997618, 
            0.15747311999999660803, 2.204623679999952568, 35.273978879999241087]
            convert(self,list, id_entrada, id_saida, entry)
        elif id == 2:
            df = pandas.read_csv(f"df{id}.csv")
            fator_conversão = float(df[f'{id_entrada}'].iloc[id_saida])
            saida = self.builder.get_object('saida1')
            texto = saida.set_text(str(fator_conversão*entry))
            label = self.builder.get_object('label_saida')
            texto = label.set_text(f"Multiplique a entrada por {fator_conversão} para obter a saída")
        else:
            list = [1, 1.01325, 101325, 14.696, 760]
            convert(self,list, id_entrada, id_saida, entry)

    def on_click(self,button):
        links = []; lst = []; moeda = []; lista_nova=[]; lista_df = []; i=0
        moeda.append("1")
        with open("links.dat") as file:
            for line in file:
                lst=line.split()
                links.append(lst[1])

        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

        while len(moeda) != 7:
            page = requests.get(f"{links[i]}", headers= headers)
            soup = bp(page.content,'html.parser')
            moedas = soup.find("span", class_= "DFlfde SwHCTb")
            moeda.append(moedas.text)
            i+=1

        for i in range(len(moeda)):
            valor = float(moeda[i].replace(',', '.'))
            for i in range(len(moeda)):
                valor_novo = float(moeda[i].replace(',', '.'))
                lista_nova.append(valor_novo/valor)
            lista_df.append([*lista_nova])
            lista_nova.clear()
            df = pandas.DataFrame(lista_df)
            df = (pandas.DataFrame(df)).to_csv("df2.csv")

def convert(self,list, id_saida,  id_entrada, entry): #converter os valores das listas em uma tabela pare pegar o fator que da match com os ids de entrada e saida
    lista_nova =[]
    lista_df = []
    for i in range(len(list)):
        valor = list[i]
        for i in range(len(list)):
            valor_novo = float(list[i])
            lista_nova.append(valor_novo/valor)
        lista_df.append([*lista_nova])
        lista_nova.clear()
    df = (pandas.DataFrame(lista_df)).to_csv(f"df{id}.csv")
    df = pandas.read_csv(f"df{id}.csv")
    fator_conversão = float(df[f'{id_entrada}'].iloc[id_saida])
    saida = self.builder.get_object('saida1')
    texto = saida.set_text(str(fator_conversão*entry))
    label = self.builder.get_object('label_saida')
    texto = label.set_text(f"Multiplique a entrada por {fator_conversão} para obter a saída")
    return texto

def constructor(self, colors2): #constructor de combo
    self.liststore2 = Gtk.ListStore(str, str)

    for color in colors2:
        self.liststore2.append(color)

    #bloco da entrada
    self.combo1 = self.builder.get_object('combo1').clear() #não deixar duplicar
    self.combo1 = self.builder.get_object('combo1')
    self.combo1.set_model(self.liststore2)
    renderer_text = Gtk.CellRendererText()
    self.combo1.pack_start(renderer_text, True)
    self.combo1.add_attribute(renderer_text, "text", 1)
    self.combo1.set_active(0)
    self.builder.connect_signals(self)
    self.window.show()

    #bloco da saida
    self.combo2 = self.builder.get_object('combo2').clear() #não deixar duplicar
    self.combo2 = self.builder.get_object('combo2')
    self.combo2.set_model(self.liststore2)
    renderer_text = Gtk.CellRendererText()
    self.combo2.pack_start(renderer_text, True)
    self.combo2.add_attribute(renderer_text, "text", 1)        
    self.combo2.set_active(0)
    self.builder.connect_signals(self)
    self.window.show()  

if __name__ == '__main__':
    try:
        gui = TheApp()
        Gtk.main()

    except KeyboardInterrupt:
        pass