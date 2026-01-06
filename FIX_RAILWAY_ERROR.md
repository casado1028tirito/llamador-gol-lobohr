# 🔧 SOLUCIÓN RÁPIDA - Error de Variables en Railway

## ❌ Error Actual

```
pydantic_core._pydantic_core.ValidationError: 8 validation errors for Settings
telegram_bot_token: Field required
telegram_admin_ids: Field required
twilio_account_sid: Field required
twilio_auth_token: Field required
twilio_phone_number: Field required
openai_api_key: Field required
elevenlabs_api_key: Field required
webhook_url: Field required
```

## ✅ Solución (5 minutos)

### Paso 1: Ir a Railway Variables

1. Abre tu proyecto en Railway
2. Click en la pestaña **"Variables"**
3. Verás solo `PORT=8080`

### Paso 2: Agregar Variables Faltantes

Click en **"New Variable"** y agrega cada una de estas:

```env
TELEGRAM_BOT_TOKEN=tu_token_de_botfather
TELEGRAM_ADMIN_IDS=tu_telegram_user_id
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_PHONE_NUMBER=+15551234567
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
ELEVENLABS_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
WEBHOOK_URL=https://tu-proyecto.up.railway.app
```

### Paso 3: Obtener tus Valores Reales

#### TELEGRAM_BOT_TOKEN
1. Ir a [@BotFather](https://t.me/BotFather) en Telegram
2. Enviar `/mybots`
3. Seleccionar tu bot
4. Click en "API Token"
5. Copiar el token (formato: `1234567890:ABCdefGHI...`)

#### TELEGRAM_ADMIN_IDS
1. Ir a [@userinfobot](https://t.me/userinfobot)
2. Enviar `/start`
3. Copiar tu "Id" (ejemplo: `123456789`)

#### TWILIO_ACCOUNT_SID y TWILIO_AUTH_TOKEN
1. Ir a https://console.twilio.com
2. En el Dashboard, buscar "Account Info"
3. Copiar "Account SID" (empieza con `AC`)
4. Copiar "Auth Token" (click en el ojo para ver)

#### TWILIO_PHONE_NUMBER
1. En Twilio Console: Phone Numbers → Manage → Active Numbers
2. Copiar tu número (formato: `+15551234567`)

#### OPENAI_API_KEY
1. Ir a https://platform.openai.com/api-keys
2. Click en "Create new secret key"
3. Copiar la key (empieza con `sk-`)

#### ELEVENLABS_API_KEY
1. Ir a https://elevenlabs.io/app/settings
2. En la sección "API Key", copiar tu key

#### WEBHOOK_URL
1. En Railway, ir a **Settings** → **Networking**
2. Click en **"Generate Domain"**
3. Copiar el dominio generado (ejemplo: `llamador-production-a1b2.up.railway.app`)
4. Usar: `https://tu-dominio-copiado.up.railway.app`

### Paso 4: Guardar y Redeploy

1. **Railway detectará los cambios automáticamente**
2. Espera 1-2 minutos
3. Click en **"Deployments"** para ver el progreso

### Paso 5: Verificar Logs

En Railway → Deployments → View Logs

**✅ Logs exitosos:**
```
✅ Voz colombiana profesional (E5HSnXz7WUojYdJeUcng) inicializada
✅ Cliente Twilio inicializado correctamente
✅ Servidor webhook activo
✅ Bot de Telegram iniciado
🎉 Sistema completamente inicializado y operativo
```

**❌ Si sigues viendo errores:**
- Verifica que copiaste todos los valores correctamente
- Asegúrate de no tener espacios al inicio/final
- Verifica que los tokens sean válidos

---

## 🎙️ Configuración de Voz Colombiana

**Ya está configurada automáticamente en el código:**

- **Voice ID:** `E5HSnXz7WUojYdJeUcng`
- **Estabilidad:** 0.55 (Natural y conversacional)
- **Similitud:** 0.85 (Alta fidelidad)
- **Estilo:** 0.65 (Muy expresiva)
- **Speaker Boost:** Activado (Claridad telefónica)

**No necesitas cambiar nada en el código** - la voz ya está optimizada para:
- ✅ Acento colombiano (Medellín)
- ✅ Tono profesional bancario
- ✅ Máxima naturalidad y expresividad
- ✅ Fluidez conversacional

---

## 📋 Checklist de Verificación

Marca cada item cuando lo completes:

- [ ] `TELEGRAM_BOT_TOKEN` agregado
- [ ] `TELEGRAM_ADMIN_IDS` agregado
- [ ] `TWILIO_ACCOUNT_SID` agregado
- [ ] `TWILIO_AUTH_TOKEN` agregado
- [ ] `TWILIO_PHONE_NUMBER` agregado
- [ ] `OPENAI_API_KEY` agregado
- [ ] `ELEVENLABS_API_KEY` agregado
- [ ] `WEBHOOK_URL` agregado con dominio de Railway
- [ ] Deployment exitoso en Railway
- [ ] Logs muestran "Sistema completamente inicializado"
- [ ] Bot responde a `/start` en Telegram

---

## 🆘 Problemas Comunes

### "Bot doesn't respond to /start"
**Solución:** Asegúrate de que `TELEGRAM_BOT_TOKEN` sea correcto

### "Twilio authentication failed"
**Solución:** Verifica `TWILIO_ACCOUNT_SID` y `TWILIO_AUTH_TOKEN`

### "ElevenLabs API error"
**Solución:** 
1. Verifica tu API key
2. Verifica que tengas créditos en tu cuenta
3. Ir a https://elevenlabs.io/app/settings

### "Webhook URL not accessible"
**Solución:**
1. Verifica que el dominio esté generado en Railway
2. Asegúrate de usar `https://` (no `http://`)
3. No incluyas `/` al final

---

## ✨ Después de Configurar

### 1. Configura Twilio Webhooks

Ve a https://console.twilio.com → Phone Numbers → Tu número

**Voice Configuration:**
- A CALL COMES IN: `https://tu-dominio.railway.app/webhook/voice` (POST)
- STATUS CALLBACK: `https://tu-dominio.railway.app/webhook/status` (POST)

### 2. Prueba el Sistema

En Telegram, envía a tu bot:
```
/start
```

Deberías ver:
```
📞 SISTEMA DE LLAMADAS AUTOMATIZADAS

🎯 COMANDOS DISPONIBLES:
/llamar +573001234567 - Hacer llamada
/activas - Ver llamadas en curso
...
```

### 3. Haz una Llamada de Prueba

```
/llamar +573001234567
```

La voz colombiana profesional responderá con naturalidad y expresividad.

---

## 📞 Soporte

Si después de seguir estos pasos aún tienes problemas:

1. Verifica los logs en Railway (Deployments → View Logs)
2. Revisa que todas las variables tengan valores válidos
3. Asegúrate de que tu cuenta de ElevenLabs tenga créditos
4. Verifica que tu cuenta de Twilio esté activa

---

**¡Listo! Tu sistema estará funcionando con la voz colombiana profesional en menos de 5 minutos. 🎉**
