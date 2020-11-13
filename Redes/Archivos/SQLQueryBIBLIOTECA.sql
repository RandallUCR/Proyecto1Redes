USE IF4100

INSERT INTO BIBLIOTECA.AUTOR 
(
 CODIGO
,NOMBRE
)
VALUES
(
100, 'Charles Dickens'
),
(
101, 'Gabriel Garcia Marquez'
),
(
102, 'William Bulter'
),
(
103, 'Truman Capote'
)

INSERT INTO [BIBLIOTECA].[LIBRO]
(
  [CODIGO_LIBRO]
, [TITULO]
, [ISBN]
, [PAGINAS]
, [EDITORIAL]
)
VALUES
(
1,'El Principito' , 'abcefg123',100, 'EditorialClubdeLibros'

)
,(
2, 'SQL Server MVP','12345678r',787, 'Manning Publications'
)
,(
3,'Harry Potter', 'gfgfgfgf',890,'HarryHarry'
)
,(
4,'El Padrino','4545jhjh',568,'Ediciones Perro Azul'
)
,(
5,'El Quijote','quiquiqui',1234,'Ed Barcelona'
)


INSERT INTO [BIBLIOTECA].[EJEMPLAR]
(
 [CODIGO_EJEMPLAR]
,[LOCALIZACION]
)
VALUES
(
1000,'Turrialba'
)
,(
1001,'Turrialba'
)
,(
1010,'Paraiso'
)
,(
1020,'Guapiles'
)
,(
2000,'Turrialba'
)
,(
3000,'Guapiles'
)
,(
4000,'Paraiso'
)
,(
5000,'Turrialba'
)

--SELECT * FROM [BIBLIOTECA].[EJEMPLAR]

INSERT INTO BIBLIOTECA.USUARIO
(
[CODIGO_USUARIO],
[NOMBRE],
[APELLIDOS],
[TELEFONO], 
[DIRECCION], 
[CARRERA]
)
VALUES
(
 10000
,'Aracely'
,'Soto'
,'84848484'
,'Cartago, Turrialba'
,'Informatica'
)
,(
10001
, 'Fabricio'
, 'Castillo'
, '25529696'
, 'San Jose, San Pedro, Calle 2'
, 'Direccion Empresas'
)
,(
10002
, 'Michelle'
, 'Molina'
, '85658565'
, 'Cartago. Central, Oriental'
, 'Turismo'
)
,(
10003
,'Yareth'
,'Fernandez'
,'25547896'
,'Siquirres, Calle 23'
,'Informatica'
)

INSERT INTO BIBLIOTECA.LIBRO_EJEMPLAR
(
  [CODIGO_LIBRO]
, [CODIGO_EJEMPLAR]
)
VALUES
(
1,1000
)
,(
1,1001
)
,(
1,1010
)
,(
1,1020
)
,(
2,2000
)
,(
3,3000
)
,(
4,4000
)
,(
5,5000
)

SELECT * FROM BIBLIOTECA.LIBRO_EJEMPLAR
SELECT * FROM BIBLIOTECA.LIBRO
SELECT * FROM BIBLIOTECA.EJEMPLAR

INSERT BIBLIOTECA.USUARIO_EJEMPLAR
(
  [CODIGO_USUARIO]
, [CODIGO_EJEMPLAR]
, [FECHA_PRESTAMO]
, [FECHA_DEVOLUCION]
)

VALUES
(
 10001
,3000
,'2020-08-19 10:45:36.387'
,'2020-08-26'
)

--USO DE TO, ORDER BY Y ASC-DESC
SELECT TOP 2
  [CODIGO_LIBRO]
, [TITULO]
, [ISBN]
, [PAGINAS]
, [EDITORIAL] 
FROM  BIBLIOTECA.LIBRO 
ORDER BY PAGINAS DESC

--USO FILTROS (WHERE)

SELECT [CODIGO_LIBRO], [TITULO] FROM BIBLIOTECA.LIBRO
WHERE EDITORIAL = 'HarryHarry'