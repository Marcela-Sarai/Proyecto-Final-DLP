import os
import pandas as pd
import matplotlib.pyplot as plt
import datetime


def limpiarPantalla():
  """
  Función que limpia la pantalla de la consola.
  """
  os.system('pause')
  os.system('cls')

def sesionAdmin():
  """
  Función que muestra el menú principal y las opciones disponibles para el administrador.
  Permite al administrador seleccionar una opción y realizar las acciones correspondientes.
  """
  while True:
    print("\t\tBienvenido a la tienda\n")
    print("\t\tSeleccione una opción:")
    print("\n(1) Registrar producto"
        "\n(2) Listar productos"
        "\n(3) Buscar producto"
        "\n(4) Eliminar producto"
        "\n(5) Modificar producto"
        "\n(6) Generar reporte"
        "\n(7) Agregar entrada"
        "\n(8) Salir\n"
    )
    try:
      opcion = int(input('Elige una opción: '))
      os.system('cls')
      match opcion:
        case 1:
          print('\n\t\tRegistro de productos\n')
          registrarProducto()
          limpiarPantalla()
          
        case 2:
          print('\n\t\tLitar productos\n')
          listarProductos()
          limpiarPantalla()

        case 3:
          print('\n\t\tBuscar producto\n')
          buscarProducto()
          limpiarPantalla()

        case 4:
          print('\n\t\tEliminar producto\n')
          eliminarProducto()
          limpiarPantalla()

        case 5:
          print('\n\t\tModificar producto\n')
          modificarProducto() 
          limpiarPantalla()
        case 6:
          print('\n\t\t Generar reporte de ventas\n')
          generarReporteVentas()
          limpiarPantalla()
        case 7: 
          print('\n\t\t Agregar entrada\n')
          registrarEntrada()
          limpiarPantalla()
        case 8:
          break
        case _:
          print('Opción no válida')
          sesionAdmin()
    except ValueError:
      print('Opción no válida')
      limpiarPantalla()
      sesionAdmin()

def sesionVendedor():
  """
  Función que muestra el menú principal y las opciones disponibles para el vendedor.
  Permite al vendedor seleccionar una opción y realizar las acciones correspondientes.
  """
  while True:
    print("\t\tBienvenido a la tienda\n")
    print("\t\tSeleccione una opción:")
    print("\n(1) Listar producto producto"
        "\n(2) Buscar productos"
        "\n(3) Registrar una venta"
        "\n(4) Salir\n"
    )
    try:
      opcion = int(input('Elige una opción: '))
      os.system('cls')
      match opcion:
        case 1:
          print('\n\t\tLitar productos\n')
          listarProductos()
          limpiarPantalla()
        
        case 2:
          print('\n\t\tBuscar producto\n')
          buscarProducto()
          limpiarPantalla()
        
        case 3:
          print('\n\t\tRegistrar una venta\n')
          registrarSalida()
          limpiarPantalla()
        
        case 4:
          print('\n\t\tGracias por usar el programa\n')
          break
        case _:
          print('\n\t\tOpción no válida')
          sesionVendedor()
    except ValueError:
      print('Opción no válida')
      limpiarPantalla()
      sesionVendedor()

def registrarProducto():
  """
  Función que registra un nuevo producto.
  Solicita al usuario ingresar los datos del producto y los guarda en un archivo CSV.
  """
  archivo = open("productos.csv", "a")
  
  try:
    nombreProducto = str(input("Ingrese el nombre del producto: "))
    precioProducto = float(input("Ingrese el precio unitario producto: "))
    cantidadProducto = int(input("Ingrese la cantidad del producto: "))

    precioTotal = precioProducto * cantidadProducto
    fechaActual = datetime.date.today().strftime( "%d/%m/%Y")

    archivo.write(nombreProducto + "," + str(fechaActual) + "," + str(precioProducto) + "," + str(precioTotal) + "," + str(cantidadProducto) + "," + ","+ str(cantidadProducto) + "\n")
    archivo.close()
  except:
    print('Error al ingresar los datos')
    os.system('pause')
    os.system('cls')
    registrarProducto()

def listarProductos():
  """
  Función que lista todos los productos registrados.
  Lee los datos del archivo CSV y muestra la información en forma de tabla.
  """
  df = pd.read_csv('productos.csv')
  print(df.to_string(index=False))

