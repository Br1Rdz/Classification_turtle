# Classification imagen turtle

> [!NOTE]
> <div align="justify"> La app clasifica imagenes de las siguientes tortugas <i><b>Gopherus flavomarginatus</b></i>, <i><b>Terrapene coahuila</b></i>, <i><b>Trachemys scripta</b></i> y <i><b>Kinosternon flavescens</b></i>. Usa un <b>dataset</b> para cada una de las clases (especie) de ~ 201 - 300 imagenes, las imagenes se redimensionaron a <b>224 x 224</b>, para su pre-entreno, el tamaño del procesamiento por lote (batch) fue de 32. Adicionalmente se añadadio <b>Data Augmentation</b> para la creacion de datos sinteticos, con la finalidad de aumentar las posibles variaciones de texturas, anchos, alturas, zoom, brillo y orientacion de las imagenes del dataset. Debido a los pocos datos que tiene el <b>"dataset"</b> se opto por crear un modelo de pre-entreno (Pretrained Model for Transfer Learning) usando el modelo de <b>ResNet50</b>, asi tambien se usaron funsiones de activacion como lo fue <b>relu</b>, <b>softmax</b> y el optimizar <b>"adam"</b>, el modelo desempeño despues de 10 epocas se obtuvo los siguientes valores:  - Precisión: 1.0 - Validacion de precisión: 0.86 - Perdida: 0.0059 - Validacion de perdida: 0.39.</div> 

> [!TIP]
> Si usas GPU la clasificacion es mas rapido minimo de 2 Gbs

> [!IMPORTANT]  
> Para desplegar la aplicacion y uso
> 1. Clona el repertorio [Classification_turtle](https://github.com/Br1Rdz/Classification_turtle.git) en alguna carpeta de tu eleccion
> 2. Instalacion de las dependencias a usar pip install -r requirements.txt
> 3. Ejecuta la aplicación streamlit run Classification_turtle.py
> 4. Añade la imagen a clasificar
> 5. FELICIDADES AQUI ESTA TU CLASIFFICACION
> 6. La aplicacion tambien tiene un chatbot sobre datos generales de las especie
> 7. ESPERO DISFRUTES LA APP.

> [!WARNING]  
> Puede ser que algunas clasificaciones falle en su predicion esto es debido al tamaño del dataset.

> [!CAUTION]
> En PC que no tenga una tarjeta de video posiblemente no funcione
