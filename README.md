<a id="financial-agent-diagram"></a>
# Agentic AI Project 🚀

<!-- Financial Agent Architectural Diagram Placeholder -->
![Financial Agent Diagram](assets/FinancialAgentDiagram.png)

In Agentic AI Exploration, I designed 2 multi-agent systems that leverages the Groq language model alongside specialized tools to perform tasks such as financial data analysis, web searches, and PDF document assistance. The system integrates multiple APIs and libraries—including DuckDuckGo for web searches, yfinance for financial data, and Hugging Face for PDF embeddings—to provide comprehensive solutions.


## Project Overview

### Agents

- **Multi-Agent Setup**  
  The project features a coordinated multi-agent architecture comprising two main sub-agents:

  - **Web Agent**  
    - Utilizes the DuckDuckGo tool to fetch online information.
    - Configured to always include source citations in its output.

  - **Financial Agent**  
    - Retrieves financial data such as stock prices, analyst recommendations, and company news using the YFinance tool.
    - Displays data in formatted tables.
    - *(Refer to the Financial Agent Diagram above for a visual overview.)*

- **PDF Assistant Agent**  
  Processes PDF documents by:
  - Retrieving content from specified URLs.
  - Embedding the information using a Hugging Face model.
  - Storing the embedded data in a PostgreSQL vector database for interactive querying.

---
## Directory Structure

```
Yash8745-Agentic-Ai/
├── README.md
├── financial_agent.py
├── pdf_assistant.py
├── requirements.txt
└── test.py
```

## Architecture Explanation

### Financial Agent Architecture

The **Financial Agent** is designed to deliver comprehensive financial insights:
- **Tool Calling:** Integrates various tools to pull real-time financial data.
- **Agent Orchestration:** 
    1. Manages the agent's workflow and data retrieval.
    2. The Orchestrator Agent coordinates the Web Agent and Financial Agent.
    3. The Web Agent fetches data from DuckDuckGo and the Financial Agent retrieves financial data from YFinance.


[See the Financial Agent Diagram at the top of this document](#financial-agent-diagram)


### PDF Assistant Architecture

The **PDF Assistant Agent** focuses on document processing:
- **Document Retrieval:** Loads PDF content from predefined URLs.
- **Embedding:** Uses Hugging Face’s model to embed the document content.
- **Storage & Querying:** Saves the embedded data in a PostgreSQL vector database for later retrieval and analysis.


<!-- PDF Agent Architectural Diagram Placeholder -->
![PDF Agent Diagram](assets/PdfAssistantDiagram.png)

## Setup and Installation

### Prerequisites

- **Python:** Version 3.10 or higher.
- **PostgreSQL:** Required for the PDF Assistant. Ensure you have a running PostgreSQL instance with pgvector support.

### Installation Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/yash8745-agentic-ai.git
   cd yash8745-agentic-ai
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables:**

   Create a `.env` file in the project root and add your configurations. For example:

   ```ini
    PHI_API_KEY=""
    GROQ_API_KEY=""
   ```

   Adjust other variables as needed (e.g., database connection strings).



## Usage

### Running the Agents
```bash
python financial_agent.py
python pdf_assistant.py
```

## To-Do List ✅

1. **PDF Assistant Issue:**  
   The PDF assistant is running but encounters issues with Hugging Face embedding. Review the error logs and adjust the configuration. 



## Contributing

Contributions are welcome! If you find issues or have suggestions:
- Open an issue on the repository.
- Submit a pull request with your improvements.

