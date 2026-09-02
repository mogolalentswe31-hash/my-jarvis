"""
Unit tests for JARVIS AI Assistant
"""

import unittest
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from config import DevelopmentConfig


class TestConfig(unittest.TestCase):
    """Test configuration module"""
    
    def test_config_loaded(self):
        """Test that configuration loads correctly"""
        config = DevelopmentConfig()
        self.assertIsNotNone(config.OPENAI_API_KEY)
        self.assertEqual(config.ASSISTANT_NAME, "JARVIS")
        self.assertTrue(config.DEBUG)


class TestAIEngine(unittest.TestCase):
    """Test AI Engine module"""
    
    def setUp(self):
        """Set up test fixtures"""
        from src.ai_engine import AIEngine
        self.config = DevelopmentConfig()
        self.ai_engine = AIEngine(self.config)
    
    def test_system_prompt_creation(self):
        """Test system prompt is created correctly"""
        self.assertIsNotNone(self.ai_engine.system_prompt)
        self.assertIn("JARVIS", self.ai_engine.system_prompt)
    
    def test_conversation_history_initialization(self):
        """Test conversation history is initialized"""
        self.assertEqual(len(self.ai_engine.conversation_history), 0)
    
    def test_clear_history(self):
        """Test conversation history can be cleared"""
        self.ai_engine.conversation_history.append({"role": "user", "content": "Test"})
        self.ai_engine.clear_history()
        self.assertEqual(len(self.ai_engine.conversation_history), 0)


class TestVoiceProcessor(unittest.TestCase):
    """Test Voice Processor module"""
    
    def setUp(self):
        """Set up test fixtures"""
        from src.voice_processor import VoiceProcessor
        self.config = DevelopmentConfig()
        self.voice_processor = VoiceProcessor(self.config)
    
    def test_voice_processor_initialization(self):
        """Test voice processor initializes correctly"""
        self.assertIsNotNone(self.voice_processor.recognizer)
        self.assertIsNotNone(self.voice_processor.tts_engine)
    
    def test_audio_cache_directory_creation(self):
        """Test audio cache directory is created"""
        self.assertTrue(self.voice_processor.audio_cache_dir.exists())


if __name__ == '__main__':
    unittest.main()
