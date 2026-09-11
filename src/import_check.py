import traceback
import sys
print('sys.path:', sys.path)
try:
    import face_recognition
    print('face_recognition imported', getattr(face_recognition, '__version__', 'unknown'))
except Exception:
    print('face_recognition import error:')
    traceback.print_exc()
try:
    import face_recognition_models
    print('face_recognition_models imported, location:', getattr(face_recognition_models, '__file__', 'n/a'))
except Exception:
    print('face_recognition_models import error:')
    traceback.print_exc()
