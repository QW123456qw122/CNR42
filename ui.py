import sys
import os
import subprocess

from QtFusion.path import abs_path


def run_script(script_path):
    """
    使用当前 Python 环境运行指定的脚本。

    Args:
        script_path (str): 要运行的脚本路径

    Returns:
        None
    """
    # 获取当前 Python 解释器的路径
    python_path = sys.executable

    if not os.path.isfile(script_path):
        print(f"脚本不存在：{script_path}")
        return

    # 构建运行命令并执行
    command = [python_path, "-m", "streamlit", "run", script_path]
    result = subprocess.run(command)
    if result.returncode != 0:
        print("脚本运行出错。")


# 实例化并运行应用
if __name__ == "__main__":
    # 指定您的脚本路径
    script_path = abs_path("web.py")

    # 运行脚本
    run_script(script_path)
