import unittest
from src.agents.conversation_agent import ConversationAgent
from unittest.mock import patch, MagicMock
import os, sys

# 添加 src 目录到模块搜索路径，以便可以导入 src 目录中的模块
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))


class TestConversationAgent(unittest.TestCase):

    @patch("src.agents.conversation_agent.AgentBase.chat_with_history")
    def test_conversation_agent(self, mock_chat_with_history):
        mock_chat_with_history.return_value = "Test Response"
        agent = ConversationAgent()
        response = agent.chat_with_history("Test Input")
        self.assertEqual(response, "Test Response")


if __name__ == "__main__":
    unittest.main()
