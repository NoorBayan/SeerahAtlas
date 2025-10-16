# SeerahAtlas: The Prophetic Sustainability Atlas

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

This repository hosts the data, code, and interactive visualizations for the "Prophetic Sustainability Atlas," a digital humanities project that analyzes the integrated system of sustainability within the prophetic guidance (Sunnah).

This project addresses the "knowledge fragmentation" of sustainability-related teachings in Islamic texts by creating a unified, data-driven framework. We apply computational methods to transform scattered hadith into an explorable, holistic model of environmental, health, and social well-being.

---

## 📖 Table of Contents
*   [About the Project](#about-the-project)
*   [Key Features](#key-features)
*   [Technology Stack](#technology-stack)
*   [The Corpus](#the-corpus)
*   [Installation & Setup](#installation--setup)
*   [How to Use](#how-to-use)
*   [Project Structure](#project-structure)
*   [Key Findings & Visualizations](#key-findings--visualizations)
*   [How to Cite This Work](#how-to-cite-this-work)
*   [License](#license)
*   [Contact](#contact)

---

## 🌟 About the Project

The teachings of Prophet Muhammad (ﷺ) contain a wealth of guidance on environmental stewardship, public health, and social justice. However, these directives are dispersed across vast collections of hadith literature, making it difficult to grasp the integrated system they form.

This project bridges the gap between classical Islamic sciences and modern data science to build the **Prophetic Sustainability Atlas**. We have created a comprehensive digital corpus of prophetic teachings on sustainability and employed Natural Language Processing (NLP) and Network Analysis to uncover the deep structural connections within this system.

The goal is to move beyond a fragmented reading of individual texts and reveal the complete, interconnected "ecosystem" of prophetic sustainability.

---

## ✨ Key Features

1.  **📊 The Prophetic Sustainability Corpus:** A first-of-its-kind, structured, and machine-readable dataset of hundreds of prophetic traditions, semantically annotated across the three pillars of sustainability: **Environmental**, **Health**, and **Social**.
2.  **🧠 AI-Powered Thematic Analysis:** Using **Topic Modeling (LDA)**, we have identified the core themes and priorities within the prophetic discourse on sustainability, providing a quantitative, unbiased view of its primary areas of focus.
3.  **🕸️ Conceptual Network Analysis:** We have built a knowledge graph that maps the relationships between key concepts (e.g., 'moderation', 'purity', 'justice', 'mercy'). This analysis reveals the "bridging values" that integrate the different domains of sustainability into a single, cohesive system.
4.  **🌐 Interactive Knowledge Atlas:** A web-based platform that visualizes the project's findings, allowing users to explore the data, analyze trends, and understand the holistic nature of the prophetic model.

---

## 🛠️ Technology Stack

*   **Data Processing & Analysis:** Python (Pandas, NLTK, Scikit-learn)
*   **Topic Modeling:** Gensim
*   **Network Analysis:** NetworkX
*   **Data Storage:** CSV / JSON
*   **Interactive Visualizations:** D3.js, Plotly
*   **Development Environment:** Jupyter Notebooks

---

## 🗃️ The Corpus

The foundation of this project is the **Prophetic Sustainability Corpus**, a manually curated and annotated dataset (`prophetic_sustainability_corpus.csv`).

Each entry in the corpus contains:
*   The original Hadith text (in Arabic and English translation).
*   Source and authenticity grade.
*   **Primary Domain:** Environmental, Health, or Social.
*   **Sub-category:** (e.g., Water Conservation, Dietary Habits, Neighbor's Rights).
*   **Keywords & Concepts:** A list of annotated semantic tags.
*   **Chronological Context:** Meccan or Medinan period, where applicable.

This dataset is provided in the `/data` directory and is available for other researchers to use and build upon.

---

## ⚙️ Installation & Setup

To replicate our analysis and explore the data, please follow these steps:

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/your-username/prophetic-sustainability-atlas.git
    cd prophetic-sustainability-atlas
    ```

2.  **Set up a Python virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```

3.  **Install the necessary libraries:**
    ```sh
    pip install -r requirements.txt
    ```

---

## 🚀 How to Use

The entire analytical workflow is documented in Jupyter Notebooks located in the `/notebooks` directory.

1.  **Start Jupyter Lab:**
    ```sh
    jupyter lab
    ```
2.  **Run the notebooks in order:**
    *   `1_Corpus_Exploration.ipynb`: Load and explore the annotated dataset.
    *   `2_Topic_Modeling.ipynb`: Execute the LDA topic modeling to discover latent themes.
    *   `3_Concept_Network_Analysis.ipynb`: Build and analyze the network of sustainability concepts.

---

## 📁 Project Structure

```
prophetic-sustainability-atlas/
├── data/
│   └── prophetic_sustainability_corpus.csv   # The core annotated dataset
│
├── notebooks/
│   ├── 1_Corpus_Exploration.ipynb
│   ├── 2_Topic_Modeling.ipynb
│   └── 3_Concept_Network_Analysis.ipynb
│
├── visualizations/
│   ├── atlas_webapp/                         # Source code for the interactive web atlas
│   └── static_plots/                         # Saved charts and graphs from the notebooks
│
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🔬 Key Findings & Visualizations

Our analysis has produced several innovative visualizations that form the core of the Atlas:

*   **The Prophetic "Sustainability Footprint":** This visualization compares the thematic focus of the prophetic model with contemporary sustainability frameworks (like the UN SDGs), highlighting its unique priorities and holistic nature.

    ![Sustainability Footprint](https://via.placeholder.com/600x350.png?text=Prophetic+Sustainability+Footprint+Chart)
    *(Replace with an actual image of your chart)*

*   **The Integration Network:** Our concept network graph visually demonstrates the interconnectedness of the system. It reveals that values like **moderation (al-wasatiyyah)** and **mercy (rahmah)** act as central nodes, bridging environmental ethics with social justice and health practices.

    ![Concept Network](https://via.placeholder.com/600x350.png?text=Concept+Network+Graph)
    *(Replace with an actual image of your network graph)*

*   **Dynamic Timeline of Revelation:** By analyzing the data chronologically, the Atlas provides insights into the evolution of sustainability awareness and emphasis between the Meccan and Medinan periods.

---

## ✍️ How to Cite This Work

If you use the data, code, or findings from this project in your research, please cite our work:

> [Your Name/Team Name]. (Year). "The Prophetic Sustainability Atlas: A Computational Analysis of Sustainability in the Prophetic Guidance". *Journal/Conference Name*, Volume(Issue), pp. Page-Numbers. [DOI/URL]

---

## 📜 License

This project is distributed under the MIT License. See the `LICENSE` file for more information.

---

## 📬 Contact

**Principal Investigator:** [Your Name] – [youremail@example.com]

Project Link: [https://github.com/your-username/prophetic-sustainability-atlas](https://github.com/your-username/prophetic-sustainability-atlas)
