# Classification imagen turtle

> [!NOTE]
> <div align="justify"> La app clasifica imagenes de las siguientes tortugas <i>Gopherus flavomarginatus</i>, <i>Terrapene coahuila</i>, <i>Trachemys scripta</i> y <i>Kinosternon flavescens</i>. Usa un `dataset` para cada una de las clases (especie) de ~ 201 - 300 imagenes, las imagenes se redimensionaron a 224 x 224, para su preentreno, el tamaño del procesamiento por lote (batch) fue de 32. Adicionalmente se añadadio `data augmentation` para la creacion de datos sinteticos, con la finalidad de aumentar las posibles variaciones de texturas, anchos, alturas, zoom, brillo y orientacion de las imagenes del dataset. Debido a los pocos datos que tiene el "dataset" se opto por crear un modelo de preentreno (Pretrained Model for Transfer Learning) usando el modelo de `ResNet50`, asi tambien se usaron funsiones de activacion como lo fue "relu", "softmax" y el optimizar "adam", el modelo desempeño despues de 10 epocas los siguientes valores:
> - accuracy: 1.0000
> - val_accuracy: 0.8500
> - loss: 0.0059
> -  val_loss: 0.3905.</div>

> [!IMPORTANT]  
>Para desplegar la aplicacion y uso
>  1. Clona el repertorio [Classification_turtle](https://github.com/Br1Rdz/Classification_turtle.git) en alguna carpeta de tu eleccion
>  2. Intala pip install freeze
>  3. Instalacion de las dependencias a usar pip install -r requirements.txt
>  4. Ejecuta la aplicación streamlit run Classification_turtle.py
>  5. Añade la imagen a clasificar
>  6. FELICIDADES AQUI ESTA TU CLASIFFICACION
>  7. La aplicacion tambien tiene un chatbot sobre datos generales de las especie
>  8. ESPERO DISFRUTES LA APP.

> [!TIP]
> > Si usas GPU la clasificacion es mas rapido minimo de 2 Gbs
