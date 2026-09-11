import traceback
try:
    import face_recognition_models
    print('face_recognition_models imported, location:', face_recognition_models.__file__)
    import pkg_resources
    print('resource_filename test:', pkg_resources.resource_filename('face_recognition_models', 'models/shape_predictor_68_face_landmarks.dat'))
except Exception:
    traceback.print_exc()
