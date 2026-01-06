# 📞 Sistema de Llamadas Automatizadas - Asesora Bancaria Colombiana

Sistema profesional de llamadas automatizadas con voz natural colombiana, optimizado para atención bancaria en Medellín.

## 🌟 Características Principales

### 🎙️ Voz Natural Colombiana
- **Voice ID:** `E5HSnXz7WUojYdJeUcng` (ElevenLabs)
- **Acento:** Colombiano (Medellín)
- **Estilo:** Profesional bancario, cálido y amigable
- **Configuración optimizada:**
  - Stability: 0.55 (naturalidad alta)
  - Similarity: 0.85 (fidelidad excelente)
  - Style: 0.65 (muy expresiva)
  - Speaker Boost: Activado (claridad telefónica)

### 🤖 IA Conversacional
- **Modelo:** GPT-4o-mini (OpenAI)
- **Temperature:** 0.82 (profesional y natural)
- **Idioma:** Español Colombia (es-CO)
- **Respuestas:** 15-30 palabras, precisas y completas

### 📱 Control por Telegram
- Iniciar llamadas individuales o masivas
- Monitorear llamadas activas
- Ver estadísticas en tiempo real
- Finalizar llamadas remotamente

### 📞 VoIP Profesional
- **Proveedor:** Twilio
- **Capacidad:** 50 llamadas simultáneas
- **Reconocimiento:** Optimizado para español colombiano
- **Calidad:** HD Voice con speaker boost

## 🏗️ Arquitectura

```
┌─────────────────────────────────────────────┐
│           Sistema de Llamadas               │
├─────────────────────────────────────────────┤
│                                             │
│  ┌──────────────────────────────────────┐  │
│  │  CallerBot (Orquestador Principal)   │  │
│  │                                      │  │
│  │  ┌────────────────────────────────┐ │  │
│  │  │ TelegramBot                    │ │  │
│  │  │ - Comandos de control          │ │  │
│  │  │ - Interfaz administrativa      │ │  │
│  │  └────────────────────────────────┘ │  │
│  │                                      │  │
│  │  ┌────────────────────────────────┐ │  │
│  │  │ VoIPManager                    │ │  │
│  │  │ - Gestión de llamadas Twilio   │ │  │
│  │  │ - Webhooks de voz              │ │  │
│  │  └────────────────────────────────┘ │  │
│  │                                      │  │
│  │  ┌────────────────────────────────┐ │  │
│  │  │ VoiceSynthesizer               │ │  │
│  │  │ - ElevenLabs API               │ │  │
│  │  │ - Voz colombiana natural       │ │  │
│  │  └────────────────────────────────┘ │  │
│  │                                      │  │
│  │  ┌────────────────────────────────┐ │  │
│  │  │ AIConversation                 │ │  │
│  │  │ - OpenAI GPT-4o-mini           │ │  │
│  │  │ - Contexto conversacional      │ │  │
│  │  └────────────────────────────────┘ │  │
│  │                                      │  │
│  │  ┌────────────────────────────────┐ │  │
│  │  │ WebhookServer                  │ │  │
│  │  │ - FastAPI                      │ │  │
│  │  │ - Endpoints de Twilio          │ │  │
│  │  └────────────────────────────────┘ │  │
│  └──────────────────────────────────────┘  │
└─────────────────────────────────────────────┘
```

## 🚀 Instalación y Configuración

### Requisitos Previos

