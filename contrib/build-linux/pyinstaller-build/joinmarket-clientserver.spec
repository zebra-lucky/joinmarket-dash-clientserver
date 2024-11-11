# -*- mode: python; coding: utf-8 -*-


a = Analysis(
    [
        'scripts/add-utxo.py',
        'scripts/bond-calculator.py',
        'scripts/bumpfee.py',
        'scripts/genwallet.py',
        'scripts/jmwalletd.py',
        'scripts/joinmarketd.py',
        'scripts/joinmarket-qt.py',
        'scripts/receive-payjoin.py',
        'scripts/sendpayment.py',
        'scripts/sendtomany.py',
        'scripts/start-dn.py',
        'scripts/tumbler.py',
        'scripts/wallet-tool.py',
        'scripts/yg-privacyenhanced.py',
        'scripts/yield-generator-basic.py',
    ],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

add_utxo_exe = EXE(
    pyz, a.scripts, [],
    name='add-utxo',
    exclude_binaries=True, debug=False, bootloader_ignore_signals=False,
    strip=False, upx=True, console=True, disable_windowed_traceback=False,
    argv_emulation=False, target_arch=None, codesign_identity=None,
    entitlements_file=None,
)

bond_calculator_exe = EXE(
    pyz, a.scripts, [],
    name='bond-calculator',
    exclude_binaries=True, debug=False, bootloader_ignore_signals=False,
    strip=False, upx=True, console=True, disable_windowed_traceback=False,
    argv_emulation=False, target_arch=None, codesign_identity=None,
    entitlements_file=None,
)

bumpfee_exe = EXE(
    pyz, a.scripts, [],
    name='bumpfee',
    exclude_binaries=True, debug=False, bootloader_ignore_signals=False,
    strip=False, upx=True, console=True, disable_windowed_traceback=False,
    argv_emulation=False, target_arch=None, codesign_identity=None,
    entitlements_file=None,
)

genwallet_exe = EXE(
    pyz, a.scripts, [],
    name='genwallet',
    exclude_binaries=True, debug=False, bootloader_ignore_signals=False,
    strip=False, upx=True, console=True, disable_windowed_traceback=False,
    argv_emulation=False, target_arch=None, codesign_identity=None,
    entitlements_file=None,
)

jmwalletd_exe = EXE(
    pyz, a.scripts, [],
    name='jmwalletd',
    exclude_binaries=True, debug=False, bootloader_ignore_signals=False,
    strip=False, upx=True, console=True, disable_windowed_traceback=False,
    argv_emulation=False, target_arch=None, codesign_identity=None,
    entitlements_file=None,
)

joinmarketd_exe = EXE(
    pyz, a.scripts, [],
    name='joinmarketd',
    exclude_binaries=True, debug=False, bootloader_ignore_signals=False,
    strip=False, upx=True, console=True, disable_windowed_traceback=False,
    argv_emulation=False, target_arch=None, codesign_identity=None,
    entitlements_file=None,
)

joinmarket_qt_exe = EXE(
    pyz, a.scripts, [],
    name='joinmarket-qt',
    exclude_binaries=True, debug=False, bootloader_ignore_signals=False,
    strip=False, upx=True, console=True, disable_windowed_traceback=False,
    argv_emulation=False, target_arch=None, codesign_identity=None,
    entitlements_file=None,
)

receive_payjoin_exe = EXE(
    pyz, a.scripts, [],
    name='receive-payjoin',
    exclude_binaries=True, debug=False, bootloader_ignore_signals=False,
    strip=False, upx=True, console=True, disable_windowed_traceback=False,
    argv_emulation=False, target_arch=None, codesign_identity=None,
    entitlements_file=None,
)

sendpayment_exe = EXE(
    pyz, a.scripts, [],
    name='sendpayment',
    exclude_binaries=True, debug=False, bootloader_ignore_signals=False,
    strip=False, upx=True, console=True, disable_windowed_traceback=False,
    argv_emulation=False, target_arch=None, codesign_identity=None,
    entitlements_file=None,
)

sendtomany_exe = EXE(
    pyz, a.scripts, [],
    name='sendtomany',
    exclude_binaries=True, debug=False, bootloader_ignore_signals=False,
    strip=False, upx=True, console=True, disable_windowed_traceback=False,
    argv_emulation=False, target_arch=None, codesign_identity=None,
    entitlements_file=None,
)

start_dn_exe = EXE(
    pyz, a.scripts, [],
    name='start-dn',
    exclude_binaries=True, debug=False, bootloader_ignore_signals=False,
    strip=False, upx=True, console=True, disable_windowed_traceback=False,
    argv_emulation=False, target_arch=None, codesign_identity=None,
    entitlements_file=None,
)

tumbler_exe = EXE(
    pyz, a.scripts, [],
    name='tumbler',
    exclude_binaries=True, debug=False, bootloader_ignore_signals=False,
    strip=False, upx=True, console=True, disable_windowed_traceback=False,
    argv_emulation=False, target_arch=None, codesign_identity=None,
    entitlements_file=None,
)

wallet_tool_exe = EXE(
    pyz, a.scripts, [],
    name='wallet-tool',
    exclude_binaries=True, debug=False, bootloader_ignore_signals=False,
    strip=False, upx=True, console=True, disable_windowed_traceback=False,
    argv_emulation=False, target_arch=None, codesign_identity=None,
    entitlements_file=None,
)

yg_privacyenhanced_exe = EXE(
    pyz, a.scripts, [],
    name='yg-privacyenhanced',
    exclude_binaries=True, debug=False, bootloader_ignore_signals=False,
    strip=False, upx=True, console=True, disable_windowed_traceback=False,
    argv_emulation=False, target_arch=None, codesign_identity=None,
    entitlements_file=None,
)

yield_generator_basic_exe = EXE(
    pyz, a.scripts, [],
    name='yield-generator-basic',
    exclude_binaries=True, debug=False, bootloader_ignore_signals=False,
    strip=False, upx=True, console=True, disable_windowed_traceback=False,
    argv_emulation=False, target_arch=None, codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    add_utxo_exe,
    bond_calculator_exe,
    bumpfee_exe,
    genwallet_exe,
    jmwalletd_exe,
    joinmarketd_exe,
    joinmarket_qt_exe,
    receive_payjoin_exe,
    sendpayment_exe,
    sendtomany_exe,
    start_dn_exe,
    tumbler_exe,
    wallet_tool_exe,
    yg_privacyenhanced_exe,
    yield_generator_basic_exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='start-dn',
)
