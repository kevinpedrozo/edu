from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/estudiantes")
def estudiantes():
    return render_template("estudiantes.html")

@app.route("/profesores")
def profesores():
    return render_template("profesores.html")

@app.route("/cursos")
def cursos():
    return render_template("cursos.html")

@app.route("/notas")
def notas():
    return render_template("notas.html")

@app.route("/asistencia")
def asistencia():
    return render_template("asistencia.html")

@app.route("/reportes")
def reportes():
    return render_template("reportes.html")

if __name__ == "__main__":
    app.run(debug=True)
