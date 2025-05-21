# 🚀 IranFletDev Instagram clone

Welcome to this **Flet** project! This README will guide you step-by-step on how to set up, run, and enjoy your app — whether on desktop or web.

---

## 📋 Table of Contents

- 📖 [About](#about)  
- 🔧 [Prerequisites](#prerequisites)  
- 📥 [Installation](#installation)  
- 🚀 [Running the Project](#-running-the-project)  
- 🛠️ [Usage](#️-usage)  
- 🐞 [Troubleshooting](#-troubleshooting)  
- 🤝 [Contributing](#-contributing)  
- 📄 [License](#-license)  
- 👤 [Authors](#authors)  


---

## 📖 About

This project is built with **Flet**, a modern Python framework to create realtime web, desktop, and mobile apps powered by Flutter UI.

This is a simple example of an Instagram application.

It aims to provide a clean, cross-platform user interface that works seamlessly everywhere.

---

## 🔧 Prerequisites

Make sure you have these installed on your machine:

- Python 3.7+  
- pip
- A virtual environment tool such as `venv` or `virtualenv`  

---

## 📥 Installation

1. **Clone the repo:**

```bash
git clone https://github.com/yourusername/your-flet-project.git
cd your-flet-project
```

2. **Create and activate a virtual environment (recommended):**

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. **Install required packages:**

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Project

You can run the app in **two different ways** depending on how you want to use it:

---

### 🖥️ 1. Default View (Desktop / Native Window)

Runs the app as a native desktop window.

```python
ft.app(target=app.main)
```



---

### 🌐 2. Web View (Browser)

Runs the app in a browser window, accessible via a local web server.

```python
ft.app(
    target=app.main,
    assets_dir="assets",
    view=ft.WEB_BROWSER,
    host="0.0.0.0",
    port=8550
)
```

Open your browser and visit:  
`http://localhost:8550`

![insta-output1](https://github.com/user-attachments/assets/5ac16415-f934-4493-840e-758843b0d351)

![insta-output2](https://github.com/user-attachments/assets/d6222f96-b08b-41ce-9a35-04d647e784c5)


---

## 🛠️ Usage

- Interact with the UI elements as designed.  
- When running in web mode, the app will be reachable at the address shown in the console (default: `http://localhost:8550`).  
- Stop the app anytime with `Ctrl+C` in your terminal.

---

## 🐞 Troubleshooting

- If you face errors about missing modules, double-check dependencies with:  
```bash
pip install -r requirements.txt
```

- Verify your Python version is 3.7 or higher.  
- If the app does not open automatically in your browser, try opening the URL manually.  

---

## 🤝 Contributing

Feel free to open issues or submit pull requests!  

Please follow the existing style and keep commits clear and descriptive.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

If you have any questions or need help, open an issue or contact the maintainer.  

**Enjoy building with Flet! 🚀**

---

## 👤 Authors

- [Amirali Bahramjerdi](https://github.com/AmirAli-BahramJerdi)
