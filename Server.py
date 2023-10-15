from socket import *
import threading
import random

# Funktionen til at tilkoble vores klient
def handleClient(connectionSocket, address):
    while True:
        data = connectionSocket.recv(1024) # Socket prøver at modtage data(op til 1024 bytes)
        message = data.decode()  # UFT = Unicode transformation format. 8 betyder at beskeden er encodet i 8-bit. Decode når man modtager 
        message = message.strip().lower()  # Fjerner mellemrum og konverter til små bogstaver

        
        if message.lower() == ('exit'):
            print("Connection has been terminated")
            connectionSocket.close()
            break

        print("Received message from client:", message)

        # Udfør en beregning baseret på den modtagne besked
        result = 0
        operation_list = message.split()  # Deler beskeden op (operand og operator)
        oprnd1 = operation_list[0]  # Første operand
        operation = operation_list[1]  # Operator
        oprnd2 = operation_list[2]  # Anden operand

        num1 = int(oprnd1)  # Konverter første operand til heltal
        num2 = int(oprnd2)  # Konverter anden operand til heltal

        # Udfør beregningen fra den data vi har fået(operator)
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "/":
            result = num1 / num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "random":
            result = random.randint(num1,num2)

        # Sender resultatet tilbage
        output = str(result)
        connectionSocket.send(output.encode())  # encode når man sender

    connectionSocket.close()

# Serverkonfiguration
serverName = "127.0.0.1"  # Localhost IP-adresse
serverPort = 12000  # Port
serverSocket = socket(AF_INET, SOCK_STREAM)  # AF_INET = IPv4. SOCK_STREAM = en TCP-socket
serverSocket.bind((serverName, serverPort))  
serverSocket.listen(5)  # Leder efter maksimal clients
print('Server is running and listening')


while True:
    connectionSocket, addr = serverSocket.accept()  # Accepter forbindelser
    threading.Thread(target=handleClient, args=(connectionSocket, addr)).start()  # Starter en ny thread til at håndtere klienten