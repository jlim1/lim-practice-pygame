# Pygame practice

Lessons 01–28 build an asset-free snake game; 43–44 draw pixels and shapes; 85–99 explore projection and cubes. Each script stands alone. Use Python 3 and a graphical desktop. From this directory:

```text
python -m pip install pygame-ce
python 28_PythonGameDevelopment.py
```

Use the arrow keys to move the green snake toward the red food. After losing, press C to restart or Q to quit. For a version-only check, run `python 01_PythonGameDevelopment.py`.

For 91–99 also install `python -m pip install PyOpenGL`. Interactive OpenGL lessons require a compatible graphics driver and desktop OpenGL context. Lessons 01, 02, 28, 44, 91 and 92 passed headless smoke tests; these did not check visual appearance or interactive OpenGL rendering.

Lessons 29–39 and 42 use original geometric replacements for the two snake-game PNGs. Keep both sprites beside the scripts. For the packaging examples, install `cx-Freeze` and run `python 40_PythonGameDevelopment.py build` (or lesson 41) from this directory; both package lesson 39. No frozen build was tested or included. Lessons 45–52 demonstrate menus and button handling with neutral captions. Restored lessons 29, 35, 39, 42, 45 and 52 passed headless startup and quit checks.

Lessons 53–84 build a two-dimensional arcade game from pixel shapes. Run `python 84_PythonGameDevelopment.py` for the final version; choose **Controls** from the opening menu for the game keys. Lessons 83–84 run silently by default. To enable effects, place your own licensed `boom.wav` and `explosion.wav` beside the scripts. The original sounds are not included.
