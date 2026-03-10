# Running the Project Tests

This project contains tests written using `pytest`. You can run the tests either **locally** or **using Docker**.

---

## 1. Running Tests Locally

### Step 1: Clone the repo

```bash
git clone https://github.com/AbrhamYishak/ai-experts-assignment-3.git
cd ai-experts-assignment-3
```

### Step 2: Create virtual environment (Optional)

```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Run the test

```bash
python -m pytest -v
```

## 2. Running Tests Using Docker

### Step 1: Clone the repo

```bash
git clone https://github.com/AbrhamYishak/ai-experts-assignment-3.git
cd ai-experts-assignment-3
```

### Step 2: Build the docker image

```bash
docker build -t token-client .
```

### Step 3: Run the tests in the container

```bash
docker run token-client
```
