### **Distributed Application Using RPC for Remote Computation: Factorial Calculation**

---

**1. Introduction:**

"In this project, we have implemented a distributed application using **RPC (Remote Procedure Call)**, where the **client** sends an integer to the **server**. The server then computes the factorial of that integer and sends the result back to the client. The main components involved are the **client**, the **server**, and the **RPC framework** facilitating the communication."

---

**2. What is RPC?**

"RPC is a protocol that allows a program (the **client**) to request a procedure or function execution on a remote server, as if it were being executed locally. This abstraction allows us to treat remote function calls just like local function calls, without worrying about network communication details."

---

**3. Components of RPC:**

"The **RPC** system involves the following components:
- **Client**: Initiates the request to the server.
- **Server**: Executes the function on the remote machine.
- **Stub**: A client-side proxy for the remote function, responsible for packaging the function call and sending it to the server.
- **Skeleton**: A server-side proxy that receives the request, unpacks it, and invokes the function on the server side."

---

**4. RPC Workflow:**

"Here’s how the communication happens step-by-step:
1. The **client** calls a function (e.g., `calculate_factorial(n)`) through the **stub**.
2. The **stub** sends the function call with the parameters (in this case, the integer `n`) to the **server** via network communication.
3. The **server's skeleton** receives the request, unpacks it, and calls the `calculate_factorial(n)` function.
4. The server computes the factorial and returns the result back to the **stub**.
5. The **stub** receives the result and sends it back to the **client**, which displays the result."

---

**5. Server-Side Implementation:**

"The server is implemented using Python’s **xmlrpc.server** module. The main steps include:
1. **Importing the necessary library**: `from xmlrpc.server import SimpleXMLRPCServer`.
2. **Defining the `calculate_factorial` function**:
   - This function takes an integer `n` as input and calculates the factorial using an iterative approach (avoiding recursion to prevent stack overflow).
   - The result is returned as a string to prevent integer overflow in case of very large results.
   
   ```python
   def calculate_factorial(n):
       result = 1
       for i in range(2, n + 1):
           result *= i
       return str(result)  # Avoid int overflow
   ```

3. **Creating the server**: 
   - The server listens on the localhost (127.0.0.1) at port 8000. It registers the `calculate_factorial` function so that it can be accessed by the client.
   
   ```python
   server = SimpleXMLRPCServer(("localhost", 8000))
   server.register_function(calculate_factorial, "calculate_factorial")
   server.serve_forever()
   ```

   The server continuously listens for incoming requests and processes them in real-time."

---

**6. Client-Side Implementation:**

"The client program is implemented using Python’s **xmlrpc.client** module. Here’s the breakdown:
1. **Connecting to the server**: The client connects to the server using the `ServerProxy` object, which creates a proxy to call the remote function.
   
   ```python
   proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
   ```

2. **Client interaction**: The client asks the user for an integer and sends that integer to the server’s `calculate_factorial` function using the remote procedure call.
   
   ```python
   while True:
       n = input("Enter a number (or type exit): ")
       if n.lower() == "exit":
           break
       print("Factorial:", proxy.calculate_factorial(int(n)))
   ```

   This loop allows continuous interaction, where the client keeps requesting the factorial for different numbers until the user types "exit". The server processes each request, computes the factorial, and sends the result back to the client."

---

**7. Explanation of the Server Logs:**

"When the server is running, it logs the requests it receives. Here’s an example of what the log output looks like:

```
127.0.0.1 - - [26/Apr/2025 00:40:38] "POST / HTTP/1.1" 200 -
```

- **127.0.0.1**: The IP address of the client (in this case, localhost, indicating the client and server are on the same machine).
- **Timestamp**: This shows when the request was made.
- **"POST / HTTP/1.1"**: The HTTP method used (POST), and the request path (root path `/`).
- **200**: The HTTP status code indicating a successful request.

Each entry represents a client request where the server receives the factorial computation request, processes it, and returns the result."

---

**8. Expected Output:**

"The client will continuously prompt the user for input (until the user types 'exit'), and for each valid input, it will display the calculated factorial result. For example:

```
Enter a number (or type exit): 5
Factorial: 120
```

If the user enters a very large number, the server still computes the factorial correctly, and the result is returned as a string to avoid overflow issues."

---

**9. Error Handling:**

"We also implemented basic error handling to ensure that invalid inputs (like non-integer values) are handled gracefully. If an invalid input is given, the client will prompt the user again for valid input."

---

**10. Conclusion:**

"In this project, we successfully implemented a distributed application using **RPC** for remote computation. The client sends an integer to the server, the server computes the factorial, and the result is returned to the client. This demonstrates the use of **RPC** for creating distributed applications, abstracting away the complexities of network communication and enabling easy remote procedure execution."

---
