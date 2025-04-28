# Beginner_0_MCP
Here’s an understandable explanation for your README.md file:

---

# Spam Detector using MCP (Model Context Protocol)

This project is a simple yet effective way to detect whether a given text (such as an email or message) is spam or not. It uses a **client-server architecture**, and the backend is built using **Flask API**. The spam detection model is based on **DistilBERT**, and fine-tuned using **Head-Only Fine-Tuning (HOFT)**. The project also uses **MCP (Model Context Protocol)** to communicate between the client and server, making the system scalable and easier to manage.

### Project Structure

```
spam-detector-llm/
├── server_local_llm.py       # Backend API
├── model.py                  # Fine-tuned model
├── model_context.py          # Model info for MCP
├── client_llm.py             # Testing client
├── streamlit_app.py          # Frontend UI
├── requirements.txt          # Python packages list
└── README.md (Optional)      # Project documentation
```

### 1. **Model.py**
The `model.py` file is where the spam detection model is created and fine-tuned. The model uses **DistilBERT** for text classification, specifically to determine whether the text is "spam" or "not spam." To improve performance, **Head-Only Fine-Tuning (HOFT)** is applied, which helps the model capture patterns better. The fine-tuned model is saved in a folder for later use.

### 2. **Model_context.py**
This file stores the metadata of the model, including version information, accuracy, and the model's name. This metadata can be helpful to keep track of the model's updates and performances.

### 3. **Server_llm.py**
The `server_llm.py` file runs the **Flask API** on the server side. It loads the fine-tuned model stored earlier and exposes an API endpoint for the client to interact with. The server accepts the client's request, processes the input text, and returns the classification result (spam or not spam). The server is also responsible for updating the model metadata as needed.

### 4. **Client_llm.py**
This file is optional but helps to test whether the client and server are connected and functioning properly. It simulates a client that sends requests to the server to check the spam classification.

### 5. **Streamlit_app.py**
The `streamlit_app.py` file is the **frontend UI** for the user to interact with the system. It allows users to input text, which is sent to the server for spam detection. The result (spam or not spam) is returned from the server and displayed to the user. The Streamlit UI serves as an interface for the users to test the spam detection model.

---

### Why use MCP (Model Context Protocol)?

The **MCP** is a communication protocol designed to improve scalability and version control in client-server architecture. Initially, developers face challenges with scalability, version mismatches, and code duplication across both client and server sides. By adopting MCP, the following benefits are achieved:

1. **Scalability**: It’s easier to scale the system as new services can be added without affecting the existing client-server communication.
2. **Centralized Model Updates**: When there is a version mismatch, you don’t have to modify the client-side code. Instead, the server can manage and serve the updated model directly.
3. **Simplified Communication**: MCP simplifies how the client and server communicate, allowing for easy integration and extension.

This project serves as a base version of an MCP setup.
