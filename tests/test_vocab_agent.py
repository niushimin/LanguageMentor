import unittest
from src.agents.vocab_agent import VocabAgent
from unittest.mock import patch, MagicMock
import os, sys

# 添加 src 目录到模块搜索路径，以便可以导入 src 目录中的模块
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))


class TestVocabAgent(unittest.TestCase):

    @patch("src.agents.vocab_agent.AgentBase.chat_with_history")
    def test_vocab_agent(self, mock_chat_with_history):
        mock_chat_with_history.return_value = "Test Vocab Response"
        agent = VocabAgent()
        response = agent.chat_with_history("Test Input")
        self.assertEqual(response, "Test Vocab Response")

    @patch("src.agents.vocab_agent.get_session_history")
    def test_restart_session(self, mock_get_session_history):
        mock_get_session_history.return_value.clear = MagicMock()
        agent = VocabAgent()
        response = agent.restart_session()
        mock_get_session_history.return_value.clear.assert_called()
        self.assertNotEqual(response.messages, [])


if __name__ == "__main__":
    unittest.main()
