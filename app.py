
import os
from sqlite3.dbapi2 import Date
import time
import re
 
""" cadena="14.235.222-5"
resultado=re.sub('[\.-]','', cadena) """

def tiempo():
    return time.sleep(5)
tiempo()

def clear():
    return os.system("cls")
clear()

import conexion as conn

db=conn.DB()

def salir():
    print('Gracias por utilizar esta aplicación')
    exit()


#GESTIONAR PACIENTES (CREAR, MODIFICAR, ELIMINAR, BUSCAR)

def gestionPaciente():
    option = 0
    salir = 4
    while option != salir:
        print(" [1]    REGISTRAR PACIENTE")
        print(" [2]    MODIFICAR PACIENTE")
        print(" [3]    ELIMINAR PACIENTE")
        print(" [4]    BUSCAR PACIENTE")
        print(" [5]    MOSTRAR PACIENTES")
        print(" [6]    VOLVER")
        print("___________________________")
        opcion= input("Ingrese una opción: ")
        clear()
        if opcion=="1":
         createPaciente()
         tiempo()
         clear()
         
        elif opcion=="2":
            updatePacientes()
            tiempo()
            clear()
        elif opcion=="3":
            deletePaciente()
            tiempo()
            clear()
        elif opcion=="4":
            searchPaciente()
            tiempo()
            clear()

        elif opcion=="5":
            readPacientes()
            tiempo()
            clear()
        elif opcion=="6":
            menu()
        else:
            print("\nseleccione una opción correcta")

def createPaciente():
    dni = input('Ingrese D.N.I: ')
    dni=dni.replace(' ','')
    dni=dni.replace('.','')
    result=db.ejecutar_consulta("SELECT dni FROM paciente")
    for date in result:
        if( dni == date[0]):
            print('\nPaciente ya existe')
            tiempo()
            clear()
            gestionPaciente()
    nombre= input("Ingrese nombre: ")
    apellido= input("Ingrese apellido:  ")
    fechaNac = input("Ingrese Fecha de Nacimiento:  ")
    if (len(nombre)>0) and (len(apellido)>0 and (len(dni) > 0) and (len(fechaNac) > 0) ):
        sql="INSERT INTO paciente(dni, nombre, apellido, fechaNac) VALUES(?,?,?,?)"
        parametros=(dni,nombre,apellido,fechaNac)
        db.ejecutar_consulta(sql,parametros)
        print("INSERTADO CON EXITO....")
    else:{
        print('\nComplete todos los campos')
    }

def readPacientes():
    print("--------------------------------------------------------")
    print("-------------------- PACIENTES -------------------------")
    print("--------------------------------------------------------")
    result=db.ejecutar_consulta("SELECT * FROM paciente")
    for data in result:
        print("""
            DNI: {} 
            NOMBRE:{} 
            APELLIDO:{} 
            FECHA DE NACIMIENTO:{}""".format(data[0], data[1], data[2],  data[3])
            )
        print("--------------------------------------------------------")
        print(' [1] VOLVER')
        print("--------------------------------------------------------")
        op = input('Opcion: ')
        print("--------------------------------------------------------")
        if( op == '1'):
            gestionPaciente()
        else:
            print('Ingrese una opcion correcta')
    
    

    



def updatePacientes():
    dpa = 0
    dni = input("Ingrese el DNI: ")
    print("--------------------------------------------------------")
    if (len(dni)>0):
        sql="SELECT * FROM paciente WHERE dni LIKE ?"
        parametros=(dni, )
        result=db.ejecutar_consulta(sql,parametros)
        for data in result:
            dpa = 1
        if(dpa == 1):
            print("DNI: {} \nNOMBRE:{} \nAPELLIDO:{} \nFECHA DE NACIMIENTO:{}".format(data[0], data[1], data[2],data[3]))
            print("--------------------------------------------------------")
            nombre=input("Ingrese nombre:  ")
            apellido=input("Ingrese apellido:  ")
            fechaNac = input("Ingrese Fecha de Nacimiento:  ")
            if  (len(nombre)>0) and  (len(apellido)>0) and  (len(fechaNac)>0):
                sql="UPDATE paciente SET  nombre=?, apellido=?, fechaNac = ? WHERE dni=?"
                parametros=(nombre, apellido, fechaNac, dni)
                db.ejecutar_consulta(sql,parametros)
                print("\nACTUALIZADO CON EXITO")
            else:
                print("\nCOMPLETE TODOS LOS CAMPOS")
        else:
            print("\nPACIENTE NO EXISTE")
        
    else:
        print('\n INGRESE UN DNI VALIDO')

