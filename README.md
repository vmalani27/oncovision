# Skin Cancer Detection Web Application

This web application provides information about skin cancer types, prevention methods, and uses machine learning to analyze skin lesions for potential cancer detection.

## Features

- Comprehensive information about different types of skin cancer
- Prevention guidelines and best practices
- AI-powered skin lesion analysis
- Modern, responsive user interface
- Educational content about skin health

## Prerequisites

- Python 3.8 or higher
- TensorFlow 2.8.0
- Flask 2.0.1
- Other dependencies listed in requirements.txt

## Installation

1. Clone the repository:
```bash
git clone https://github.com/vmalani27/oncovision
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Ensure you have the trained model file (`mobilenetv2_skin_cancer.h5`) in the root directory. (not necessary now)

## Running the Application

1. Activate the virtual environment (if not already activated):
```bash
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Start the Flask application:
```bash
python app.py
```

3. Open your web browser and navigate to:
```
http://localhost:5000
```

## Project Structure

```
skin-cancer-detection/
├── app.py                 # Main Flask application
├── mobilenetv2_skin_cancer.h5  # Trained model
├── requirements.txt       # Python dependencies
├── templates/            # HTML templates
│   ├── base.html        # Base template
│   ├── index.html       # Homepage
│   ├── types.html       # Skin cancer types
│   ├── prevention.html  # Prevention information
│   └── predict.html     # Prediction interface
└── README.md            # This file
```

## Important Notes

- This application is for educational and informational purposes only
- The AI model is not a substitute for professional medical advice
- Always consult healthcare providers for proper diagnosis and treatment
- The model's predictions should be used as a preliminary screening tool

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
