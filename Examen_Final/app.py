from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def menu():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])

        precio_unitario = 9000
        total_bruto = precio_unitario * cantidad

        if edad < 18:
            descuento = 0
        elif 18 <= edad <= 30:
            descuento = 0.15
        else:
            descuento = 0.25

        monto_descuento = total_bruto * descuento
        total_final = total_bruto - monto_descuento

        return render_template('ejercicio1.html',
                               nombre=nombre,
                               total_bruto=total_bruto,
                               monto_descuento=monto_descuento,
                               total_final=total_final)
    return render_template('ejercicio1.html')


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = None
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        # Diccionario de usuarios válidos
        usuarios_validos = {
            "juan": "1234",
            "pepe": "1234"
        }

        if usuario in usuarios_validos and contrasena == usuarios_validos[usuario]:
            mensaje = f"Bienvenido Administrador {usuario}"
        else:
            mensaje = "Usuario o contraseña incorrectos."

    return render_template('ejercicio2.html', mensaje=mensaje)


if __name__ == '__main__':
    app.run(debug=True)
