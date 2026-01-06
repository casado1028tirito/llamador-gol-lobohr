"""Configuración - Sistema de Llamadas Colombia"""
from pydantic_settings import BaseSettings
from pydantic import Field
from typing import List, Optional


class Settings(BaseSettings):
    """Configuración optimizada para llamadas en Colombia"""
    
    # APIs esenciales - Con valores por defecto para evitar crashes
    telegram_bot_token: str = Field(default="")
    telegram_admin_ids: str = Field(default="")
    twilio_account_sid: str = Field(default="")
    twilio_auth_token: str = Field(default="")
    twilio_phone_number: str = Field(default="")
    openai_api_key: str = Field(default="")
    elevenlabs_api_key: str = Field(default="")
    
    # ========================================
    # VOZ COLOMBIANA - ASESORA PROFESIONAL BANCARIA
    # ========================================
    
    # Voz E5HSnXz7WUojYdJeUcng - Natural, expresiva, profesional
    # Ideal para asesora de banco colombiano en Medellín
    voice_bot: str = "E5HSnXz7WUojYdJeUcng"  # Voz colombiana profesional
    default_voice_id: str = "E5HSnXz7WUojYdJeUcng"
    
    # CONFIGURACIÓN ÓPTIMA PARA VOZ NATURAL Y EXPRESIVA
    # Ajustada para máxima naturalidad y fluidez en conversación bancaria
    voice_stability: float = 0.55  # Balance entre naturalidad y consistencia
    voice_similarity: float = 0.85  # Alta fidelidad con la voz original
    voice_style: float = 0.65      # Muy expresiva y conversacional
    voice_speaker_boost: bool = True  # Claridad cristalina en llamadas telefónicas
    
    # IA Conversacional - Optimizada para atención bancaria profesional
    ai_model: str = "gpt-4o-mini"  # Modelo eficiente y rápido
    ai_temperature: float = 0.82  # Profesional, cálida y natural
    ai_max_tokens: int = 65  # Respuestas completas y precisas (15-30 palabras)
    ai_timeout: float = 2.5  # Tiempo adecuado para respuestas de calidad
    
    # Configuración de llamadas - Optimizada para conversación natural
    gather_timeout: int = 6  # Tiempo para que el cliente comience a hablar
    speech_timeout: int = 2  # Silencio que indica fin de respuesta
    max_speech_time: int = 60  # Tiempo máximo por intervención del cliente
    max_concurrent_calls: int = 50  # Capacidad de llamadas simultáneas
    no_speech_attempts: int = 2  # Intentos antes de finalizar por silencio
    profanity_filter: bool = False  # Sin filtro para lenguaje natural
    
    # Reconocimiento de voz - Optimizado para español colombiano
    speech_model: str = "phone_call"  # Modelo especializado en llamadas
    language: str = "es-CO"  # Español de Colombia
    enhanced: bool = True  # Reconocimiento mejorado activado
    partial_result_callback: bool = False  # Desactivar resultados parciales
    profanity_filter_twilio: bool = False  # Sin filtro restrictivo
    
    # DTMF - Entrada por teclado telefónico
    dtmf_enabled: bool = True  # Permitir entrada numérica
    num_digits: int = 20  # Máximo de dígitos DTMF
    
    # Webhook - Configuración para Railway (puerto dinámico)
    webhook_url: str = Field(default="")
    webhook_port: int = Field(default=8000, validation_alias='PORT')
    
    class Config:
        env_file = ".env"
        case_sensitive = False
        extra = "ignore"  # Ignorar campos adicionales
        
    def validate_configuration(self) -> bool:
        """Validar que las configuraciones críticas estén presentes"""
        required_fields = {
            "telegram_bot_token": self.telegram_bot_token,
            "twilio_account_sid": self.twilio_account_sid,
            "twilio_auth_token": self.twilio_auth_token,
            "openai_api_key": self.openai_api_key,
            "elevenlabs_api_key": self.elevenlabs_api_key,
            "webhook_url": self.webhook_url
        }
        
        missing_fields = [field for field, value in required_fields.items() if not value]
        
        if missing_fields:
            from loguru import logger
            logger.error(f"❌ Variables de entorno faltantes: {', '.join(missing_fields)}")
            logger.error("⚠️ Configura estas variables en Railway o tu .env antes de continuar")
            return False
        
        return True
    
    @property
    def admin_ids_list(self) -> List[int]:
        """Convertir IDs de admin de string a lista de integers"""
        return [int(id.strip()) for id in self.telegram_admin_ids.split(",") if id.strip()]


settings = Settings()