def deletePaciente():
    pacienteExiste = 0
    dni= input("Ingrese DNI:  ")
    print("------------------------------------")
    if ( len(dni) > 0):
        sql="SELECT * FROM paciente WHERE dni LIKE ?"
        parametros=(dni, )
        result=db.ejecutar_consulta(sql,parametros)
        for data in result:
            pacienteExiste = 1

        if( pacienteExiste == 1):
            print("DNI: {} \nNOMBRE:{} \nAPELLIDO:{} \nFECHA DE NACIMIENTO:{}".format(data[0], data[1], data[2],data[3]))
            print("--------------------------------------------------------")
            op = input('Desea eliminar paciente? [S/N]: ')
            if( op == 'S' or op == 's'):
                sql="DELETE FROM paciente WHERE dni=?"
                parametros=(dni, )
                db.ejecutar_consulta(sql,parametros)
                print("\nELIMINADO")
            elif( op == 'N' or op == 'n' ):
                print("\nPROCESO CANCELADO")
        else:
            print("\nPACIENTE NO EXISTE")
    else:
        print('\n INGRESE UN DNI VALIDO')

def searchPaciente():
    dpa = 0
    print("-------------------  PACIENTE --------------------------")
    print("--------------------------------------------------------")
    dni = input("Ingrese el DNI: ")
    print("--------------------------------------------------------")
    if (len(dni)>0):
        sql="SELECT * FROM paciente WHERE dni LIKE ?"
        parametros=(dni, )
        result=db.ejecutar_consulta(sql,parametros)
        for data in result:
            dpa = 1

        if(dpa == 1):
            print("DNI: {} \nNOMBRE:{} \nAPELLIDO:{} \nFECHA DE NACIMIENTO:{}".format(data[0], data[1], data[2],data[3]))
        else:
            print("\nPACIENTE NO EXISTE")



#GESTIONAR MEDICOS (CREAR, MODIFICAR, ELIMINAR, BUSCAR)

def gestionMedico():
    option = 0
    salir = 4
    while option != salir:
        print(" [1]    REGISTRAR MEDICO")
        print(" [2]    MODIFICAR MEDICO")
        print(" [3]    ELIMINAR MEDICO")
        print(" [4]    BUSCAR MEDICO")
        print(" [5]    VOLVER")
        print("___________________________")
        opcion= input("Ingrese una opción: ")
        clear()
        if opcion=="1":
         createMedico()
         tiempo()
         clear()
         
        elif opcion=="2":
            """ searchMedico() """
            updateMedico()
            tiempo()
            clear()
        elif opcion=="3":
            deleteMedico()
            tiempo()
            clear()
        elif opcion=="4":
            searchMedico()
            tiempo()
            clear()

        elif opcion=="5":
            menu()
        else:
            print("seleccione una opción correcta")

def createMedico():
    dni = input('Ingrese D.N.I: ')
    result=db.ejecutar_consulta("SELECT dniMedico FROM medico")
    for date in result:
        if( dni == date[0]):
            print('MEDICO YA EXISTE')
            tiempo()
            clear()
            gestionMedico()
    
    nombre= input("Ingrese nombre: ")
    apellido= input("Ingrese apellido:  ")
    showEspecialidad()
    codEsp = input("Ingrese Especialidad (número):  ")
    print('-----------------------------------------------------------')
    print("-------------------- HORARIOS -------------------------")
    result=db.ejecutar_consulta("SELECT * FROM horarioAtencion")
    for data in result:
        print("""
            cod: {} 
            hora:{}""".format(data[0], data[1])
            )
        print("--------------------------------------------------------")
    codHorario = input("Ingrese Horario (número):  ")
    if ( (len(nombre)> 0 ) and (len(apellido)> 0 ) and (len(dni) > 0) and (len(codEsp) > 0) and (len(codHorario) > 0) ):
        sql="INSERT INTO medico(dniMedico, nombre, apellido,  codEsp, codHr ) VALUES(?,?,?,?,?)"
        parametros=(dni,nombre,apellido,codEsp,codHorario)
        db.ejecutar_consulta(sql,parametros)

        print("\nINSERTADO CON EXITO....")
    else:{
        print('\nComplete todos los campos')
    }

def readMedico():
    print("--------------------------------------------------------")
    print("-------------------- MEDICOS -------------------------")
    print("--------------------------------------------------------")
    result = db.ejecutar_consulta("SELECT * FROM medico")
    for data in result:
        print("""
            DNI: {} 
            NOMBRE:{} 
            APELLIDO:{} 
            ESPECIALIDAD: {}""".format(data[0], data[1], data[2],  data[3]))
        print("--------------------------------------------------------")

