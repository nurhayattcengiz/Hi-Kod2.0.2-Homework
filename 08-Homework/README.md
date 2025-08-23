# 🎓 Student Performance Analysis

This project analyzes student performance data based on gender, race/ethnicity, parental education level, lunch type, and test preparation course. It uses Python libraries such as `pandas`, `matplotlib`, and `seaborn` for data exploration and visualization.

# Dataset

- **Source**: [Students Performance Dataset](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)
- **File name**: `students_performance.csv`
- **Features**:
  - `gender`
  - `race/ethnicity`
  - `parental level of education`
  - `lunch`
  - `test preparation course`
  - `math score`, `reading score`, `writing score`

# Analysis Steps

1. Load and preview the dataset
2. Count gender distribution and visualize with histogram
3. Explore race/ethnicity groups and visualize
4. Identify unique values in parental education and lunch types
5. Count participants by lunch and test preparation course
6. Calculate average scores grouped by:
   - Gender
   - Race/Ethnicity
   - Parental Education
   - Lunch Type
   - Test Preparation Course

# Visualizations

- Gender distribution (`countplot`)
- Race/Ethnicity distribution (`countplot`)
- All plots created using `matplotlib` and `seaborn`

# Technologies Used

- Python 3.x  
- pandas  
- matplotlib  
- seaborn  

# How to Run

```bash
python student_analysis.py
