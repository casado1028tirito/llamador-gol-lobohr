"""Sistema de Llamadas Automatizadas - Asesora Bancaria Colombiana
Arquitectura modular y profesional con manejo robusto de errores
"""
import asyncio
import os
import threading
from loguru import logger
from telegram_bot import TelegramBot
from voip_manager import VoIPManager
from voice_synthesizer import VoiceSynthesizer
from ai_conversation import AIConversation
from config import settings
import uvicorn
from webhook_server import app, set_caller_bot
import sys

# Configuración de logging profesional
os.makedirs("logs", exist_ok=True)
logger.add(
    "logs/app_{time}.log",
    rotation="1 day",
    retention="7 days",
    level="INFO",
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan> - <level>{message}</level>"
)


class CallerBot:
    """Sistema principal de llamadas automatizadas
    
    Gestiona la integración de todos los componentes:
    - Bot de Telegram para control
    - VoIP Manager para llamadas
    - Voice Synthesizer para generación de audio
    - AI Conversation para respuestas inteligentes
    - Webhook Server para recibir eventos
    """
    
    def __init__(self):
        self.telegram_bot: TelegramBot = TelegramBot(self)
        self.voip_manager: VoIPManager = VoIPManager(self)
        self.voice_synthesizer: VoiceSynthesizer = VoiceSynthesizer()
        self.ai_conversation: AIConversation = AIConversation()
        self.webhook_server: threading.Thread = None
        self._is_running: bool = False
        
    async def start(self):
        """Iniciar todos los servicios del sistema"""
        if self._is_running:
            logger.warning("⚠️ El sistema ya está en ejecución")
            return
            
        logger.info("🚀 Iniciando Sistema de Llamadas Automatizadas...")
        
        try:
            # Validar configuración antes de iniciar
            if not settings.validate_configuration():
                logger.error("❌ Configuración inválida. Verifica las variables de entorno.")
                sys.exit(1)
            
            # Inicializar componentes en orden
            logger.info("🎙️ Inicializando sintetizador de voz...")
            await self.voice_synthesizer.initialize()
            
            logger.info("📞 Inicializando gestor VoIP...")
            await self.voip_manager.initialize()
            
            # Configurar referencia del bot en el webhook server
            set_caller_bot(self)
            
            # Iniciar servidor webhook en thread dedicado
            logger.info(f"🌐 Iniciando servidor webhook en puerto {settings.webhook_port}...")
            self.webhook_server = threading.Thread(
                target=self._run_webhook_server,
                daemon=True,
                name="WebhookServer"
            )
            self.webhook_server.start()
            
            # Esperar a que el servidor esté listo
            await asyncio.sleep(2)
            logger.success("✅ Servidor webhook activo")
            
            # Iniciar bot de Telegram
            logger.info("📱 Iniciando bot de Telegram...")
            await self.telegram_bot.start()
            
            self._is_running = True
            logger.success("🎉 Sistema completamente inicializado y operativo")
            
        except Exception as e:
            logger.error(f"❌ Error crítico durante inicialización: {e}")
            logger.exception("Detalles del error:")
            await self.stop()
            raise
    
    def _run_webhook_server(self):
        """Ejecutar servidor webhook en thread dedicado"""
        try:
            port = settings.webhook_port
            logger.info(f"🌐 Webhook server escuchando en 0.0.0.0:{port}")
            logger.info(f"📡 URL pública: {settings.webhook_url}")
            
            uvicorn.run(
                app,
                host="0.0.0.0",
                port=port,
                log_level="info",
                access_log=True
            )
        except Exception as e:
            logger.error(f"❌ Error en servidor webhook: {e}")
            raise
    
    async def stop(self):
        """Detener todos los servicios de forma ordenada"""
        if not self._is_running:
            logger.info("ℹ️ El sistema ya está detenido")
            return
            
        logger.info("🛑 Deteniendo servicios...")
        
        try:
            await self.telegram_bot.stop()
            logger.info("✅ Bot de Telegram detenido")
            
            await self.voip_manager.cleanup()
            logger.info("✅ VoIP Manager limpiado")
            
            self._is_running = False
            logger.success("✅ Sistema detenido correctamente")
            
        except Exception as e:
            logger.error(f"❌ Error al detener servicios: {e}")
            raise


async def main():
    """Punto de entrada principal del sistema"""
    logger.info("=" * 70)
    logger.info("🚀 SISTEMA DE LLAMADAS AUTOMATIZADAS - ASESORA BANCARIA COLOMBIANA")
    logger.info("=" * 70)
    logger.info(f"📍 Webhook URL: {settings.webhook_url or 'NO CONFIGURADO'}")
    logger.info(f"🎙️ Voice ID: {settings.voice_bot}")
    logger.info(f"🤖 Modelo IA: {settings.ai_model}")
    logger.info(f"🌍 Idioma: {settings.language}")
    logger.info("=" * 70)
    
    bot = CallerBot()
    
    try:
        logger.info("🔧 Iniciando componentes del sistema...")
        await bot.start()
        
        logger.success("✅ SISTEMA ACTIVO Y LISTO")
        logger.info("📞 Esperando llamadas entrantes...")
        logger.info("💡 Presiona Ctrl+C para detener el sistema")
        
        # Configurar manejo de señales de interrupción
        import signal
        stop_event = asyncio.Event()
        
        def signal_handler(signum, frame):
            signal_name = "SIGINT" if signum == signal.SIGINT else "SIGTERM"
            logger.info(f"⚠️ Señal {signal_name} recibida, deteniendo sistema...")
            stop_event.set()
        
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
        
        # Mantener el sistema en ejecución
        await stop_event.wait()
        
    except KeyboardInterrupt:
        logger.info("⚠️ Interrupción manual detectada (Ctrl+C)")
    except Exception as e:
        logger.error(f"❌ Error fatal en el sistema: {e}")
        logger.exception("Detalles completos del error:")
    finally:
        await bot.stop()
        logger.info("👋 Sistema finalizado")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("👋 Adiós")
    except Exception as e:
        logger.error(f"❌ Error no manejado: {e}")
        sys.exit(1)
