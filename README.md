//////////////////////////////////////.

/.
/.

* NOTA: Buenas profesora, tuvimos un problema con el github que no le dejaban subir sus respectivos aportes a las ramas personales de cada uno, por lo tanto en la rama MASTER, Se encuentra el aporte de cada uno

   Jose: Preprocesado de datos en el periodo 2013-2015 | Sobre calculo de promedio de afectado, mensual, anual, por paises y su respectiva region

   Angel: Preprocesado de datos en el periodo 2010-2012 | Sobre la relacion entre la magnitud y daños economicos

   Julio y Andrea: Preprocesado de datos desde 2016-2021 | Sobre la relacion entre magnitud y total de muertos

* NOTA 2: La idea principal de nosotros era dividirnos por periodo de tiempo y luego en un archivo aparte relacionar que las variantes se presentaba en cada periodo y porque variaba o que diferencias habrian. Pero luego nos dividimos los puntos sobre temas que podriamos usar ya que son interesante y cada uno se encargo de ello  nos falta es poner todo en un orden y agruparlos todo en un mismo documento para facil compresion y lectura de informacion

/.
/.

////////////////////////////////////////.





.

.

.

.

.

.

1. Nombre y función de los miembros del equipo Nombre de los Integrantes Papel a desempeñar en el equipo
   
  Julio Zambrano
  Ángel Villegas
  Andrea Ruiz
  José Villalobos
  Rodolfo Rodríguez

2. Descripción del proyecto
   
  Proyecto: Análisis de Desastres Naturales
  
  Objetivo: analizar y comprender los patrones, tendencias y correlaciones entre diferentes tipos de desastres naturales y su impacto a lo largo del tiempo en diversas regiones del mundo.
  Datos de Estudio:
  
  Fecha: Fecha de ocurrencia del desastre.
  
  Tipo de Desastre: Clasificación del desastre (por ejemplo, terremoto, inundación, tormenta).
  
  País: País afectado.
  
  Región: Región afectada.
  
  Ubicación Específica: Ubicaciones afectadas dentro del país.
  
  Magnitud/Intensidad: Medida de la magnitud o intensidad del desastre (por ejemplo, magnitud del terremoto, velocidad del viento).
  
  Impacto: Número de personas afectadas, daños materiales, etc.
  
  Actividades:
  
  1. Exploración de Datos:
  o Explorar los datos para determinar el formato y las variables necesarias.
  o Identificar las características relevantes para el análisis (tipo de desastre, mag-nitud, impacto, etc.).
  2. Carga de Datos en Pandas DataFrames:
  o Importar los datos desde Excel a Pandas DataFrames.
  o Realizar una exploración inicial de los datos para verificar su integridad y con-sistencia.
  3. Preprocesamiento de Datos:
  o Identificar y corregir valores faltantes o nulos.
  o Convertir tipos de datos (por ejemplo, fechas, valores numéricos).
  o Normalizar los datos para asegurar coherencia.
  o Agrupar datos por categorías relevantes (por ejemplo, tipo de desastre, región, año).
  4. Análisis de Datos:
  o Analizar la correlación entre diferentes variables (por ejemplo, magnitud del desastre y número de personas afectadas).
  o Identificar patrones y tendencias en la ocurrencia de desastres a lo largo del tiempo.
  o Evaluar el impacto de los desastres en diferentes regiones y períodos.
  5. Visualización de Datos:
  o Crear gráficos y diagramas para visualizar los datos y los resultados del análisis.
  o Utilizar subplots para comparar diferentes tipos de desastres o regiones en una sola figura.

3.- Describa en qué consistirá el proyecto o propuesta de su equipo. Describa el problema que le gustaría resolver 
(incluya cualquier dato que pueda tener para apoyar que este problema existe) y el concepto general para resolver este problema).

A) ¿Qué valor social genera su idea (medioambiental, social, financiero, etc.)?
  El proyecto de análisis de desastres naturales tiene un impacto significativo en varios ámbitos:
   Medioambiental: Al identificar patrones y causas de desastres, el proyecto puede desarrollar estrategias para mitigar el impacto ambiental y proteger ecosistemas vulnerables.
   Social: Mejorar la preparación y respuesta a desastres puede salvar vidas y reducir el sufrimiento. Además, educa y conciencia a las comunidades sobre los riesgos y las medidas preventivas, fomentando la resiliencia comunitaria.
   Financiero: Anticipar desastres permite minimizar pérdidas económicas. Los datos pueden ayudar en la planificación financiera, la asignación de recursos y mejorar modelos de seguros contra desastres.

