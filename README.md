# 🧮 Calculator API (Flask / Docker Compose)

This is a simple Flask-based API for performing basic arithmetic operations: addition, subtraction, multiplication, and division.

The app is fully containerized using **Docker Compose** and connects to a **MongoDB** instance also managed via Docker.

---

## 🚀 How to Run This Project with Docker Compose

Follow the steps below to run the API using Docker Compose.

---

### ✅ 1. Prerequisites

Make sure you have **Docker** and **Docker Compose** installed.

To check your installation, run:

```bash
docker --version
docker compose version
````

You should see outputs like:

```
Docker version 24.x.x, build xxxxx
Docker Compose version v2.x.x
```

If you don't have Docker installed, follow the official guide:
👉 [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)

---

### 📁 2. Clone the Repository

```bash
git clone https://github.com/MGGodo/Flask-calculator.git
cd Flask-calculator
```

---

### 🧾 3. Create a `.env` File

In the root directory, create a file named `.env` with the following content:

```env
# URI complete to connect Mongo with Flask
MONGO_URI=mongodb://mongoadmin:adminmongo.@mongo:27017/

# Password and user for MongoDB container
DB_USERNAME=mongoadmin
DB_PASSWORD=adminmongo.
```

> 🔒 **Note:** Do not share this file publicly as it contains sensitive credentials.

---

### 🐳 4. Start the Services with Docker Compose

Use the following command to build and start both the Flask app and MongoDB:

```bash
docker compose up --build -d
```

* `--build`: Rebuilds the images before starting.
* `-d`: Runs containers in the background (detached mode).

Once running, the API will be available at:
📍 `http://127.0.0.1:5000/`

To view logs:

```bash
docker compose logs -f
```

To stop the services:

```bash
docker compose down
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

Available endpoints:

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

## 🧹 Useful Docker Compose Commands

List running containers:

```bash
docker compose ps
```

Rebuild containers after code changes:

```bash
docker compose up --build -d
```

Stop and remove containers, networks, and volumes:

```bash
docker compose down
```

---

## 📎 Notes

* Port `5000` must be available on your machine.
* The `flask-app` service will connect to MongoDB at the hostname `mongo` (from `docker-compose.yml`).
* All dependencies are installed inside the container; no need for a virtual environment or manual `pip install`.

---
