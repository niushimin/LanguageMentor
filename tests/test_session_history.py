import unittest
from src.agents.session_history import get_session_history
from langchain_core.chat_history import InMemoryChatMessageHistory
import os, sys

# 添加 src 目录到模块搜索路径，以便可以导入 src 目录中的模块
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))


class TestSessionHistory(unittest.TestCase):

    def test_get_session_history(self):
        session_id = "test_session"
        history = get_session_history(session_id)
        self.assertIsInstance(history, InMemoryChatMessageHistory)

    def test_multiple_sessions(self):
        session_id_1 = "test_session_1"
        session_id_2 = "test_session_2"

        history_1 = get_session_history(session_id_1)
        history_2 = get_session_history(session_id_2)

        self.assertIsNot(history_1, history_2)


if __name__ == "__main__":
    unittest.main()
