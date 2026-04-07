# Extra: Flask `test_client()`

Use Flask’s built-in test client to exercise real routes without starting a server.

---

## What It Is

- A lightweight in-process client for your Flask app
- Sends requests to your route handlers
- Returns a response object you can inspect

Think of it as a fake browser for tests.

---

## Why Use It?

- Fast
- No browser needed
- No live server needed
- Tests the actual Flask routes and templates

Use it for integration-style tests of your web app.

---

## Basic Pattern

```python
with app.test_client() as client:
    response = client.get("/list")
```

This calls the real `@app.route("/list")` handler.

---

## Inspect The Response

```python
response.status_code
response.get_data(as_text=True)
response.headers
```

Common checks:
- status code
- page text
- redirect location

---

## GET Example

```python
with app.test_client() as client:
    response = client.get("/owners")
    assert response.status_code == 200
    assert "Owners" in response.get_data(as_text=True)
```

This tests the rendered page content.

---

## POST Example

```python
with app.test_client() as client:
    response = client.post(
        "/owner/create",
        data={"name": "greg", "city": "Portland", "type_of_home": "condo"},
    )
    assert response.status_code == 302
```

This tests a form submission through the real route.

---

## Redirects

```python
client.post("/owner/create", data=form_data, follow_redirects=False)
```

- `False` keeps the redirect response
- `True` follows the redirect and returns the final page

Use `False` when you want to assert the redirect target.

---

## Validation Example

```python
response = client.post("/owner/create", data={"name": ""})
assert response.status_code == 400
assert "name is required" in response.get_data(as_text=True)
```

This is useful for constraint and input checks.

---

## In This Course

We use `test_client()` to test:
- pet and owner CRUD routes
- constraint errors from the database layer
- redirect behavior after create, update, and delete

The app stays in-process, but the route code is real.
