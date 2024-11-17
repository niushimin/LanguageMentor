import unittest
from src.agents.scenario_agent import ScenarioAgent
from unittest.mock import patch, MagicMock
import os, sys

# 添加 src 目录到模块搜索路径，以便可以导入 src 目录中的模块
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))


class TestScenarioAgent(unittest.TestCase):

    @patch("src.agents.scenario_agent.AgentBase.chat_with_history")
    def test_scenario_agent(self, mock_chat_with_history):
        mock_chat_with_history.return_value = "Test Scenario Response"
        agent = ScenarioAgent(scenario_name="job_interview")
        response = agent.chat_with_history("Test Input")
        self.assertEqual(response, "Test Scenario Response")

    @patch("src.agents.scenario_agent.get_session_history")
    def test_start_new_session(self, mock_get_session_history):
        mock_get_session_history.return_value.messages = []
        agent = ScenarioAgent(scenario_name="job_interview")
        initial_message = agent.start_new_session()
        self.assertNotEqual(initial_message, "Test AI Message")


if __name__ == "__main__":
    unittest.main()
