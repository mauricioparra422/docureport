from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "un-secreto-temporal"          # cámbialo luego

# 📦 memoria temporal para el prototipo
REPORTES = []

@app.route("/", methods=["GET", "POST"])
def formulario():
    if request.method == "POST":
        data = dict(request.form)
        data["fecha_registro"] = datetime.now().strftime("%Y-%m-%d %H:%M")
        REPORTES.append(data)
        flash("✅ Reporte guardado (modo demo).", "success")
        return redirect(url_for("formulario"))
    return render_template("form.html")

@app.route("/admin")
def admin():
    return render_template("admin.html", reportes=REPORTES)

if __name__ == "__main__":
    app.run(debug=True)
