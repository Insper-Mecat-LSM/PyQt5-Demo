from PyQt5 import QtCore, QtGui, QtWidgets
from serial.tools import list_ports
import serial
from time import sleep

# Identificação das portas COM do Computador

serial_ports = list_ports.comports()

for port, desc, _ in sorted(serial_ports):

    print("{}: {}\n".format(port, desc))

# Definição da Porta referente a Placa Nucleo

Porta = "COM10" # Definir a porta para aquela conectada a Nucleo

# Cada computador terá uma porta COM diferente conectada de acordo com a quantidade de dispositivos que utilizam de tais portas

Porta = serial.Serial(Porta, 115200) # Criação do canal de comunicação com determinado baud rate

# Classe Principal de UI

class Ui_Widget(object):

    # Setup das Widgets a serem Utilizadas

    def setupUi(self, Widget):

        # Configuração da Janela de Exibição

        Widget.setObjectName("Widget") # Nomenclatura da Variável
        Widget.resize(600, 250) # Variação do Tamanho da Janela

        # Criação do Primeiro Texto

        self.Teste1 = QtWidgets.QLabel(Widget) # Criação de um Widget do tipo "Label"
        self.Teste1.setObjectName("Teste1") # Nomenclatura da Variável
        self.Teste1.setGeometry(QtCore.QRect(150, 50, 100, 40)) # Posicionamento na tela e tamanho do texto

        font = QtGui.QFont() # Criação de fonte
        font.setFamily("Segoe UI Variable Small Semibol") # Tipo de fonte utilizada
        font.setPointSize(10) # Tamanho de fonte
        font.setBold(True) # Habilitação de Negrito
        self.Teste1.setFont(font) # Associar fonte ao texto desejado

        # Criação do Botão

        self.BotaoLed = QtWidgets.QPushButton(Widget) # Criação de um Widget do tipo "Push Button"
        self.BotaoLed.setObjectName("BotaoLED") # Nomenclatura da Variável
        self.BotaoLed.setGeometry(QtCore.QRect(300, 50, 200, 40)) # Posicionamento na tela e tamanho do botão
        self.BotaoLed.clicked.connect(self.LED) # Função é executada quando botão é clicado

        # Criação do Slider

        self.Brilho = QtWidgets.QSlider(Widget) # Criação de um Widget do tipo "Slider"
        self.Brilho.setObjectName("Brilho") # Nomenclatura da Variável
        self.Brilho.setGeometry(QtCore.QRect(300, 150, 200, 40)) # Posicionamento na tela e tamanho do potênciometro
        self.Brilho.setOrientation(QtCore.Qt.Horizontal) # Orientação do potênciometro como sendo horizontal
        self.Brilho.valueChanged.connect(self.Poder) # Função é executada quando o valor do potênciometro mudar

        # Criação do Segundo Texto

        self.Teste2 = QtWidgets.QLabel(Widget) # Criação de um Widget do tipo "Label"
        self.Teste2.setObjectName("Teste2") # Nomenclatura da Variável
        self.Teste2.setGeometry(QtCore.QRect(142, 150, 120, 40)) # Posicionamento na tela e tamanho do texto
        self.Teste2.setFont(font) # Associar fonte ao texto desejado

        # Função de tradução dos textos

        self.retranslateUi(Widget)

        # Exibição dos Widgets

        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):

        # Renomeação dos botões, textos e titulos de janela

        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Teste - PyQt5"))
        self.BotaoLed.setText(_translate("Widget", "Mudar LED"))
        self.Teste1.setText(_translate("Widget", "Teste - LED"))
        self.Teste2.setText(_translate("Widget", "Teste - Brilho"))
    
    # Função que envia informação via Serial para ligar / desligar o LED interno da placa

    def LED(self):

        Porta.write(bytes("Troca\n", "utf-8"))

    # Função que envia informação via Serial para controlar o brilho de LED 

    def Poder(self, value):

        Porta.write(bytes(str(value) + "\n", "utf-8"))

# Geração da UI como uma devida janela de computador
        
if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())