1. Python 3.12+
2. Cuenta de Telegram Bot ([@BotFather](https://t.me/BotFather))
3. Cuenta de Twilio con número telefónico
4. API Key de OpenAI
5. API Key de ElevenLabs

### Variables de Entorno

Crear archivo `.env` en la raíz del proyecto:

```env
# Telegram
TELEGRAM_BOT_TOKEN=tu_token_de_botfather
TELEGRAM_ADMIN_IDS=tu_telegram_user_id

# Twilio
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_PHONE_NUMBER=+15551234567

# OpenAI
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# ElevenLabs
ELEVENLABS_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Webhook
WEBHOOK_URL=https://tu-dominio.ngrok.io
```

### Instalación Local

```bash
# Clonar repositorio
git clone https://github.com/tu-usuario/llamador-gol-lobohr.git
cd llamador-gol-lobohr

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar
python main.py
```

## ☁️ Despliegue en Railway

Ver documentación completa en [RAILWAY_DEPLOY.md](RAILWAY_DEPLOY.md)

### Pasos Rápidos

1. **Subir a GitHub**
```bash
git init
git add .
git commit -m "Initial commit"
git push origin main
```

2. **Crear proyecto en Railway**
   - Login en https://railway.app
   - New Project → Deploy from GitHub
   - Seleccionar repositorio

3. **Configurar variables de entorno**
   - Variables tab → New Variable
   - Agregar todas las variables del `.env`

4. **Generar dominio**
   - Settings → Networking → Generate Domain
   - Actualizar `WEBHOOK_URL` con el dominio generado

5. **Configurar Twilio**
   - Voice webhook: `https://tu-dominio.railway.app/webhook/voice`
   - Status webhook: `https://tu-dominio.railway.app/webhook/status`

## 💡 Uso

### Comandos de Telegram

```
/start - Iniciar bot y ver comandos
/llamar +573001234567 - Hacer llamada individual
/masivo +573001234567 +573001234568 - Llamadas masivas
/activas - Ver llamadas en curso
/colgar - Finalizar todas las llamadas
/stats - Estadísticas del sistema
```

### Ejemplo de Conversación

```
Usuario: Hola
Asesora: ¡Hola! Buen día, soy Carolina de Bancolombia. 
         ¿En qué puedo ayudarte hoy?

Usuario: ¿Cuál es el saldo de mi cuenta?
Asesora: Con gusto te ayudo con eso. Por seguridad, 
         ¿me podrías confirmar tu número de documento?

Usuario: 1234567890
Asesora: Perfecto. Estoy consultando tu información...
```

## 🔧 Configuración Avanzada

### Ajustar Voz

Editar en [config.py](config.py):

```python
# Más estable y menos variada
voice_stability: float = 0.70

# Más similar a la voz original
voice_similarity: float = 0.90

# Menos expresiva, más neutral
voice_style: float = 0.40
```

### Ajustar IA

```python
# Más creativa y variada
ai_temperature: float = 0.90

# Respuestas más largas
ai_max_tokens: int = 80
```

### Ajustar Timeouts de Llamada

```python
# Más tiempo para que el usuario comience a hablar
gather_timeout: int = 8

# Más tiempo de silencio antes de considerar que terminó
speech_timeout: int = 3
```

## 📊 Monitoreo

### Logs Estructurados

El sistema genera logs detallados en `logs/`:

```
✅ Voz colombiana profesional (E5HSnXz7WUojYdJeUcng) inicializada
🎤 Generando voz: '¡Hola! Buen día, soy Carolina...'
✅ Audio generado exitosamente: 45,678 bytes (44.6 KB)
📞 Llamada iniciada: +573001234567
💬 Usuario dijo: "Cuál es mi saldo"
🤖 IA responde: "Con gusto te ayudo con eso..."
```

### Métricas en Tiempo Real

```python
# Ver llamadas activas
/activas

# Respuesta:
📊 Llamadas Activas: 3
├─ +573001234567 (2:34)
├─ +573001234568 (1:15)
└─ +573001234569 (0:45)
```

## 🛡️ Seguridad

### Variables de Entorno
- ✅ Nunca commitear archivos `.env`
- ✅ Usar variables de entorno en producción
- ✅ Rotar API keys periódicamente

### Validación
- ✅ Solo admins pueden usar comandos
- ✅ Validación de números telefónicos
- ✅ Rate limiting en llamadas

### Logging
- ✅ Logs estructurados y seguros
- ✅ No registrar información sensible
- ✅ Rotación automática de logs

## 🧪 Testing

```bash
# Ejecutar tests
pytest tests/

# Con cobertura
pytest --cov=. tests/
```

## 📝 Estructura del Proyecto

```
llamador-gol-lobohr/
├── main.py                 # Punto de entrada
├── config.py              # Configuración central
├── telegram_bot.py        # Bot de Telegram
├── voip_manager.py        # Gestión de llamadas
├── voice_synthesizer.py   # Síntesis de voz
├── ai_conversation.py     # IA conversacional
├── webhook_server.py      # Servidor FastAPI
├── call_flows.py          # Flujos de llamadas
├── requirements.txt       # Dependencias
├── Procfile              # Railway config
├── railway.json          # Railway settings
├── README.md             # Este archivo
├── RAILWAY_DEPLOY.md     # Guía de despliegue
├── audio_cache/          # Cache de audio
└── logs/                 # Logs del sistema
```

## 🤝 Contribuir

1. Fork el proyecto
2. Crear rama feature (`git checkout -b feature/nueva-caracteristica`)
3. Commit cambios (`git commit -m 'Agregar nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Abrir Pull Request

## 📄 Licencia

Este proyecto es privado y propietario.

## 🆘 Soporte

Para soporte y consultas:
- 📧 Email: tu-email@ejemplo.com
- 💬 Telegram: @tu_usuario

## 🙏 Agradecimientos

- **ElevenLabs** - Síntesis de voz natural
- **OpenAI** - IA conversacional
- **Twilio** - Infraestructura VoIP
- **Railway** - Plataforma de despliegue

---

**Desarrollado con ❤️ para brindar la mejor experiencia de atención al cliente**
