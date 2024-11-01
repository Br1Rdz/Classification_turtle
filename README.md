# Classification imagen turtle

La app clasifica imagenes de las siguientes tortugas *Gopherus flavomarginatus*, *Terrapene coahuila*, *Trachemys scripta* y *Kinosternon flavescens*.
Usa un "dataset" para cada una de las clases (especie) de ~ 201 - 300 imagenes, las imagenes se redimensionaron a 224 x 224, para su preentreno, el tamaño del procesamiento por lote (batch) fue de 32. Adicionalmente se añadadio "data augmentation" para la creacion de datos sinteticos, con la finalidad de aumentar las posibles variaciones de texturas, anchos, alturas, zoom, brillo y orientacion de las imagenes del dataset.

Debido a los pocos datos que tiene el "dataset" se opto por crear un modelo de preentreno (Pretrained Model for Transfer Learning) usando el modelo de "ResNet50", asi tambien se usaron funsiones de activacion como lo fue "relu", "softmax" y el optimizar "adam", el modelo desempeño despues de 10 epocas los siguientes valores: 

- accuracy: 1.0000
- val_accuracy: 0.8500
- loss: 0.0059
- val_loss: 0.3905.

 ##Para desplegar la aplicaacion en un entorno de "streamlit" 
 1. Clona el repertorio en alguna carpeta de tu eleccion 
