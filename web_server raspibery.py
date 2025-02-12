        
import network
import socket
import time

from machine import Pin

led = Pin(15, Pin.OUT)

ssid = 'aa'
password = 'acetona0'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

html = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Termostato</title>
    
    <style>
        @import url(https://fonts.googleapis.com/css?family=Open+Sans:700,300);

        body {
            background: #191c1c;
        }

        .frame {
            position: absolute;
            top: 50%;
            left: 50%;
            width: 400px;
            height: 400px;
            margin-top: -200px;
            margin-left: -200px;
            border-radius: 2px;
            background: #191c1c;
            box-shadow: 1px 2px 10px 0px rgba(0,0,0,0);
            color: #333;
            overflow: hidden;
            font-family: 'Open Sans', Helvetica, sans-serif;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }

        .frame h4 {
            color: #82adad;
            text-align: center;
            padding: 10px 0;
        }

        .center {
            position: absolute;
            top: 55%;
            left: 50%;
            transform: translate(-50%,-50%);
        }

        .thermo-bg:before {
            content: " ";
            position: absolute;
            width: 250px;
            height: 250px;
            top: 50%;
            left: 50%;
            transform: translate(-50%,-50%);
            background: linear-gradient(to bottom, #c1c1c1, #d6d6d6, #d6d6d6, #d6d6d6);
            border-radius: 50%;
            box-shadow: inset -3px 2px 3px 0 rgba(0,0,0,.2);
        }

        .thermo-bg:after {
            content: " ";
            position: absolute;
            width: 230px;
            height: 230px;
            top: 50%;
            left: 50%;
            transform: translate(-50%,-50%);
            background: linear-gradient(-90deg, hotpink, #148f93);
            border-radius: 50%;
            box-shadow: inset 2px 4px 4px 0 rgba(0,0,0,.4);
        }

        .thermo-border {
            content: " ";
            position: absolute;
            width: 232px;
            height: 232px;
            top: 50%;
            left: 50%;
            transform: translate(-50%,-50%);
            border-radius: 50%;
            border: 50px solid;
            box-sizing: border-box;
            border-color: transparent transparent #d6d6d6 transparent;
        }

        .thermo-center {
            content: " ";
            position: absolute;
            width: 180px;
            height: 180px;
            top: 50%;
            left: 50%;
            transform: translate(-50%,-50%);
            background: #d6d6d6;
            border-radius: 50%;
            box-shadow: 1px 2px 3px rgba(0,0,0,.3);
        }

        .cold {
            position: absolute;
            width: 30px;
            height: 30px;
            background: none;
            top: 50%;
            left: 50%;
            transform: translate(-325%, 170%);
            cursor: pointer;
        }

        button {
            border: none;
            background: none;
            outline: none;
        }

        .cold button, .hot button {
            border: none;
            outline: none;
            background: none;
            cursor: pointer;
        }

        .hot {
            position: absolute;
            width: 30px;
            height: 30px;
            background: none;
            top: 50%;
            left: 50%;
            transform: translate(220%, 170%);
            cursor: pointer;
        }

        .screen {
            position: absolute;
            width: 80px;
            height: 40px;
            border-radius: 10px;
            background: #6b6b6b;
            box-shadow: inset 2px 2px 4px 0 rgba(0,0,0,.3);
            top: 50%;
            left: 50%;
            transform: translate(-48%, -80%);
        }

        #result {
            color: #47ffea;
            text-shadow: 0 0 4px #1bbe9e;
            text-align: center;
            margin-top: 3px;
            font-size: 30px;
        }

        .hot-active {
            z-index: 999999;
            fill: #ff4a74;
        }

        .cold-active {
            z-index: 999999;
            fill: #4aabff;
        }

        .place p {
            position: absolute;
            width: 30px;
            height: 30px;
            font-size: 15px;
            font-weight: 700;
            background: transparent;
            color: #6b6b6b;
            top: 50%;
            left: 50%;
            transform: translate(-125.5%, 50%);
            text-transform: uppercase;
            text-shadow: 0 0 1px gray;
            transition: color .4s ease-in-out;
        }

        .fahrenheit {
            position: absolute;
            width: 30px;
            height: 30px;
            font-size: 10px;
            background: transparent;
            color: red;
            top: 50%;
            left: 50%;
            transform: translate(70%, -30%);
            text-transform: uppercase;
            color: #47ffea;
            text-shadow: 0 0 4px #1bbe9e;
        }

        .content {
            width: 400px;
            height: 400px;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            padding: 50%;
        }

        #bed {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -330%);
            width: 20px;
            height: 20px;
            visibility: hidden;
            transition: all .8s ease-in-out;
        }

        .content:hover #bed, .content:hover .place p {
            visibility: visible;
            text-shadow: 0 0 3px #6b6b6b;
            color: #47ffea;
        }

        .content:hover #bed {
            transform: translate(-50%, -260%);
        }
    </style>