def buscarProducto():
  """
  Función que busca un producto por su nombre.
  Lee los datos del archivo CSV y muestra la información del producto si es encontrado.
  """
  try:
    df = pd.read_csv("productos.csv")
    
    nombreProducto = str(input("Ingrese el nombre del producto a buscar: "))
    
    producto = df.iloc[df.index[df['NOMBRE'] == nombreProducto].tolist()[0], :]
    
    if not producto.empty:
      print(f"{'NOMBRE':<16}{'FECHA':<16}{'PRECIO UNITARIO':<16}{'PRECIO TOTAL':<16}{'ENTRADAS':<16}{'SALIDAS':<16}{'STOCK':<16}")
      print(f"{producto['NOMBRE']:<16}{producto['FECHA']:<16}{producto['PRECIO UNITARIO']:<16}{producto['PRECIO TOTAL']:<16}{producto['ENTRADAS']:<16}{producto['SALIDAS']:<16}{producto['STOCK']:<16}")
    else:
      print("El Producto no fue encontrado")
  except Exception as e:
    print("El Producto no fue encontrado")
    print(f"Error: {e}") 
    os.system('pause')
    os.system('cls')

def eliminarProducto():
  """
  Función que elimina un producto por su nombre.
  Lee los datos del archivo CSV, busca el producto y lo elimina del DataFrame.
  """
  df = pd.read_csv('productos.csv')

  nombreProducto = str(input('Nombre del producto: '))
  try:
    idice = df.index[df['NOMBRE'] == nombreProducto].tolist()[0]
    df.drop([idice], axis=0, inplace=True)
    df.to_csv('productos.csv',index=False)
    print(f'El {nombreProducto} fue eliminado correctamente')
  except Exception as e:
    print('Producto no encontrado')
    print(f'Error: {e}')
    limpiarPantalla()
    eliminarProducto()

def registrarSalida():
  """
  Función que registra una salida de productos.
  Lee los datos del archivo CSV, actualiza la cantidad de salidas y el stock del producto.
  """
  try:
    df = pd.read_csv('productos.csv')

    nombreProducto = str(input('Nombre del prodcuto: '))
    cantidadProducto = str(input(f'Numero de {nombreProducto}s a vender: '))

    indice = df.index[df['NOMBRE'] == nombreProducto].tolist()[0]

    salidaProducto = df.iloc[indice,5]
    stockActual = df.iloc[indice,6]
  
    if int(stockActual) < int(cantidadProducto):
      print(f'La cantidad de {nombreProducto}s no es suficente para consilidar la venta\n')
    else:
      stock = int(stockActual) - int(cantidadProducto)
      actualizacionSalida = int(salidaProducto) + int(cantidadProducto)

      df.loc[indice,'SALIDAS'] = actualizacionSalida
      df.loc[indice,'STOCK'] = stock
      df.to_csv('productos.csv',index=False)
      actualizarTotal(nombreProducto)
      print('Datos actualizados')
      print(df.to_string(index=False))
  except Exception as e:
    print('Producto no encontrado') 

def registrarEntrada():
  df = pd.read_csv("productos.csv")   #llamo al documento productos
  nombreProducto = input("Ingrese el nombre del producto al que desea registra entrada:  ")  # pido el nombre del producto al usuario
  cantidadAgregada = input("Ingrese la cantidad de productos entrantes:  ")
  indice = df.index[df['NOMBRE'] == nombreProducto].tolist()[0]
  stock = df.iloc[indice,6]
  entradas = df.iloc[indice,4]
  # stock nuevo
  if not indice.empty:
    stockNuevo = int(stock)+int(cantidadAgregada) 
    actual = int(entradas) + int(cantidadAgregada)
    #guardar cambios
    df.loc[indice,'STOCK'] = stockNuevo 
    df.to_csv('productos.csv',index=False)
    actualizarTotal(nombreProducto)
    print('Datos actualizados')
    print(f"{'NOMBRE':<16}{'FECHA':<16}{'PRECIO UNITARIO':<16}{'PRECIO TOTAL':<16}{'ENTRADAS':<16}{'SALIDAS':<16}{'STOCK':<16}")
    print(f"{indice['NOMBRE']:<16}{indice['FECHA']:<16}{indice['PRECIO UNITARIO']:<16}{indice['PRECIO TOTAL']:<16}{indice['ENTRADAS']:<16}{indice['SALIDAS']:<16}{indice['STOCK']:<16}")    
  else:
        print('Producto no encontrado')


def modificarProducto():
      """
      Función que despliega un menú para modificar un producto.
      """
      print("Seleccione una opción:")
      print(" 1. Modificar nombre \n 2. Modificar precio \n")
      opcion = int(input("Ingrese una opción: "))
      try:
        match opcion:
          case 1:
            modificarNombre()
          case 2:
            modificarPrecio()
          case _:
            print("Opción no válida")
            modificarProducto()
      except ValueError:
        print("Ingrese el número de la opción deseada.") 
        modificarProducto()
          

