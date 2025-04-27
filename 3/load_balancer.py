import random
import time

class Server:
    def __init__(self, id, weight=1):
        self.id = id
        self.weight = weight
        self.active_connections = 0
        self.busy_time = 0  # To track server's busy time

    def __str__(self):
        return f"Server {self.id} [Connections: {self.active_connections}]"
        
class Request:
    def __init__(self, id):
        self.id = id
        self.processing_time = random.randint(1, 5)

class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.rr_index = 0
        self.weight_index = 0
        self.total_requests = 0
        self.total_waiting_time = 0
        self.total_simulation_time = 0  # To track the total time of all requests

    def assign_round_robin(self, request):
        server = self.servers[self.rr_index]
        self.rr_index = (self.rr_index + 1) % len(self.servers)
        server.active_connections += 1
        self.process(server, request)

    def assign_least_connections(self, request):
        server = min(self.servers, key=lambda s: s.active_connections)
        server.active_connections += 1
        self.process(server, request)

    def assign_weighted_rr(self, request):
        weights = [s.weight for s in self.servers]
        total_weight = sum(weights)
        flat_list = [server for server in self.servers for _ in range(server.weight)]
        server = flat_list[self.weight_index % total_weight]
        self.weight_index += 1
        server.active_connections += 1
        self.process(server, request)

    def process(self, server, request):
        # Track the time spent on each request (waiting time)
        start_time = time.time()
        print(f"Request {request.id} → {server} | Time: {request.processing_time}s")
        # Simulate processing based on the processing time (in seconds)
        time.sleep(request.processing_time)  # Process for the actual request time
        server.active_connections -= 1
        end_time = time.time()

        # Add the time spent on this request to the server's busy time
        server.busy_time += request.processing_time  # Busy time is directly the processing time
        self.total_simulation_time += request.processing_time  # Adding the actual processing time
        # Track the waiting time
        self.total_waiting_time += request.processing_time
        self.total_requests += 1
        
    def calculate_utilization(self):
        # Normalize server utilization as a percentage of total simulation time
        server_utilization = {
            server.id: round((server.busy_time / self.total_simulation_time) * 100, 2 )for server in self.servers
        }
        return server_utilization
def simulate(algorithm):
    print(f"\n🔁 Simulating {algorithm.upper()} Load Balancing\n")
    servers = [Server(i, weight=random.randint(1, 3)) for i in range(3)]
    lb = LoadBalancer(servers)

    for i in range(10):  # simulate 10 requests
        req = Request(i + 1)
        if algorithm == "rr":
            lb.assign_round_robin(req)
        elif algorithm == "lc":
            lb.assign_least_connections(req)
        elif algorithm == "wrr":
            lb.assign_weighted_rr(req)
        else:
            print("Unknown algorithm")
            break
    # After all requests are processed, calculate the average waiting time and server utilization
    avg_waiting_time = lb.total_waiting_time / lb.total_requests
    server_utilization = lb.calculate_utilization()
    # Print the results
    print(f"\nTotal Requests Processed: {lb.total_requests},")
    print(f"Average Waiting Time: {avg_waiting_time:.2f} seconds,")
    print(f"Server Utilization: {server_utilization},\n")
simulate("rr")
simulate("lc")
simulate("wrr")
