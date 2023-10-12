from socket import *

# Serverkonfiguration
serverName = "127.0.0.1"  # Localhost IP-adresse
serverPort = 12000  # Port
client = socket(AF_INET, SOCK_STREAM)  # AF_INET = IPv4. SOCK_STREAM = en TCP-socket
client.connect((serverName, serverPort))  # Opret forbindelse til serveren

# Velkomstbesked
print("Welcome to my calculator")
print(" ")

while True:
    oprnd1 = input("Enter a number: ")
    operation = input("Enter operation (+, -, *, /, random): ")
    oprnd2 = input("Enter a second number: ")

    # behandler input data til en samlet string
    inp = f"{oprnd1} {operation} {oprnd2}"

    # Sender data input til serveren
    client.send(inp.encode())  # Sendes via bytes til serveren. encode når man sender

    # Viser resultatet fra serveren
    answer = client.recv(1024)  # prøver at modtage data(op til 1024 bytes)
    print(f'Answer is ' + answer.decode())  # Decode, når man sender. Udskriver dataen som en string

    
    exit_choice = input("Type 'Exit' to terminate or press Enter to continue: ")
    if exit_choice == ("Exit") or ("exit"):
        break


client.close()