import streamlit as st
import hashlib
from blockchain import Blockchain
from auth import authenticate_user, register_user
from crypto import generate_keys, sign_data, verify_signature

bc = Blockchain()

st.title("🔐 Digital Notary")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    st.subheader("Login")
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")
    if st.button("Login"):
        if authenticate_user(user, pwd):
            st.session_state.user = user
            st.session_state.logged_in = True
            st.success("✅ Logged in")
        else:
            st.error("Invalid credentials")

def register():
    st.subheader("Register")
    user = st.text_input("New Username")
    pwd = st.text_input("New Password", type="password")
    if st.button("Register"):
        if register_user(user, pwd):
            generate_keys(user)
            st.success("User registered.")
        else:
            st.warning("Username taken.")

if not st.session_state.logged_in:
    action = st.radio("Login or Register", ["Login", "Register"])
    if action == "Login":
        login()
    else:
        register()
else:
    user = st.session_state.user
    menu = st.sidebar.selectbox("Menu", ["Notarize File", "Verify", "Blockchain"])

    if menu == "Notarize File":
        st.subheader("📄 Notarize a File")
        uploaded_file = st.file_uploader("Upload File")
        if uploaded_file and st.button("Notarize"):
            content = uploaded_file.read()
            file_hash = hashlib.sha256(content).hexdigest()
            block = bc.add_block(file_hash)
            signature = sign_data(user, file_hash)
            st.success("Document notarized.")
            st.code(f"Hash: {file_hash}")
            st.code(f"Signature: {signature}")

    elif menu == "Verify":
        st.subheader("Verify Signature")
        doc = st.text_area("Paste original document")
        sig = st.text_input("Paste signature (hex)")
        signer = st.text_input("Signed by (username)")
        if st.button("Verify Signature"):
            h = hashlib.sha256(doc.encode()).hexdigest()
            if verify_signature(signer, h, sig):
                st.success("Signature is valid.")
            else:
                st.error("Invalid signature.")

    elif menu == "Blockchain":
        st.subheader("📜 Blockchain")
        for block in bc.get_all_blocks():
            st.json(block)