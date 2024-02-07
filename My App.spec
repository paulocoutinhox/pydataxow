# -*- mode: python ; coding: utf-8 -*-

import os
import platform

# general
root_dir = os.path.abspath(os.getcwd())
platform_name = platform.system().lower()
extras_dir = os.path.join(root_dir, "extras")

# platform data
program_name = "DataXow"
icon_path = None
program_file = None

if platform_name == "darwin":
    icon_path = os.path.join(extras_dir, "macos", "icon.icns")
    program_file = "{0}.app".format(program_name)
elif platform_name == "linux":
    icon_path = os.path.join(extras_dir, "linux", "icon.png")
    program_file = "{0}".format(program_name)
elif platform_name == "windows":
    icon_path = os.path.join(extras_dir, "windows", "icon.ico")
    program_file = "{0}.exe".format(program_name)

# pyinstaller
block_cipher = None

a = Analysis(
    [
        os.path.join(
            "src",
            "backend",
            "main.py",
        )
    ],
    pathex=[
        root_dir,
        os.path.join(root_dir, "src", "backend"),
    ],
    binaries=[],
    datas=[
        (os.path.join(root_dir, "gui"), "gui"),
    ],
    hiddenimports=[
        "modules.app",
        "modules.config",
        "modules.datetime",
        "modules.net",
        "modules.player",
        "modules.system",
        "clr",
        "pythonnet",
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=block_cipher,
)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name=program_name,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name=program_name,
)

app = BUNDLE(
    coll,
    name=program_file,
    icon=icon_path,
    bundle_identifier="com.dataxow.app",
)
