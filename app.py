from flask import Flask, render_template

app = Flask(__name__)

# Define the label mapping for display purposes
label_mapping = {
    'bkl': 'Benign',
    'nv': 'Benign',
    'df': 'Benign',
    'mel': 'Malignant',
    'vasc': 'Benign',
    'bcc': 'Malignant',
    'akiec': 'Pre-cancerous'
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/types')
def types():
    return render_template('types.html', label_mapping=label_mapping)

@app.route('/prevention')
def prevention():
    return render_template('prevention.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

if __name__ == '__main__':
    app.run(debug=True) 