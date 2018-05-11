# -*- mode: python -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=['/home/oleg/projects/15'],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher
)

game_files =  [('data/1.png', 'data/1.png', 'DATA')]
game_files +=  [('data/2.png', 'data/2.png', 'DATA')]
game_files +=  [('data/3.png', 'data/3.png', 'DATA')]
game_files +=  [('data/4.png', 'data/4.png', 'DATA')]
game_files +=  [('data/5.png', 'data/5.png', 'DATA')]
game_files +=  [('data/6.png', 'data/6.png', 'DATA')]
game_files +=  [('data/7.png', 'data/7.png', 'DATA')]
game_files +=  [('data/8.png', 'data/8.png', 'DATA')]
game_files +=  [('data/9.png', 'data/9.png', 'DATA')]
game_files +=  [('data/10.png', 'data/10.png', 'DATA')]
game_files +=  [('data/11.png', 'data/11.png', 'DATA')]
game_files +=  [('data/12.png', 'data/12.png', 'DATA')]
game_files +=  [('data/13.png', 'data/13.png', 'DATA')]
game_files +=  [('data/14.png', 'data/14.png', 'DATA')]
game_files +=  [('data/15.png', 'data/15.png', 'DATA')]
game_files +=  [('data/win.png', 'data/win.png', 'DATA')]
game_files +=  [('15.conf', '15.conf', 'DATA')]

pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=block_cipher
)

exe = EXE(
    pyz,
    a.scripts,
    exclude_binaries=True,
    name='15',
    debug=False,
    strip=False,
    upx=True,
    console=False
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas + game_files,
    strip=False,
    upx=True,
    name='15_linux'
)

