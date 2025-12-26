from flask import Flask, render_template, request, send_file
import os
from encryption import encrypt_file, decrypt_file

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        uploaded_file = request.files["file"]

        if uploaded_file.filename == "":
            return "No file selected"

        file_data = uploaded_file.read()
        encrypted_data = encrypt_file(file_data)

        encrypted_path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename + ".enc")
        with open(encrypted_path, "wb") as f:
            f.write(encrypted_data)

        return "File uploaded and encrypted successfully"

    return render_template("upload.html")


@app.route("/download/<filename>")
def download_file(filename):
    encrypted_path = os.path.join(UPLOAD_FOLDER, filename)

    with open(encrypted_path, "rb") as f:
        encrypted_data = f.read()

    decrypted_data = decrypt_file(encrypted_data)

    decrypted_path = encrypted_path.replace(".enc", "")
    with open(decrypted_path, "wb") as f:
        f.write(decrypted_data)

    return send_file(decrypted_path, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