</head>
<body>
    <div class="frame">
        <h4>Clique na floco de neve ou chama</h4>

        <div class="center">
            <div class="thermo-bg"></div>
            <div class="thermo-bg-color"></div>
            <div class="thermo-border"></div>
            <div class="thermo-center"></div>

            <div class="content">
                <button id="cold" onclick="down()">
                    <div class="cold">
                        <svg width="15px" viewBox="0 0 448 512">
                            <path fill="#d6d6d6" d="M440.3 345.2l-33.8-19.5 26-7c8.2-2.2 13.1-10.7 10.9-18.9l-4-14.9c-2.2-8.2-10.7-13.1-18.9-10.9l-70.8 19-63.9-37 63.8-36.9 70.8 19c8.2 2.2 16.7-2.7 18.9-10.9l4-14.9c2.2-8.2-2.7-16.7-10.9-18.9l-26-7 33.8-19.5c7.4-4.3 9.9-13.7 5.7-21.1L430.4 119c-4.3-7.4-13.7-9.9-21.1-5.7l-33.8 19.5 7-26c2.2-8.2-2.7-16.7-10.9-18.9l-14.9-4c-8.2-2.2-16.7 2.7-18.9 10.9l-19 70.8-62.8 36.2v-77.5l53.7-53.7c6.2-6.2 6.2-16.4 0-22.6l-11.3-11.3c-6.2-6.2-16.4-6.2-22.6 0L256 56.4V16c0-8.8-7.2-16-16-16h-32c-8.8 0-16 7.2-16 16v40.4l-19.7-19.7c-6.2-6.2-16.4-6.2-22.6 0L138.3 48c-6.3 6.2-6.3 16.4 0 22.6l53.7 53.7v77.5l-62.8-36.2-19-70.8c-2.2-8.2-10.7-13.1-18.9-10.9l-14.9 4c-8.2 2.2-13.1 10.7-10.9 18.9l7 26-33.8-19.5c-7.4-4.3-16.8-1.7-21.1 5.7L2.1 145.7c-4.3 7.4-1.7 16.8 5.7 21.1l33.8 19.5-26 7c-8.3 2.2-13.2 10.7-11 19l4 14.9c2.2 8.2 10.7 13.1 18.9 10.9l70.8-19 63.8 36.9-63.8 36.9-70.8-19c-8.2-2.2-16.7 2.7-18.9 10.9l-4 14.9c-2.2 8.3 2.7 16.8 10.9 18.9l26 7-33.8 19.5c-7.4 4.3-9.9 13.7-5.7 21.1L17.6 393c4.3 7.4 13.7 9.9 21.1 5.7l33.8-19.5-7 26c-2.2 8.2 2.7 16.7 10.9 18.9l14.9 4c8.2 2.2 16.7-2.7 18.9-10.9l19-70.8 62.8-36.2v77.5l-53.7 53.7c-6.2 6.2-6.2 16.4 0 22.6l11.3 11.3c6.2 6.2 16.4 6.2 22.6 0l53.7-53.7v-77.5l62.8 36.2 19 70.8c2.2 8.2 10.7 13.1 18.9 10.9l14.9-4c8.2-2.2 13.1-10.7 10.9-18.9l-7-26 33.8 19.5c7.4 4.3 16.8 1.7 21.1-5.7L430.4 119c4.3-7.4 1.7-16.8-5.7-21.1z"/>
                        </svg>
                    </div>
                </button>

                <div class="screen">
                    <div id="result">23</div>
                </div>
                <button id="hot" onclick="up()">
                    <div class="hot">
                        <svg width="15px" viewBox="0 0 512 512">
                            <path fill="#d6d6d6" d="M256 0C114.6 0 0 114.6 0 256s114.6 256 256 256 256-114.6 256-256S397.4 0 256 0zM185.8 180.3C178.4 183.8 170 185.7 162 187.1c-3.4 7.1-6 14.6-8 22.2-7.2 20.7 1.4 42.8 20.7 53.7 11.8 7.6 27.6 7.7 40.8 2 10.5-3.8 21.6-10.1 29.6-18.4 15.2-15.5 25.2-34.5 30.6-55.3 5.5-21.2 5.2-43.8-1.4-64.6-5.5-18.2-17.2-32.3-31.6-41.5-13.4-8.6-29.4-14.2-45.4-15.5-12.6-1-25.3-.2-37.3 4.1 18.7-4.8 39.4-3.4 58.4 7.4 16.7 5.9 30.1 17.9 37.5 33.5 6.3 12.5 11.5 25.6 14.5 39.2 3.3 13.7 5.6 28.4 6.8 43.2 1.2 14.8.4 29.9-4.4 44.2-11.5 37.3-43.5 65.3-81.6 71.6-5.3 1-10.6 2.1-16.3 2.1-2.9 0-5.8-.1-8.6-.4z"/>
                        </svg>
                    </div>
                </button>

                <div class="fahrenheit">°C</div>
            </div>
        </div>
    </div>

    <script>
        var cold = document.getElementById("cold");
        var hot = document.getElementById("hot");
        var btnCold = document.getElementById("btn-cold");
        var btnHot = document.getElementById("btn-hot");
        var result = document.getElementById("result");
        var score = 23; // Valor inicial da temperatura
        var timeout; // Variável que irá armazenar o temporizador de inatividade

        function sendTemperature() {
            console.log("Enviando temperatura: " + score); // Exibe a temperatura no console antes de enviar

            fetch('http://127.0.0.1:5000/temperatura-manual', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    temperatura: score,
                    ie_manual: true
                })
            })
            .then(response => response.json())
            .then(data => console.log("Resposta do endpoint:", data))
            .catch(error => console.error("Erro na chamada ao endpoint:", error));
        }

        function up() {
            if (score < 30) {
                score++; 
            }
            result.innerHTML = score;
            resetInactivityTimer(); 
        }

        function down() {
            if (score > 18) { 
                score--;
            }
            result.innerHTML = score;
            resetInactivityTimer(); 
        }

        cold.addEventListener('mouseover', function() {
            btnCold.classList.add('cold-active');
            resetInactivityTimer();
        });

        cold.addEventListener('mouseout', function() {
            btnCold.classList.remove('cold-active');
        });

        hot.addEventListener('mouseover', function() {
            btnHot.classList.add('hot-active');
            resetInactivityTimer();
        });

        hot.addEventListener('mouseout', function() {
            btnHot.classList.remove('hot-active');
        });

        function resetInactivityTimer() {
            clearTimeout(timeout);
            timeout = setTimeout(sendTemperature, 1000);
        }

        resetInactivityTimer();
    </script>
</body>
</html>
"""

max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)

if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )

addr = socket.getaddrinfo('0.0.0.0', 5500)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)

# Listen for connections
while True:
    try:
        cl, addr = s.accept()
        print('client connected from', addr)
        request = cl.recv(1024)
        print(request)

        request = str(request)
        led_on = request.find('/light/on')
        led_off = request.find('/light/off')
        print( 'led on = ' + str(led_on))
        print( 'led off = ' + str(led_off))

        if led_on == 6:
            print("led on")
            led.value(1)
            stateis = "LED is ON"

        if led_off == 6:
            print("led off")
            led.value(0)
            stateis = "LED is OFF"

        response = html % stateis

        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(response)
        cl.close()

    except OSError as e:
        cl.close()
        print('connection closed')