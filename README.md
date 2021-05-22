# MicroPython-Socket-programming

### Prerequisites
* Knowledge on how to work with MicroPython on ESP32 or any other Micropython compitable development board.
* Comfortable with soldering on PCB board.
* Basic knowledge in arduino programming.
* Basic knowledge in python programming.

### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/rakesh-i/MicroPython-Socket-programming
   ```
2. Install MicroPyhon on ESP32
   
    Follow this [link](https://randomnerdtutorials.com/flashing-micropython-firmware-esptool-py-esp32-esp8266/) to flash MicroPython on ESP32.
3. Copying files to ESP32
    
    * Connect ESP32 to yoru PC, check on which com port esp32 is connected by going to device manager in Windows.. Open CMD terminal in ESP32 folder, which is in downloaded repo. Execute the followng command to connect to esp32.(repalce X with port number eg: COM5, COM9) 
        ```sh
        rshell --port COMX
        ``` 
    * Copy files to esp32 one by one.
    (Remember to go through server.py and web.py to add wifi credentials and ip addresses. And PLEASE READ "wireless-setup.txt" how to do so. )
        ```sh
        cp boot.py /pyboard
        cp main.py /pyboard
        cp server.py /pyboard
        cp web.py /pyboard
        ```
    * If you done every thing right till now, when you press EN button on esp32, you should see onboard led of esp32 lightup for 5 seconds notifying it is connected to the wifi.
    * You can type 
        ```sh
        repl
        ```
        to open esp32 serial monitor. If you see connection successful message then you are good-to-go.
    * Now esp32 is wating for connection from client. Run client.py, which is in Client folder. If you see "Got connection from: 111.111.111.111, 11111" message then you have successfully established a tcp connection between your PC and ESP32.

###Extra
* Use send command files to send commands to esp32, which can be helpful for creating other projects.
