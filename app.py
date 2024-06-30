from scripts.webchecker import run_lighthouse_command

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():
    if request.method == "POST":
        url = request.form.get("user-input-url")
        if request.form.get("view") == "desktop-view":
            run_lighthouse_command(url, view="desktop")
        run_lighthouse_command(url)
        return render_template('report.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True) 
