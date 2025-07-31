# 🔏 Digital Notary on the Blockchain

Welcome to **Digital Notary**, a simple and secure way to prove that your document existed at a specific point in time — all powered by **blockchain** and **digital signatures**.

---

## 🌟 What is This?

Imagine you're an artist 🎨, writer ✍️, or entrepreneur 💼 and want to prove that **you had a file or idea before anyone else**. This app lets you:

✅ Upload your document
✅ It gets timestamped and locked into a blockchain
✅ You receive a **digital certificate (signature)** to prove its authenticity
✅ Anyone can verify it later!

> 🔐 Think of it like a virtual notary who never sleeps.

---

## 🚀 Features

- 📁 **File Upload** — Notarize any file (text, PDFs, etc.)
- 🔐 **Blockchain Ledger** — Your document’s proof is locked forever
- 👤 **User Accounts** — Register/login securely
- ✍️ **Digital Signature (RSA)** — Each document is signed with your private key
- 🛡️ **Verification** — Anyone can check if a file is valid and notarized
- 🌐 **Web Interface** — Powered by [Streamlit](https://streamlit.io)
- 🧠 **REST API** — Built with [FastAPI](https://fastapi.tiangolo.com)

---

## 🧠 How Does It Work?

1. You log in or register 📲
2. Upload a document 📄
3. The system calculates a unique "fingerprint" (hash) of your file 🧬
4. That fingerprint is:
- Signed with your private key 🔐
- Added to a chain of records (blockchain) ⛓️
5. Later, anyone can upload the same file and:
- See if it matches a record ✅
- Verify the original signature 👁️‍🗨️

---

## 💻 Tech Stack (Simple View)

| Tech | What it does |
|------------|--------------|
| **Streamlit** | Builds the interactive web app |
| **FastAPI** | Runs behind-the-scenes API |
| **Python** | Brain of the app |
| **Blockchain** | Stores document records forever |
| **RSA Crypto** | Signs each document securely |

---

## 🧪 Try It Out

1. 🚀 Deploy it on [Render.com](https://render.com) (Docker-ready)
2. 🐳 Or run it locally:
```bash
docker build -t digital-notary .
docker run -p 8501:8501 -p 8000:8000 digital-notary
