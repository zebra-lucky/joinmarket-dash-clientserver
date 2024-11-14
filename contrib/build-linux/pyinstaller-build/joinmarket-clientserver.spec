# -*- mode: python; coding: utf-8 -*-

import itertools
import os
from pathlib import Path


PROJECT_ROOT = os.path.abspath('.')


binaries = []
binaries += [(f'{PROJECT_ROOT}/jmvenv/lib/lib*', '.')]


datas = []
datas += [(f'{PROJECT_ROOT}/jmvenv/lib/python3.8/site-packages/'
           f'twisted/plugins/dropin.cache','twisted/plugins')]
datas += [(f'{PROJECT_ROOT}/jmvenv/lib/python3.8/site-packages/'
           f'twisted/plugins/__init__.py', 'twisted/plugins')]
datas += [(f'{PROJECT_ROOT}/jmvenv/lib/python3.8/site-packages/'
           f'twisted/plugins/txtorcon_endpoint_parser.py', 'twisted/plugins')]


scripts = [
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
]


hiddenimports = [
    'chromalog.mark.helpers',
    'chromalog.mark.helpers.simple',
    'twisted.plugins',
#    'twisted.plugins.autobahn_endpoints',
#    'twisted.plugins.autobahn_twistd',
    'twisted.plugins.txtorcon_endpoint_parser',
]


a = {}
pyz = {}
exe = {}


for s in scripts:
    a[s] = Analysis(
        [s],
        pathex=[],
        binaries=binaries,
        datas=datas,
        hiddenimports=hiddenimports,
        hookspath=[],
        hooksconfig={},
        runtime_hooks=[],
        excludes=[],
        noarchive=False,
        optimize=0,
    )

    pyz[s] = PYZ(a[s].pure)

    exe[s] = EXE(
        pyz[s], a[s].scripts, [],
        name=Path(s).stem,
        exclude_binaries=True, debug=False, bootloader_ignore_signals=False,
        strip=False, upx=True, console=True, disable_windowed_traceback=False,
        argv_emulation=False, target_arch=None, codesign_identity=None,
        entitlements_file=None,
    )


coll = COLLECT(
    *list(exe.values()),
    list(set(itertools.chain.from_iterable(b.binaries for b in a.values()))),
    list(set(itertools.chain.from_iterable(d.datas for d in a.values()))),
    strip=False,
    upx=True,
    upx_exclude=[],
    name='joinmarket-clientserver',
)
