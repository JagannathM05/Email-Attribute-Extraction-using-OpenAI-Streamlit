# 📧 Email Attribute Extraction using OpenAI & Streamlit

This is a simple Streamlit application that uses **OpenAI's GPT model** to extract structured attributes from unstructured **e-commerce complaint email threads**.

---

## 🚀 Features

- ✅ Upload `.txt` files containing email threads
- ✅ Uses `gpt-3.5-turbo` model for intelligent attribute extraction
- ✅ Outputs a structured JSON response with key details such as:
  - Product name/description
  - Issue summary
  - Order number
  - Resolution steps
  - Complaint name, email ID, etc.

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/JagannathM05/Email-Attribute-Extraction-using-OpenAI-Streamlit.git
cd email-attribute-extraction
````

### 2. Create Virtual Environment (optional)

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 API Key Setup

Set your OpenAI API key securely:

### Option 1: Using Environment Variable

```bash
export OPENAI_API_KEY="your_api_key_here"   # Linux/macOS
set OPENAI_API_KEY="your_api_key_here"      # Windows CMD
$env:OPENAI_API_KEY="your_api_key_here"     # PowerShell
```

### Option 2: Edit the Script

Replace the line in `attribute_extraction.py`:

```python
os.environ["OPENAI_API_KEY"] = "your_api_key_here"
```

> ⚠️ **Never commit your actual API key** into version control.

---

## ▶️ Run the App

```bash
streamlit run attribute_extraction.py
```

The app will open in your browser. Upload a `.txt` file containing an email thread and click **Submit** to get structured results.

---

## 📁 Project Structure

```
.
├── attribute_extraction.py    # Main Streamlit app
├── requirements.txt           # Python dependencies
└── sample_email.txt           # (Optional) Sample test input
```

---

