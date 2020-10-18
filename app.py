from flask import Flask, render_template, send_file, request
# import flask

# variable app = struct Flask(name);
app = Flask(__name__)

#Json pair
links = {
    "github": "https://www.github.com",
    "facebook": "https://www.facebook.com",
    "linkedin": "https://www.linkedin.com/in/qianqian-wan-a32717170/"
}

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST": # POST request
        with open("../static/resume.pdf", "rb") as f:
            return send_file(f, attachment_filename="Karin Wan. Resume")
    else: # GET request
        return render_template("index0.html", links=links)

@app.route('/home/<name>')
def homepage(name):
    return "<h1>Hello</h1>" + name

# ↓ Fixed, tell compile to run the program from here. 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    # app.run(debug=True, host='0.0.0.0', port = '5000')
