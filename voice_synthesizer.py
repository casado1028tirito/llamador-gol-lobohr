"""Síntesis de voz profesional - Asesora bancaria colombiana
Sistema optimizado con ElevenLabs para máxima naturalidad y expresividad
"""
from elevenlabs import generate, set_api_key, Voice, VoiceSettings
from loguru import logger
from config import settings
import os
import asyncio
from functools import partial
from typing import Optional


class VoiceSynthesizer:
    """Generador de voz con ElevenLabs - Asesora profesional colombiana
    
    Utiliza la voz E5HSnXz7WUojYdJeUcng optimizada para:
    - Máxima naturalidad y expresividad
    - Fluidez conversacional profesional
    - Claridad en llamadas telefónicas
    - Tono cálido y profesional típico de asesoras bancarias en Medellín
    """
    
    def __init__(self):
        self.voice_id = settings.voice_bot
        self.audio_dir = "audio_cache"
        self._settings: Optional[VoiceSettings] = None
        self._initialized = False
    
    async def initialize(self):
        """Inicializar ElevenLabs con configuración óptima"""
        try:
            set_api_key(settings.elevenlabs_api_key)
            os.makedirs(self.audio_dir, exist_ok=True)
            
            # Configuración optimizada para asesora colombiana
            self._settings = VoiceSettings(
                stability=settings.voice_stability,      # 0.55 - Balance perfecto
                similarity_boost=settings.voice_similarity,  # 0.85 - Alta fidelidad
                style=settings.voice_style,              # 0.65 - Muy expresiva
                use_speaker_boost=settings.voice_speaker_boost  # True - Claridad
            )
            
            self._initialized = True
            logger.info(f"✅ Voz colombiana profesional ({self.voice_id}) inicializada")
            logger.info(f"🎙️ Configuración: Estabilidad={settings.voice_stability}, "
                       f"Similitud={settings.voice_similarity}, Estilo={settings.voice_style}")
        except Exception as e:
            logger.error(f"❌ Error al inicializar sintetizador de voz: {e}")
            raise
    
    async def text_to_speech(self, text: str, filename: Optional[str] = None) -> bytes:
        """Generar audio profesional con modelo turbo v2.5
        
        Args:
            text: Texto a sintetizar
            filename: Nombre opcional del archivo para guardar en caché
            
        Returns:
            bytes: Audio en formato MP3
            
        Raises:
            Exception: Si falla después de 3 reintentos
        """
        if not self._initialized:
            raise Exception("VoiceSynthesizer no inicializado. Llama a initialize() primero.")
        
        # Sistema de reintentos robusto
        max_attempts = 3
        retry_delay = 0.3  # 300ms entre reintentos
        
        for attempt in range(1, max_attempts + 1):
            try:
                logger.info(f"🎤 Generando voz (intento {attempt}/{max_attempts}): "
                          f"'{text[:50]}{'...' if len(text) > 50 else ''}'")
                
                # Ejecutar en thread pool para evitar bloqueo del event loop
                loop = asyncio.get_event_loop()
                audio = await asyncio.wait_for(
                    loop.run_in_executor(
                        None,
                        partial(
                            generate,
                            text=text,
                            voice=Voice(
                                voice_id=self.voice_id,
                                settings=self._settings
                            ),
                            model="eleven_turbo_v2_5"  # Modelo más rápido y eficiente
                        )
                    ),
                    timeout=7.0  # Timeout generoso para mayor confiabilidad
                )
                
                # Normalizar a bytes
                audio_bytes = audio if isinstance(audio, bytes) else b''.join(audio)
                
                # Validación de calidad del audio
                if not audio_bytes or len(audio_bytes) < 1000:
                    raise Exception(f"Audio inválido: {len(audio_bytes) if audio_bytes else 0} bytes")
                
                # Guardar en caché si se especifica
                if filename:
                    filepath = os.path.join(self.audio_dir, filename)
                    with open(filepath, 'wb') as f:
                        f.write(audio_bytes)
                    logger.debug(f"💾 Audio guardado: {filepath}")
                
                logger.success(f"✅ Audio generado exitosamente: {len(audio_bytes):,} bytes "
                             f"({len(audio_bytes) / 1024:.1f} KB)")
                return audio_bytes
                
            except asyncio.TimeoutError:
                logger.warning(f"⏱️ Timeout en intento {attempt}/{max_attempts}")
                if attempt < max_attempts:
                    await asyncio.sleep(retry_delay)
                    continue
                logger.error("❌ ElevenLabs timeout después de 3 intentos")
                raise Exception("Timeout generando audio después de múltiples reintentos")
                
            except Exception as e:
                logger.error(f"❌ Error en intento {attempt}/{max_attempts}: {str(e)}")
                if attempt < max_attempts:
                    await asyncio.sleep(retry_delay)
                    continue
                logger.error(f"❌ Fallo definitivo generando audio: {str(e)}")
                raise
