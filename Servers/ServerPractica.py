#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from os import listdir
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer

def existeDocumento(nombreDocumento):
	try:
		Documento = open(nombreDocumento)	
		Documento.close()
		return True
	except:
		return False

def crearDocumento(nombreDocumento):
	archivo = open(nombreDocumento, 'a')
	nombre = archivo.name
	archivo.close()
	return "Documento "+nombre+" Creado"

def eliminarDocumento(nombreDocumento):
	try:
		os.remove(nombreDocumento)
		return "Documento Eliminado"
	except:
		return "Problemas al Eliminar el Documento"

def verDocumento(nombreDocumento):
	objetoBinario = xmlrpclib.Binary(open(nombreDocumento).read())
	return objetoBinario
	
def agregarADocumento(nombreDocumento,texto):

	Documento = open(nombreDocumento, 'a+')
	Documento.write(texto)
	Documento.close()

	return "Texto agregado al Documento"

def listaDocumentos():
	lista = []
	for archivo in listdir("."):
		if archivo[-2:] != 'py':
			lista.append(archivo)
	return lista

def obtenerArchivo(nombreDocumento):
     with open(nombreDocumento, "rb") as Documento:
         return xmlrpclib.Binary(Documento.read())




server = SimpleXMLRPCServer( ("localhost", 8000) ,allow_none=True )
print "Servidor en linea"
server.register_function(existeDocumento, 'existeDocumento')
server.register_function(crearDocumento, "crearDocumento")
server.register_function(eliminarDocumento, "eliminarDocumento")
server.register_function(verDocumento, "verDocumento")
server.register_function(agregarADocumento, "agregarADocumento")
server.register_function(listaDocumentos, "listaDocumentos")
server.register_function(obtenerArchivo, "obtenerArchivo")

print "Servicio listo para usarse . . ."
server.serve_forever()
