# Combinador de PDFs

Una aplicación de escritorio simple y eficiente para combinar múltiples archivos PDF en uno solo.

## Características

- Interfaz gráfica intuitiva
- Selección de carpeta con PDFs mediante explorador de archivos
- Barra de progreso para seguimiento del proceso
- Área de logs para ver el estado de la operación
- Ordenamiento automático de archivos por nombre

## Requisitos

- Python 3.x
- PyPDF2
- tkinter (generalmente viene incluido con Python)

## Instalación

1. Clona este repositorio:
```bash
git clone [URL del repositorio]
```

2. Instala las dependencias:
```bash
pip install PyPDF2
```

## Uso

1. Ejecuta el programa:
```bash
python merger.py
```

2. En la interfaz:
   - Haz clic en "Buscar Carpeta" para seleccionar la carpeta que contiene tus PDFs
   - Haz clic en "Guardar Como" para elegir dónde guardar el PDF combinado
   - Presiona "Combinar PDFs" para iniciar el proceso

## Notas

- Los archivos PDF se combinarán en orden alfabético según sus nombres
- La aplicación mostrará el progreso en tiempo real
- Se mostrarán mensajes de error si algo sale mal durante el proceso

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue primero para discutir los cambios que te gustaría realizar. 