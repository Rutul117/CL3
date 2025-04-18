import random
import time

class Server:
    def __init__(self, id, weight=1):
        self.id = id
        self.weight = weight
        self.active_connections = 0

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
        print(f"Request {request.id} → {server} | Time: {request.processing_time}s")
        time.sleep(0.1)  # simulate processing
        server.active_connections -= 1

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

# Run all three
simulate("rr")
simulate("lc")
simulate("wrr")

