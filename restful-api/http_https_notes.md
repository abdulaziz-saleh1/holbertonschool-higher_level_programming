# Basics of HTTP/HTTPS

## 1. Difference Between HTTP and HTTPS

- **HTTP (HyperText Transfer Protocol)** is the basic protocol for communication between a web client and a server.
- **HTTPS (HTTP Secure)** is the secured version of HTTP that uses **SSL/TLS encryption**.
- **HTTP** sends data in plain text, making it vulnerable to **eavesdropping**.
- **HTTPS** encrypts the data, ensuring **confidentiality**, **integrity**, and **authentication** — especially important for login pages, banking, and email.

---

## 2. HTTP Request and Response Structure

### 🔹 Request Structure
- **Method**: e.g. `GET`, `POST`
- **URL/Path**: e.g. `/index.html`
- **Headers**: Metadata like `User-Agent`, `Content-Type`
- **Body**: Optional, usually used in POST/PUT to send data

### 🔹 Response Structure
- **Status Code**: e.g. `200 OK`, `404 Not Found`
- **Headers**: e.g. `Content-Type: text/html`
- **Body**: The actual content returned (HTML, JSON, etc.)

---

## 3. Common HTTP Methods

| Method | Description                           | Use Case Example                             |
|--------|---------------------------------------|----------------------------------------------|
| GET    | Requests data from the server         | Fetch a webpage or retrieve JSON data        |
| POST   | Sends data to the server              | Submitting a form (e.g. login/register)      |
| PUT    | Updates existing data on the server   | Updating user profile information            |
| DELETE | Deletes a resource from the server    | Deleting a user's comment or post            |

---

## 4. Common HTTP Status Codes

| Code | Meaning              | Description & Scenario                                      |
|------|----------------------|--------------------------------------------------------------|
| 200  | OK                   | Request succeeded (e.g. page loaded correctly)               |
| 201  | Created              | Resource was successfully created (e.g. after POST request) |
| 400  | Bad Request          | Malformed request (e.g. missing required form fields)        |
| 404  | Not Found            | Resource not found (e.g. broken link)                        |
| 500  | Internal Server Error| Server-side issue occurred unexpectedly                     |

---
