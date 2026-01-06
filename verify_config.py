"""Script de verificación pre-deployment
Verifica que todas las configuraciones estén correctas antes de desplegar
"""
import os
import sys
from typing import Dict, List, Tuple


def check_environment_variables() -> Tuple[bool, List[str]]:
    """Verificar que todas las variables de entorno necesarias estén presentes"""
    required_vars = [
        "TELEGRAM_BOT_TOKEN",
        "TELEGRAM_ADMIN_IDS",
        "TWILIO_ACCOUNT_SID",
        "TWILIO_AUTH_TOKEN",
        "TWILIO_PHONE_NUMBER",
        "OPENAI_API_KEY",
        "ELEVENLABS_API_KEY",
        "WEBHOOK_URL"
    ]
    
    missing_vars = []
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    return len(missing_vars) == 0, missing_vars


def check_voice_configuration() -> Tuple[bool, str]:
    """Verificar configuración de voz"""
    try:
        from config import settings
        
        expected_voice = "E5HSnXz7WUojYdJeUcng"
        
        if settings.voice_bot != expected_voice:
            return False, f"Voice ID incorrecto: {settings.voice_bot} (esperado: {expected_voice})"
        
        # Verificar configuración óptima
        checks = [
            (settings.voice_stability, 0.55, "stability"),
            (settings.voice_similarity, 0.85, "similarity"),
            (settings.voice_style, 0.65, "style"),
        ]
        
        for actual, expected, name in checks:
            if abs(actual - expected) > 0.01:  # Tolerancia de 0.01
                return False, f"Configuración {name} no óptima: {actual} (esperado: {expected})"
        
        return True, "Configuración de voz correcta"
        
    except Exception as e:
        return False, f"Error al verificar configuración: {str(e)}"


def check_dependencies() -> Tuple[bool, List[str]]:
    """Verificar que todas las dependencias estén instaladas"""
    required_packages = [
        "telegram",
        "twilio",
        "openai",
        "elevenlabs",
        "fastapi",
        "uvicorn",
        "pydantic",
        "pydantic_settings",
        "loguru"
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    return len(missing_packages) == 0, missing_packages


def check_files() -> Tuple[bool, List[str]]:
    """Verificar que todos los archivos necesarios existan"""
    required_files = [
        "main.py",
        "config.py",
        "telegram_bot.py",
        "voip_manager.py",
        "voice_synthesizer.py",
        "ai_conversation.py",
        "webhook_server.py",
        "call_flows.py",
        "requirements.txt",
        "Procfile",
        "railway.json"
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    return len(missing_files) == 0, missing_files


def print_section(title: str):
    """Imprimir sección con formato"""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)


def main():
    """Ejecutar todas las verificaciones"""
    print("\n🔍 VERIFICACIÓN PRE-DEPLOYMENT")
    print("Sistema: Llamadas Automatizadas - Asesora Bancaria Colombiana")
    
    all_passed = True
    
    # 1. Verificar archivos
    print_section("📁 VERIFICACIÓN DE ARCHIVOS")
    files_ok, missing_files = check_files()
    if files_ok:
        print("✅ Todos los archivos necesarios están presentes")
    else:
        print("❌ Archivos faltantes:")
        for file in missing_files:
            print(f"   - {file}")
        all_passed = False
    
    # 2. Verificar dependencias
    print_section("📦 VERIFICACIÓN DE DEPENDENCIAS")
    deps_ok, missing_deps = check_dependencies()
    if deps_ok:
        print("✅ Todas las dependencias están instaladas")
    else:
        print("❌ Paquetes faltantes:")
        for package in missing_deps:
            print(f"   - {package}")
        print("\n💡 Instalar con: pip install -r requirements.txt")
        all_passed = False
    
    # 3. Verificar variables de entorno
    print_section("🔐 VERIFICACIÓN DE VARIABLES DE ENTORNO")
    env_ok, missing_vars = check_environment_variables()
    if env_ok:
        print("✅ Todas las variables de entorno están configuradas")
    else:
        print("❌ Variables faltantes:")
        for var in missing_vars:
            print(f"   - {var}")
        print("\n💡 Configura estas variables en:")
        print("   - Local: archivo .env")
        print("   - Railway: Variables tab")
        all_passed = False
    
    # 4. Verificar configuración de voz
    print_section("🎙️ VERIFICACIÓN DE VOZ")
    voice_ok, voice_msg = check_voice_configuration()
    if voice_ok:
        print(f"✅ {voice_msg}")
        print("   Voice ID: E5HSnXz7WUojYdJeUcng")
        print("   Estabilidad: 0.55 (Natural)")
        print("   Similitud: 0.85 (Alta fidelidad)")
        print("   Estilo: 0.65 (Muy expresiva)")
    else:
        print(f"❌ {voice_msg}")
        all_passed = False
    
    # Resultado final
    print_section("📊 RESULTADO FINAL")
    if all_passed:
        print("✅ ¡TODAS LAS VERIFICACIONES PASARON!")
        print("\n🚀 El sistema está listo para deployment")
        print("\nPasos siguientes:")
        print("1. git add .")
        print("2. git commit -m 'Sistema optimizado y verificado'")
        print("3. git push origin main")
        print("4. Railway redesplegará automáticamente")
        return 0
    else:
        print("❌ ALGUNAS VERIFICACIONES FALLARON")
        print("\n⚠️ Corrige los errores antes de desplegar")
        print("\nPara más información, consulta:")
        print("- README_NEW.md")
        print("- RAILWAY_DEPLOY.md")
        return 1


if __name__ == "__main__":
    sys.exit(main())
