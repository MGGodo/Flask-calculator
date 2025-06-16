# 🧮 Flask Calculator API

This is a simple Flask-based API for performing basic arithmetic operations: addition, subtraction, multiplication, and division.

---

## 🚀 How to Run This Project

Follow these steps to set up and run the project locally.

---

### ✅ 1. Check Python Installation

Make sure you have **Python 3.9 or later** installed:

```bash
python --version
````

You should see something like:

```
Python 3.9.x
```

If Python is not installed, download it from [https://www.python.org/downloads/](https://www.python.org/downloads/).

---

### 📁 2. Clone the Repository

```bash
git clone https://github.com/MGGodo/Flask-calculator.git
cd Flask-calculator.git
```

---

### 🛠️ 3. Create and Activate a Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it:
# On Linux/macOS
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

---

### 📦 4. Install Dependencies

Install the required packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

### ▶️ 5. Run the Application

Run the Flask app using:

```bash
python run.py
```

You should see output indicating the app is running on:

```
http://127.0.0.1:5000/
```

---

## 📬 How to Test the API (Using Postman)

1. Open **Postman** or any REST client.
2. Set the request method to **POST**.
3. Use `http://127.0.0.1:5000/<endpoint>` as the URL.
4. Go to the **Body** tab, select **raw** and **JSON**, and use the following format:

```json
{
  "a": 10,
  "b": 5
}
```

5. Try any of these endpoints:

| Endpoint          | Description                          |
| ----------------- | ------------------------------------ |
| `/addition`       | Adds `a` + `b`                       |
| `/subtraction`    | Subtracts `a` - `b`                  |
| `/multiplication` | Multiplies `a` \* `b`                |
| `/division`       | Divides `a` / `b` (null if `b == 0`) |
| `/all-op`         | Returns all four operations          |

Example test:

* **URL:** `http://127.0.0.1:5000/addition`
* **Method:** `POST`
* **Body (raw JSON):**

```json
{
  "a": 12,
  "b": 8
}
```

* **Expected Response:**

```json
{
  "a": 12,
  "b": 8,
  "res-add": 20
}
```

---


