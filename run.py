"""
IPQC Automation System - Flask Backend
Main application entry point (DEVELOPMENT MODE)

For PRODUCTION deployment, use production_server.py instead
"""
from app import create_app
import os

app = create_app()

if __name__ == '__main__':
    print("=" * 60)
    print("🔧 PDI Complete System - DEVELOPMENT Server")
    print("=" * 60)
    print("⚠️  This is DEVELOPMENT mode with auto-reload enabled")
    print("📝 For PRODUCTION, use: python production_server.py")
    print("=" * 60)
    
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True, use_reloader=True, reloader_type='stat')
