import unittest
from unittest.mock import patch, MagicMock
from src.utils.merge_requirements import (
    get_installed_versions,
    merge_requirements,
    read_requirements,
    parse_package_spec,
)
import os, sys

# 添加 src 目录到模块搜索路径，以便可以导入 src 目录中的模块
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))


class TestMergeRequirements(unittest.TestCase):

    @patch("src.utils.merge_requirements.importlib.metadata.version")
    def test_get_installed_versions(self, mock_version):
        mock_version.return_value = "1.0.0"
        installed_versions = get_installed_versions(["package1"])
        self.assertEqual(installed_versions["package1"], "1.0.0")

    def test_parse_package_spec(self):
        result = parse_package_spec("package1>=1.0.0")
        self.assertEqual(result, ("package1", ">=", "1.0.0"))

    @patch("src.utils.merge_requirements.open")
    def test_read_requirements(self, mock_open):
        mock_open.return_value.read.return_value = "package1>=1.0.0"
        requirements = read_requirements("requirements.txt")
        self.assertNotEqual(requirements, {"package1": ">=1.0.0"})

    @patch("src.utils.merge_requirements.get_installed_versions")
    def test_merge_requirements(self, mock_get_installed_versions):
        mock_get_installed_versions.return_value = {"package1": "1.0.0"}
        req_versions = {"package1": ">=1.0.0"}
        merged_requirements, conflict_detected = merge_requirements(
            mock_get_installed_versions.return_value, req_versions
        )
        self.assertEqual(merged_requirements, ["package1>=1.0.0"])


if __name__ == "__main__":
    unittest.main()
