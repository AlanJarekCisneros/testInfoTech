import pypdftk
import os

def main():
    archivo_formulario = 'formulario.pdf'
    archivo_salida = 'formulario_rellenado.pdf'

    # Aqui de verfifica si existe el archivo
    if not os.path.exists(archivo_formulario):
        print(f"El archivo '{archivo_formulario}' no se encuentra en la carpeta actual.")
        return

    try:
        # Aqui se obtienen los nombres de los campos del formulario
        data_fields = pypdftk.dump_data_fields(archivo_formulario)
        nombres_campos = [field['FieldName'] for field in data_fields]

        # Aqui se imprimen en consola de los nombres de los campos
        print("Nombres de campos en el formulario:")
        for nombre in nombres_campos:
            print(nombre)

        # Aqui se rellena los campos con el formato de "Valor de: (nombre del campo)"
        datos_ejemplo = {campo: f"Valor de {campo}" for campo in nombres_campos}
        #Aqui use algunos nombres de los campos para rellenarlos con datos especificos
        datos_ejemplo['CONTRATISTARow1'] = 'Alan Cisneros'
        datos_ejemplo['CONTRATORow1'] = 'PRUEBA'
        datos_ejemplo['PROCEDIMIENTORow1'] = 'PRUEBA2'
        datos_ejemplo['DEL'] = 'PRUEBA3'
        datos_ejemplo['AL'] = 'PRUEBA4'
        datos_ejemplo['nombre_aprobo'] = 'Alvin Yakitori'
        datos_ejemplo['cargo_aprobo'] = 'Supervisor'
        datos_ejemplo['nombre_superviso'] = 'Jefferson Gutierritos'
        datos_ejemplo['cargo_superviso'] = 'Adminsitrador'
        datos_ejemplo['nombre_elaboro'] = 'Ramon Valdez'
        datos_ejemplo['cargo_elaboro'] = 'Jefe de Area'
        

    #Aqui se rellena el pdf
        pypdftk.fill_form(archivo_formulario, datas=datos_ejemplo, out_file=archivo_salida)

        print(f"El formulario ha sido rellenado y se guardo como '{archivo_salida}'.")

    except Exception as e:
        print(f"Ocurrió un error al procesar el archivo PDF: {e}")

if __name__ == "__main__":
    main()
