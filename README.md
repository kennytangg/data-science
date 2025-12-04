# Data Science
Fundamental of Data Science final project (semester 3)

> **Note**: This is ongoing undergraduate research. 

## Dataset
For this research, I use the data from January 2024 to December 2024 
- Original plan was using lichess dataset: [Lichess](https://database.lichess.org/)

However the file size is too big, that I change it to a filtered version which is [Lichess Elite](https://database.nikonoel.fr/) . 

## Results
Model Performance by Game Depth

| Move Depth | XGBoost | Neural Network (MLP) | Random Forest | Logistic Regression | Decision Tree |
|------------|---------|---------------------|---------------|---------------------|---------------|
| **Pre-game only** (no moves) | 58.31% | 58.28% | 58.12% | 58.12% | 57.32% |
| **First 10 moves** (20 half-moves) | 58.55% | 58.50% | 58.52% | - | - |
| **First 20 moves** (40 half-moves) | 60.01% | 60.02% | 59.89% | 59.17% | 57.51% |
| **First 30 moves** (60 half-moves) | 62.45% | 62.44% | 62.33% | 61.09% | 59.22% |
| **First 35 moves** (70 half-moves) | 63.19% | 63.25% | 63.08% | 61.74% | 59.66% |
| **First 40 moves** (80 half-moves) | **63.64%** | **63.74%** | **63.55%** | 61.84% | 59.57% |