rmdir /Q /S build
rmdir /Q /S dist

pyinstaller --name klotski_app --noupx --icon app.ico --paths=src\game_tests  --hidden-import games.stack_queue_impl src\game_tests\klotski_test.py
