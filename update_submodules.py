import os
import subprocess

def run(cmd, cwd=None):
    print(f"\n>>> Running: {cmd}")
    result = subprocess.run(cmd, cwd=cwd, shell=True)
    if result.returncode != 0:
        print("❌ Command failed!")
        exit(1)

# 获取 deploy_project 根目录
ROOT = os.path.dirname(os.path.abspath(__file__))

# 子仓库路径
FRONTEND = os.path.join(ROOT, "frontend")
BACKEND = os.path.join(ROOT, "backend")

print("====================================")
print(" Updating FRONTEND submodule (Dev) ")
print("====================================")

run("git checkout Dev", cwd=FRONTEND)
run("git pull origin Dev", cwd=FRONTEND)


print("====================================")
print(" Updating BACKEND submodule (Dev) ")
print("====================================")

run("git checkout Dev", cwd=BACKEND)
run("git pull origin Dev", cwd=BACKEND)


print("====================================")
print(" Committing submodule updates")
print("====================================")

run("git add frontend backend", cwd=ROOT)
run('git commit -m "Update submodules to latest Dev"', cwd=ROOT)

print("\n🎉 All done! Submodules updated and committed.\n")
