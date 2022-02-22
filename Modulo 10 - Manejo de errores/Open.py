def  principal ():
    prueba :
        configuración  =  abrir ( 'config.txt' )
    excepto  FileNotFoundError :
        print ( "¡No se pudo encontrar el archivo config.txt!" )
    excepto  IsADirectoryError :
        print ( "Fuente config.txt pero es un directorio, no pude leerlo" )
    excepto ( BlockingIOError , TimeoutError ):
        print ( "Sistema de archivos bajo carga pesada, no se puede completar la lectura del archivo de configuración" )


def  principal ():
    prueba :
        abierto ( 'config.txt' )
    excepto  OSError  como  error :
        si  errar . error  ==  2 :
            print ( "¡No se pudo encontrar el archivo config.txt!" )
        elif  err . error  ==  13 :
            print ( "Encontré config.txt pero no pude leerlo'" )


si  __nombre__  ==  '__principal__' :
    principal ()