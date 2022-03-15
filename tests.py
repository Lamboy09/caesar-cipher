from app import decrypt, encrypt


def test_encrypt():
    text = "hello"
    shift = 5
    encrypted_text = encrypt(text, shift)
    assert encrypted_text == "mjqqt"

    text = "mjqqt btwqi"
    shift = 5
    encrypted_text = encrypt(text, shift)
    assert encrypted_text == "hello world"


if __name__ == "__main__":
    test_encrypt()
