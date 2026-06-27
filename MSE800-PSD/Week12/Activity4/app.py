import os
from flask import Flask, request, render_template_string, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configure the folder where images will be saved
UPLOAD_FOLDER = os.path.join("static", "uploads")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Define the HTML page
HTML_PAGE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Week 12 - Activity 4</title>
</head>
<body>
    <h1>Week 12 - Activity 4: Load and Show an Image</h1>
    
    <form method="post" enctype="multipart/form-data">
        <input type="file" name="image" accept="image/*">
        <button type="submit">Upload</button>
    </form>

    {% if filename %}
        <hr>
        <h3>Displaying: {{ filename }}</h3>
        <img src="{{ url_for('static', filename='uploads/' + filename) }}" 
             alt="uploaded image" width="300">
    {% endif %}
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def learn():
    filename = None
    if request.method == "POST":
        # Get the file from the request
        file = request.files.get("image")
        if file and file.filename:
            # Get the filename
            filename = secure_filename(file.filename)
            # Save the file
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
    # Render the HTML string defined above
    return render_template_string(HTML_PAGE, filename=filename)

if __name__ == "__main__":
    app.run(debug=True)