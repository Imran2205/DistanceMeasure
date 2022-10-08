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
# inno setup compiler


import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

additional_modules = []
options = {
    'build_exe': {
        'includes': additional_modules,
        'packages': ['scipy', 'sys', 'pyaudio', 'librosa', 'sounddevice', 'tensorflow'],
        'include_files': [
            'C:/Users/labib/AppData/Local/Programs/Python/Python38/DLLs/tk86t.dll',
            'C:/Users/labib/AppData/Local/Programs/Python/Python38/DLLs/tcl86t.dll',
            'C:/Users/labib/OneDrive/Desktop/imran_do_not_delete/DistanceMeasure/resources/libsndfile.dll',
            ('resources', 'resources')
        ],
    }
}
# , icon="icon.ico"
executables = [
    Executable('./main.py', base=base, icon='./ui/icon.ico', targetName="MeasureDistance.exe")
]

setup(
    name='MeasureDistance',
    version='1.0',
    author='Imran Kabir',
    description='Distance Measurement software.',
    options=options,
    executables=executables
)
