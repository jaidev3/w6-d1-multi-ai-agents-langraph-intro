import streamlit as st
import os
import pandas as pd
import openpyxl
import xlrd
from io import BytesIO
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent
from fuzzywuzzy import fuzz
from pydantic import SecretStr

load_dotenv()

key = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4o", temperature=0, api_key=SecretStr(key) if key else None)

column_synonyms = {
    'sales': ['sales', 'revenue', 'amount', 'amt', 'total'],
    'date': ['date', 'order_date', 'purchase_date', 'dt'],
    'region': ['region', 'area', 'zone', 'territory'],
    'product': ['product', 'item', 'sku', 'prod'],
    'quantity': ['quantity', 'qty', 'count', 'quant'],
    'customer': ['customer', 'client', 'buyer', 'cust'],
    # Add more as needed
}

def standardize_columns(df):
    candidates = []
    for col in df.columns:
        for standard, syns in column_synonyms.items():
            max_score = max(fuzz.ratio(syn.lower(), col.lower()) for syn in syns)
            if max_score > 80:
                candidates.append((col, standard, max_score))
    candidates.sort(key=lambda x: x[2], reverse=True)
    mapping = {}
    used = set()
    for col, standard, score in candidates:
        if standard not in used:
            mapping[col] = standard
            used.add(standard)
    df.rename(columns=mapping, inplace=True)
    return df

st.title("Intelligent Excel Agent")

uploaded_file = st.file_uploader("Upload Excel file", type=['xlsx', 'xls'])

if uploaded_file:
    try:
        bytes_content = uploaded_file.getvalue()
        engine = 'xlrd' if uploaded_file.name.endswith('.xls') else 'openpyxl'
        dfs_dict = pd.read_excel(BytesIO(bytes_content), sheet_name=None, engine=engine)

        sheet_names = list(dfs_dict.keys())
        dfs = []
        for name, df in dfs_dict.items():
            df = standardize_columns(df)
            dfs.append(df)
        prefix = "You have access to the following dataframes from Excel sheets: " + ", ".join([f"df{i} from sheet '{sheet_names[i]}'" for i in range(len(dfs))]) + "\nUse them appropriately in your code based on the query."
        agent = create_pandas_dataframe_agent(llm, dfs, prefix=prefix, verbose=True, allow_dangerous_code=True)
        query = st.text_input("Enter your natural language query:")
        if st.button("Run Query") and query:
            with st.spinner("Processing..."):
                result = agent.run(query)
            st.success("Query Result:")
            st.write(result)
    except Exception as e:
        st.error(f"Error loading or processing file: {str(e)}. If the file is password-protected, please remove the protection.")
else:
    st.info("Please upload an Excel file to begin.")
