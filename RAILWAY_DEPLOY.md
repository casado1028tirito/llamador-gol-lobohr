# 🚀 Guía de Despliegue en Railway - Sistema Profesional

## 📋 Requisitos Previos

Antes de comenzar, asegúrate de tener:

1. ✅ Cuenta de GitHub
2. ✅ Cuenta de Railway (https://railway.app)
3. ✅ Token de Telegram Bot (obtener en @BotFather)
4. ✅ Cuenta de Twilio con número telefónico
5. ✅ API Key de OpenAI
6. ✅ API Key de ElevenLabs

---

## 🔧 Paso 1: Preparar el Código

### 1.1 Subir a GitHub

```powershell
# Navegar a la carpeta del proyecto
cd C:\Users\Hansel\Desktop\LLAMADOR-GOL-LOBOHR

# Inicializar repositorio (si no existe)
git init

# Agregar repositorio remoto
git remote add origin https://github.com/TU_USUARIO/TU_REPOSITORIO.git

# Agregar todos los archivos
git add .

# Commit
git commit -m "Sistema de llamadas automatizadas - Asesora bancaria colombiana"

# Subir a GitHub
git push -u origin main
```

**Nota:** Si necesitas crear un token de acceso personal:
- Ve a: https://github.com/settings/tokens
- Click en "Generate new token (classic)"
- Selecciona permisos: `repo`
- Guarda el token generado

---

## 🚂 Paso 2: Desplegar en Railway

### 2.1 Crear Proyecto

1. Ir a https://railway.app
2. Click en **"Login"** → Iniciar sesión con GitHub
3. Click en **"New Project"**
4. Seleccionar **"Deploy from GitHub repo"**
5. Buscar y seleccionar tu repositorio
6. Railway comenzará el despliegue automático

### 2.2 Configurar Variables de Entorno

**⚠️ IMPORTANTE:** El error que viste se debe a que Railway necesita estas variables configuradas.

1. En tu proyecto de Railway, click en la pestaña **"Variables"**
2. Click en **"New Variable"** y agregar cada una:

```env
# ======================================
# TELEGRAM
# ======================================
TELEGRAM_BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
TELEGRAM_ADMIN_IDS=123456789

# ======================================
# TWILIO (VoIP)
# ======================================
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_PHONE_NUMBER=+15551234567

# ======================================
# OPENAI (Conversación IA)
# ======================================
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# ======================================
# ELEVENLABS (Voz Colombiana)
# ======================================
ELEVENLABS_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# ======================================
# WEBHOOK (Railway lo genera)
# ======================================
WEBHOOK_URL=https://tu-proyecto.up.railway.app
```

### 2.3 Generar Dominio Público

1. En Railway, ve a **"Settings"**
2. Busca la sección **"Networking"**
3. Click en **"Generate Domain"**
4. Copia el dominio generado (ejemplo: `llamador-production-a1b2.up.railway.app`)
5. Regresa a **"Variables"**
6. Actualiza la variable `WEBHOOK_URL` con: `https://tu-dominio-copiado.up.railway.app`
7. Guarda los cambios

### 2.4 Verificar el Despliegue

Railway redesplegará automáticamente después de cambiar las variables.

**Ver logs:**
1. Click en **"Deployments"**
2. Click en el deployment más reciente
3. Click en **"View Logs"**

**Logs exitosos deberían mostrar:**
```
✅ Voz colombiana profesional (E5HSnXz7WUojYdJeUcng) inicializada
✅ Cliente Twilio inicializado correctamente
✅ Servidor webhook activo
✅ Bot de Telegram iniciado
🎉 Sistema completamente inicializado y operativo
```

**Si ves errores de validación:**
- Verifica que todas las variables de entorno estén configuradas
- Asegúrate de que no tengan espacios al inicio o final
- Verifica que los tokens sean válidos

---

## 📞 Paso 3: Configurar Twilio

### 3.1 Acceder a Twilio Console

1. Ir a: https://console.twilio.com
2. Iniciar sesión
3. Navegar a **"Phone Numbers"** → **"Manage"** → **"Active Numbers"**
4. Click en tu número de teléfono

### 3.2 Configurar Webhooks de Voz

En la sección **"Voice Configuration"**:

**A CALL COMES IN:**
```
Webhook: https://tu-dominio.railway.app/webhook/voice
HTTP Method: POST
```

**STATUS CALLBACK URL:**
```
Webhook: https://tu-dominio.railway.app/webhook/status
HTTP Method: POST
```

### 3.3 Guardar Configuración

Click en **"Save Configuration"** al final de la página.

---

## ✅ Paso 4: Probar el Sistema

### 4.1 Probar Bot de Telegram

1. Abrir Telegram
2. Buscar tu bot por su username
3. Enviar `/start`

**Respuesta esperada:**
```
📞 SISTEMA DE LLAMADAS AUTOMATIZADAS

🎯 COMANDOS DISPONIBLES:
/llamar +573001234567 - Hacer llamada
/activas - Ver llamadas en curso
/colgar - Finalizar todas las llamadas
```

### 4.2 Hacer Llamada de Prueba

```
/llamar +573001234567
```

**El sistema debería:**
1. ✅ Confirmar que la llamada se inició
2. 📞 Llamar al número
3. 🎙️ Reproducir saludo con voz colombiana profesional
4. 💬 Responder a las preguntas del usuario
5. 📊 Reportar el resultado en Telegram

---

## 🔍 Solución de Problemas

### Error: "Field required" en Railway

**Causa:** Variables de entorno no configuradas

**Solución:**
1. Ir a Railway → Variables
2. Verificar que TODAS las variables estén configuradas
3. Redeploy el proyecto

### Error: "Twilio authentication failed"

**Causa:** Credenciales de Twilio incorrectas

**Solución:**
1. Verificar `TWILIO_ACCOUNT_SID` y `TWILIO_AUTH_TOKEN` en Twilio Console
2. Actualizar las variables en Railway
3. Redeploy

### Error: "ElevenLabs API error"

**Causa:** API key inválida o sin créditos

**Solución:**
1. Verificar API key en https://elevenlabs.io/app/settings
2. Verificar que tengas créditos disponibles
3. Actualizar `ELEVENLABS_API_KEY` en Railway

### Las llamadas no se conectan

**Causa:** Webhooks de Twilio no configurados

**Solución:**
1. Verificar URLs de webhook en Twilio
2. Asegurarse de usar el dominio correcto de Railway
3. Verificar que los webhooks sean POST, no GET

### La voz no suena natural

**Causa:** Configuración de voz incorrecta

**Solución:**
Ya está configurada óptimamente en el código:
- Voice ID: `E5HSnXz7WUojYdJeUcng`
- Stability: 0.55 (natural)
- Similarity: 0.85 (fidelidad alta)
- Style: 0.65 (muy expresiva)

---

## 📊 Monitoreo del Sistema

### Ver Logs en Tiempo Real

```bash
# En Railway → Deployments → View Logs
```

### Métricas Importantes

**CPU y Memoria:**
- Railway → Metrics
- Monitorear uso de recursos

**Llamadas Activas:**
- Usar comando `/activas` en Telegram

**Errores:**
- Revisar logs en Railway
- Buscar líneas con ❌

---

## 🎙️ Características de la Voz

### Voz: E5HSnXz7WUojYdJeUcng

**Características:**
- 🇨🇴 Acento colombiano (Medellín)
- 👩‍💼 Tono profesional bancario
- 😊 Cálida y amigable
- 🎯 Alta expresividad (0.65)
- 📞 Optimizada para llamadas telefónicas

**Configuración:**
```python
voice_stability: 0.55    # Balance naturalidad/consistencia
voice_similarity: 0.85   # Fidelidad a la voz original
voice_style: 0.65        # Expresividad alta
voice_speaker_boost: True # Claridad en teléfono
```

---

## 🔄 Actualizar el Sistema

### Cuando hagas cambios en el código:

```powershell
# 1. Commit cambios
git add .
git commit -m "Descripción de los cambios"

# 2. Push a GitHub
git push origin main

# 3. Railway redesplegará automáticamente
```

Railway detecta los cambios en GitHub y redesplega automáticamente.

---

## 🆘 Soporte

### Recursos Útiles

- **Railway Docs:** https://docs.railway.app
- **Twilio Docs:** https://www.twilio.com/docs
- **ElevenLabs Docs:** https://docs.elevenlabs.io
- **OpenAI Docs:** https://platform.openai.com/docs

### Verificar Estado del Sistema

```
/start - Verificar que el bot responde
/activas - Ver llamadas en curso
```

---

## ✨ Arquitectura del Sistema

```
┌─────────────────────────────────────────────────┐
│           RAILWAY (Cloud Platform)              │
│                                                 │
│  ┌──────────────────────────────────────────┐  │
│  │         main.py (Entry Point)            │  │
│  │  ┌──────────────────────────────────┐   │  │
│  │  │    CallerBot (Orchestrator)      │   │  │
│  │  │                                  │   │  │
│  │  │  ┌────────────────────────────┐ │   │  │
│  │  │  │  TelegramBot (Control)     │ │   │  │
│  │  │  └────────────────────────────┘ │   │  │
│  │  │  ┌────────────────────────────┐ │   │  │
│  │  │  │  VoIPManager (Twilio)      │ │   │  │
│  │  │  └────────────────────────────┘ │   │  │
│  │  │  ┌────────────────────────────┐ │   │  │
│  │  │  │  VoiceSynthesizer (Voice)  │ │   │  │
│  │  │  │  🎙️ E5HSnXz7WUojYdJeUcng   │ │   │  │
│  │  │  └────────────────────────────┘ │   │  │
│  │  │  ┌────────────────────────────┐ │   │  │
│  │  │  │  AIConversation (OpenAI)   │ │   │  │
│  │  │  └────────────────────────────┘ │   │  │
│  │  │  ┌────────────────────────────┐ │   │  │
│  │  │  │  WebhookServer (FastAPI)   │ │   │  │
│  │  │  └────────────────────────────┘ │   │  │
│  │  └──────────────────────────────────┘   │  │
│  └──────────────────────────────────────────┘  │
└─────────────────────────────────────────────────┘
         ↓                    ↓                ↓
    Telegram API        Twilio API      ElevenLabs API
```

---

## 🎯 Checklist Final

- [ ] Código subido a GitHub
- [ ] Proyecto creado en Railway
- [ ] Todas las variables de entorno configuradas
- [ ] Dominio público generado
- [ ] `WEBHOOK_URL` actualizado con el dominio
- [ ] Webhooks configurados en Twilio
- [ ] Bot de Telegram responde a `/start`
- [ ] Llamada de prueba exitosa
- [ ] Voz suena natural y profesional

---

**¡Sistema Listo para Producción! 🎉**

Sistema profesional con:
- ✅ Arquitectura modular y limpia
- ✅ Manejo robusto de errores
- ✅ Logging profesional
- ✅ Validación de configuración
- ✅ Voz colombiana natural y expresiva
- ✅ Código optimizado y documentado
