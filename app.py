from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
import forms
from models import Alumnos, db

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/")
@app.route("/index")
def index():
    create_form = forms.UserForm2(request.form)  # Crea el formulario
    alumno = Alumnos.query.all()  # Obtén todos los alumnos para mostrar en la tabla
    return render_template("index.html", form=create_form, alumno=alumno)

@app.route("/Alumnos1", methods=['POST'])
def Alumnos1():
    create_form = forms.UserForm2(request.form)  # Crea el formulario con los datos enviados
    if request.method == "POST":  # Valida el formulario
        alum = Alumnos(
            nombre=create_form.nombre.data,
            apaterno=create_form.apaterno.data,
            email=create_form.email.data
        )
        db.session.add(alum)  # Agrega el nuevo alumno a la base de datos
        db.session.commit()  # Guarflash("Alumno agregado correctamente", "success")da los cambios
          # Mensaje de éxito
    else:
        flash("Error al agregar el alumno", "error")  # Mensaje de error si el formulario no es válido
    return redirect(url_for('index'))  # Redirige al index después de procesar el formulario

@app.route('/modificar', methods=["GET", "POST"])
def modificar():
    create_form = forms.UserForm2(request.form)

    if request.method == "GET":
        id = request.args.get('id')  # Obtener el ID del alumno desde la URL
        alum = db.session.query(Alumnos).filter(Alumnos.id == id).first()  # Buscar el alumno en la base de datos
        if alum:
            # Precargar los datos del alumno en el formulario
            create_form.id.data = id
            create_form.nombre.data = alum.nombre
            create_form.apaterno.data = alum.apaterno  # Asegúrate de precargar "apaterno"
            create_form.email.data = alum.email
        else:
            flash("Alumno no encontrado", "error")
            return redirect(url_for('index'))
    elif request.method == "POST":
        # Lógica para guardar los cambios
        id = create_form.id.data
        alum = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        if alum:
            alum.nombre = create_form.nombre.data
            alum.apaterno = create_form.apaterno.data  # Asegúrate de actualizar "apaterno"
            alum.email = create_form.email.data
            db.session.commit()
           
        else:
            flash("Alumno no encontrado", "error")
        return redirect(url_for('index'))

    # Renderizar index.html con el modal de modificar abierto
    alumno = Alumnos.query.all()  # Obtener todos los alumnos para la tabla
    return render_template("index.html", form=create_form, alumno=alumno, modificar_modal=True)

@app.route("/eliminar", methods=["GET", "POST"])
def eliminar():
    create_form = forms.UserForm2(request.form)
    if request.method == "GET":
        id = request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_form.id.data = request.args.get('id')
        create_form.nombre.data = alum1.nombre
        create_form.apaterno.data = alum1.apaterno
        create_form.email.data = alum1.email
    if request.method == "POST":
        id = create_form.id.data
        alum = Alumnos.query.get(id)
        db.session.delete(alum)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("eliminar.html", form=create_form)

if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()