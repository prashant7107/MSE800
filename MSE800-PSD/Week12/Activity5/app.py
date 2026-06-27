from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = None
    category = None
    w = None
    h = None
    error = None

    if request.method == 'POST':
        try:
            # Get inputs
            w_input = float(request.form.get('weight'))
            h_input = float(request.form.get('height'))
            
            if w_input <= 0 or h_input <= 0:
                error = "Please enter positive values for weight and height."
            else:
                w, h = w_input, h_input
                
                # 4. Calculate BMI
                bmi_value = w / (h ** 2)
                bmi = round(bmi_value, 2)
                
                # 5. Determine category
                if bmi < 18.5:
                    category = 'Underweight'
                elif 18.5 <= bmi < 25:
                    category = 'Normal weight'
                elif 25 <= bmi < 30:
                    category = 'Overweight'
                else:
                    category = 'Obese'
        except (ValueError, TypeError):
            error = "Invalid input. Please enter numeric values."

    return render_template('index.html', bmi=bmi, category=category, weight=w, height=h, error=error)

if __name__ == '__main__':
    app.run(debug=True)