from flask import Flask, render_template, abort
from xml import etree
app = Flask (__name__)

@app.route('/')
def inicio():
    return render_template("inicio.html")

@app.route('/potencia/<base>/<exponente>')
def potencia(base,exponente):
    try:
        base=int(base)
        exponente=int(exponente)
    except:
        abort(404)
    if exponente > 0:
        resultado = base**exponente
    elif exponente == 0:
        resultado = 1
    elif exponente < 0:
        resultado = 1/(base**abs(exponente))
    return render_template("potencia.html",ba=base,ex=exponente,res=resultado)

@app.route('/cuenta/<cad1>/<cad2>')
def contar(cad1,cad2):
    if len(cad2) == 1:
        aparece = cad1.count(cad2)
    else:
        abort(404)
    return render_template("contar.html",palabra=cad1,letra=cad2,apariciones=aparece)

@app.route('/libro/<int:codigo>')
def buscar(codigo):
    doc = etree.parse('libros.xml')
    if str(codigo) in doc.xpath("/biblioteca/libro/codigo/text()"):
        titulo=doc.xpath("/biblioteca/libro[codigo/text()='%s']/titulo/text()"%codigo)[0]
        autor=doc.xpath("/biblioteca/libro[codigo/text()='%s']/autor/text()"%codigo)[0]
    else:
        abort(404)
    return render_template("buscar.html",titulo=titulo,autor=autor)

app.run(debug=True)
