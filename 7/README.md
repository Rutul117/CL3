### **1. Introduction to Artificial Immune Systems (AIS)**

- **Artificial Immune Systems (AIS)** are computational algorithms inspired by the biological immune system. The main idea is to mimic the immune system's ability to recognize and classify patterns as either "self" (healthy) or "non-self" (damaged/foreign).
- AIS is used in areas like pattern recognition, anomaly detection, and classification problems. It has applications in various fields like healthcare, structural health monitoring, and cybersecurity.

---

### **2. Problem Statement: Structure Damage Classification**

- The problem at hand is to **classify structural damage** using two features: **vibration** and **crack length**. The classification task involves determining whether a structure is **healthy (0)** or **damaged (1)** based on these two features.
- The classification is done using **Artificial Immune Systems**, specifically applying the **Negative Selection Algorithm (NSA)**, inspired by the immune system's way of detecting harmful invaders.

---

### **3. Overview of the Four AIS Algorithms Mentioned**

In the theory provided, four algorithms related to **Artificial Immune Systems** are discussed:

1. **Clonal Selection Algorithm**:
   - This algorithm involves optimizing solutions by cloning the best solutions and applying mutations. It's often used in optimization tasks.
  
2. **Negative Selection Algorithm (NSA)**:
   - This algorithm mimics how the immune system detects "non-self" (foreign invaders) by generating detectors that represent "self" (healthy) patterns. The algorithm then identifies anomalies or patterns that deviate from the "self" as "non-self" (damaged).
  
3. **Immune Network Algorithms**:
   - This algorithm models the immune system's network structure, where antibodies (solutions) interact to regulate immune responses. It's used in clustering and optimization.
  
4. **Dendritic Cell Algorithms (DCA)**:
   - This algorithm models the multi-scale processing of dendritic cells, which play a key role in the immune system’s pattern recognition. It's used in complex anomaly detection tasks.

---

### **4. Algorithm Used in the Code**

- **The code provided implements the Negative Selection Algorithm (NSA)**. Here's why:

   1. **Detector Generation**:
      - The code starts by **generating detectors** that represent "healthy" patterns (class 0). These detectors are randomly generated vectors, and the program ensures they are **distant from all healthy samples** using a **threshold** distance. This mimics the immune system's tolerance to "self".
   
   2. **Classification**:
      - When classifying a new data point (vibration, crack length), the code compares the input with each of the detectors. The classification rule is:
        - If the input is **close enough** (within a defined threshold) to any detector, it is classified as **damaged (1)**.
        - If the input is **far from all detectors**, it is classified as **healthy (0)**.
      - This process mirrors how the immune system distinguishes between "self" and "non-self".

---

### **5. Code Walkthrough**

- **Dataset Creation**:
  ```python
  data = [
      ([0.1, 0.2], 0),
      ([0.15, 0.25], 0),
      ([0.8, 0.9], 1),
      ([0.9, 0.85], 1),
      ([0.2, 0.3], 0),
      ([0.75, 0.8], 1),
      ([0.25, 0.4], 0),
      ([0.95, 0.95], 0)
  ]
  ```
  - This is a small sample dataset consisting of **two features** (vibration and crack length) and their corresponding **labels** (0 for healthy, 1 for damaged).

- **Parameter Definition**:
  ```python
  NUM_DETECTORS = 10
  THRESHOLD = 0.3
  ```
  - **NUM_DETECTORS**: This is the number of **detectors** (immune responses) we want to generate.
  - **THRESHOLD**: The **distance threshold** for classifying a structure as damaged. If the distance between an input and any detector is smaller than this threshold, it’s classified as **damaged**.

- **Detector Generation**:
  ```python
  def generate_detectors():
      detectors = []
      while len(detectors) < NUM_DETECTORS:
          vec = [random.uniform(0, 1), random.uniform(0, 1)]
          if all(np.linalg.norm(np.array(vec) - np.array(f)) > THRESHOLD for f, label in data if label == 0):
              detectors.append(vec)
      return detectors
  ```
  - **Detectors** are randomly generated vectors in the feature space. A new detector is only added if it is **sufficiently distant** from the healthy patterns (class 0).
  - The distance is measured using **Euclidean distance** and checked against the **threshold**.

- **Classification**:
  ```python
  def classify(detectors, input_vec):
      for det in detectors:
          if np.linalg.norm(np.array(input_vec) - np.array(det)) < THRESHOLD:
              return 1  # Damaged
      return 0  # Healthy
  ```
  - For each input, the program compares the input vector to the detectors. If the input is close enough to any detector, it is classified as **damaged** (1). Otherwise, it’s classified as **healthy** (0).

- **Training and Testing**:
  ```python
  detectors = generate_detectors()
  
  correct = 0
  for features, label in data:
      pred = classify(detectors, features)
      status = "✅ Correct" if pred == label else "❌ Wrong"
      print(f"Features: {features} | Actual: {label} | Predicted: {pred} → {status}")
      correct += int(pred == label)
  
  accuracy = (correct / len(data)) * 100
  print(f"\n🎯 Accuracy: {accuracy:.2f}%")
  ```
  - The **detectors** are generated and the **classification** is performed on each data point.
  - The program calculates the **accuracy** based on how many predictions match the actual labels.

---

### **6. Conclusion**

- **Summary**: The code implements the **Negative Selection Algorithm** from the four AIS algorithms to classify structural damage based on features like vibration and crack length. It generates **detectors** that represent healthy patterns and uses them to classify new input patterns as either **healthy** or **damaged**.
  
- **Result**: After running the classifier, the **accuracy** is calculated, showing how well the system performs at classifying damage correctly.

- **Significance**: This approach is an example of how biologically inspired algorithms, like AIS, can be applied to solve real-world problems like structural health monitoring. The method can be extended to more complex datasets or used in real-time monitoring systems.

---
