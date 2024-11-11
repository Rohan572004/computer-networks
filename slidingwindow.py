import random
import time

class SlidingWindowProtocol:
    def __init__(self, window_size, total_packets):
        self.window_size = window_size
        self.total_packets = total_packets
        self.sent_packets = []
        self.acknowledged = []

    def send_packets(self):
        """Simulate sending packets."""
        for i in range(self.total_packets):
            self.sent_packets.append(i)
            print(f"Sent packet: {i}")
            time.sleep(0.5)  # Simulate network delay

    def receive_acknowledgments(self):
        """Simulate receiving acknowledgments."""
        for i in range(self.total_packets):
            if random.random() < 0.8:  # Simulate 80% chance of successful acknowledgment
                self.acknowledged.append(i)
                print(f"Acknowledged packet: {i}")
            else:
                print(f"Packet {i} lost, not acknowledged.")
            time.sleep(0.5)  # Simulate network delay

    def go_back_n(self):
        """Simulate Go-Back-N protocol."""
        self.send_packets()
        self.receive_acknowledgments()

        # Go back to the last acknowledged packet
        last_ack = -1
        for i in range(self.total_packets):
            if i in self.acknowledged:
                last_ack = i
            else:
                print(f"Go-Back-N: Resending packets from {last_ack + 1} to {i}")
                for j in range(last_ack + 1, i + 1):
                    print(f"Resent packet: {j}")
                break

    def selective_repeat(self):
        """Simulate Selective Repeat protocol."""
        self.send_packets()
        self.receive_acknowledgments()

        # Resend only the lost packets
        lost_packets = set(range(self.total_packets)) - set(self.acknowledged)
        if lost_packets:
            print(f"Selective Repeat: Resending lost packets: {lost_packets}")
            for packet in lost_packets:
                print(f"Resent packet: {packet}")

if __name__ == "__main__":
    window_size = int(input("Enter the window size: "))
    total_packets = int(input("Enter the total number of packets: "))

    protocol = SlidingWindowProtocol(window_size, total_packets)

    print("\n--- Go-Back-N Protocol Simulation ---")
    protocol.go_back_n()

    print("\n--- Selective Repeat Protocol Simulation ---")
    protocol.selective_repeat()