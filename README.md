# PyQt5-Demo

Código Demo para compreender funcionamento da biblioteca PyQt5 em conjunto com a Placa de Desenvolvimento Rápido Núcleo

O código em Python gera uma interface interativa simplificada de forma a compreender como realizar a transmissão de informações via Serial e construir Widgets utilizando da biblioteca PyQt5. Ambos os códigos presentes neste arquivo funcionam em conjunto: enquanto o usuário interage na UI, a placa Nucleo recebe informações via Serial (cabo USB) e realiza ações conforme tais informações.

Para o devido funcionamento deste conjunto, é necessário atentar às seguintes ações:

  1. Realizar a inspeção de portas COM do computador e definir qual porta COM está conectada à Placa Nucleo;
  2. A Placa Nucleo a ser utilizada deve ser a STM32F401RE;
  3. É preciso conectar um LED na porta D9 da placa, esta que possui saída PWM que servirá para controlar o brilho do LED;
  4. O Código .bin deve ser alocado diretamente na placa no seu Explorador de Arquivos
