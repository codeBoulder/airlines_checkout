import sys
import os
import subprocess
import pybind11
import sysconfig

script_dir = os.path.dirname(os.path.abspath(__file__))

print(f"📂 Робоча папка скрипта: {script_dir}")

includes = [
    pybind11.get_include(),
    pybind11.get_include(user=True),
    sysconfig.get_path("include"),
    sysconfig.get_path("platinclude"),
]

includes.append(script_dir)

include_args = [f'-I"{path}"' for path in includes]

lib_dir = sysconfig.get_config_var('LIBDIR') or sysconfig.get_path('stdlib')
if sys.platform == "win32":
    base_prefix = sys.base_prefix
    lib_dir = os.path.join(base_prefix, 'libs')

lib_args = [f'-L"{lib_dir}"']

ver = sys.version_info
lib_name = f"python{ver.major}{ver.minor}"
lib_args.append(f"-l{lib_name}")

source_files = [
    os.path.join(script_dir, "pythonModule.cpp"),
    os.path.join(script_dir, "BookingSystem.cpp")
]

output_file = os.path.join(script_dir, "core_backend.pyd")

missing_files = []
for f in source_files:
    if not os.path.exists(f):
        missing_files.append(f)

if missing_files:
    print("\n❌ ПОМИЛКА: Не знайдено наступні файли:")
    for f in missing_files:
        print(f"   - {f}")
    print("\nПеревірте, чи правильно ви назвали файли (наприклад, BookingSystem.cpp чи system.cpp?)")
    sys.exit(1)

cmd = [
    "g++", "-O3", "-Wall", "-shared", "-std=c++17", "-fPIC",
] + include_args + [f'"{f}"' for f in source_files] + lib_args + ["-o", f'"{output_file}"']

print("\n🚀 Запуск компіляції...")
full_command = " ".join(cmd)

try:
    subprocess.check_call(full_command, shell=True)
    print(f"\n✅ Успішно скомпільовано: {output_file}")
except subprocess.CalledProcessError:
    print("\n❌ Помилка компіляції! Перевірте лог вище.")