def showEspecialidad():
    print('-----------------------------------------------------------')
    print("-------------------- ESPECIALIDAD -------------------------")
    result=db.ejecutar_consulta("SELECT * FROM especialidad")
    for data in result:
        print("""
            cod: {} 
            nombre:{}""".format(data[0], data[1])
            )
        print("--------------------------------------------------------")

def showHorario():
    print('-----------------------------------------------------------')
    print("-------------------- HORARIOS -------------------------")
    result=db.ejecutar_consulta("SELECT * FROM horarioAtencion")
    for data in result:
        print("""
            cod: {} 
            hora:{}""".format(data[0], data[1])
            )
        print("--------------------------------------------------------")

def updateMedico():
    dpa = 0
    dni = input('Ingrese D.N.I: ')
    print("--------------------------------------------------------")
    result=db.ejecutar_consulta("SELECT dni FROM medico")
    for date in result:
        if( dni != date[0]):
            print('MEDICO NO EXISTE')
            tiempo()
            clear()
            gestionMedico()
    if (len(dni)>0):
        sql="SELECT m.dniMedico, m.nombre, m.apellido, e.nombre, ha.hora FROM medico m, especialidad e, horarioAtencion ha  WHERE dni LIKE ? AND e.CodEsp = m.codEsp AND ha.codHr = m.codHr"
        parametros=(dni, )
        result=db.ejecutar_consulta(sql,parametros)
        for data in result:
            dpa = 1
        if(dpa == 1):
            print("DNI: {} \nNOMBRE:{} \nAPELLIDO:{} \nESPECIALIDAD:{} \nHORARIO:{}".format(data[0], data[1], data[2],data[3],data[4]))
            print("--------------------------------------------------------")
            nombre= input("Ingrese nombre: ")
            apellido= input("Ingrese apellido:  ")
            showEspecialidad()
            codEsp = input("Ingrese Especialidad (número):  ")
            showHorario()
            codHr = input("Ingrese Horario (número):  ")
            if ( (len(nombre)> 0 ) and (len(apellido)> 0 ) and (len(dni) > 0) and (len(codEsp) > 0) and (len(codHr) > 0) ):
                sql="UPDATE medico SET  nombre=?, apellido=?, codEsp=?, codHr=? WHERE dniMedico=?"
                parametros=(nombre,apellido,codEsp,codHr,dni)
                db.ejecutar_consulta(sql,parametros,)
                print("ACTUALIZADO CON EXITO....")

            else:{
                print('Complete todos los campos')
            }

def deleteMedico():
    me = 0
    readMedico()
    dni= input("Ingrese DNI:  ")
    result=db.ejecutar_consulta("SELECT dniMedico FROM medico")
    for date in result:
        me = 1
    if( me == 0):
            print('\nMEDICO NO EXISTE')
            tiempo()
            clear()
            gestionMedico()
    elif( me == 1):
            op = input('Desea eliminar medico? [S/N]: ')
            if( op == 'S' or op == 's'):
                sql="DELETE FROM medico WHERE dniMedico=?"
                parametros=(dni, )
                db.ejecutar_consulta(sql,parametros)
                print("\nELIMINADO")
            elif( op == 'N' or op == 'n' ):
                print("\nPROCESO CANCELADO")
           

def searchMedico():
    dpa = 0
    print("-------------------   MEDICO  --------------------------")
    print("--------------------------------------------------------")
    dni = input("Ingrese el DNI: ")
    print("--------------------------------------------------------")
    if (len(dni)>0):
        sql="SELECT m.dni, m.nombre, m.apellido, e.nombre, ha.hora FROM medico m, especialidad e, horarioAtencion ha  WHERE dni LIKE ? AND e.CodEsp = m.codEsp AND ha.codHr = m.codHr"
        parametros=(dni, )
        result=db.ejecutar_consulta(sql,parametros)
        for data in result:
            dpa = 1
        if(dpa == 1):
            print("DNI: {} \nNOMBRE:{} \nAPELLIDO:{} \nESPECIALIDAD:{} \nHORARIO:{}".format(data[0], data[1], data[2],data[3],data[4]))
        elif( dpa == 0):
            print('\nMEDICO NO EXISTE')
    else:
        print('COMPLETE LOS CAMPOS')            
      



