# banco_test_cm3panel

## Preparazione della microSD

Partendo dalla [microSD standard per CM3-Panel](https://www.acmesystems.it/CM3-PANEL_microsd): 

Configurare il login su video senza richiesta di password:

	sudo raspi.config

	Boot Options -> Desktop /CLI -> Console Autologin

Installare __evdev__ per il test del touch

	sudo apt-get install python-pip
	sudo pip install evdev
