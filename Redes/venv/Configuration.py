import mysql.connector
def guardarCliente(ip_address,puerto):
    try:
        conexion = mysql.connector.connect(host='localhost', user='root', passwd='12345', db='proyecto1Redes')
        cur = conexion.cursor()
        cur.execute(f"INSERT INTO cliente (ip_address,puerto) values ('{ip_address}','{puerto}')")
        conexion.commit()
    except IOError as e:
        print('Error'+e)
    finally:
        conexion.close()
def listar_clientes():
    try:

        conexion = mysql.connector.connect(host='localhost', user='root', passwd='12345', db='proyecto1Redes')
        cur = conexion.cursor()
        cur.execute('SELECT * from cliente')
        data = cur.fetchall()

        conexion.commit()

        array = []
        array2 = []
        if len(data) > 0:

            for row in data:
                print(row[0])
                print(row[1])
                roww=row[0]+"   "+row[1]
                array.append(roww)
        return array
    except:
        print('Error')
    finally:
        conexion.close()
lista_hashg=[]

def listar_hashs():
    print("Resultados de mysql.connector:")

    miConexion = mysql.connector.connect(host='localhost', user='root', passwd='12345', db='proyecto1Redes')
    cur = miConexion.cursor()
    cur.execute("SELECT id_hash,hash_virus FROM hash_virus")
    lista_hash=''
    global lista_hashg
    cont =0
    for id_hash, hash_virus in cur.fetchall():

        print (id_hash, hash_virus)
        lista_hashg.append(hash_virus)
        if(cont==0):
            lista_hash+=' '+hash_virus
        else :
            lista_hash +=' ' + hash_virus
        cont+=1

    miConexion.close()

    return lista_hash
def eliminarCliente ():
    try:
        conexion = mysql.connector.connect(host='localhost', user='root', passwd='12345', db='proyecto1Redes')
        cur = conexion.cursor()
        cur.execute("DELETE FROM cliente")
        conexion.commit()
    except IOError as e:
        print('Error'+e)
    finally:
        conexion.close()