def gestionCita():
    option = 0
    salir = 4
    while option != salir:
        print(" [1]    REGISTRAR CITA")
        print(" [2]    MODIFICAR CITA")
        print(" [3]    ELIMINAR CITA")
        print(" [4]    BUSCAR CITA")
        print(" [5]    LISTAR CITAS")
        print(" [6]    VOLVER")
        print("___________________________")
        opcion= input("Ingrese una opción: ")
        clear()
        if opcion=="1":
         createCitas()
         tiempo()
         clear()
         
        elif opcion=="2":
            #searchMedico()
            #updateMedico()
            tiempo()
            clear()
        elif opcion=="3":
            deleteCita()
            tiempo()
            clear()
        elif opcion=="4":
            searchMedico()
            tiempo()
            clear()

        elif opcion=="5":
            readCitas()
        elif opcion=="6":
            menu()
        else:
            print("seleccione una opción correcta")


def createCitas():
    dpa = 0
    print("--------------------------------------------------------")
    print("-------------------  PACIENTE --------------------------")
    print("--------------------------------------------------------")
    dniP = input("Ingrese el DNI: ")
    print("--------------------------------------------------------")
    if (len(dniP)>0):
        sql="SELECT * FROM paciente WHERE dni LIKE ?"
        parametros=(dniP, )
        result=db.ejecutar_consulta(sql,parametros)
        for data in result:
            print(data)
            dpa = 1

        if(dpa != 1):
            print('NO EXISTE')
            for data in result:
                print(data)
            agregar = input('Quiere agregar un nuevo paciente? [S/N]')
            if( agregar == 's' or agregar == 'S'):
                clear()
                createPaciente()
        elif( dpa == 1):
            showEspecialidad()
            codEsp = input("Ingrese especialidad (nro): ")
            print("-----------------------------------------------")
            sql=" SELECT m.codMedico, m.dniMedico, m.nombre, ha.hora FROM medico m, horarioAtencion ha WHERE m.codHr = ha.codHr  AND codEsp LIKE ?"
            parametros=(codEsp,)
            result=db.ejecutar_consulta(sql,parametros)
            for data in result:
                print("ID: {} \tDNI:{} \tNOMBRE:{} \tHORA:{}".format(data[0], data[1],data[2],data[3]))
                print("--------------------------------------------------------")
    
            idm=  input("Ingrese ID:  ")
            print("-------------------------------------")
            sqlh = "SELECT ha.codHr, ha.hora FROM horarioAtencion ha, medico m WHERE ha.codHr = m.codHr AND codMedico LIKE ?"
            p = (idm, )
            rh = db.ejecutar_consulta(sqlh, p)
            for data in rh:
                print( "ID:{} \tHORA: {}".format(data[0],data[1]))
            
            hora = int(input("Ingrese Hora (ID): "))
            print("-----------------------------------------------")
            fecha= input("Ingrese Fecha: ")
            print("-----------------------------------------------")
            refech = db.ejecutar_consulta("SELECT fecha, hora FROM cita")
            for data in refech:
                if( fecha == data[0] and hora == data[1] ):
                    print("FECHA NO DISPONIBLE")
                    tiempo()
                    clear()
                    gestionCita()

   
            precio = input("Ingrese Precio:  ")
            
            if( (len(fecha) > 0)  and (len(codEsp) > 0)  and (len(dniP) > 0) and (len(idm) > 0) and (len(precio) > 0)  ):
                    sql="INSERT INTO cita(codMedico, dniPaciente, fecha, hora, precio) VALUES(?,?,?,?,?)"
                    parametros=(idm,dniP,fecha,hora,precio)
                    db.ejecutar_consulta(sql,parametros)


                    print("INSERTADO CON EXITO....")

            
""" resultM = db.ejecutar_consulta("SELECT * FROM medico")
        resultP = db.ejecutar_consulta("SELECT * FROM paciente")
        DM = 0
        DP = 0
        for data in resultM:
            data[0]
            if( dnimedico ==  data[0]):
                DM = dnimedico
            
        for d in resultP:
            d[0]
            if(dnipaciente == d[0]):
                DP = dnipaciente
           
        if( DM == dnimedico and DP == dnipaciente):
            sql="INSERT INTO cita(fecha,  dniMedico, dniPaciente, precio) VALUES(?,?,?,?)"
            parametros=(fecha,dnimedico,dnipaciente,precio)
            db.ejecutar_consulta(sql,parametros)
            print("INSERTADO CON EXITO....")
        else:{
            print('Datos Incorrectos')
        }
    else:{
        print('Complete todos los campos')
    } """

def create():
    option = 0
    salir = 4
    while option != salir:
        print(" [1]    REGISTRAR PACIENTE")
        print(" [2]    REGISTRAR MEDICO")
        print(" [3]    REGISTRAR CITAS")
        print(" [4]    VOLVER")
        print("___________________________")
        opcion= input("Ingrese una opción: ")
        clear()
        if opcion=="1":
         createPaciente()
         tiempo()
         clear()
         
        elif opcion=="2":
            createMedico()
            tiempo()
            clear()
        elif opcion=="3":
            createCitas()
            tiempo()
            clear()

        elif opcion=="4":
            menu()
        else:
            print("seleccione una opción correcta")
   
