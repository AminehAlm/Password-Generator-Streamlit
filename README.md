# 🔐 Streamlit Password Generator

An interactive **Password Generator App** built with **Streamlit**.  
It allows you to generate **Random**, **Memorable**, or **Numeric (PIN)** passwords — each customizable and rated for entropy-based strength.

---

## 📑 Table of Contents

1. [Features](#features)  
2. [How it Works](#how-it-works)  
3. [Installation and Setup](#installation-and-setup)  
4. [Example Gameplay](#example-gameplay)  
5. [File Structure](#file-structure)  
6. [Tech Stack](#tech-stack)  
7. [Future Improvements](#future-improvements)  
8. [Author](#author)  
9. [License](#license)  

---

## 🌟 Features

| Feature | Description |
|---------|-------------|
| Random Password | Customizable mix of letters, digits, and symbols |
| Memorable Password | Word-based, easy to remember but secure |
| Pincode | Numeric passwords for simple use cases |
| Entropy Calculation | Shows password strength in bits (Weak → Strong → Excellent) |
| Custom Options | Choose password length, include symbols/letters/digits, letter case, and separators |
| Symbol Replacement | Optional letter replacement (`a → @`, `o → 0`, `l → |`, `i → !`) |
| Session State | Keeps generated password visible across reruns |
| Optimized Performance | Cached word list from NLTK for efficiency |

---

## ⚙️ How it Works

1. **Random Password:**  
   - User selects length, character types (digits, letters, symbols), and letter case.  
   - The app generates a secure random password using Python's `secrets` module.  

2. **Memorable Password:**  
   - User selects number of words and separator.  
   - Words are sampled randomly from a filtered NLTK corpus (`brown`) excluding stopwords.  
   - Optional symbol replacement enhances security while keeping it memorable.  

3. **Pincode:**  
   - User selects numeric password length.  
   - A secure random number sequence is generated.  

- The app calculates **entropy** for each password and shows its strength.

---

## 🛠 Installation and Setup

1. **Clone the repository**
```bash
git clone https://github.com/<your-username>/password-generator-app.git
cd password-generator-app
```
**2.	Create a virtual environment (optional but recommended)**
```
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```
**3.	Install dependencies**
```
pip install -r requirements.txt
```
**4.	Run the app**
```
streamlit run app.py
```
**5.	Open in browser**
Visit http://localhost:8501

## 🎮 Example Gameplay

**Random Password:**
```
u8#Yb9zK@
Entropy: 59.79 bits → 🥇 Strong Password
```
**Memorable Password:**
```
river@Light@forest@moon
Entropy: 100.21 bits → 🏆 Excellent! Very Strong Password 🎊
```
**Pincode:**
```
493851
Entropy: 19.93 bits → ⚠️ Weak Password
```

## 🗂 File Structure
```
password-generator-app/
│
├── pass-generator-streamlit.py                # Main application script
├── requirements.txt      # Python dependencies
├── .gitignore            # Ignore unnecessary files
└── README.md             # Project documentation
```
## 🖥 Tech stack
This project uses the following technologies:
	•	Python – Core logic and functionality
	•	Streamlit – Interactive web interface
	•	NLTK – Word corpus for generating memorable passwords
	•	Secrets & Math modules – Secure random generation & entropy calculation
	•	String module – Predefined character sets for random passwords

## 🔮 Future Improvements
	•	Add password history to save previously generated passwords
	•	Enhance memorable password security with additional transformations
	•	Add user authentication for personalized settings
	•	Add export options (CSV, TXT) for generated passwords
	•	Support for multiple languages in memorable passwords

## 🧑‍💻 Author
Amineh Alimohammadi
💼 [LinkedIn](www.linkedin.com/in/amineh-alimohammadi)￼ | 🐙 🔗 [GitHub Profile](https://github.com/AminehAlm)**
