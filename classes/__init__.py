import main
import mobiles
import paths
import statics
import bases

for cls in dir(main):
    if isinstance(getattr(main,cls),type):
        globals()[cls] = getattr(main,cls)
for cls in dir(mobiles):
    if isinstance(getattr(mobiles,cls),type):
        globals()[cls] = getattr(mobiles,cls)
for cls in dir(statics):
    if isinstance(getattr(statics,cls),type):
        globals()[cls] = getattr(statics,cls)
for cls in dir(bases):
    if isinstance(getattr(bases,cls),type):
        globals()[cls] = getattr(bases,cls)
for cls in dir(paths):
    if isinstance(getattr(paths,cls),type):
        globals()[cls] = getattr(paths,cls)

