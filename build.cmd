REM 建議加上 --standalone 產生獨立資料夾，或是 --onefile 產生單一檔案
python -m nuitka ^
    --standalone ^
    --plugin-enable=pyside6 ^
    --assume-yes-for-downloads ^
    --include-qt-plugins=sensible,styles ^
    --include-windows-runtime-dlls=yes ^
    --nofollow-import-to=pytest,unittest,tkinter ^
    --output-dir=dist ^
    src/main.py