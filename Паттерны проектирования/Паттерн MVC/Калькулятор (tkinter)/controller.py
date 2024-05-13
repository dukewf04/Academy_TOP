def logicalc(app, operation):
    try:
        if operation == "C":
            app.formula = ""
        elif operation == "DEL":
            app.formula = app.formula[0:-1]
        elif operation == "X^2":
            app.formula = str((eval(app.formula)) ** 2)
        elif operation == "%":
            app.formula = str(eval(app.formula) / 100)
        elif operation == "=":
            app.formula = str(eval(app.formula))
        else:
            if app.formula == "0":
                app.formula = ""
            app.formula += operation
    except:
        pass

    update(app)


def update(app):
    if app.formula == "":
        app.formula = "0"

    app.lbl.configure(text=app.formula)
