import os
import zipfile

with zipfile.PyZipFile("modules.zip", mode='w', compression=zipfile.ZIP_DEFLATED, optimize=2) as pyzip:
    pyzip.writepy('./ibis/ibis')
    pyzip.writepy('./sqlglot/sqlglot')
    pyzip.writepy('./public/src/public')
    pyzip.writepy('./parsy/src/parsy')