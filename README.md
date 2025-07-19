# 🏋️‍♂️ Workout Tracker

Este proyecto permite registrar tus ejercicios físicos automáticamente en una hoja de cálculo de Google Sheets usando:

- [Nutritionix API](https://www.nutritionix.com/business/api) para interpretar descripciones de ejercicios naturales.
- [Sheety](https://sheety.co/) para guardar los datos en Google Sheets.
- `dotenv` para proteger tus credenciales.
- Python y `requests` para integrar las APIs.

## 📦 ¿Qué hace?

1. Recibe del usuario una frase como:
   > "Caminé 30 minutos y corrí 20 minutos"
2. La envía a Nutritionix para convertirla en datos estructurados.
3. Guarda los datos en una hoja de Google Sheets con:
   - Fecha
   - Hora
   - Ejercicio
   - Duración
   - Calorías quemadas

## 🚀 Cómo usarlo

1. Clona este repositorio:

```bash
git clone https://github.com/tuusuario/workout-tracker.git
cd workout-tracker
```

2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

3. Crea un archivo `.env` con las siguientes variables:

```env
TOKEN=tu_nutritionix_api_key
BEARER={"Authorization": "Bearer tu_token_de_sheety"}
```

4. Ejecuta el programa:

```python
python main.py
```