def modificarNombre():
      """
      Esta función modifica el nombre del produto en el archivo CSV.
      """
      
      df = pd.read_csv('productos.csv')

      nombreProducto = input("Ingrese el nombre del producto que desea modificar: ")
      
      producto = df.iloc[df.index[df['NOMBRE'] == nombreProducto].tolist()[0], :]

      if not producto.empty:
        print(f"{'NOMBRE':<16}{'FECHA':<16}{'PRECIO UNITARIO':<16}{'PRECIO TOTAL':<16}{'ENTRADAS':<16}{'SALIDAS':<16}{'STOCK':<16}")
        print(f"{producto['NOMBRE']:<16}{producto['FECHA']:<16}{producto['PRECIO UNITARIO']:<16}{producto['PRECIO TOTAL']:<16}{producto['ENTRADAS']:<16}{producto['SALIDAS']:<16}{producto['STOCK']:<16}")
        nuevoNombre = input("Ingrese el nuevo nombre: ")
        df.loc[df['NOMBRE'] == nombreProducto, 'NOMBRE'] = nuevoNombre
        df.to_csv('productos.csv')
        nuevoNombre = df.iloc[df.index[df['NOMBRE'] == nuevoNombre].tolist()[0], :]
        print("El cambio se realizo on exito.")
        print(f"{'NOMBRE':<16}{'FECHA':<16}{'PRECIO UNITARIO':<16}{'PRECIO TOTAL':<16}{'ENTRADAS':<16}{'SALIDAS':<16}{'STOCK':<16}")
        print(f"{nuevoNombre['NOMBRE']:<16}{nuevoNombre['FECHA']:<16}{nuevoNombre['PRECIO UNITARIO']:<16}{nuevoNombre['PRECIO TOTAL']:<16}{nuevoNombre['ENTRADAS']:<16}{nuevoNombre['SALIDAS']:<16}{nuevoNombre['STOCK']:<16}")
      else:
        print("El Producto no fue encontrado")

def modificarPrecio():
      """
      Esta funcion modifica el precio del producto en el archivo CSV.
      """
      df = pd.read_csv('productos.csv')
      nombreProducto = input("Ingrese el nombre del producto: ")
      locacionProducto = df.iloc[df.index[df['NOMBRE']==nombreProducto].tolist()[0],:]
      if not locacionProducto.empty:
            print(f"{'NOMBRE':<16}{'FECHA':<16}{'PRECIO UNITARIO':<16}{'PRECIO TOTAL':<16}{'ENTRADAS':<16}{'SALIDAS':<16}{'STOCK':<16}")
            print(f"{locacionProducto['NOMBRE']:<16}{locacionProducto['FECHA']:<16}{locacionProducto['PRECIO UNITARIO']:<16}{locacionProducto['PRECIO TOTAL']:<16}{locacionProducto['ENTRADAS']:<16}{locacionProducto['SALIDAS']:<16}{locacionProducto['STOCK']:<16}")
            nuevoPrecio = float(input("Ingrese el nuevo precio: "))
            df.loc[df['NOMBRE']==nombreProducto, 'PRECIO UNITARIO'] = nuevoPrecio
            df.to_csv('productos.csv')
            locacionProducto = df.iloc[df.index[df['NOMBRE']==nombreProducto].tolist()[0],:]
            print("El cambio se realizo con exito")
            print(f"{'NOMBRE':<16}{'FECHA':<16}{'PRECIO UNITARIO':<16}{'PRECIO TOTAL':<16}{'ENTRADAS':<16}{'SALIDAS':<16}{'STOCK':<16}")
            print(f"{locacionProducto['NOMBRE']:<16}{locacionProducto['FECHA']:<16}{locacionProducto['PRECIO UNITARIO']:<16}{locacionProducto['PRECIO TOTAL']:<16}{locacionProducto['ENTRADAS']:<16}{locacionProducto['SALIDAS']:<16}{locacionProducto['STOCK']:<16}")
      else: 
        print("El producto no fue encontrado")



def generarReporteVentas():
  """
  Función que genera un reporte de ventas.
  Lee los datos del archivo CSV, ordena los productos por cantidad de salidas y genera una gráfica.
  """
  df = pd.read_csv('productos.csv')
  #ordenar los datos segun las ventas
  dfOrdenado = df.sort_values('SALIDAS', ascending=False)
  #generar grafica
  dfOrdenado.plot(kind='bar', x='NOMBRE', y='SALIDAS', title='Ventas por producto') #, color=['b','g','r','y','c','k']
  plt.tight_layout()
  fechaActual = datetime.date.today().strftime( "%d-%m-%Y")
  #gurar grafica
  plt.savefig(f'report/Reporte-de-ventas-{fechaActual}.png')
  plt.show()