B) ¿Hay alguna consideración que deba tenerse en cuenta para la comunidad (¿cómo crees que le beneficiaría a la comunidad esta idea, afecta negativamente a alguna persona?)
Es fundamental analizar cómo un proyecto de análisis de desastres naturales puede afectar a la comunidad. Evaluar tanto los beneficios como cualquier posible impacto negativo asegura un enfoque equilibrado y ético.

  Beneficios para la Comunidad:
  
   Educación y Conciencia: Aumentar la comprensión sobre los desastres naturales y las medidas preventivas puede salvar vidas y proteger propiedades.
   Preparación y Resiliencia: Equipar a las comunidades con información y estrategias para mejorar su respuesta y recuperación ante desastres.
   Apoyo a las Políticas Públicas: Los datos pueden influir en la creación de políticas más efectivas para la gestión de riesgos y recursos.
 
  Consideraciones Negativas:
 
   Datos Sensibles: Es esencial manejar la información con cuidado para no generar alarmas innecesarias o malinterpretaciones que puedan causar pánico.
   Acceso a la Información: Asegurarse de que los datos sean accesibles y comprensibles para toda la comunidad, evitando exclusiones tecnológicas o educativas
  
C) ¿Alguna pregunta pendiente y/o suposición a la que pueda responder sobre su idea?
Al desarrollar un proyecto de esta magnitud, es normal que surjan preguntas y suposiciones que podrían necesitar más clarificación para avanzar de manera efectiva.
Suposiciones:

   Consistencia Temporal: Se asume que los datos son consistentes y comparables a lo largo de los años, permitiendo identificar tendencias fiables.
   Representatividad: Se presupone que la muestra de datos es representativa de la realidad y abarca una variedad suficiente de tipos de desastres y ubicaciones.
   Neutralidad de Análisis: Se asume que los análisis y conclusiones serán neutra-les y no estarán influenciados por sesgos o limitaciones en la calidad de los datos.
  
5) ¿Cuál es el objetivo principal o la métrica sobre la que intenta influir con esta prueba (por ejemplo, compras, valor medio de los pedidos, envío de formularios, etc.)?
En el caso del análisis de desastres naturales, buscamos influir en métricas clave que permitan una mejor comprensión y gestión de estos eventos.
Objetivo Principal: Mejora en la Preparación y Respuesta: Evaluar y mejorar la capacidad de respuesta ante desastres naturales mediante el análisis de datos históricos para prever futuros eventos y mitigar su impacto.
 
  Métricas Clave:

   Frecuencia de Desastres: Número de desastres naturales ocurridos por año y tipo.
   Impacto Humano: Número de personas afectadas y víctimas mortales.
   Impacto Económico: Daños económicos estimados causados por los desastres.
   Tiempo de Respuesta: Eficiencia de los tiempos de respuesta ante desastres en diferentes regiones.
   Evaluación de Riesgo: Identificación y análisis de las áreas más vulnerables y los factores de riesgo.
  En el desarrollo de nuestro proyecto de análisis de desastres naturales, hemos establecido un enfoque metodológico integral que abarca la exploración, carga, preprocesamiento, análisis y visualización de datos relacionados con más de ocho mil eventos catastróficos. El objetivo principal de esta investigación es identificar patrones y tendencias, así como evaluar el impacto de estos desastres a lo largo del tiempo en diversas regiones del mundo.
  Nuestro análisis busca mejorar significativamente la preparación y respuesta ante desastres naturales, mediante el uso de datos históricos para prever futuros eventos y mitigar su impacto. Al proporcionar información valiosa, esperamos contribuir a la creación de políticas públicas más efectivas y a la educación de las comunidades sobre los riesgos y las medidas preventivas.
  En este contexto, es crucial aprender de eventos recientes, como la catástrofe de la DANA en Valencia. Este trágico incidente puso de manifiesto la necesidad de una mejor gestión de la información y una respuesta más oportuna por parte de las autoridades. Nuestro proyecto aspira a que errores como estos no se repitan, mediante la implementación de sistemas de alerta temprana más eficientes y la optimización de las estrategias de comunicación y respuesta.
  Al final, nuestro objetivo es salvar vidas, reducir el sufrimiento humano y proteger el medio ambiente y los recursos económicos frente a los desastres naturales. Con el análisis y la aplicación adecuada de nuestros datos, podemos construir comunidades más resilientes y mejor preparadas para enfrentar estos desafíos.
