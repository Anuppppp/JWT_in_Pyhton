import jwt

SECRET_KEY = "anup_jwt"
token = '''eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzZW5kZXIiOiJBbnVwIEpXVCIsIm1lc3NhZ2UiOiJKV1QgaXMgYXdlc29tZS4gWW91IHNob3VsZCB0cnkgaXQhIiwiZGF0ZSI6IjIwMjMtMTEtMDcgMDA6NDQ6MTAuNTUzNzI5IiwiZXhwIjoxNjk5Mzg0NDUwfQ.L9_u93BnfW9vD62ZZQeBm498PfJIZsOWptcwnIdUfCA
'''
try:
    decode_data = jwt.decode(jwt=token, key=SECRET_KEY, algorithm="HS256")
    print(decode_data)
except Exception as e:
    message = f"Token is invalid --> {e}"
    print({"message": message})

