import threading 
import time 
import random 

class Process(threading.Thread):
    def __init__(self, process_id, processes):
        super().__init__()
        self.process_id = process_id
        self.processes = processes
        self.is_leader = False 
        self.alive = True 
        self.election_event = threading.Event()
        self.coordinator_event = threading.Event()
    
    def run(self):
        while self.alive:
            if not self.is_leader:
                time.sleep(random.uniform(0.5, 2.0))
            else:
                print(f"Process {self.process_id} is the leader ")
                time.sleep(2)
                
    def start_election(self):
        print(f"process {self.process_id} is starting an election")
        higher_processes = [p for p in self.processes if p.process_id > self.process_id and p.alive]
        if not higher_processes:
            self.become_leader()
        else:
            received_ok = False 
            for process in higher_processes:
                received_ok = process.receive_election_message(self.process_id)
                if received_ok:
                    self.become_leader()
                    
    def receive_election_message(self, sender_id):
        print(f"process {self.process_id} received an election message from Process {sender_id}")
        if self.process_id > sender_id:
            print(f"process {self.process_id} sends an ok to process {sender_id}")
            self.start_election()
            return True 
        return False 
    
    def become_leader(self):
        print(f"process {self.process_id} becomes the leader ")
        self.is_leader = True
        for process in self.processes:
            if process.process_id != self.process_id: 
                process.receive_coordinator_message(self.process_id)

    def receive_coordinator_message(self, leader_id):
        print(f"process {self.process_id} acknowledges process {leader_id} as the leader")
        self.is_leader = False
        
def simulate_bully_algorithm(num_processes, duration):
    processes = [Process(i, []) for i in range(1, num_processes + 1)]
    for process in processes:
        process.processes = processes
    for process in processes:
        process.start()

    # start an initial election 
    time.sleep(1) # allow processes to start 
    processes[random.randint(0, num_processes - 1)].start_election()

    # run the simulation for a certain duration 
    time.sleep(duration)

    # simulate leader crash and recovery 
    for process in processes:
        if process.is_leader:
            process.alive = False 
            process.join()
            break
    time.sleep(1)
    for process in processes:
        if process.alive:
            process.start_election()
            break

    # stop all processes after the duration 
    for process in processes:
        process.alive = False 
        process.join()
        
if __name__ == "__main__":
    num_processes = 5 
    duration = 10 # run the simulation for 10 seconds
    simulate_bully_algorithm(num_processes, duration)