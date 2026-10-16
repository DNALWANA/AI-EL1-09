# SYSTEM REKOMENDASI METODE BELAJAR
An expert system for study method recommendations built with **Python**, utilizing a **Rule-Based Expert System** and **Forward Chaining** inference engine. This project features a robust knowledge base containing conditional rules (IF-THEN) designed to diagnose a student's learning challenges, habits, and preferences, providing personalized learning strategies (such as Active Recall, Spaced Repetition, Feynman Technique, and more) along with a complete explanation trace.

## Key Features

* **Forward Chaining Inference Engine:** Automatically evaluates rules iteratively, matching facts from the working memory to derive conclusions until no new facts are found.
* **Interactive Questioning:** Dynamically collects user inputs regarding study habits, time availability, target grades, and learning preferences.
* **Explanation Facility:** Traces and displays the exact reason and rule IDs (R01–R19) that led to each recommendation.
* **Working Memory Tracking:** Records and lists all active facts and fired rules for full transparency and debugging.

## Screenshots

| Main Menu | Choose Learning Problem | Learning Recommendation |Conclusion |
| :---: | :---: | :---: | :---: |
| ![Menu](./assets/---) | ![Choose](./assets/--) | ![Req](./assets/--) | ![Conclusion](./assets/--) |


## Limitations

### 1. Static Rule Base
   The system relies entirely on predefined rules and cannot learn or adapt new rules automatically from user interactions.
### 2. Mutually Exclusive Inputs
   User inputs are gathered sequentially via predefined menus and binary prompts, which might not fully capture complex or overlapping learning behaviors.
### 3. Requirements & Dependencies
To run this project, you only need Python installed with standard libraries:

* Python 3.x (no external third-party libraries required)

## Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/DNALWANA/AI-EL1-09.git
    ```

2.  **Search Folder**
    ```bash
    cd "Pertemuan 4/Expert System/Manager"
    ```

3.  **Verify Python Installation**
    ```bash
    python3 --version
    ```

## Usage
```bash
python3 Gabungan.py
```

## How to run the program

### 1. Setup Conditions
Answer the interactive prompt questions based on your study habits, difficulties, time constraints, and preferences.
### 2. Processing
Let the Forward Chaining inference engine automatically evaluate your inputs against the knowledge base rules.
### 3. View Recommendations
Review the tailored study methods, explanation trace, and final working memory facts generated in the terminal.



