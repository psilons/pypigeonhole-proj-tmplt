from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize

ext_modules = [
    Extension("games.klotski",  ["src/games/klotski.py"]),
    Extension("games.stack_queue_impl",  ["src/games/stack_queue_impl.py"]),
]

setup(
    name='klotski_lib',
    cmdclass={'build_ext': build_ext},
    ext_modules=cythonize(
        ext_modules,
        build_dir="build",
        compiler_directives={'language_level': "3"}),

    install_requires=['cython'],
    extras_require={
        'dev': ['pipdeptree'],
    }
)
