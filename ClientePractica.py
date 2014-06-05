#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xmlrpclib
import os

def mostrarMenu():
	print "1-Crear Documento\n2-Eliminar Documento"
	print "3-Ver Documento\n4-Agregar a Documento\n" 
	print "5-Creditos\n6-Salir"
	print "7-Respaldo (Cualquier Documento )"

	print "\n\n"

def creditos():
	print "Universidad Politecnica de Chiapas\Tuxtla Gtz Chiapas 6 de junio 2014"
	print "SOA \nCatedratico: Dr. Juan Carlos López Pimentel "
	print "Eduardo Ismael García Pérez 113015"
	print "\n\n"

bandera = True


conexionServer = xmlrpclib.ServerProxy("http://localhost:8000/")                        

print "Conexion establecida"

while (bandera):
	mostrarMenu()
		
	opcion = input("Opcion : ")
	os.system('cls')

	if opcion == 6:
		bandera = False
	
	elif opcion == 7:
		
		listaDocs = conexionServer.listaDocumentos()
		for doc in listaDocs:
			print doc

		print "\n\nEs necesario colocar la extension del archivo "
		nombreArchivo = raw_input("Nombre del documento : ")
		with open(nombreArchivo, "wb") as Documento:
			Documento.write(conexionServer.obtenerArchivo(nombreArchivo).data)
		print "\n\n"
	else:
		os.system('cls')
		print "Solo archivos con extension .txt"
		nombreArchivo = raw_input("Nombre del documento : ")

		if opcion == 1:
			#Crear un archivo
			if conexionServer.existeDocumento(nombreArchivo) == False:
				print conexionServer.crearDocumento( nombreArchivo )
			else:
				print "El archivo no puede ser creado debido a que este ya existe"

		elif opcion == 2:
			#Eliminar un archivo
			if conexionServer.existeDocumento(nombreArchivo) :
				print conexionServer.eliminarDocumento(nombreArchivo)
			else:
				print "El documento no puede ser eliminado ya que no existe"
		
		elif opcion == 3:
			#Leer un archivo
			if conexionServer.existeDocumento( nombreArchivo ):
				datos = conexionServer.verDocumento(nombreArchivo) #Recibe los datos en binario y automaticamente los transforma
				print datos
			else:
				print "El documento no existe "

		elif opcion == 4:
			#Agregar texto a un documento
			if conexionServer.existeDocumento( nombreArchivo ) == False:
				print "El documento NO existe, se creara Automaticamente"
			print conexionServer.agregarADocumento( nombreArchivo, raw_input("Texto : "))
			
		elif opcion ==5:
			creditos()
		
		print "\n\n"
		