def readCitas():
    print("--------------------------------------------------------")
    print("-------------------- CITAS -------------------------")
    print("--------------------------------------------------------")
    result=db.ejecutar_consulta("SELECT c.fecha, ha.hora, m.nombre, m.apellido, p.nombre, p.apellido , c.precio FROM  horarioAtencion ha , medico m, paciente p , cita c WHERE  m.codMedico = c.codMedico  AND p.dni = c.dniPaciente AND c.hora = ha.codHr")
    for data in result:
        print("""
            FECHA: {} 
            HORA: {} 
            MEDICO: {} {}
            PACIENTE: {} {}
            PRECIO: {}""".format(data[0], data[1], data[2],data[3],data[4],data[5],data[6])
            )
        print("--------------------------------------------------------")

def deleteCita():
    readCitas()
    cod = int(input("Ingrese Codigo de cita:  "))
    if cod !=0:
        sql="DELETE FROM cita WHERE cod=?"
        parametros=(cod, )
        db.ejecutar_consulta(sql,parametros)
        print("ELIMINADO")


#def read():
    option = 0
    salir = 3
    while (option != salir):
        print("---------------------------")
        print(" [1]    LISTAR PACIENTE")
        print(" [2]    LISTAR MEDICO")
        print(" [3]    LISTAR CITAS")
        print(" [4]    VOLVER ")
        print("___________________________")
        option= input("Ingrese una opción: ")
        clear()
        if(option == '1'):
            readPacientes()
        if(option == '2'):
            readMedico()
        if( option == '3'):
            readCitas()
        if( option == '4'):
            menu()

#def update():
    option = 0
    salir = 3
    while (option != salir):
        print("---------------------------")
        print(" [1]    MODIFICAR PACIENTE")
        print(" [2]    MODIFICAR MEDICO")
        print(" [3]    VOLVER ")
        print("___________________________")
        option= input("Ingrese una opción: ")
        clear()
        if(option == '1'):
           updatePacientes()
        if(option == '2'):
            updateMedico()
        if(option == '3'):
            menu()

#def delete():
    option = 0
    salir = 3
    while (option != salir):
        print("---------------------------")
        print(" [1]    ELIMINAR PACIENTE")
        print(" [2]    ELIMINAR MEDICO")
        print(" [3]    ELIMINAR CITA")
        print(" [4]    VOLVER ")
        print("___________________________")
        option= input("Ingrese una opción: ")
        clear()
        if(option == '1'):
            deletePaciente()
        if(option == '2'):
            deleteMedico()
        if( option == '3'):
            deleteCita()
        if( option == '4'):
            menu()

#def search():
    option = 0
    salir = 3
    while (option != salir):
        print("---------------------------")
        print(" [1]    BUSCAR PACIENTE")
        print(" [2]    BUSCAR MEDICO")
        print(" [3]    VOLVER ")
        print("___________________________")
        option= input("Ingrese una opción: ")
        clear()
        if( option == '1'):
            searchPaciente()
        if( option == '2'):
            searchMedico()
           
        if( option == '3'):
                menu()


  
def callHorarios():
    sql = 'SELECT * FROM horarioAtencion'
    result=db.ejecutar_consulta(sql)
    for data in result:
        print("""
            COD: {} 
            HORARIO: {}""".format(data[0], data[1])
            )
        print("--------------------------------------------------------")
    print(result)
    



            
        

def menu():
    opcion=0
    finalizar=6
    while opcion!=finalizar:
        print("___________________________")
        print("_____Clinica Santa María______")
        print("___________________________")
        print(" [1]    GESTIONAR PACIENTES")
        print(" [2]    GESTIONAR MEDICOS")
        print(" [3]    GESTIONAR CITAS")
        print(" [4]    SALIR")
        print(" [5]    HOrarios")
        print("___________________________")
        opcion= input("Ingrese una opción: ")
        clear()
        if opcion=="1":
            gestionPaciente()
            tiempo()
            clear()
            
        elif opcion=="2":
            gestionMedico()
            tiempo()
            clear()
        elif opcion=="3":
            gestionCita()
            tiempo()
            clear()
        elif opcion=="5":
            callHorarios()
            tiempo()
            clear()
        elif opcion=="4":
            salir()
        else:
            print("seleccione una opción correcta")

menu()

