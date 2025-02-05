# 📈 Tiingo Fetcher - A Python Library for Fetching Market Data

## 📌 About
`tiingo_fetcher` is a **lightweight Python library** that allows users to **fetch large amounts of historical stock data** for free using the **[Tiingo API](https://www.tiingo.com/)**.

Unlike other APIs that limit minute-level data to **7 days**, **Tiingo Fetcher** allows you to retrieve **up to 9 years** of minute, hourly, and daily data efficiently.

---

## 📦 Installation
You can install the package using `pip`:

```bash
pip install tiingo-fetcher
```

---

## 🔑 Setup: Get a Tiingo API Key
To use this package, you need a **Tiingo API key**:
1. **Sign up for a free Tiingo account**: [https://www.tiingo.com/](https://www.tiingo.com/)
2. **Generate your API key** from the **Account → API Section**.
3. **Use the API key directly in your script** (no `.env` file is required).

---

## 🚀 Usage
### **1️⃣ Fetching Historical Stock Data**
You can fetch stock data by calling `fetch_data()` and passing the **stock symbol, API key, start date, end date, and frequency**:

```python
from tiingo_fetcher.fetch_data import fetch_data

data = fetch_data("AAPL", "your_api_key_here", "2023-01-01", "2023-02-01", "1min")

print(data.head())
```

### **Parameters:**
- `symbol` (**str**) - Stock ticker symbol (e.g., "AAPL").
- `api_key` (**str**) - Your **Tiingo API Key** (must be provided directly in the function call).
- `start_date` (**str**) - Start date in `YYYY-MM-DD` format.
- `end_date` (**str**) - End date in `YYYY-MM-DD` format.
- `freq` (**str**) - Frequency (**'1min', '5min', '15min', '30min', '60min', 'daily'**).

---

## 🏗 Project Structure
```
tiingo_fetcher/
├── tiingo_fetcher/         # Package folder
│   ├── __init__.py         # Marks it as a package
│   ├── fetch_data.py       # Core data-fetching logic
├── example_usage/          # Example scripts
│   ├── test.py             # Example usage script
├── README.md               # Documentation
├── setup.py                # Package setup
├── requirements.txt        # Dependencies
```

---

## 🔧 Troubleshooting
### **"ModuleNotFoundError: No module named 'tiingo_fetcher'"**
- Ensure the package is installed:
  ```bash
  pip install --upgrade tiingo-fetcher
  ```
- If running locally, try:
  ```bash
  python -m example_usage.test
  ```

---

## 📜 License
This project is licensed under the **MIT License**. You are free to use, modify, and distribute it.

---

## ⭐ Support
If you find this project useful, consider giving it a ⭐ on GitHub!

