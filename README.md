# Spam Email Detection App

A machine learning-based GUI application to detect spam emails and messages using a trained Naive Bayes classifier.

## Features

- **GUI Interface** - User-friendly tkinter-based graphical interface
- **Real-time Detection** - Instantly classify messages as spam or not spam
- **Machine Learning** - Uses TF-IDF vectorization with Multinomial Naive Bayes
- **Simple & Fast** - Quick message classification

## Requirements

- Python 3.8+
- pandas
- scikit-learn
- joblib
- tkinter (usually comes with Python)

## Installation

1. Install required packages:
```bash
pip install pandas scikit-learn joblib
```

2. Navigate to the project directory:
```bash
cd c:\Users\Jyoti\OneDrive\Desktop\python_project\.dist
```

## How to Use

### Step 1: Train the Model
First, run the training script to create the model files:

```bash
python main.py
```

This will:
- Load the dataset from `dataset.cv`
- Train a Naive Bayes classifier
- Save the trained model and vectorizer as pickle files (`spam_model.pkl`, `vectorizer.pkl`)

### Step 2: Run the App
Launch the GUI application:

```bash
python app.py
```

### Step 3: Detect Spam
1. Type or paste a message in the text box
2. Click the **"Check"** button
3. The result will appear below:
   - ✅ **Not Spam** (green) - Regular message
   - ❌ **Spam Message** (red) - Spam detected

## Project Structure

```
python_project/
├── .dist/
│   ├── main.py           # Training script
│   ├── app.py            # GUI application
│   ├── dataset.cv        # Training dataset
│   ├── requirements.txt   # Dependencies
│   └── README.md
├── README.md             # This file
└── .qodo/               # Project metadata
```

## Files Description

- **main.py** - Trains the spam detection model
  - Loads dataset
  - Vectorizes text using TF-IDF
  - Trains Multinomial Naive Bayes classifier
  - Saves model and vectorizer

- **app.py** - GUI application
  - Loads trained model and vectorizer
  - Provides user interface for message input
  - Displays spam detection results

- **dataset.cv** - Training data (CSV format)
  - Contains messages labeled as ham (0) or spam (1)

## Dataset Format

The `dataset.cv` file should have the following structure:
```
message,label
"Hello there!",ham
"Click here to win FREE money!!!",spam
...
```

## How It Works

1. **Data Loading** - Reads messages and labels from CSV
2. **Text Vectorization** - Converts text to numerical features using TF-IDF
3. **Model Training** - Trains Naive Bayes classifier
4. **Prediction** - Takes user input and classifies as spam or ham
5. **Display Result** - Shows result with color coding

## Troubleshooting

| Issue | Solution |
|-------|----------|
| ModuleNotFoundError | Install missing packages: `pip install pandas scikit-learn joblib` |
| FileNotFoundError (pkl files) | Run `main.py` first to train the model |
| FileNotFoundError (dataset.cv) | Ensure `dataset.cv` is in the `.dist/` folder |
| App window not showing | Close and restart with: `python app.py` |

## Example Usage

```
Input: "Congratulations! You won a prize! Click here to claim"
Output: ❌ Spam Message (red)

Input: "Hi, how are you doing?"
Output: ✅ Not Spam (green)
```

## Future Improvements

- Add email integration
- Improve model accuracy with more training data
- Add model performance metrics display
- Support for multiple languages
- Save prediction history

## Author

Created for spam detection project

## License

Open source - feel free to use and modify
