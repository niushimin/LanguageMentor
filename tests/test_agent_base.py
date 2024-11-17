import unittest
from unittest.mock import patch, mock_open
from src.agents.agent_base import AgentBase
import os, sys

# 添加 src 目录到模块搜索路径，以便可以导入 src 目录中的模块
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))


class TestAgentBase(unittest.TestCase):

    # Test for load_prompt method
    @patch("builtins.open", new_callable=mock_open, read_data="Mocked prompt data")
    def test_load_prompt(self, mock_file):
        # Simulate reading from a file and assert the content is correct
        agent = AgentBase(name="test", prompt_file="test_prompt.txt")
        self.assertEqual(agent.load_prompt(), "Mocked prompt data")
        mock_file.assert_called_with("test_prompt.txt", "r", encoding="utf-8")

    # Test for load_intro method
    @patch("builtins.open", new_callable=mock_open, read_data='{"intro": "Test Intro"}')
    def test_load_intro(self, mock_file):
        # Simulate reading from a JSON file
        agent = AgentBase(
            name="test", prompt_file="test_prompt.txt", intro_file="test_intro.json"
        )
        self.assertEqual(agent.load_intro(), {"intro": "Test Intro"})
        mock_file.assert_called_with("test_intro.json", "r", encoding="utf-8")

    # Test for create_chatbot method
    @patch("src.agents.agent_base.ChatOpenAI", autospec=True)
    @patch("builtins.open", new_callable=mock_open, read_data="Mocked prompt data")
    def test_create_chatbot(self, mock_file, MockChatOpenAI):
        agent = AgentBase(name="test", prompt_file="test_prompt.txt")
        agent.create_chatbot()
        self.assertIsNotNone(agent.chatbot)
        self.assertIsNotNone(agent.chatbot_with_history)
        mock_file.assert_called_with("test_prompt.txt", "r", encoding="utf-8")

    @patch("src.agents.agent_base.LOG.debug")
    @patch("src.agents.agent_base.RunnableWithMessageHistory.invoke")
    @patch("builtins.open", new_callable=mock_open, read_data="Mocked prompt data")
    def test_chat_with_history(self, mock_invoke):
        mock_invoke.return_value.content = "Test Response"
        agent = AgentBase(name="test", prompt_file="test_prompt.txt")

        response = agent.chat_with_history("Test Input")
        self.assertNotEqual(response, "Test Response")


if __name__ == "__main__":
    unittest.main()
