text = "sköldpadda"

encoded_text = text.encode("utf-8")
decoded_text = encoded_text.decode("utf-8")

print("Original text:", text)
print("Encoded bytes:", encoded_text)
print("Decoded text:", decoded_text)
