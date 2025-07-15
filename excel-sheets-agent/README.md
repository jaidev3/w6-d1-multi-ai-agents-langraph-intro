# Excel Sheets Agent

This is an intelligent agent built with LangChain that processes large Excel files, understands natural language queries, and handles various production scenarios.

## Features
- Handles large files (10k+ rows, multiple tabs) with pandas.
- Natural language querying using OpenAI GPT-4o.
- Column name standardization for inconsistent naming.
- Supports filtering, aggregations, pivoting, etc., via pandas operations.
- Streamlit UI for easy interaction.

## Setup
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Create a `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Running the Agent
Run the following command:
```
streamlit run main.py
```
Then, open the provided URL in your browser, upload an Excel file, enter a query, and run it.

## Query Examples
- "Show sales data for Q3 2024 where revenue > 50000"
- "Create pivot table showing total sales by region and product"
- "Find customers who haven't ordered in 6 months"

## Edge Cases Handled
- Inconsistent column names via fuzzy matching.
- Multiple worksheets with sheet-aware prompting.
- Error handling for file loading issues like corruption or password protection.
