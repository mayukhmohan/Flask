from passlib.hash import sha256_crypt

password = sha256_crypt.encrypt("password")
password2 = sha256_crypt.encrypt("password")

print(password)
print(password2)

print(sha256_crypt.verify("password",password))

print(sha256_crypt.verify("12345","$5$rounds=535000$QBgwvbADt7MkmAzD$CmkRfbCopXG8K3xE2QxJx4DCTrzV8vEvilHtZWvY4f7"))
