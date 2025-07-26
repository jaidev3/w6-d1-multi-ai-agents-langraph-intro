# 🤖 Google Sheets Agent

A powerful AI agent built with LangChain and Google Gemini that can interact with Google Sheets through natural language commands. This agent can read, analyze, filter, aggregate, sort, and manipulate spreadsheet data intelligently.

## ✨ Features

- **Natural Language Interface**: Interact with Google Sheets using conversational commands
- **Data Operations**: Read, filter, aggregate, and sort spreadsheet data
- **Sheet Management**: Create new sheets with processed data
- **Memory**: Maintains conversation context for complex multi-step operations
- **Web Interface**: User-friendly Streamlit dashboard
- **LangChain Integration**: Powered by LangChain for robust agent capabilities
- **Google Gemini**: Uses Google's advanced AI model for intelligent responses

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Google Cloud Service Account with Sheets API access
- Google Gemini API key

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd googleSheetsAgent
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your API keys and configuration
```

5. Add your Google Service Account JSON file as `service_account.json`

6. Run the application:
```bash
streamlit run app.py
```

## 🔧 Configuration

Create a `.env` file with the following variables:

```env
GEMINI_API_KEY=your_gemini_api_key_here
SHEET_ID=your_google_sheet_id_here
```

## 📁 Project Structure

```
googleSheetsAgent/
├── agents/
│   ├── langchain_agent.py       # Main LangChain agent orchestrator
│   └── langchain_tools.py       # LangChain tool definitions for Google Sheets
├── .env                         # Environment variables (not tracked)
├── .gitignore                   # Git ignore patterns
├── app.py                       # Streamlit web interface
├── requirements.txt             # Python dependencies
├── service_account.json         # Google API credentials (not tracked)
└── README.md                   # This file
```

## 🎯 Usage Examples

- "Show me all the data from the Sales sheet"
- "Filter the data where revenue is greater than 1000"
- "Create a summary of total sales by region"
- "Sort the customer data by date"
- "Create a new sheet with the filtered results"

## 🔒 Security

- Environment variables are used for sensitive data
- Service account credentials are excluded from version control
- All sensitive files are properly ignored in `.gitignore`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

graph TD
    A[User Input] --> B[Streamlit Frontend<br/>app.py]
    B --> C{Select Sheet & Query}
    C --> D[LangChain Agent<br/>langchain_agent.py]
    
    D --> E[Query Processing<br/>Enhanced with Context]
    E --> F[LLM Decision Making<br/>GPT-4o-mini/OpenAI]
    F --> G[Tool Selection<br/>Based on Query Intent]
    
    G --> H1[filter_sheets_data]
    G --> H2[aggregate_sheets_data]
    G --> H3[create_pivot_table]
    G --> H4[sort_sheets_data]
    G --> H5[add_column_to_sheet]
    G --> H6[add_row_to_sheet]
    G --> H7[get_sheet_info]
    G --> H8[write_custom_results]
    
    H1 --> I[SheetsService<br/>Google Sheets API]
    H2 --> I
    H3 --> I
    H4 --> I
    H5 --> I
    H6 --> I
    H7 --> I
    H8 --> I
    
    I --> J[Google Sheets<br/>Operations]
    J --> K[Pandas Processing<br/>Data Manipulation]
    K --> L[Write Results<br/>Back to Sheets]
    L --> M[Response to User<br/>via Streamlit]
    
    N[Memory System<br/>ConversationBufferMemory] --> D
    D --> N
    
    O[Service Account<br/>Authentication] --> I
    P[Environment Variables<br/>.env file] --> D
    P --> I
    
    style A fill:#e1f5fe
    style B fill:#f3e5f5
    style D fill:#e8f5e8
    style F fill:#fff3e0
    style I fill:#fce4ec
    style J fill:#f1f8e9