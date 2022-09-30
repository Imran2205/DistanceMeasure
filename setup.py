"""import sys
from cx_Freeze import setup, Executable
# Dependencies are automatically detected, but it might need fine tuning.
additional_modules = []
build_exe_options = {"includes": additional_modules,
                     "packages": ["random", "sys"],
                     "excludes": ['tkinter'],
                     "include_files": ['dimension.png', 'file.html', 'logo.png']}
base = "Win32GUI"
if sys.platform == "win32":
    base = "Win32GUI"
setup(name="Avesta agro vet",
      version="1.0",
      description="Stock management",
      options={"build_exe": build_exe_options},
      executables=[Executable(script="Avesta_agro_vet_Func.py", base=base)])"""

import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

options = {
    'build_exe': {
        'includes': ['cx_Freeze'],
        'include_files': [
            'C:/Users/admin/AppData/Local/Programs/Python/Python38/DLLs/tk86t.dll',
            'C:/Users/admin/AppData/Local/Programs/Python/Python38/DLLs/tcl86t.dll',
            ('resources', 'resources')
        ],
    }
}
# , icon="icon.ico"
executables = [
    Executable('./tools/measure_app.py', base=base, targetName="MeasureDistance.exe")
]

setup(
    name='MeasureDistance',
    version='1.0',
    author='Imran Kabir',
    description='Distance Measurement software.',
    options=options,
    executables=executables
)
