
# Quantum-Safe Code API

This Django-based API provides secure, time-limited code generation and verification, designed to be resistant to quantum attacks. It is ideal for applications requiring enhanced security for authentication or transaction validation.

## Features

- Generates secure, time-limited codes
- Verifies codes for validity and usage
- Indicates if a code is quantum-safe
- Simple RESTful endpoints for integration

## API Endpoints

- `GET /current_code/`  
  Returns the current valid code, its expiry, and quantum safety status.

- `POST /verify_code/`  
  Verifies a user-submitted code.  
  **Body:** `code=<user_code>`

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Fadi-Mabrouk/Quantum_crypto.git
   cd quantum-safe
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Run the server:**
   ```bash
   python manage.py runserver
   ```
